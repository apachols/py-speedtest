# py-speedtest

Writes a csv file with data from `speedtest-cli`:
```
Date,Time,SSID,Ping (ms),Download (Mbit/s),Upload (Mbit/s)
06/08/20,13:31,iCantBelieveItsNotGigabit,18.136,81.30,10.80
06/08/20,13:34,iCantBelieveItsNotGigabit,18.277,65.85,11.27
06/08/20,14:00,iCantBelieveItsNotGigabit,17.326,86.06,11.27
06/08/20,14:05,iCantBelieveItsNotGigabit,22.516,82.40,10.87
06/08/20,14:10,iCantBelieveItsNotGigabit,67.668,49.21,7.91
...
```

## setup
- `brew install speedtest-cli`
- `cd $HOME/git/ && git clone https://github.com/apachols/py-speedtest.git`
- `mkdir -p /tmp/py-speedtest/`
- Set to run via crontab or launchd (see below)
- `tail -f /tmp/py-speedtest/speedtest.csv`
- `tail -f /tmp/std*.log`

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

... And, here's how to uninstall:


Here's how to install the plist:

```
launchctl unload ~/Library/LaunchAgents/com.zerowidth.launched.py-speedtest.plist
```

