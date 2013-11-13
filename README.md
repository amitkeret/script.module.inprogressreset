# script.module.inprogressreset
XBMC add-on to reset a video's "in progress" state.  
The script will reset a video's "In-Progress" status, eliminating the "Resume from..." dialog when playing the video again.

### Usage
Place a control in a media list that calls the script:

    <control ...>
      ....
      <onclick>RunScript(script.module.inprogressreset)</onclick>
      ....
    </control>

#### Dependancies
This add-on requires JSON-RPC version >= 6.2.0
