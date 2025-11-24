# Telcolearn

Challenges Faced During Bidirectional Communication Project
 
--> Unable to establish connection between clien and server container images.
    It was later resolved by creating a network.

--> Capturing traffic packets and saving them as pcap/pcapng files as soon as the established connection is brokedown.
    Npcap was used to save pcap files directly.


Logs obtained using tail command for different commands in a Linux system
1. sudo apt update
2025-11-17T09:34:00.390659+00:00 Ubuntu systemd[1]: Starting apt-news.service - Update APT News...
2025-11-17T09:34:00.399518+00:00 Ubuntu systemd[1]: Starting esm-cache.service - Update the local ESM caches...
2025-11-17T09:34:00.582016+00:00 Ubuntu systemd[1]: apt-news.service: Deactivated successfully.
2025-11-17T09:34:00.582454+00:00 Ubuntu systemd[1]: Finished apt-news.service - Update APT News.
2025-11-17T09:34:01.925792+00:00 Ubuntu systemd[1]: esm-cache.service: Deactivated successfully.


2. rm -r d2
2025-11-17T10:09:29.878841+00:00 Ubuntu tracker-miner-fs-3[3626]: (tracker-extract-3:3626): GLib-GIO-WARNING **: 10:09:29.878: Error creating IO channel for /proc/self/mountinfo: Invalid argument (g-io-error-quark, 13)


3. mkdir new 

2025-11-17T10:11:00.602887+00:00 Ubuntu tracker-miner-fs-3[3661]: (tracker-extract-3:3661): GLib-GIO-WARNING **: 10:11:00.602: Error creating IO channel for /proc/self/mountinfo: Invalid argument (g-io-error-quark, 13)


4. ls -l projects/app.py
-rw-rw-r-- 1 vboxuser vboxuser 0 Nov 17 10:12 projects/app.py

5. chmod 750 projects/app.py

2025-11-17T10:14:31.818857+00:00 Ubuntu systemd[1]: systemd-tmpfiles-clean.service: Deactivated successfully.
2025-11-17T10:14:31.820287+00:00 Ubuntu systemd[1]: Finished systemd-tmpfiles-clean.service - Cleanup of Temporary Directories.
2025-11-17T10:15:01.055509+00:00 Ubuntu CRON[3714]: (root) CMD (command -v debian-sa1 > /dev/null && debian-sa1 1 1)

6. chmod a+x projects/app.py
2025-11-17T10:17:01.095510+00:00 Ubuntu CRON[3733]: (root) CMD (cd / && run-parts --report /etc/cron.hourly)
2025-11-17T10:17:32.772397+00:00 Ubuntu tracker-miner-fs-3[3736]: (tracker-extract-3:3736): GLib-GIO-WARNING **: 10:17:32.771: Error creating IO channel for /proc/self/mountinfo: Invalid argument (g-io-error-quark, 13)

7. sudo chown root/projects.app.py
2025-11-17T10:20:27.023997+00:00 Ubuntu rtkit-daemon[1247]: The canary thread is apparently starving. Taking action.
2025-11-17T10:20:27.024754+00:00 Ubuntu rtkit-daemon[1247]: Demoting known real-time threads.
2025-11-17T10:20:27.024883+00:00 Ubuntu rtkit-daemon[1247]: Successfully demoted thread 2476 of process 2445.
2025-11-17T10:20:27.025055+00:00 Ubuntu rtkit-daemon[1247]: Successfully demoted thread 2206 of process 2177.
2025-11-17T10:20:27.025218+00:00 Ubuntu rtkit-daemon[1247]: Successfully demoted thread 2215 of process 2185.
2025-11-17T10:20:27.025358+00:00 Ubuntu rtkit-daemon[1247]: Successfully demoted thread 2185 of process 2185.
2025-11-17T10:20:27.025482+00:00 Ubuntu rtkit-daemon[1247]: Successfully demoted thread 2208 of process 2173.
2025-11-17T10:20:27.025596+00:00 Ubuntu rtkit-daemon[1247]: Successfully demoted thread 2173 of process 2173.
2025-11-17T10:20:27.025693+00:00 Ubuntu rtkit-daemon[1247]: Successfully demoted thread 2195 of process 2182.
2025-11-17T10:20:27.025819+00:00 Ubuntu rtkit-daemon[1247]: Successfully demoted thread 2182 of process 2182.
2025-11-17T10:20:27.025942+00:00 Ubuntu rtkit-daemon[1247]: Demoted 8 threads.
2025-11-17T10:20:31.373173+00:00 Ubuntu kernel: clocksource: Long readout interval, skipping watchdog check: cs_nsec: 8022630082 wd_nsec: 8022627385


8. sudo chgrp root  app.py

2025-11-17T10:23:40.166252+00:00 Ubuntu rtkit-daemon[1247]: The canary thread is apparently starving. Taking action.
2025-11-17T10:23:40.174359+00:00 Ubuntu rtkit-daemon[1247]: Demoting known real-time threads.
2025-11-17T10:23:40.174773+00:00 Ubuntu rtkit-daemon[1247]: Successfully demoted thread 2476 of process 2445.
2025-11-17T10:23:40.174821+00:00 Ubuntu rtkit-daemon[1247]: Successfully demoted thread 2206 of process 2177.
2025-11-17T10:23:40.174857+00:00 Ubuntu rtkit-daemon[1247]: Successfully demoted thread 2215 of process 2185.
2025-11-17T10:23:40.174893+00:00 Ubuntu rtkit-daemon[1247]: Successfully demoted thread 2185 of process 2185.
2025-11-17T10:23:40.174929+00:00 Ubuntu rtkit-daemon[1247]: Successfully demoted thread 2208 of process 2173.
2025-11-17T10:23:40.174965+00:00 Ubuntu rtkit-daemon[1247]: Successfully demoted thread 2173 of process 2173.
2025-11-17T10:23:40.175010+00:00 Ubuntu rtkit-daemon[1247]: Successfully demoted thread 2195 of process 2182.
2025-11-17T10:23:40.175043+00:00 Ubuntu rtkit-daemon[1247]: Successfully demoted thread 2182 of process 2182.
2025-11-17T10:23:40.175085+00:00 Ubuntu rtkit-daemon[1247]: Demoted 8 threads.