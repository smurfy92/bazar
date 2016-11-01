#!/usr/bin/python

from os import system

quote = '\"'
backslash = """\\"""

percent = """
osascript -e 'tell application "System Events" to keystroke "%"'
"""

dquote =   """osascript -e """ + """ 'tell application "System Events" to keystroke """ + quote + backslash + quote + quote + """ ' """
a = """
osascript -e 'tell application "System Events" to keystroke "a"'
"""
b = """
osascript -e 'tell application "System Events" to keystroke "b"'
"""
c = """
osascript -e 'tell application "System Events" to keystroke "c"'
"""
d = """
osascript -e 'tell application "System Events" to keystroke "d"'
"""
e = """
osascript -e 'tell application "System Events" to keystroke "e"'
"""
f = """
osascript -e 'tell application "System Events" to keystroke "f"'
"""
g = """
osascript -e 'tell application "System Events" to keystroke "g"'
"""
h = """
osascript -e 'tell application "System Events" to keystroke "h"'
"""
i = """
osascript -e 'tell application "System Events" to keystroke "i"'
"""
j = """
osascript -e 'tell application "System Events" to keystroke "j"'
"""
k = """
osascript -e 'tell application "System Events" to keystroke "k"'
"""
l = """
osascript -e 'tell application "System Events" to keystroke "l"'
"""
m = """
osascript -e 'tell application "System Events" to keystroke "m"'
"""
n = """
osascript -e 'tell application "System Events" to keystroke "n"'
"""
o = """
osascript -e 'tell application "System Events" to keystroke "o"'
"""
p = """
osascript -e 'tell application "System Events" to keystroke "p"'
"""
q = """
osascript -e 'tell application "System Events" to keystroke "q"'
"""
r = """
osascript -e 'tell application "System Events" to keystroke "r"'
"""
s = """
osascript -e 'tell application "System Events" to keystroke "s"'
"""
t = """
osascript -e 'tell application "System Events" to keystroke "t"'
"""
diez = """
osascript -e 'tell application "System Events" to keystroke "#"'
"""

excl = """
osascript -e 'tell application "System Events" to keystroke "!"'
"""

u = """
osascript -e 'tell application "System Events" to keystroke "u"'
"""
v = """
osascript -e 'tell application "System Events" to keystroke "v"'
"""
w = """
osascript -e 'tell application "System Events" to keystroke "w"'
"""
x = """
osascript -e 'tell application "System Events" to keystroke "x"'
"""
y = """
osascript -e 'tell application "System Events" to keystroke "y"'
"""
z = """
osascript -e 'tell application "System Events" to keystroke "z"'
"""

un = """
osascript -e 'tell application "System Events" to keystroke "1"'
"""
deu = """
osascript -e 'tell application "System Events" to keystroke "2"'
"""
troi = """
osascript -e 'tell application "System Events" to keystroke "3"'
"""
quat = """
osascript -e 'tell application "System Events" to keystroke "4"'
"""
cinq = """
osascript -e 'tell application "System Events" to keystroke "5"'
"""
six = """
osascript -e 'tell application "System Events" to keystroke "6"'
"""
sept = """
osascript -e 'tell application "System Events" to keystroke "7"'
"""
hui = """
osascript -e 'tell application "System Events" to keystroke "8"'
"""
neu = """
osascript -e 'tell application "System Events" to keystroke "9"'
"""
zer = """
osascript -e 'tell application "System Events" to keystroke "0"'
"""


arob = """
osascript -e 'tell application "System Events" to keystroke "@"'
"""

A = """
osascript -e 'tell application "System Events" to keystroke "A"'
"""
B = """
osascript -e 'tell application "System Events" to keystroke "B"'
"""
C = """
osascript -e 'tell application "System Events" to keystroke "C"'
"""
D = """
osascript -e 'tell application "System Events" to keystroke "D"'
"""
croc = """
osascript -e 'tell application "System Events" to keystroke ">"'
"""
E = """
osascript -e 'tell application "System Events" to keystroke "E"'
"""
F = """
osascript -e 'tell application "System Events" to keystroke "F"'
"""
G = """
osascript -e 'tell application "System Events" to keystroke "G"'
"""
H = """
osascript -e 'tell application "System Events" to keystroke "H"'
"""
I = """
osascript -e 'tell application "System Events" to keystroke "I"'
"""
J = """
osascript -e 'tell application "System Events" to keystroke "J"'
"""
K = """
osascript -e 'tell application "System Events" to keystroke "K"'
"""
L = """
osascript -e 'tell application "System Events" to keystroke "L"'
"""
M = """
osascript -e 'tell application "System Events" to keystroke "M"'
"""
N = """
osascript -e 'tell application "System Events" to keystroke "N"'
"""
O = """
osascript -e 'tell application "System Events" to keystroke "O"'
"""
mult = """
osascript -e 'tell application "System Events" to keystroke "*"'
"""
P = """
osascript -e 'tell application "System Events" to keystroke "P"'
"""
Q = """
osascript -e 'tell application "System Events" to keystroke "Q"'
"""
R = """
osascript -e 'tell application "System Events" to keystroke "R"'
"""
S = """
osascript -e 'tell application "System Events" to keystroke "S"'
"""
T = """
osascript -e 'tell application "System Events" to keystroke "T"'
"""
U = """
osascript -e 'tell application "System Events" to keystroke "U"'
"""
V = """
osascript -e 'tell application "System Events" to keystroke "V"'
"""
W = """
osascript -e 'tell application "System Events" to keystroke "W"'
"""
X = """
osascript -e 'tell application "System Events" to keystroke "X"'
"""
Y = """
osascript -e 'tell application "System Events" to keystroke "Y"'
"""
Z = """
osascript -e 'tell application "System Events" to keystroke "Z"'
"""
dol = """
osascript -e 'tell application "System Events" to keystroke "$"'
"""

underscore = """
osascript -e 'tell application "System Events" to keystroke "_"'
"""

pcome = """
osascript -e 'tell application "System Events" to keystroke ";"'
"""


minus = """
osascript -e 'tell application "System Events" to keystroke "-"'
"""
dot = """
osascript -e 'tell application "System Events" to keystroke "."'
"""
slash = """
osascript -e 'tell application "System Events" to keystroke "/"'
"""
wsp = """
osascript -e 'tell application "System Events" to keystroke " "'
"""

enter = """
osascript -e 'tell application "System Events" to keystroke return'
"""

dots = """
osascript -e 'tell application "System Events" to keystroke ":"'
"""


cmd = "ls -la"

cc = """
osascript -e 'tell application "System Events" to keystroke "c"'
"""
shifttab = """
osascript -e 'tell application "System Events" to keystroke tab using {shift down}'
"""

equal = """
osascript -e 'tell application "System Events" to keystroke "="'
"""
oped = """
osascript -e 'tell application "System Events" to keystroke "{"'
"""

cled = """
osascript -e 'tell application "System Events" to keystroke "}"'
"""

pop = """
osascript -e 'tell application "System Events" to keystroke "("'
"""
cop = """
osascript -e 'tell application "System Events" to keystroke ")"'
"""


pcoma = """
osascript -e 'tell application "System Events" to keystroke ";"'
"""

ppipe = """
osascript -e 'tell application "System Events" to keystroke "|"'
"""
single = """
osascript -e 'tell application "System Events" to key code 39'
"""


def send_command(line):
	lain = len(line)
	index = 0
	while index < lain:
		c = line[index]
		if (c == '|'):
			system(ppipe)
		if (c == '('):
			system(pop)
		if (c == ')'):
			system(cop)
		if (c == '}'):
			system(cled)
		if (c == 'a'):
			system(a)
		if (c == '{'):
			system(oped)
		if (c == 'b'):
			system(b)
		if (c == 'c'):
			system(cc)
		if (c == 'd'):
			system(d)
		if (c == 'e'):
			system(e)
		if (c == 'f'):
			system(f)
		if (c == 'g'):
			system(g)
		if (c == 'h'):
			system(h)
		if (c == 'i'):
			system(i)
		if (c == 'j'):
			system(j)
		if (c == 'k'):
			system(k)
		if (c == 'l'):
			system(l)
		if (c == 'm'):
			system(m)
		if (c == 'n'):
			system(n)
		if (c == 'o'):
			system(o)
		if (c == 'p'):
			system(p)
		if (c == 'q'):
			system(q)
		if (c == 'r'):
			system(r)
		if (c == 's'):
			system(s)
		if (c == 't'):
			system(t)
		if (c == 'u'):
			system(u)
		if (c == 'v'):
			system(v)
		if (c == 'w'):
			system(w)
		if (c == 'x'):
			system(x)
		if (c == 'y'):
			system(y)
		if (c == 'z'):
			system(z)
		if (c == 'A'):
			system(A)
		if (c == 'B'):
			system(B)
		if (c == 'C'):
			system(C)
		if (c == 'D'):
			system(D)
		if (c == 'E'):
			system(E)
		if (c == 'F'):
			system(F)
		if (c == 'G'):
			system(G)
		if (c == 'H'):
			system(H)
		if (c == 'I'):
			system(I)
		if (c == 'J'):
			system(J)
		if (c == 'K'):
			system(K)
		if (c == 'L'):
			system(L)
		if (c == 'M'):
			system(M)
		if (c == 'N'):
			system(N)
		if (c == 'O'):
			system(O)
		if (c == 'P'):
			system(P)
		if (c == 'Q'):
			system(Q)
		if (c == 'R'):
			system(R)
		if (c == 'S'):
			system(S)
		if (c == 'T'):
			system(T)
		if (c == 'U'):
			system(U)
		if (c == 'V'):
			system(V)
		if (c == 'W'):
			system(W)
		if (c == 'X'):
			system(X)
		if (c == 'Y'):
			system(Y)
		if (c == 'Z'):
			system(Z)
		if (c == '-'):
			system(minus)
		if (c == '^'):
			system(enter)
		if (c == '_'):
			system(underscore)
		if (c == quote):
			system(dquote)
		if (c == ' '):
			system(wsp)
		if (c == '1'):
			system(un)
		if (c == '2'):
			system(deu)
		if (c == '3'):
			system(troi)
		if (c == ';'):
			system(pcoma)
		if (c == '!'):
			system(excl)
		if (c == '4'):
			system(quat)
		if (c == '5'):
			system(cinq)
		if (c == '6'):
			system(six)
		if (c == '7'):
			system(sept)
		if (c == '8'):
			system(hui)
		if (c == '9'):
			system(neu)
		if (c == '.'):
			system(dot)
		if (c == '/'):
			system(slash)
		if (c == '0'):
			system(zer)
		if (c == '$'):
			system(dol)
		if (c == ':'):
			system(dots)
		if (c == '@'):
			system(arob)
		if (c == '='):
			system(equal)
		if (c == '>'):
			system(croc)
		if (c == '~'):
			system(shifttab)
		if (c == '\''):
			system(single)
		if (c == '#'):
			system(diez)
		if (c == '*'):
			system(mult)
		if (c == '%'):
			system(percent)
		index+=1
import time
towait = 1

send_command('~')
send_command("clear^")
time.sleep(towait)




send_command("unsetenv rvm_bin_path^")
send_command("unsetenv TERM_PROGRAM^")
# time.sleep(towait)
send_command("unsetenv ANDROID_HOME^")
# time.sleep(towait)
send_command("unsetenv SHELL^")
# time.sleep(towait)
send_command("unsetenv TERM^")
# time.sleep(towait)
send_command("unsetenv TEST_ENV_NUMBER^")
# time.sleep(towait)
send_command("unsetenv TMPDIR^")
# time.sleep(towait)
send_command("unsetenv Apple_PubSub_Socket_Render^")
# time.sleep(towait)
send_command("unsetenv TERM_PROGRAM_VERSION^")
# time.sleep(towait)
send_command("unsetenv TERM_SESSION_ID^")
# time.sleep(towait)
send_command("unsetenv LC_ALL^")
# time.sleep(towait)
send_command("unsetenv USER^")
# time.sleep(towait)
send_command("unsetenv _system_type^")
# time.sleep(towait)
send_command("unsetenv rvm_path^")
# time.sleep(towait)
send_command("unsetenv SSH_AUTH_SOCK^")
# time.sleep(towait)
send_command("unsetenv __CF_USER_TEXT_ENCODING^")
# time.sleep(towait)
send_command("unsetenv PAGER^")
# time.sleep(towait)
send_command("unsetenv HOMEBREW_CACHE^")
# time.sleep(towait)
send_command("unsetenv rvm_prefix^")
# time.sleep(towait)
send_command("unsetenv PATH^")
# time.sleep(towait)
send_command("unsetenv PWD^")
# time.sleep(towait)
send_command("unsetenv JAVA_HOME^")
# time.sleep(towait)
send_command("unsetenv LANG^")
# time.sleep(towait)
send_command("unsetenv _system_arch^")
# time.sleep(towait)
send_command("unsetenv XPC_FLAGS^")
# time.sleep(towait)
send_command("unsetenv _system_version^")
# time.sleep(towait)
send_command("unsetenv XPC_SERVICE_NAME^")
# time.sleep(towait)
send_command("unsetenv rvm_version^")
# time.sleep(towait)
send_command("unsetenv SHLVL^")
# time.sleep(towait)
send_command("unsetenv HOME^")
# time.sleep(towait)
send_command("unsetenv LANGUAGE^")
# time.sleep(towait)
send_command("unsetenv RAILS_ENV^")
# time.sleep(towait)
send_command("unsetenv LOGNAME^")
# time.sleep(towait)
send_command("unsetenv VISUAL^")
# time.sleep(towait)
send_command("unsetenv LC_CTYPE^")
# time.sleep(towait)
send_command("unsetenv ARCHFLAGS^")
# time.sleep(towait)
send_command("unsetenv _system_name^")
# time.sleep(towait)
send_command("unsetenv HISTTIMEFORMAT^")
# time.sleep(towait)
send_command("unsetenv _^")
# time.sleep(towait)
