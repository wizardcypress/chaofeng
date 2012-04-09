#!/usr/bin/python2
# -*- coding: utf-8 -*-

'''
Some const and simple wrap of the ascii char to terminal. It include
the color and font style, the IAC , the cursor control and some
keycode.
'''

# Color

w = lambda code: '\x1b[' + str(code) +'m'

reset   = w(0)

black   = w(30)
red     = w(31)
green   = w(32)
yellow  = w(33)
blue    = w(34)
magenta = w(35)
cyan    = w(36)
white   = w(37)

bg_black   = w(40)
bg_red     = w(41)
bg_green   = w(42)
bg_yellow  = w(43)
bg_blue    = w(44)
bg_magenta = w(45)
bg_cyan    = w(46)
bg_white   = w(47)
bg_default = w(49)

bold       = w(1)
underscore = w(4)
inverted   = w(7)
italic     = w(3)

# Control characters

bell = chr(7)

# IAC and her firends

print_ab = chr(32)

IAC  = chr(255) # "Interpret As Command"
DO   = chr(253)
WONT = chr(252)
WILL = chr(251)
theNULL = chr(0)

SE  = chr(240)  # Subnegotiation End
NOP = chr(241)  # No Operation
DM  = chr(242)  # Data Mark
BRK = chr(243)  # Break
IP  = chr(244)  # Interrupt process
AO  = chr(245)  # Abort output
AYT = chr(246)  # Are You There
EC  = chr(247)  # Erase Character
EL  = chr(248)  # Erase Line
GA  = chr(249)  # Go Ahead
SB =  chr(250)  # Subnegotiation Begin

BINARY = chr(0) # 8-bit data path
ECHO = chr(1) # echo
RCP = chr(2) # prepare to reconnect
SGA = chr(3) # suppress go ahead
NAMS = chr(4) # approximate message size
STATUS = chr(5) # give status
TM = chr(6) # timing mark
RCTE = chr(7) # remote controlled transmission and echo
NAOL = chr(8) # negotiate about output line width
NAOP = chr(9) # negotiate about output page size
NAOCRD = chr(10) # negotiate about CR disposition
NAOHTS = chr(11) # negotiate about horizontal tabstops
NAOHTD = chr(12) # negotiate about horizontal tab disposition
NAOFFD = chr(13) # negotiate about formfeed disposition
NAOVTS = chr(14) # negotiate about vertical tab stops
NAOVTD = chr(15) # negotiate about vertical tab disposition
NAOLFD = chr(16) # negotiate about output LF disposition
XASCII = chr(17) # extended ascii character set
LOGOUT = chr(18) # force logout
BM = chr(19) # byte macro
DET = chr(20) # data entry terminal
SUPDUP = chr(21) # supdup protocol
SUPDUPOUTPUT = chr(22) # supdup output
SNDLOC = chr(23) # send location
TTYPE = chr(24) # terminal type
EOR = chr(25) # end or record
TUID = chr(26) # TACACS user identification
OUTMRK = chr(27) # output marking
TTYLOC = chr(28) # terminal location number
VT3270REGIME = chr(29) # 3270 regime
X3PAD = chr(30) # X.3 PAD
NAWS = chr(31) # window size
TSPEED = chr(32) # terminal speed
LFLOW = chr(33) # remote flow control
LINEMODE = chr(34) # Linemode option
XDISPLOC = chr(35) # X Display Location
OLD_ENVIRON = chr(36) # Old - Environment variables
AUTHENTICATION = chr(37) # Authenticate
ENCRYPT = chr(38) # Encryption option
NEW_ENVIRON = chr(39) # New - Environment variables
# the following ones come from
# http://www.iana.org/assignments/telnet-options
# Unfortunately, that document does not assign identifiers
# to all of them, so we are making them up
TN3270E = chr(40) # TN3270E
XAUTH = chr(41) # XAUTH
CHARSET = chr(42) # CHARSET
RSP = chr(43) # Telnet Remote Serial Port
COM_PORT_OPTION = chr(44) # Com Port Control Option
SUPPRESS_LOCAL_ECHO = chr(45) # Telnet Suppress Local Echo
TLS = chr(46) # Telnet Start TLS
KERMIT = chr(47) # KERMIT
SEND_URL = chr(48) # SEND-URL
FORWARD_X = chr(49) # FORWARD_X
PRAGMA_LOGON = chr(138) # TELOPT PRAGMA LOGON
SSPI_LOGON = chr(139) # TELOPT SSPI LOGON
PRAGMA_HEARTBEAT = chr(140) # TELOPT PRAGMA HEARTBEAT
EXOPL = chr(255) # Extended-Options-List
NOOPT = chr(0)

#Codes used in SB SE data stream for terminal type negotiation
IS = chr(0)
SEND = chr(1)

# Wrap for command

CMD_CHAR_PER =  IAC+WILL+SGA + IAC+WILL+ECHO
CMD_LINEMODE = IAC+WONT+ECHO + IAC+WONT+SGA# + IAC+WILL+LINEMODE

# Cursor

movex = lambda x : '\x1b[%d%c' % (abs(x),'D' if x<0 else 'C')
movey = lambda y : '\x1b[%d%c' % (abs(y),'A' if y<0 else 'B')
movey_1 = '\x1b[B'
movex_f = '\x1b[C'
movex_d = '\x1b[D'
save =    '\x1b[s'
restore = '\x1b[u'
clear =   '\x1b[2J'
clear_l = '\x1b[k'
move2 = lambda x,y : '\x1b[%d;%dH' % (x,y)

# KeyCode

k_up = '\x1b[A'
k_down = '\x1b[B'
k_right = '\x1b[C'
k_left = '\x1b[D'

k_c_a = '\x01'
k_c_b = '\x02'
k_c_c = '\x03'
k_c_h = '\x08'

k_del = chr(127)
k_backspace = chr(8)

k_enter_linux = chr(13)
k_enter_window = chr(10)

backspace = k_left+ ' '+k_left
