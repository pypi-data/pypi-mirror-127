"""
J1939 functions for use with RP1210 APIs. Note that this implementation is RP1210-specific - i.e.
if you try to generate J1939 messages to transmit directly onto a CANbus, these functions will fail!

While a dict of J1939 PGNs would be convenient, they are not provided here because the list is a
copyright of SAE.

J1939 functions:
- toJ1939Message
- getJ1939ProtocolString
- getJ1939ProtocolDescription

J1939 classes:
- J1939MessageParser
"""

from RP1210 import sanitize_msg_param

def toJ1939Message(pgn, priority, source, destination, data, sanitize = True) -> bytes:
    """
    Converts args to J1939 message suitable for RP1210_SendMessage function.

    String arguments are read as base-10! If you want to provide an argument in base-16, do it as
    an int or byte string.

    RP1210_SendMessage J1939 format:
    - PGN (3 bytes)
    - Priority (1 byte)
    - Source Address (1 byte)
    - Destination Address (1 byte)
    - Message Data (0 - 1785 byes)

    Arguments can be strings, ints, or bytes. This function will decode UTF-8 characters in strings
    to base-10 ints, so don't provide it with letters or special characters. If you want to send it
    0xFF, send it as an int and not "FF".
    """
    ret_val = sanitize_msg_param(pgn, 3, 'little')
    ret_val += sanitize_msg_param(priority, 1)
    ret_val += sanitize_msg_param(source, 1)
    ret_val += sanitize_msg_param(destination, 1)
    ret_val += sanitize_msg_param(data)
    return ret_val

def toJ1939Request(pgn_requested, source, destination = 255, priority = 6) -> bytes:
    """
    Formats a J1939 request message. This puts out a request for the specified PGN, and will prompt
    other devices on the network to respond.

    - pgn_requested: the parameter group you're requesting
    - source: the source address, e.g. your address on the CANBus
    - destination: 255 = global request; enter a different number to request from a specific address
    - priority: priority of request; default is 6
    """
    pgn_request = sanitize_msg_param(pgn_requested, 3, 'little') # must be little-endian
    return toJ1939Message(0x00EA00, priority, source, destination, pgn_request)

def toJ1939Name(arbitrary_address : bool, industry_group : int, system_instance : int, system : int,
                function : int, function_instance : int, ecu_instance : int, mfg_code : int, id : int) -> bytes:
    def add_bits(name, val, num_bits):
        mask = (1 << num_bits) - 1
        value = int.from_bytes(sanitize_msg_param(val), (num_bits + 7) // 8)
        return (name << num_bits) + (value & mask)
    name = 0b0
    # arbitrary address (1 bit)
    name = add_bits(name, arbitrary_address, 1)
    # industry group (3 bits)
    name = add_bits(name, industry_group, 3)
    # vehicle system instance (4 bits)
    name = add_bits(name, system_instance, 4)
    # vehicle system (7 bits)
    name = add_bits(name, system, 7)
    # reserved bit
    name = add_bits(name, 1, 1)
    # function (8 bits)
    name = add_bits(name, function, 8)
    # function instance (5 bits)
    name = add_bits(name, function_instance, 5)
    # ecu instance (3 bits)
    name = add_bits(name, ecu_instance, 3)
    # manufacturer code (11 bits)
    name = add_bits(name, mfg_code, 11)
    # identity number (21 bits)
    name = add_bits(name, id, 21)
    return sanitize_msg_param(name)

def getJ1939ProtocolString(protocol = 1, Baud = "Auto", Channel = -1,
                        SampleLocation = 95, SJW = 1,
                        PROP_SEG = 1, PHASE_SEG1 = 2, PHASE_SEG2 = 1,
                        TSEG1 = 2, TSEG2 = 1, SampleTimes = 1) -> bytes:
    """
    Generates fpchProtocol string for ClientConnect function. The default values you see above
    were made up on the spot and shouldn't necessarily be used.

    Keyword arguments have the same names as below (e.g. Baud, SampleLocation, PHASE_SEG1).

    IDSize is automatically set to 29 whenever relevant because that is its only valid value.

    This function also accepts a Channel argument!

    Examples:
    - protocol1 = J1939.getProtocolString(protocol = 1, Baud = "Auto")
    - protocol2 = J1939.getProtocolString(protocol = 3, Baud = 500, SampleLocation = 75, SJW = 3, IDSize = 29)
    """
    if Channel != -1:
        chan_arg = f",Channel={str(Channel)}"
    else:
        chan_arg = ""

    if protocol == 1:
        return bytes(f"J1939:Baud={str(Baud)}" + chan_arg, 'utf-8')
    elif protocol == 2:
        return bytes("J1939" + chan_arg, 'utf-8')
    elif protocol == 3:
        return bytes(f"J1939:Baud={str(Baud)},SampleLocation={str(SampleLocation)},SJW={str(SJW)},IDSize=29" + chan_arg, 'utf-8')
    elif protocol == 4:
        return bytes(f"J1939:Baud={str(Baud)},PROP_SEG={str(PROP_SEG)},PHASE_SEG1={str(PHASE_SEG1)},PHASE_SEG2={str(PHASE_SEG2)},SJW={str(SJW)},IDSize=29" + chan_arg, 'utf-8')
    elif protocol == 5:
        return bytes(f"J1939:Baud={str(Baud)},TSEG1={str(TSEG1)},TSEG2={str(TSEG2)},SampleTimes={str(SampleTimes)},SJW={str(SJW)},IDSize=29" + chan_arg, 'utf-8')
    else:
        return b"J1939" # default to protocol format 2, default channel

def getJ1939ProtocolDescription(protocol : int) -> str:
    """
    Returns a description of the protocol selected with protocol arg.
    
    Feed the result of RP1210Config.getJ1939FormatsSupported() into this function to get a description of what
    the format means.

    Honestly, I don't see anyone ever using this function.
    """
    if protocol == 1:
        return "Variable J1939 baud rate. Select 125, 250, 500, 1000, or Auto."
    elif protocol == 2:
        return "General default for J1939 baud rate (250k baud)."
    elif protocol == 3:
        return "Driver uses SampleLocation to calculate parameters."
    elif protocol == 4:
        return "Baud formula derived from BOSCH CAN specification."
    elif protocol == 5:
        return "Baud formula derived from Intel implementations."
    else:
        return "Invalid J1939 protocol format selected."

class J1939MessageParser():
    """
    A convenience class for parsing a J1939 message received from RP1210_ReadMessage.

    Message must include timestamp (4 bytes) in its leading bytes (this conforms w/ return value
    of RP1210_ReadMessage).

    - Initialize the object with the message received from ReadMessage.
    - If you used the command 'Set Echo Transmitted Messages' to turn echo on, set arg echo = True.
    """
    def __init__(self, j1939_message : bytes, echo = False) -> None:
        self.msg = j1939_message
        self.echo_offset = int(echo)

    def isEcho(self) -> bool:
        """Returns True if the message is an echo of a message you transmitted, False if not."""
        if self.echo_offset == 1:
            return int.from_bytes(self.msg[4]) == 0x01
        return False

    def isRequest(self) -> bool:
        """Returns true if PGN matches J1939 Request PGN."""
        return self.getPGN() == 0x00EA00

    def getTimestamp(self) -> int:
        """Returns timestamp (4 bytes) as int."""
        print(self.msg)
        print(self.msg[0:4])
        return int.from_bytes(self.msg[0:4], 'big')

    def getPGN(self) -> int:
        """Returns PGN (3 bytes) as int."""
        start = 4 + self.echo_offset
        end = 6 + self.echo_offset
        return int.from_bytes(self.msg[start:end], 'little')

    def getPriority(self) -> int:
        """Returns Priority (1 byte) as int."""
        loc = 7 + self.echo_offset
        return self.msg[loc]

    def getSource(self) -> int:
        """Returns Source Address (1 byte) as int."""
        loc = 8 + self.echo_offset
        return self.msg[loc]

    def getDestination(self) -> int:
        """Returns Destination Address (1 byte) as int."""
        loc = 9 + self.echo_offset
        return self.msg[loc]

    def getData(self) -> bytes:
        """Returns message data (0 - 1785 bytes) as bytes."""
        loc = 10 + self.echo_offset
        return self.msg[loc:]
