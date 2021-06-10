import xbmcaddon
import xbmcgui

import os

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

os.system('/usr/bin/steam -bigpicture')