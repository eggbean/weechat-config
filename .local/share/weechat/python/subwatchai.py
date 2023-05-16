try:
    import weechat as w
    import_ok = True
except ImportError:
    print("This script must be run under WeeChat")
    print("Get WeeChat now at: https://weechat.org/")
    import_ok = False

SCRIPT_NAME    = "subwatchai"
SCRIPT_AUTHOR  = "David Schultz (Examknow)"
SCRIPT_VERSION = "0.1"
SCRIPT_LICENSE = "MIT"
SCRIPT_DESC    = "Simple script to keep the subwatch bot in a channel"

CHANNEL        = "#eggbean"
NICK           = "SubWatch"

def checkforbot(data, remain):
    buffer = w.buffer_search("==", "irc.snoonet." + CHANNEL)
    nick = w.nicklist_search_nick(buffer, "", NICK)
    server = w.buffer_get_string(buffer, 'localvar_server')
    if nick == "":
        w.command("", f"/quote -server {server} INVITE {NICK} {CHANNEL}")
    return w.WEECHAT_RC_OK

if import_ok and w.register(SCRIPT_NAME, SCRIPT_AUTHOR, SCRIPT_VERSION, SCRIPT_LICENSE, SCRIPT_DESC, "", ""):
    w.hook_timer(300 * 1000, 60, 0, "checkforbot", "")

'''
PROBLEM: 	When the subwsatch bot user is unavailable, a constant stream of error messages appear in the *current* buffer
			It would be better for them to go to the snoonet server buffer, with the buflist entry being highlighted

			Also, the checks to reconnect should be done less frequently after it fails to connect x times
'''
