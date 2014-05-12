from util import hook
import time, threading
from cStringIO import StringIO
import Queue

#@hook.command('timeban', permissions=["timeout"], autohelp=False)
@hook.command
def timeban(inp, conn=None):
    user = inp[:inp.find(' ')]
    inp = inp[inp.find(' ') + 1:]
    try:
        int(inp[0])
        timebanned_raw = inp[:inp.find(' ')]
        inp = inp[inp.find(' ') + 1:]
    except:
        timebanned_raw = '60m'

    if timebanned_raw[-1] in ['s', 'S']:
        timebanned_raw = long(timebanned_raw[:-1])
        timeban_final = timebanned_raw
    elif timebanned_raw[-1] in ['m', 'M']:
        timebanned_raw = long(long(timebanned_raw[:-1]) * 60)
        timeban_final = timebanned_raw
    elif timebanned_raw[-1] in ['h', 'H']:
        timebanned_raw = long(long(timebanned_raw[:-1]) * 3600)
        timeban_final = timebanned_raw
    elif timebanned_raw[-1] in ['d', 'D']:
        timebanned_raw = long(long(timebanned_raw[:-1]) * 3600 * 24)
        timeban_final = timebanned_raw
    elif timebanned_raw[-1] in ['w', 'W']:
        timebanned_raw = long(long(timebanned_raw[:-1]) * 3600 * 24 * 7)
        timeban_final = timebanned_raw


    #    conn.gettext(["WHOIS", [str(user)]])
    #    hostname_unfil = conn.gettext(["WHOIS", [str(user)]])
#   This is where i fail ----> hostname_unfil = raw whois output for user
    #how would i get the whois data :(


    hostname = hostname_unfil[hostname_unfil.find('@'):hostname_unfil(')')]

    conn.cmd("BAN", ["*!*" + str(hostname)])
    conn.cmd("KICK", ['#coding', str(user), str(inp)])
    threading.Timer(int(timeban_final), conn.cmd("UNBAN", '*!*' + hostname))
