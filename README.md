```
.venv ❯ cat ipaddress.txt
192.168.0.100
192.168.3.10
192.168.10.10
172.16.10.1
172.16.20.1
10.121.0.5
10.121.10.5

~/work/check_ip_in_range master
.venv ❯ cat iprange.txt
192.168.0.1,192.168.0.254
192.168.3.1,192.168.3.254

~/work/check_ip_in_range master
.venv ❯ 

~/work/check_ip_in_range master
.venv ❯ python src/main.py
192.168.0.100,192.168.0.1,192.168.0.254
192.168.3.10,192.168.3.1,192.168.3.254
192.168.10.10
172.16.10.1
172.16.20.1
10.121.0.5
10.121.10.5
```
