# CS642-Spring-2020
 

| Week  | Date| Topic (Slides will be in  hyperlinks before lecture)| Required Reading | Optional Material|
| --- | --- | --- | --- | --- |
| 1  | 21-Jan | [Introduction: Logistics, Security Mindset,Threat Modeling](Slides/cs642-lecture1a-intro.pdf) | | [This World of Ours](https://www.usenix.org/system/files/1401_08-12_mickens.pdf) |
| | 23-Jan | [Basic Crypto: Randomness, Historical Ciphers,Alice-Bob Setting](Slides/cs642-lecture-2a-crypto-intro-sp20.pdf) | | |
| 2  | 28-Jan | [Basic Crypto: Symmetric Encryption, Modes ofOperation](Slides/cs642-lecture-3a-symmetric-encrypt-sp19.pdf) | [Cryptography Engineering, Chapters 1-4](https://onlinelibrary-wiley-com.ezproxy.library.wisc.edu/doi/pdf/10.1002/9781118722367) | |
| | 30-Jan | [Basic Crypto: MACs and Hashes](Slides/cs642-lecture4a-MACHashStart-sp19.pdf) | [Cryptography Engineering, Chapters 5, 6](https://onlinelibrary-wiley-com.ezproxy.library.wisc.edu/doi/pdf/10.1002/9781118722367) | [Why I Hate CBC-MAC](https://blog.cryptographyengineering.com/2013/02/15/why-i-hate-cbc-mac/) |
| |  | [HW1 Released: Crypto, Hashing](Slides/cs642-lecture4a-MACHashStart-sp19.pdf) | | |
| 3  | 4-Feb  | [Authentication: Passwords, MFA, Biometrics](Slides/CS642-UserAuthentication.pdf) | | [Password Thicket](http://www.preibusch.de/publications/Bonneau_Preibusch__password_thicket.pdf) |
| | 6-Feb  | [Basic Crypto: Asymmetric Setting, DH KeyExchange, some RSA](Slides/cs642-lecture5a-PKI-sp19.pdf) | [Cryptography Engineering, Chapters 11, 12](https://onlinelibrary-wiley-com.ezproxy.library.wisc.edu/doi/pdf/10.1002/9781118722367) | [Khan Academy Lecture](https://www.khanacademy.org/computing/computer-science/cryptography/modern-crypt/v/the-fundamental-theorem-of-arithmetic-1) |
| 4  | 11-Feb | [RSA and Signatures](Slides/CS642-RSA_Signatures.pdf) | [Cryptography Engineering, Chapters 11, 12](https://onlinelibrary-wiley-com.ezproxy.library.wisc.edu/doi/pdf/10.1002/9781118722367) | |
| |  | [Certificates](Slides/cs642-lecture5b-finishPKI-sp19.pdf) | | |
| | 13-Feb | [Web Security: Overview, Browser Security Model](Slides/cs642-lecture7a-WebSecurityOverviewBrowserModel-sp19.pdf) | | [Lessons from Google Chrome](http://www.adambarth.com/papers/2009/reis-barth-pizano.pdf) |
| |  | [Return HW1, HW2 Released: Web Security](Slides/cs642-lecture7a-WebSecurityOverviewBrowserModel-sp19.pdf) | | |
| 5  | 18-Feb | [Web Security: Web app security, XSS](Slides/cs642-lecture7b-WebAppSec-XSS-sp19.pdf) | [XSS Explained](http://pages.cs.wisc.edu/~rist/642-fall-2014/CSS.pdf) | [XSS Cheat Sheet](https://owasp.org/www-community/xss-filter-evasion-cheatsheet) |
| | 20-Feb | [Web Security: CSRF and SQL Injection](Slides/cs642-lecture7b-WebAppSec-XSS-sp19.pdf) | [CSRF Explained](https://owasp.org/www-community/attacks/csrf) | |
| 6  | 25-Feb | [Web Security: Misc Topics and Privacy](Slides/cs642-lecture7c-WebPrivacy-sp20.pdf) | [Clickjacking Explained](http://index-of.co.uk/Clickjacking/ijais12-450793.pdf) | |
| |  | [Return HW2](Slides/cs642-lecture7c-WebPrivacy-sp20.pdf) | | |
| |  | [Network Security: Trust in the Internet,Certificate Management, TLS](Slides/CS642-NetworkSecurity-Certificates.pdf) | [The first few milliseconds of an HTTPSConnection](http://www.moserware.com/2009/06/first-few-milliseconds-of-https.html) | |
| | 27-Feb | Guest Lecture: Rahul  Chatterjee| | |
| 7  | 3-Mar  | [Network Security: DNS, DNSsec, BGP](Slides/CS642_NetworkSecurity_DNSBGP.pdf) | [DNS Cache Poisoning Explained](http://unixwiz.net/techtips/iguide-kaminsky-dns-vuln.html) | |
| | 5-Mar  | [Network Security: ARP Spoofing](Slides/CS642-NetworkSec-IPARPSpoof.pdf) | | |
| 8  | 10-Mar | Midterm 1: Basic Crypto, Authentication,| [Review Notes](Slides/cs642_wi20_midterm1_review.pdf) | |
| |  | Web Security/Privacy,  Network Security | | |
| | 12-Mar | [Network Security: Wireshark, Firewall, IDS](Slides/CS642_NetworkSec_WiFiFirewallIDS.pdf) | | [Art of Instrusion](https://repo.zenk-security.com/Magazine%20E-book/Kevin_Mitnick_-_The_Art_of_Intrusion.pdf) |
| |  | [HW3 Released: Network Security](Slides/CS642_NetworkSec_WiFiFirewallIDS.pdf) | | |
| 9  | 17-Mar | Spring Break| | |
| | 19-Mar | Spring Break| | |
| 10 | 24-Mar | [Anonymity: Tor](Slides/CS642_Anonymity.pdf) | [How does Tor Work](https://robertheaton.com/2019/04/06/how-does-tor-work/) | [US Census 2020 and Differential Privacy](https://www.sciencemag.org/news/2019/01/can-set-equations-keep-us-census-data-private) |
| |  | [Return Midterm 1: Discussion](Slides/CS642_Anonymity.pdf) | | |
| | 26-Mar | [Tor and, OS Security: UNIX/Multics, TOCTOU,Access Control](Slides/CS642-OSSec.pdf) | | [Saltzer and Schroeder Principles](https://adam.shostack.org/blog/the-security-principles-of-saltzer-and-schroeder/) |
| 11 | 31-Mar | Remaining OS (same slides  as Mar 26) | | [Video Lectures on x86 and OS Basics](https://www.youtube.com/watch?v%3DMODo6C62oCc%26list%3DPLXWSQNiNZS9RChAFurt2MtDkRhE43TCVw) |
| | 2-Apr  | [Software Security: Buffer Overflow Part 1](Slides/CS642_SoftwareSecurity_StackSmash.pdf) | [Aleph One: Smashing the Stack for Fun andProfit](http://www-inst.eecs.berkeley.edu/~cs161/fa08/papers/stack_smashing.pdf) | [Chapter 11: Ethical Hacker's Handbook](http://pages.cs.wisc.edu/~swift/classes/cs642-sp19/wiki/uploads/Main/ReadingList/gray-hat-hacking.pdf) |
|  |  | [Return HW3](Slides/CS642_SoftwareSecurity_StackSmash.pdf) | | |
| |  |  [HW4 Released: OS Security and Buffer Overflow](Slides/CS642_SoftwareSecurity_StackSmash.pdf) | | |
| 12 | 7-Apr  | [Software Security: Integer Overflow, FormatString Vuln](Slides/cs642-FormatStringIntOverflow.pdf) | [Phrack: Integer Overflow](http://phrack.org/issues/60/10.html) | [Berkeley Notes](http://www-inst.eecs.berkeley.edu/~cs161/fa05/Notes/implflaws.pdf) |
| | 9-Apr  | NO CLASS | NO CLASS | NO CLASS |
| 13 | 14-Apr | [Software Security: Misc Topics: BufferOverflow Defenses](Slides/cs642-lecture8c-BufferOverflowDefenses-sp20.pdf) | [ASLR Redux, Program Analyzers and Fuzzing](Slides/CS642_SoftwareSecurity_FuzzingPgmAnalysis.pdf) | |
| | 16-Apr | [Mobile Security](Slides/cs642-MobileSecurity-sp20.pdf) | | |
| 14 | 21-Apr | Finish Mobile (same slides as Apr 16) | [Start ML Security](Slides/CS642-ML_Security.pdf) | |
|  |  |  Return HW4; HW5  Released | | |
| | 23-Apr | Finish ML Security (same  slides as Apr 21)| [IoT and HW 5 Intro](Slides/CS642-IoTLab.pdf) | |
| 15 | 28-Apr | Midterm 2: Tor, OS,  Software Sec, ML Sec, Mobile| [Review Notes](Slides/m2-study.pdf) | |
| | 30-Apr | [Usable Security, Wrap-up of Lecturing,Feedback!](Slides/cs642-UsableSec-sp20.pdf) | | |
| | 5-May  | Return HW5  | | |