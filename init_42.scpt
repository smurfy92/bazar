#/usr/bin/bash

osascript -e '
tell app "Google Chrome"
	activate
    set bounds of window 1 to {1, 1, 1500, 1440}
  end tell
tell app "iTerm2"
	activate
    set bounds of window 1 to {1500, 1, 2560, 1440}
  end tell
'