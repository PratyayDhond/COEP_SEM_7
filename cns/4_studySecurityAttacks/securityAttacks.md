Study various security attacks...
Select anyone attack and do the following:
1. Study Various pinpointed types/ classification of that attacks
2. Study current status of that attack
3. Study and analyse existing various solutions for that attack 
4. Innovate, Suggest or modify existing solution by implementation or simulation

---

Various Security Attacks:
1. Malware 
2. Phishing
3. Man in the Middle
4. SQL Injection
5. Denial-of-service and DDOS
6. Insider Threat
7. Cryptojacking
8. Cross-site scripting

---

Selected Attack : Denial of service | Archieve.org

Archive.org, the digital library known for preserving web content and cultural artifacts, experienced a significant DDoS attack. This attack aimed to disrupt access to its vast collection of archived websites, books, and media.


1. Study Various pinpointed types/classifications of that attack:
->
Denial of Service (DoS) attacks can be classified into the following types:
1. Volume-Based Attacks: Flood the network with excessive traffic (e.g., UDP floods, ICMP floods).
2. Protocol Attacks: Exploit weaknesses in protocols (e.g., SYN floods, Ping of Death).
3. Application Layer Attacks: Target specific applications (e.g., HTTP floods, Slowloris).
4. Distributed Denial of Service (DDoS): Involves multiple compromised systems attacking a single target.
    - DNS Amplification: Exploits misconfigured DNS servers to send large responses to the target.
    - NTP Amplification: Uses Network Time Protocol servers to flood the target with excessive data

2. current status of that attack:
->
- As of the latest updates, the DDoS attacks on Archive.org and OpenLibrary.org have continued, causing the sites to remain offline.
- Internet Archive founder Brewster Kahle confirmed in a tweet on October 11 that the DDoS attacks had returned, and the sites were taken offline as a precautionary measure to prioritize data safety.
- The DDoS attacks are ongoing, and the Internet Archive is prioritizing securing its data over restoring service availability.

3. Study and analyse existing various solutions for that attack
->
DDoS attack mitigation and management solutions include:

1. Traffic Filtering: Identifying and blocking malicious traffic at the network level.
    - Involves analyzing incoming traffic to identify and block malicious requests.
    -  firewalls and intrusion detection systems (IDS) to filter out known attack patterns and traffic anomalies.
2. Rate Limiting: Restricting the amount of traffic accepted from a single source.
    - Restricts the number of requests a single source can make in a given timeframe.
    - Configure servers and web applications to limit request rates, helping to prevent abuse from individual IPs
3. Load Balancing: Distributing traffic across multiple servers to prevent overload.
    - Distributes incoming traffic across multiple servers to balance the load and reduce the risk of any single server being overwhelmed
    - Use hardware or software load balancers that can redirect traffic to healthy servers during an attack.
4. Content Delivery Networks (CDNs): Using CDNs to absorb and disperse traffic.
    - CDNs cache content at multiple locations worldwide, absorbing and dispersing traffic loads
    - Integrate with a CDN provider to mitigate DDoS attacks by spreading traffic across their extensive networks.
5. DDoS Protection Services: Leveraging third-party services specialized in DDoS mitigation.
    - Third-party services specialize in detecting and mitigating DDoS attacks
    - Partner with providers like Cloudflare, Akamai, or AWS Shield that offer dedicated DDoS protection and scrubbing services to filter out malicious traffic before it reaches your servers.
6. Incident Response Plans: Developing and practicing response strategies for potential attacks
    - Preparing a comprehensive plan to respond to DDoS attacks when they occur.
    - Develop and regularly update an incident response strategy, including roles and responsibilities, communication protocols, and recovery procedures. Conduct drills to ensure readiness.

A combination of the above strategies is generally recommended as there is no one-size-fits-all solution in tech.

4. Innovate, Suggest or modify existing solution by implementation or simulation
->


--- 
FootNotes and References
- https://en.wikipedia.org/wiki/Denial-of-service_attack
- https://emeritus.org/in/learn/different-types-of-cyber-security-threats/
