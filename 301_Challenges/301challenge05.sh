#!/bin/bash

wc -c /var/log/syslog
wc -c /var/log/wtmp

date=$(date "+%Y-%m-%d%H:%M:%S")

gzip /var/log/syslog -c > /home/andrew/cybersecurity/301_Challenges/backup/syslog-$date.gz
gzip /var/log/wtmp -c > /home/andrew/cybersecurity/301_Challenges/backup/wtmp-$date.gz

