import sys
import xbmc, xbmcgui, xbmcaddon

__addon__        = xbmcaddon.Addon()
__addonid__      = __addon__.getAddonInfo('id')
__addonversion__ = __addon__.getAddonInfo('version')

def log(txt):
    if isinstance (txt, str):
        txt = txt.decode("utf-8")
    message = u'%s: %s' % (__addonid__, txt)
    xbmc.log(msg=message.encode("utf-8"), level=xbmc.LOGDEBUG)

class Main:
    def __init__(self):
        log('version %s started' % __addonversion__ )
        self.DBID = xbmc.getInfoLabel('ListItem.DBID')
        if self.DBID <> "":
            self._inprogress_reset()
        else:
            log("No DBID found")

    def _inprogress_reset(self):
        try:
            xbmc.executeJSONRPC('{"id": 1, "jsonrpc": "2.0", "method": "VideoLibrary.SetMovieDetails", "params": {"movieid": %s, "resume": {"position": 0, "total": 0}}}' % (self.DBID))
        except Exception:
            log("unable to update in-progress state in DBID %s" %s (self.DBID))
            sys.exc_clear()
    
if ( __name__ == "__main__" ):
    Main()

log('finished')