import subprocess,os
ip_list = ['192.168.1.1','17.16.2.4','172.16.30.124',]
for ip in ip_list:
    result = subprocess.run(["ping", "-n", "1", ip], capture_output=True, text=True)

    if "TTL=" in result.stdout:
        print(f"IP address {ip} is reachable")
    else:
        print(f"IP address {ip} is unreachable")




        