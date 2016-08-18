import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks

import subprocess

try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('Bzls')
except ImportError:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x: x


class Bzls(callbacks.Plugin):
    """Lists BZFlag servers"""

    def bzls(self, irc, msg, args, moreargs):
        """<args>

        Lists BZFlag servers"""
        moreargs.insert(0, '/path/to/bzls-rust');
        moreargs.insert(1, '-l');
        moreargs.insert(2, '150');
        p = subprocess.Popen(moreargs, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        out = out.replace("\x1b[33m", "\x0307").replace("\x1b[36m", "\x0311").replace("\x1b[32m", "\x0303").replace("\x1b[31m", "\x0304").replace("\x1b[0m", "\x0F")
        for part in out.split("\n"):
            if part != '':
                irc.reply(part, prefixNick=False)
    bzls = wrap(bzls, [any('something')])


Class = Bzls


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
