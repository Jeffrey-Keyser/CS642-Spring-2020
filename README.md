# CS 642 (Spring 2020): Introduction to Information Security @ UW-Madison

# Links

- [GitHub Repo](https://github.com/ShawnZhong/CS642-Spring-2020)

- [GitHub Pages](https://shawnzhong.github.io/CS642-Spring-2020/)

- [Course Homepage](https://pages.cs.wisc.edu/~earlence/cs642sp20.html)

- [Course Homepage (Fall 2019)](https://canvas.wisc.edu/courses/168496)

 
## Homeworks

| HWs | Tasks | Files | 
| --- | --- | --- | 
| [HW1.pdf](HW1/HW1.pdf) |  Part A: Password Cracking <br> Part B: Encryption <br> Extra: More Password Cracking | [cracking_simple.py](HW1/cracking_simple.py) <br> [attack.py](HW1/attack.py) <br> [cracking_extra.py](HW1/attack.py) |
| [HW2.pdf](HW2/HW2.pdf) | Attack A: Cookie Theft <br> Attack B: Cross-Site Request Forgery <br> Attack C: SQL Injection | [a.txt](HW2/a.txt) <br> [b.html](HW2/b.html) <br> [c.html](HW2/c.html) | 
| [HW3.pdf](HW3/HW3.pdf) | Part 1: Wireshark Packet Trace <br> Part 2: Attack Detection | [solutions.txt](HW3/1_wireshark/solutions.txt) <br> [scanner.py](HW3/2_attack/scanner.py)
| [HW4.pdf](HW4/HW4.pdf) | Buffer Overflow | [sploit0.c](HW4/sploits/sploit0.c) <br> [sploit1.c](HW4/sploits/sploit1.c) <br> [sploit2.c](HW4/sploits/sploit2.c) <br> [sploit3.c](HW4/sploits/sploit3.c) <br> [sploit4.c](HW4/sploits/sploit4.c)
| [HW5.pdf](HW5/HW5.pdf) | 

## Class Schedule

| Week  | Date | Topic | Required Reading | Optional Material|
| --- | --- | --- | --- | --- |
| 1  | 1/21 | [Introduction: Logistics, Security Mindset, Threat Modeling](Slides/cs642-lecture1a-intro.pdf) | | [This World of Ours](https://www.usenix.org/system/files/1401_08-12_mickens.pdf) |
| | 1/23 | [Basic Crypto: Randomness, Historical Ciphers, Alice-Bob Setting](Slides/cs642-lecture-2a-crypto-intro-sp20.pdf) | | |
| 2  | 1/28 | [Basic Crypto: Symmetric Encryption, Modes of Operation](Slides/cs642-lecture-3a-symmetric-encrypt-sp19.pdf) | [Cryptography Engineering, Chapters 1-4](https://onlinelibrary-wiley-com.ezproxy.library.wisc.edu/doi/pdf/10.1002/9781118722367) | |
| | 1/30 | [Basic Crypto: MACs and Hashes <br> HW1 Released: Crypto, Hashing](Slides/cs642-lecture4a-MACHashStart-sp19.pdf) | [Cryptography Engineering, Chapters 5, 6](https://onlinelibrary-wiley-com.ezproxy.library.wisc.edu/doi/pdf/10.1002/9781118722367) | [Why I Hate CBC-MAC](https://blog.cryptographyengineering.com/2013/02/15/why-i-hate-cbc-mac/) |
| 3  |2/4  | [Authentication: Passwords, MFA, Biometrics](Slides/CS642-UserAuthentication.pdf) | | [Password Thicket](http://www.preibusch.de/publications/Bonneau_Preibusch__password_thicket.pdf) |
| |2/6  | [Basic Crypto: Asymmetric Setting, DH KeyExchange, some RSA](Slides/cs642-lecture5a-PKI-sp19.pdf) | [Cryptography Engineering, Chapters 11, 12](https://onlinelibrary-wiley-com.ezproxy.library.wisc.edu/doi/pdf/10.1002/9781118722367) | [Khan Academy Lecture](https://www.khanacademy.org/computing/computer-science/cryptography/modern-crypt/v/the-fundamental-theorem-of-arithmetic-1) |
| 4  | 2/11 | [RSA and Signatures](Slides/CS642-RSA_Signatures.pdf) <br> [Certificates](Slides/cs642-lecture5b-finishPKI-sp19.pdf) | [Cryptography Engineering, Chapters 11, 12](https://onlinelibrary-wiley-com.ezproxy.library.wisc.edu/doi/pdf/10.1002/9781118722367) | |
| | 2/13 | [Web Security: Overview, Browser Security Model <br> Return HW1, HW2 Released: Web Security](Slides/cs642-lecture7a-WebSecurityOverviewBrowserModel-sp19.pdf) | | [Lessons from Google Chrome](http://www.adambarth.com/papers/2009/reis-barth-pizano.pdf) |
| 5  | 2/18 | [Web Security: Web app security, XSS](Slides/cs642-lecture7b-WebAppSec-XSS-sp19.pdf) | [XSS Explained](http://pages.cs.wisc.edu/~rist/642-fall-2014/CSS.pdf) | [XSS Cheat Sheet](https://owasp.org/www-community/xss-filter-evasion-cheatsheet) |
| | 2/20 | [Web Security: CSRF and SQL Injection](Slides/cs642-lecture7b-WebAppSec-XSS-sp19.pdf) | [CSRF Explained](https://owasp.org/www-community/attacks/csrf) | |
| 6  | 2/25 | [Web Security: Misc Topics and Privacy <br> Return HW2](Slides/cs642-lecture7c-WebPrivacy-sp20.pdf) <br> [Network Security: Trust in the Internet, Certificate Management, TLS](Slides/CS642-NetworkSecurity-Certificates.pdf) | [Clickjacking Explained](http://index-of.co.uk/Clickjacking/ijais12-450793.pdf) <br> [The first few milliseconds of an HTTPSConnection](http://www.moserware.com/2009/06/first-few-milliseconds-of-https.html)| |
| | 2/27 | Guest Lecture: Rahul  Chatterjee| | |
| 7  |3/3  | [Network Security: DNS, DNSsec, BGP](Slides/CS642_NetworkSecurity_DNSBGP.pdf) | [DNS Cache Poisoning Explained](http://unixwiz.net/techtips/iguide-kaminsky-dns-vuln.html) | |
| |3/5  | [Network Security: ARP Spoofing](Slides/CS642-NetworkSec-IPARPSpoof.pdf) | | |
| 8  | 3/10 | Midterm 1: Basic Crypto, Authentication, Web Security/Privacy,  Network Security| [Review Notes](Slides/cs642_wi20_midterm1_review.pdf) | |
| | 3/12 | [Network Security: Wireshark, Firewall, IDS <br> HW3 Released: Network Security](Slides/CS642_NetworkSec_WiFiFirewallIDS.pdf) | | [Art of Instrusion](https://repo.zenk-security.com/Magazine%20E-book/Kevin_Mitnick_-_The_Art_of_Intrusion.pdf) |
| 9  | 3/17 | Spring Break| | |
| | 3/19 | Spring Break| | |
| 10 | 3/24 | [Anonymity: Tor <br> Return Midterm 1: Discussion](Slides/CS642_Anonymity.pdf) | [How does Tor Work](https://robertheaton.com/2019/04/06/how-does-tor-work/) | [US Census 2020 and Differential Privacy](https://www.sciencemag.org/news/2019/01/can-set-equations-keep-us-census-data-private) |
| | 3/26 | [Tor and, OS Security: UNIX/Multics, TOCTOU, Access Control](Slides/CS642-OSSec.pdf) | | [Saltzer and Schroeder Principles](https://adam.shostack.org/blog/the-security-principles-of-saltzer-and-schroeder/) |
| 11 | 3/31 | Remaining OS (same slides  as Mar 26) | | [Video Lectures on x86 and OS Basics](https://www.youtube.com/watch?v%3DMODo6C62oCc%26list%3DPLXWSQNiNZS9RChAFurt2MtDkRhE43TCVw) |
| | 4/2  | [Software Security: Buffer Overflow Part 1 <br> Return HW3 <br> HW4 Released: OS Security and Buffer Overflow](Slides/CS642_SoftwareSecurity_StackSmash.pdf)| [Aleph One: Smashing the Stack for Fun andProfit](http://www-inst.eecs.berkeley.edu/~cs161/fa08/papers/stack_smashing.pdf) | [Chapter 11: Ethical Hacker's Handbook](http://pages.cs.wisc.edu/~swift/classes/cs642-sp19/wiki/uploads/Main/ReadingList/gray-hat-hacking.pdf) |
| 12 | 4/7  | [Software Security: Integer Overflow, FormatString Vuln](Slides/cs642-FormatStringIntOverflow.pdf) | [Phrack: Integer Overflow](http://phrack.org/issues/60/10.html) | [Berkeley Notes](http://www-inst.eecs.berkeley.edu/~cs161/fa05/Notes/implflaws.pdf) |
| | 4/9  | NO CLASS | NO CLASS | NO CLASS |
| 13 | 4/14 | [Software Security: Misc Topics: BufferOverflow Defenses](Slides/cs642-lecture8c-BufferOverflowDefenses-sp20.pdf) | [ASLR Redux, Program Analyzers and Fuzzing](Slides/CS642_SoftwareSecurity_FuzzingPgmAnalysis.pdf) | |
| | 14/6 | [Mobile Security](Slides/cs642-MobileSecurity-sp20.pdf) | | |
| 14 | 4/21 | Finish Mobile (same slides as Apr 16)  <br> Return HW4; HW5  Released | [Start ML Security](Slides/CS642-ML_Security.pdf) | |
| | 4/23 | Finish ML Security (same  slides as Apr 21)| [IoT and HW 5 Intro](Slides/CS642-IoTLab.pdf) | |
| 15 | 4/28 | Midterm 2: Tor, OS,  Software Sec, ML Sec, Mobile| [Review Notes](Slides/m2-study.pdf) | |
| | 4/30 | [Usable Security, Wrap-up of Lecturing, Feedback!](Slides/cs642-UsableSec-sp20.pdf) | | |
| | 5/5  | Return HW5  | | |
