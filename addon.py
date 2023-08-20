import xbmcaddon
import xbmcgui

import os

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

os.system('/usr/bin/chromium --start-fullscreen --start-maximized --window-position=0,0 --window-size=1920,1080')
