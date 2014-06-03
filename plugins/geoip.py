import socket
from util import hook, http



@hook.command
def geoip(inp):
    """geoip <host/ip> -- Gets the location of <host/ip>"""

    # socket.gethostbyname and .inet_ation confirm it's a valid address, and errors if it isn't

    def is_valid_hostname(hostname):
        try:
            socket.gethostbyname(hostname)
            return True
        except:
            return False
    def is_valid_ip(ip):
        try:
            socket.inet_aton(ip)
            return True
        except:
            return False

    # strips the http:// and www. from the input

    if inp[0:7] == 'http://':
            inp = inp[7:]

    # Current API does not support hostnames, so we convert it to IP here

    if is_valid_hostname(inp):
        inp = socket.gethostbyname(inp)

    # Concatenate the API ip and the input, stripped of the boilerplate, and changed to IPv4/v6

    url = 'http://www.telize.com/geoip/'
    json_resp = http.get_json(url + inp)
    final_return = ""
    #final validity check
    if is_valid_ip(inp):
        info = json_resp.items()
        for iter in range(1,len(json_resp) + 1):
            final_return += json_resp.key()[iter] + ": " + json_resp.values()[iter]
        return final_return
    else:
        return u'The IP {} is not a valid IP'.format(inp)