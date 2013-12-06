import sys
import xbmc, xbmcaddon
import time, json
import threading
from traceback import print_exc
import xbmcgui

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
        if self.DBID <> '':
            self._inprogress_reset()
        else:
            log('No DBID found')
    
    def _inprogress_reset(self):
        try:
            xbmc.executeJSONRPC('{"id": 1, "jsonrpc": "2.0", "method": "VideoLibrary.SetMovieDetails", "params": {"movieid": %s, "resume": {"position": 0, "total": 0}}}' % (self.DBID))
        except Exception:
            log('unable to update in-progress state in DBID %s' %s (self.DBID))
            sys.exc_clear()

# WindowID 10025 = MyVideoNav

class InProgressResetThread(threading.Thread):
    def __init__(self):
        log('version %s started' % __addonversion__)
        threading.Thread.__init__(self)
        self.finished = False
        self.runNumber = 0
        self.processedItems = []
    
    def run(self):
        try:
            currentDBID = xbmc.getInfoLabel('ListItem.DBID')
            #log('currentDBID: %s' % (currentDBID))
            while not self.finished and xbmc.getCondVisibility( 'Window.IsVisible(10025)') and currentDBID not in self.processedItems:
                #log('run #%s' % (self.runNumber))
                self.processedItems.append(currentDBID)
                if currentDBID != '' and xbmc.getInfoLabel('ListItem.VideoResolution') > 0: # Easy way to check for video type
                    try:
                        response = json.loads(xbmc.executeJSONRPC(self._query_get(currentDBID)))
                        #log('resume: %s' % (response.get('result', {}).get('moviedetails', {}).get('resume', {}).get('position')))
                        position = response.get('result', {}).get('moviedetails', {}).get('resume', {}).get('position')
                            
                    except Exception:
                        log('unable to update in-progress state in DBID %s' % (currentDBID))
                        print_exc()
                        sys.exc_clear()
                self.runNumber = self.runNumber + 1
            time.sleep(5)
        except Exception:
            log('run exception')
            print_exc()
            sys.exc_clear()
            self.stop()
    
    def stop(self):
        log('stopping')
    
    def _query_get(self, currentDBID):
        return '{"id": 1, "jsonrpc": "2.0", "method": "VideoLibrary.GetMovieDetails", "params": {"movieid": %s, "properties": ["resume"]}}' % (currentDBID)
    
    def _query_set(self, currentDBID):
        return '{"id": 1, "jsonrpc": "2.0", "method": "VideoLibrary.SetMovieDetails", "params": {"movieid": %s, "resume": {"position": 0, "total": 0}}}' % (currentDBID)
    
    def _finish(self):
        log('finishing')
        self.finished = True
        self.stop()
    
    def _reset(self, currentDBID):
        try:
            xbmc.executeJSONRPC(self._query_set(currentDBID))
        except Exception:
            log('unable to update in-progress state in DBID %s' % (self.DBID))
            print_exc()
            sys.exc_clear()
    

xbmcgui.Window(10025).setProperty('InProgressResetIsRunning', 'true')
thread = InProgressResetThread()
thread.start()
