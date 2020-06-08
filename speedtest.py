import os
import re
import subprocess
import time
import traceback

print('Speedtest: finding wifi SSID')

p = subprocess.Popen(
    ['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport', '-I'],
    stdout=subprocess.PIPE
)
wifi_output, err = p.communicate()

ssid = re.findall(' SSID:\s(.*?)\s', str(wifi_output), re.MULTILINE)[0].replace('\\n','')

print('Speedtest: executing...')

speedtest_response = subprocess.Popen(
    '/usr/local/bin/speedtest-cli --simple',
    shell=True,
    stdout=subprocess.PIPE
).stdout.read().decode('utf-8')

print('Speedtest: complete, parsing response')

ping = re.findall('Ping:\s(.*?)\s', speedtest_response, re.MULTILINE)
download = re.findall('Download:\s(.*?)\s', speedtest_response, re.MULTILINE)
upload = re.findall('Upload:\s(.*?)\s', speedtest_response, re.MULTILINE)

ping = ping[0].replace(',', '.')
download = download[0].replace(',', '.')
upload = upload[0].replace(',', '.')

print('Speedtest: opening write file')

try:
    f = open('/tmp/py-speedtest/speedtest.csv', 'a+')
    if os.stat('/tmp/py-speedtest/speedtest.csv').st_size == 0:
        f.write('Date,Time,SSID,Ping (ms),Download (Mbit/s),Upload (Mbit/s)\n')
except Exception as exc:
    print('Speedtest found an exception:')
    traceback.print_exception(type(exc), exc, exc.__traceback__)

print('Speedtest: writing result')

date_mmddyy = time.strftime('%m/%d/%y')
time24hr = time.strftime('%H:%M')
csv_format = f'{date_mmddyy},{time24hr},{ssid},{ping},{download},{upload}\n'
f.write(csv_format)
