# py-speedtest

## setup

- clone into \$HOME/git/py-speedtest
- `mkdir -p /tmp/py-speedtest/`
- Set to run via crontab or launchd (see below)

### crontab

```
env EDITOR=nano crontab -e
*/5 * * * * /Users/adampacholski/git/py-speedtest/speedtest.sh >/tmp/stdout.log 2>/tmp/stderr.log
```

### launchd

Here's a launchd plist editor:

http://launched.zerowidth.com/

Here's the plist output it produced:

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>Label</key>
	<string>com.zerowidth.launched.py-speedtest</string>
	<key>ProgramArguments</key>
	<array>
		<string>sh</string>
		<string>-c</string>
		<string>/Users/adampacholski/git/py-speedtest/speedtest.sh &gt;/tmp/stdout.log 2&gt;/tmp/stderr.log</string>
	</array>
	<key>StartCalendarInterval</key>
	<array>
		<dict>
			<key>Minute</key>
			<integer>0</integer>
		</dict>
		<dict>
			<key>Minute</key>
			<integer>5</integer>
		</dict>
		<dict>
			<key>Minute</key>
			<integer>10</integer>
		</dict>
		<dict>
			<key>Minute</key>
			<integer>15</integer>
		</dict>
		<dict>
			<key>Minute</key>
			<integer>20</integer>
		</dict>
		<dict>
			<key>Minute</key>
			<integer>25</integer>
		</dict>
		<dict>
			<key>Minute</key>
			<integer>30</integer>
		</dict>
		<dict>
			<key>Minute</key>
			<integer>35</integer>
		</dict>
		<dict>
			<key>Minute</key>
			<integer>40</integer>
		</dict>
		<dict>
			<key>Minute</key>
			<integer>45</integer>
		</dict>
		<dict>
			<key>Minute</key>
			<integer>50</integer>
		</dict>
		<dict>
			<key>Minute</key>
			<integer>55</integer>
		</dict>
	</array>
	<key>UserName</key>
	<string>adampacholski</string>
</dict>
</plist>
```

Here's how to install the plist:

```
launchctl load -w ~/Library/LaunchAgents/com.zerowidth.launched.py-speedtest.plist
```
