import struct

INIT = 0
STX_DTCT = 1
LEN_DTCT = 2
SEQ_DTCT = 3
SYS_DTCT = 4
COMP_DTCT = 5
MSG_DTCT = 6
PLD_DTCT = 7
CKA_DTCT = 8
CKB_DTCT = 9

class Mavlinkprotocol:
    def __init__(self, handler=None, msgid='\x64'):
        self.handler = handler
        self.msgid = msgid
        self.msg = []
        self.msglen = 0

    def refresh(self):
        state = INIT
        self.msg = []
        self.msglen = 0
        while state != CKB_DTCT:
            b = self.handler.read()
            if state == INIT:
                if b == '\xFE':
                    state = STX_DTCT
            elif state == STX_DTCT:
                state = LEN_DTCT
                self.msglen = struct.unpack('B', b)[0]
            elif state == LEN_DTCT:
                state = SEQ_DTCT
            elif state == SEQ_DTCT:
                state = SYS_DTCT
            elif state == SYS_DTCT:
                state = COMP_DTCT
            elif state == COMP_DTCT:
                if self.msgid == b:
                    state = MSG_DTCT
                else:
                    state = INIT
            elif state == MSG_DTCT:
                if len(self.msg) < self.msglen:
                    self.msg.append(b)
                else:
                    state = CKA_DTCT
            elif state == CKA_DTCT:
                state = CKB_DTCT
        return None

    def getvalue(self, fmt='', lo=0, hi=0):
        msg = b''.join(self.msg)
        return struct.unpack(fmt, msg[lo:hi])
