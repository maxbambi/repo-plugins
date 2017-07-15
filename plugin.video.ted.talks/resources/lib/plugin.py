"""
Contains constants that we initialize to the correct values at runtime.
"""
import sys

__plugin__ = "TED Talks Uninitialized Plugin"
getLS = lambda x: x
__pluginLS__ = __plugin__
__author__ = "XXX"
__version__ = "X.X.X"


def init():
    import xbmcaddon
    addon = xbmcaddon.Addon(id='plugin.video.ted.talks')
    global __plugin__, getLS, __author__, __version__, __pluginLS__
    __plugin__ = addon.getAddonInfo('name')
    import CommonFunctions
    CommonFunctions.plugin = __plugin__
    getLS = addon.getLocalizedString
    __pluginLS__ = getLS(30000)
    __author__ = addon.getAddonInfo('author')
    __version__ = addon.getAddonInfo('version')
    import xbmc
    xbmc.log("[ADDON] Initialized %s v%s using Python: %s'" % (__plugin__, __version__, sys.version), level=xbmc.LOGNOTICE)

def report(gnarly_message, friendly_message=None, level='notice'):
    '''
    Log a message with optional onscreen notification.
    '''
    import xbmc
    level = {'notice' : xbmc.LOGNOTICE, 'debug': xbmc.LOGDEBUG}[level]
    xbmc.log("[ADDON] %s v%s - %s" % (__plugin__, __version__, gnarly_message), level=level)
    if friendly_message:
        xbmc.executebuiltin('Notification("%s","%s",)' % (__pluginLS__, friendly_message))
