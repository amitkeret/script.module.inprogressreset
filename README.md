# script.module.inprogressreset
XBMC add-on to reset a video's "in progress" state.  
The script will reset a video's "In-Progress" status, eliminating the "Resume from..." dialog when playing the video again.

Forum discussion here: http://forum.xbmc.org/showthread.php?tid=179759

### Usage
To make use of the script, you need to modify your skin.  
Place a control in a media list that calls the script:

    <control ...>
      <visible>[Container.Content(Episodes) | Container.Content(Movies) ] + system.hasaddon(script.module.inprogressreset) + !SubString(ListItem.PercentPlayed,0,left)</visible>
      <onclick>RunScript(script.module.inprogressreset,DBID=$INFO[ListItem.DBID])</onclick>
      ....
    </control>

#### Skins with built-in support
* [Quartz](https://github.com/pecinko/quartz)
* [Quartz Modded](https://github.com/amitkeret/skin.quartz.mod)

#### Dependancies
This add-on requires JSON-RPC version >= 6.2.0
