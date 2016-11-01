osascript -e '
tell app "Google Chrome"
	activate
    set bounds of window 1 to {1, 1, 700, 1000}
  end tell
tell app "iTerm"
	activate
    set bounds of window 1 to {700, 1, 1280, 1000}
  end tell
'