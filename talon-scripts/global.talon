os: windows
-
# Define voice commands
# key(pause): user.toggle_mic_on_double_esc()
# key(pause): user.mic_on()
key(pause): user.mic_toggle()
#stop: user.pause_released_actions()
stop: user.mic_off()
mute: key(f8)
backup files: user.backup_and_commit_scripts("root", "github-backup")


# Moving Windows
left: key(win-left)
right: key(win-right)
up: key(win-up)
down: key(win-down)

# Mouse controls
go: user.mouse_left_click()
select: user.mouse_double_click()
middle click: user.mouse_middle_click()
menu: user.mouse_right_click()
back: user.mouse_back()
forward: user.mouse_forward()
scroll down: user.scroll_down()
scroll up: user.scroll_up()


# Keyboard controls
delete: key(ctrl-backspace)
tab: key(win-tab)
enter: key(enter)
new line: key(shift-enter)
fullscreen: key(f11)
f12: key(f12)
remove file: key(delete)
switch apps: key(ctrl-shift-alt-tab)
listen: key(win-h)
end: key(end)
blowup: key(win-tab)

# Text manipulation
copy: key(ctrl-c)
paste: key(ctrl-v)
cut: key(ctrl-x)
select all: key(ctrl-a)
undo: key(ctrl-z)
redo: key(ctrl+shift-z)
find: key(ctrl-f)
find all: key(ctrl+shift-f)
save: key(ctrl-s)
print: key(ctrl-p)

# Web browsing shortcuts
reload: key(ctrl+r)
hard reload: key(ctrl+shift-r)
new tab: key(ctrl-t)
new window: key(ctrl-n)
open last tab: key(ctrl+shift-t)
close tab: key(ctrl-w)
next: key(ctrl-pgdown)
go back: key(ctrl-pgup)


# Other useful commands
# vscode shortcuts
terminal: key(ctrl-`)
side bar: key(ctrl-alt-b)

# Youtube controls
expand: key(f)
play: key(space)
pause: key(pause)
exit: key(esc)

browser: user.open_random_cool_site()
vscode: user.focus_or_launch_app("Visual Studio Code", "vscode")
discord: user.focus_or_launch_app("Discord", "discord")
spotify: user.focus_or_launch_app("Spotify", "spotify")
slack: user.focus_or_launch_app("Slack", "slack")
second brain: user.focus_or_launch_app("Obsidian", "obsidian")
steam: user.focus_or_launch_app("Steam", "steam")

youtube: user.open_url_with_firefox("https://www.youtube.com")
email: user.open_url_with_firefox("https://www.gmail.com")
chatgpt: user.open_url_with_firefox("https://chat.openai.com")
aimset local: user.open_url_with_firefox("localhost:3000")
my local: user.open_url_with_firefox("localhost:4200")

# aimset start
start aimset proxy: user.open_cloud_sql_and_run_batch()
start aimset dev: user.open_git_bash_and_run_npm_dev()