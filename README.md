# script.module.inprogressreset
XBMC add-on to reset a video's "in progress" state.  
The script will reset a video's "In-Progress" status, eliminating the "Resume from..." dialog when playing the video again.

Forum discussion here: http://forum.xbmc.org/showthread.php?tid=179759

### Usage
Place a control in a media list that calls the script:

    <control ...>
      <visible>[Container.Content(Episodes) | Container.Content(Movies) ] + system.hasaddon(script.module.inprogressreset) + !SubString(ListItem.PercentPlayed,0,left)</visible>
      <onclick>RunScript(script.module.inprogressreset,DBID=$INFO[ListItem.DBID])</onclick>
      ....
    </control>

#### Dependancies
This add-on requires JSON-RPC version >= 6.2.0
