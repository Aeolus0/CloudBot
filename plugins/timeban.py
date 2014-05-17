from op import mode_cmd
from util import hook
from threading import Timer


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

    #inp has now been stripped of everything but the reason
    timeban_final = long(timeban_final)
    mode_ban  = "+b"
    mode_unban = "-b"
    channel = "#coding"
    conn.send("MODE {} {} {}".format(channel, mode_ban, str(user)))
    conn.send("KICK {} {} {}".format(channel, str(user), str(inp)))
    unban_cmd = conn.send("MODE {} {} {}".format(channel, mode_unban, str(user)))
    unban = Timer(timeban_final, unban_cmd)
    unban.start()