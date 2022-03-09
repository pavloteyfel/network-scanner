# Simple Python Network Scanner

For Windows 10 Winpcap is required.

## Example Usage

```shell
python3 -m nscan -h
python3 -m nscan 192.168.0.0/24
```

Output
```
Begin emission:
Finished sending 256 packets.
***............*...........
Received 27 packets, got 4 answers, remaining 252 packets

IP Address		 MAC Address
------------------------------------------
192.168.0.1 		 ac:22:05:4f:f9:1f
192.168.0.95 		 b8:27:eb:fa:1f:27
192.168.0.136 		 4c:79:6e:57:21:91
192.168.0.150 		 28:16:ad:30:cc:a8
```