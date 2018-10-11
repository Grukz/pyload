# -*- coding: utf-8 -*-
from builtins import _

from pyload.plugins.internal.XFSAccount import XFSAccount


class FilerioCom(XFSAccount):
    __name__ = "FilerioCom"
    __type__ = "account"
    __version__ = "0.08"
    __status__ = "testing"

    __description__ = """FileRio.in account plugin"""
    __license__ = "GPLv3"
    __authors__ = [("zoidberg", "zoidberg@mujmail.cz")]

    PLUGIN_DOMAIN = "filerio.in"