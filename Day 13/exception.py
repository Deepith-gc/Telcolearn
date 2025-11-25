import logging
logging.basicConfig(filename='log.txt',level=logging.DEBUG)
logging.debug("This is debug information")
logging.info("info Information")
logging.warning('warning Information')
logging.error('error Information')
logging.critical('critical Information')

import subprocess

ip_list = ['192.168.1.1', '17.16.2.4', '172.16.30.124','172.16.30.1','8.8.8.8']

for ip in ip_list:
    try:
        result = subprocess.run(["ping", "-n", "1", ip], capture_output=True, text=True)
        output = result.stdout

        # Check if host reachable
        if "TTL=" in output:
            # Extract time from output
            # Windows format example: time=23ms
            start = output.find("time=")
            end = output.find("ms", start)
            time_ms = float(output[start+5:end])

            # Check if slow
            if time_ms > 0.5:
                print(f"{ip}: Slow ping ({time_ms} ms)")
            else:
                print(f"{ip}: Reachable ({time_ms} ms)")
        else:
            print(f"{ip}: Unreachable")

    except Exception as e:
        print(f"{ip}: Error occurred")
