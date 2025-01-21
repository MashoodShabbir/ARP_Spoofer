# ARP Spoofer

This Python script allows users to perform ARP (Address Resolution Protocol) spoofing, a technique often used in penetration testing and ethical hacking to monitor or intercept network traffic between two devices.

## Features
- Retrieve MAC Addresses: Automatically fetch the MAC address of a target device.
- ARP Spoofing: Send malicious ARP packets to mislead the target device about the MAC address of another device.
- ARP Cache Restoration: Restore the ARP cache on the target devices when the script is stopped.
- Interactive Feedback: Provides real-time feedback on the number of packets sent.

## Requirements

To run this script, you need:

- Python 3.6+
- Scapy library

Install the Scapy library using pip if it's not already installed:
```bash
pip install scapy
```

## How to Use

1. Clone the repository or download the script:
```bash
git clone https://github.com/MashoodShabbir/ARP_Spoofer.git
```

2. Navigate to the directory containing the script:
```bash
cd ARP_Spoofer
```

3. Run the script with Python, providing the target and spoof IP addresses using the -t or --target and -s or --spoof flags:
```bash
python arp_spoofer.py -t <target_ip> -s <spoof_ip>
```
Example:
```bash
python arp_spoofer.py -t 192.168.1.100 -s 192.168.1.1
```

4. When running the script, you'll see output similar to this:
```bash
[+] Packets sent: 2
[+] Packets sent: 4
[+] Packets sent: 6
```
When the script is stopped with CTRL + C, it will restore the ARP cache on the target devices:
```bash
[+] Detected CTRL + C ........ Restoring ARP Cache on targets.
```

## Arguments
-t, --target: Specifies the target IP address whose ARP cache will be spoofed.
-s, --spoof: Specifies the IP address to impersonate.


## Important Notes
- **Run as Administrator**: This script requires administrative privileges to send ARP requests. Make sure to run it with appropriate permissions.
- **Ethical Use Only: Ensure you have permission to perform ARP spoofing on the target network. Unauthorized use may violate policies or regulations.
- **Use Responsibly**: Ensure you have permission to scan any network before using this script. Unauthorized network scanning may be illegal.
- **Network Impact: ARP spoofing can disrupt network communication. Use responsibly and only for testing or educational purposes.
---
Thank you for exploring this project! This script demonstrates practical Python skills and an understanding of networking concepts. Feel free to contribute or provide feedback.

