# SY0-701 CompTIA Security+

## Block 1: Fundamentals and CIA

### CIA Triad

- Confidentiality: safegaurds information from unathorized access and disclosure.
- Integrity: ensures data remains accurate and trustworthy.
- Availability: ensures data and systems are available to authorized users when needed.

### Non-Repudiation

Ensures that someone cannot deny the validity of something, such as authorship of a statement.

### AAA Framework

- Authentication: ensures the validity of someone's identity and prevents unauthorized access.
- Authorization: determines what actions user are allowed to perform after they have been authenticated.
- Accounting: involves tracking and recording users' activities and resource use.

### Gap Analysis

Gap Analysis is a strategic planning tool used to evaluate differences between the current state and an ideal/desired state.

- Helps pinpoint deficiencies in cyber-security measures, whether in tech, software, policy enforcement, or personnel training.
- Enables organizations to address and close these gaps.

### Control Categories

- Technical Controls
- Managerial Controls
- Operational Controls
- Physical Controls

#### Technical/Logical Controls

Technical controls are logical controls implemented by a computer.

Examples:

- Authentication
- Access Control
- Auditing
- Cryptography
- Firewalls
- Session Locks
- Radius Servers
- RAID 5

#### Managerial Controls

Managerial controls reflect decisons made by an organization's managers and executives. These controls focus on risk management and how data is adminstrated.

Examples:

- Security policies and procedures
- Personnel background checks
- Security awareness training
- Formal change-management procedures

#### Operational Controls

Operational controls are carried out by people (rather than technical systems) to enhance individual group system security.

Examples:

- User training
- Computer support
- Baseline configuration development
- Facility design details
- Environmental security measures
- Incident handling procedures
- Disaster recovery plans

#### Physical Controls

Physical controls serve as the first line of defense in controlling access to an organization.

Examples:

- Ensuring entrances are secure
- Securing physical equipment
- Logging and surveilling visitors

### Control Types

- Preventative
- Deterrent
- Detective
- Corrective
- Compensating
- Directive

#### Preventative

Preventative controls are proactively implemented to thwart incidents before they occur.

Examples:

- Access Lists
- Passwords
- Fences

#### Deterrent

Deterrent controls aim to deter the thrat actors from launching offensive assaults on an organization's environments.
Similar to preventative controls, but deterrent controls focus on discouraging attackers solely because the control exists.

Examples:

- Alarm system signs
- Web banner warning about unathorized login attempts being logged

#### Detective

Detective controls are designed to detect and monitor unathorized behaviors and other hazards.
They issue alerts about failures in other controls; valuable during an attack and post-incident analysis.

#### Corrective

Corrective controls are meant to be implemented after an incident to limit damage and facilitate quick recovery.

Examples:

- Tape backup
- Hot sites
- Quarantining an infected computer

#### Compensating

Compensating controls are implemented to meet security requirements that are impractical or too challenging to implement.

- Alternatives to costly or difficult to deploy security measures
- Use with caution as they do not provide the same level of security as replaced controls

#### Directive

Directive controls guide the operation and use of systems within an organization
They direct individuals toward secure behavior and establish security conscious culture.

Examples:

- Standards
- Procedures
- Policy guidelines
- Security awareness training

## Block 2: Authentication and Access Controls

### Provisioning/De-Provisioning User Accounts

Provisioning: Setting up a user account with necessary permissions and access settings.
De-provisioning: Disabling or removing permissions and settings from a user account.

Well managed provisioning/de-provisioning are crucial for ensuring users always have appropriate access.

### Permission Assignments and Implications

Permission assignment: Granting specific levels of access or activities (read, edit, delete) to users, groups, or system processes.

Types of permission assignments:

- User level
- Group level
- Role based
- Resource based

### Identity proofing

Identity proofing is the process of verifying a user's or system's identity within an organization.
Involves multiple levels of authentication from passwords to biometrics.

### Federation

Federation: One system authenticates users and sends their authentication information to other systems.

### Centralized vs Decentralized

Centralized access control:

- one entity responsible for administering access to resources
- characterized by consoloidating control, data storage, and processing in a single location or server.
- offers uniformity and consistency

Decentralized access control:

- more than one entity is responsible for administering access to resources

### Single Sign On (SSO)

Single sign on enables one set of credentials for access to multiple services or applications.

SSO Protocols:

- LDAP: Lightweight Directory Access Protocol
- OAuth: Open Authorization
- SAML: Security Assertion Markup Language

### Interoperability

Interoperability is the ability of different systems to work together. It's crucial for identity and access management (IAM) systems.

IAM systems need to integrate seamlessly with various databases, applications, and authentication protocols. Lack of integration interferes with needs for access and auditing.

### Attestation

Attestation provides evidence or proof, allowing one program or system to authenticate itself to another.

Remote attestation enables a system to make reliable statements about the software its running to another system, which can make authorization decisions based on that information.

A TPM (Trusted Platform Model) quote operation verifies the contents of a TPM chip's platform configuration registers (PCRs) during provisioning.

Methods of attestation may be vulnerable to replay attacks, masquerading, and other cyber threats.

### Access Controls

Access controls organize and manage admission to physical areas and computer systems.

#### Role Based Access Control (RBAC)

RBAC is controlled by the system, not the resource owner. When a user is assigned a role, they get access to its resources.

#### Rule Based Access Control

Rule based access control is also known as label-based access control. Example: A rule governing access->During certain hours each day, only certain IP addresses may have access.

#### Mandatory Access Control (MAC)

MAC is the strictest control.

### Multi-Factor Authentication (MFA)

MFA is the process of authenticating a user by validating two or more claims from different categories of factors.

Factor categories:

- something you know
- something you have
- something you are

Biometrics (distinctive body measurements) and security keys (hardware devices) may be a part of MFA.

#### 2-Factor Authentication

A subset of MFA in which two factors are required to authenticate.

### Password Concepts

Password concepts are guidelines and practices for ensuring strong, secure passwords.

Passwords serve as the primary barrier to protect sensitive information and access controls

Issues to consider when setting password requirements:

- Password length
- Password complexity
- Password reuse
- Password expiration
- Password age

### Privileged Access Management (PAM) Tools

PAM tools centrally manage access to privileged accounts based on the principle of least privilege.

Just-in-time (JIT) permissions: give access for a limited time.
Ephemeral credentials are generated for specific sessions or tasks and invalidated shortly after completion. They expire more quickly than JIT permissions.
Password vaulting means using a centralized, encrypted repository to store various access credentials.

### Permissions

Permissions define the rights to perform actions on a system and are associated with files, directories, or processes.

In windows, permissions are managed using security identifiers (SID) and ACLs
In Linux, file permissions are represented symbolically or numerically. Linux has fewer permissions than windows.

Best practices for permissions include granting them to security groups rather than individual users and using central management for easier control.

### Least Privilege

The principle of least privilege advocates for granting individuals or systems only the necessary access or permissions to perform their tasks.

## Block 3: Cryptography Deep Dive

### Encryption

Converts information into a coded format to prevent unauthorized access.

Different levels of encryption offer varying degrees of protection

- Full-disk: secures an entire hard drive.
- Partition:
- File:

### Transport/Communication

Data security and encryption are essential, whether the data is at rest, in transit, or in use.

### Algorithms, Key Length, and Tools

Algorithms: Mathematical formulas used in cryptographic processes
Key length: The number of bits in an encryption algorithm's key; longer keys typically provide stronger encryption
Tools: Specialized technologies and protocols for securing and managing digital information throughout its lifecycle

### Symmetric vs Asymmetric Encryption

#### Symmetric Encryption

Symmetric encryption uses a single key for both encryption and decryption.

#### Asymmetric Encryption

Asymmetric Encryption uses a pair of keys: A public key for encryption and a private key for decryption.

### Trusted Platform Module and Hardware Security Module

#### Trusted Platform Module (TPM)

A hardware based security technology using a secure cryptoprocessor chip to execute cryptographic operations, generate and manage cryptographic keys, authenticate platform devices, and ensure platform integrity by storing security measurements.

#### Hardware Security Module (HSM)

A physical device serving as a secure cryptoprocessor, providing faster encryption than software based solutions, and generally tamper proof

### Hashing and Salting

#### Hashing

Hashing is a one way function that maps data to a fixed length value, primarily for authentication and ensuring data integrity by verifying that it hasn't been altered.

The output of hashing is a 'checksum': a sequence of numbers generated by a checksum (hashing) algorithm.

#### Salting

Salting is adding random data to a password before hashing to enhance security.

#### Peppering

Similar to salting, but added to the end rather than the beginning of a password.

##### Hashing vs Encryption

Hashing promotes integrity, Encryption promotes authentication.

### Digital Signatures

A digital signature is a mathematical scheme used to verify the authenticity and integrity of a digital message or document.

Three algorithms used in a digital signature: Key-generation algorithm, signing algorithm, signature verifying algorithm.

Two properties required for a digital signature: Authenticity verification, private key.

### Public Key Infrastructure (PKI)

PKI encompasses key management, Certificate Authorities (CAs), intermediate CAs, and Registration Authorities (RAs).

PKI enables secure connections for websites, email transmissions, and remote access by utilizing asymmetric key pairs consisting of public and private keys.

Private keys are kept secret, while public keys can be distributed. Private key escrow may be provided by trusted third parties.

### Key Exchange

Key Exchange, also known as key establishment, is a cryptographic process that enables two parties to exchange crypographic keys.

### Key Management System (KMS)

A KMS safeguards digital data by managing codes used to lock and unlock data.

Main Functions:

- Generates cryptographic keys
- Stores keys securely
- Exchanges keys
- Key use and access control
- Key replacement and rotation

### Secure Enclave

A secure enclave is a hardware based feature found in devices like iphones.

It segregates encryption tasks and runs on a seperate microprocessor with its own operating system.

Designed to resist tampering, it prevents access to its data through strict protocols.

The enclave is resistant to software and hardware attacks.

### Obfuscation and Steganography

#### Obfuscation

Obfuscation is a technique used to protect sensitive information by altering or diwguising the original data to prevent easy comprehension or access by unauthorized users.

#### Steganography

Steganography is the practice of concealing secret messages within seemingly innocous carriers (Audio, Video, Image)

### Key Stretching

Key stretching is a cryptographic technique used to enhance the security of weak keys against brute force attacks.

Salt: randomly generated data added to a password before hashing to prevent the same password from producing the same hash value.

Pepper: Another randomly generated value added to a password hash kept secret and separate from the hashed password.

### Blockchain and Open Public Ledger

#### Blockchain

Blockchain is a secure and immutable digital ledger technology that records transactions across a network of computer systems in a decentralized manner.

#### Open Public Ledger

Open public ledger is a component of blockchain technology that organizes transaction information into blocks that are chained together chronologically.

### Certificates

Certificate: a digital document issued by a CA (Certificate Authority) to verify the identity of the certificate holder and ensure the legitimacy of online communications.

### Certificate Authorities

CAs are entities, typically servers, responsible for issuing certificates to users in a PKI (Public Key Infrastructure) system, serving as a trusted third party to validate identities and secure digital exchanges

## Block 4: Network Security Architecture

### Network Infrastructure

Encompasses an organizations essential hardware and software for network connectivity, communication, operations, and management.

### Security Zones

Security zones are segregated areas in a network under specific security policies and controls.

#### Internal Zones

Internal zones are trusted segments in which sensitive or internal data is processed.

#### External Zones

External zones are areas allowing connections from public internet or other untrusted networks.

#### Screened Subnet

Screened subnet is a specialized external zone that isolates public facing services from the internet

#### Specialized Zones

Specialized zones are designed to meet regulatory compliance requirements

### Attack Surface

An attack surface is all the vulnerabilities and potential access points an attacker could use to gain access to the system.

### Connectivity

How networks, systems, and applications connect and communicate

### Failure Modes

#### Fail-open Configuration

System remains available if a portion fails

#### Fail-closed configuration

Entire system becomes inaccessible if a portion fails

### Device Attribute

A device attribute is a characteristic determining device operation in a network environment

#### Active vs Passive

Active/active: devices share workload simultaneously; critical for fail over or load balancing.

Active/passive: One device active, another on standby: passive activates if active fails or manually switched.

#### Inline monitoring vs tap/monitor mode

Inline monitoring: device is placed directly in the traffic flow, allowing active intervention.

Tap/monitor mode: device observes traffic without interfering.

### Network Appliances

Essential for network functionality, security, and efficiency

### Port Security

Port security is vital for safeguarding network access and preventing unauthorized devices from communicating through network ports.

The 802.1x authentication standard provides port based network access control

Extensible Authentication Protocol (EAP) is a universal authentication framework that defines message formats. It is frequently used with 802.1x. Generally found on enterprise networks.

### Firewall Types

A firewall is a network security device or software that acts as a barrier between a trusted internal network and untrusted external networks, such as the internet

#### Firewall

A firewall is a network security device or software that monitors incoming and outgoing network traffic

- Firewall rules control the flow of data packets
- Access Control Lists (ACL) govern how traffic flows through the network.
- Ports are virtual docks where network services can receive data
- Protocols are rules and conventions governing data transmission and acceptance
- A screened subnet is a segment that seperates the internal network from an external network

### IDS/IPS

Intrusion Detection Systems monitor and issue alerts about suspicious activities.

Intrusion Prevention Systems are proactive; they block known or potential threats.

These systems used predefined signatures to identify threats

Trends identified in analyses of logs can indicate the presence of new vulnerabilities

### OSI Model vs TCP/IP Model

OSI Application, Presentation, Session layers map onto TCP/IP Application layer

OSI Transport maps onto Transport TCP/IP layer

OSI Network layer maps onto TCP/IP Internet layer

OSI Data link and Physical layers map onto TCP/IP Link layer

## Block 5: Cloud Security Fundamentals

### Cloud Computing

Cloud computing offers on demand services that extend computer or network capabilities

### Virtualization

Virtualization technology is the creation of virtual instances of physical hardware. Vulnerabilities may lead to unauthorized use of virtual resources

#### VM Escape

Virtual Machine escape occurs when an attacker breaks out of a virtual machine to access the host system

#### Resource Reuse

Resource reuse involves sharing physical resources among multiple virtual instances, introducing the risk of data leaks between virtual environments

### Cloud Specific Services

SaaS (Software as a Service)
IaaS (Infrastructure as a Service)
PaaS (Platform as a Service)
SECaaS (Security as a Service)

### Cloud Environments

In cloud computing, availability is often determined by the storage class

### Multi-Cloud System

A multi cloud system involves using multiple cloud service platforms to fulfill diverse computational and storage needs

### Cloud Specific Environments

#### Public

Applications and storage are offered to the general public over the internet

#### Private

Designed for a particular organization and gives the security administrator some control over data and infrastructure

#### Hybrid

Mixing elements of public and private clouds

#### Community

Multiple organizations can share the public portion of a public/private mix

### Infrastructure as Code (IaC)

IaC involves managing and provisioning computer data centers through machine readable definition files

### Serverless Architecture

Serverless architecture uses cloud platforms like AWS, Azure, Google Cloud to host and develop code

## Block 6: Physical and Environmental Security

### Physical Control

Physical controls serve as the first line of defense in controlling access to an organization

### Physical Attack

Physical attacks target tangible components of information systems, such as hardware devices, data storage mediums, and physical locations.

Examples:

- Brute Force
- RFID Cloning
- Environmental

### On-premises

On premises computing architecture involves housing and managing hardware, software, servers, and network resources within an organization's physical location

### Power

Power management involves provisioning, controlling, and efficiently utilizing electricity to maintain uninterrupted facility operation

Uninterruptible Power Supply (UPS) devices offer emergency power during main power failures by storing energy in batteries or supercapacitors

Generators supply power during complete power loss or in areas without standard electrical service, converting mechanical or chemical energy into electrical energy

### Physical Security

- Bollards/Barricades
- Access Control Vestibules
- Fencing
- Video Surveillance
- Security Guards
- Access Badges
- Lighting
- Sensors (infrared, pressure, microwave, ultrasonic)

## Day One Summary

- CIA Triad & AAA — foundational exam anchors for confidentiality, integrity, availability, and identity management
- Control Types — preventive, detective, corrective, and their role in layered defense
- Authentication & Access Controls — MFA, SSO, RBAC/MAC/DAC/ABAC, least privilege, PAM
- Cryptography Essentials — symmetric vs. asymmetric, hashing/salting, PKI, certificates, key exchange, KMS
- Network Security Architecture — firewalls, IDS/IPS, segmentation, VLANs, DMZ
- Cloud Fundamentals — deployment/service models, shared responsibility, virtualization, IaC, serverless
- Physical Security Controls — access control, surveillance, fire suppression, secure areas
- Control Categories — managerial, operational, physical
- Identity Proofing, Federation, Interoperability — supporting IAM concepts
- Secure Enclave, Steganography, Blockchain — contextual crypto concepts
- Environmental Controls — HVAC, EMI shielding, hot/cold aisles
- Multi‑Cloud & Cloud‑Specific Considerations — governance, visibility, misconfiguration risks

## Block 1: Threat Landscape and Actors

### Threat Actors

- Understanding the characteristics and traits of different types of attackers is crucial for effective cyber defense
- Threat actors vary widely in experience, expertise, resources, etc. From inexperienced individuals to highly skilled syndicates of nation states

#### Unskilled Attackers

Lack technical skills and often rely on readily available malicious code copied from the internet

#### Hacktivists

Combine hacking skills with activist motives, targeting organizations or systems to promote social or political agendas

#### Cyber Criminals

Operating independently or within a syndicate, motivated by financial gain. May have access to considerable resources.

#### Advanced Persistent Threats (APTs)

Highly sophisticated and well funded attackers with extensive resources and extremely high motivation. Often associated with nation states.

#### Insider Threats

Individuals within organizations who exploit their authorized access for malicious purposes

#### Shadow IT

Employees using an organization's IT systems and services without the IT department's knowledge.

### Motivations

Motivation is the reason or drive behind an individual or group's actions

- Common motivations are financial gain, ideological beliefs, revenge, and recognition
- Understanding motivations is crucial for developing strategies to mitigate and respond to cybersecurity threats effectively

### Threat Actor Motivations

- Data exfiltration: transferring data from a computer system or network
- Blackmail: threatening to disclose embarassing or damaging information unless certain demands are met
- Financial gain: Aiming to increase wealth or financial resources
- Philosophical/Political beliefs: Acting upon deeply held convictions or ideologies related to political or philosophical concepts
- Ethics:
- Revenge
- Disruption/Chaos:

### War

Cyber Warfare is a state sponsored, politically motivated attack on an adversary's information systems

- Often focuses on systems and assets vital to the functioning of a society or a nation

## Block 2: Social Engineering and Human Factors

### Types of Social Engineering

#### Phishing

Involves fraudelent attempts to obtain private information by masquerading as someone else. A social engineering attack aimed at tricking individuals into sharing sensitive data.

##### Anatomy of Phishing Emails

- Email Header: inconsistencies in sender info
- Deceptive Links
- Generic Greetings
- Spelling Errors
- Malicious Attachments
- Urgency Cues

#### Vishing (Voice Phishing)

Using voice calls, often over VoIP, to deceive individuals into revealing sensitive information

#### Smishing

A combo of SMS and phishing, involves sending SMS to deceive

#### Spear Phishing

Phishing attempts directed towards a specific individual

#### Whaling

Phishing attacks which target high value targets such as executives, CEOs, etc

#### Evil Twin Attack

Rogue wi-fi access point for data interception

#### Pharming

DNS cache poisoning for traffic redirection

### Types of Social Engineering Attacks

#### Misinformation

False or misleading information that's spread without malicious intent

#### Disinformation

False/misleading information that is intentionally deceptive

#### Impersonation

Pretending to be someone else to gain trust or access

#### Business Email Compromise (BEC)

Sophisticated scam that compromises legitimate business email accounts to conduct unauthorized transfer of funds

#### Pretexting

The attacker invents a scenario (pretext) to persuade a victim to divulge information

#### Watering Hole Attack

Attackers load malware into sites that the targets visit frequently

#### Brand Impersonation

Involves attackers posing as trusted brands such as banks and tech companies

#### Typosquatting

Involves attackers maliciously using domain names that are typo versions of legitimate domains

### Human Vectors/Social Engineering

Human vectors are individuals manipulated into giving access to sensitive information or systems

Social engineering encompasses a broad range of techniques aimed at manipulating the human psyche

## Block 3: Malware Analysis and Defense

### Malware

Malware is software designed to infiltrate, damage, or gather information from a system without user consent

### Types of Malware

#### Ransomware

Restricts access to a computer system and demands payment for decryption. Propogated via phishing.

#### Trojans

Masquerade as legit software but perform malicious functions. Often downloaded unknowingly.

#### Worms

Self replicate to spread across networks. exploiting security vulnerabilities in OS and applications.

#### Spyware

Secretly monitors and collects user activity, potentially compromising sensitive information.

#### Bloatware

Consumes excessive system resources and can hinder system performance.

#### Viruses

Infect computers when executed by users and spread copies of themselves throughout the system

#### Keyloggers

Capture keystrokes to steal sensitive data

#### Logic Bombs

Initiate malicious functions under specific conditions, blurring the line between malware and malware delivery system

#### Rootkits

gain admin level control over system without detection

### Antivirus Software/Antimalware

Antivirus software prevents, detects, and removes malware.

### Zero Day

Refers to a previously unknown software vulnerability that attackers discover and exploit before the vendor or developer becomes aware of it and releases a patch.

The term zero day means the devs had 'zero days' to fix the vuln.

### Fileless

Fileless malware is a type of malicious software that does not rely on traditional files written to disk. Instead, it runs entirely in memory or abuses legitimate tools on the system.

## Block 4: Attack Vectors and Techniques

### Web-Based

Web based vulnerabilities are weaknesses in web applications and services

#### Structured Query Language injection (SQLi)

Vulnerabilities are flaws that attackers can use to manipulate SQL queries in web applications

#### Cross-site Scripting (XSS)

Vulnerabilities enable the injection of malicious scripts into web pages

### Intrusion Prevention System/Intrusion Detection System Logs

An IPS/IDS work together to prevent and detect potentially harmful activities within a network. Their logs can alert you to various attacks such as SQL injections and XSS

### Application Security

Application security refers to the security measures implemented at the application level

- Input validation: ensures data integrity by verifying the type and content of user or application input, preventing vulnerabilities like XSS and SQLi
- Secure cookies: implement the secure attribute in HTTP response cookies to prevent unauthorized access and transmission of sensitive information

### Application Attacks

Application attacks exploit software application weaknesses, potentially resulting in unauthorized access, data theft, or system disruption

- Injection
- Buffer overflow
- Replay
- Privilege escalation
- Forgery
- Directory traversal

#### Cross Site Request Forgery (CSRF)

Tricks a victim browser into performing an action on a website without their consent, using the victim's authenticated session

#### Privilege Escalation

Happens when a user or attacker gains higher level permissions than intended by exploiting misconfigurations or vulnerabilities

### Application

The application layer is a gateway to user interactions and data, making it a common target of attacks

#### Buffer Overflow

Involves a program writing more data to a buffer than it can hold, introducing a vulnerability

#### Memory Injection

Involves injecting malicious code into a system's memory

#### Race Condition

A race condition weakness occurs when multiple processes or threads try to access a sytem at once

#### Malicious Update

Involves altering software or firmware with harmful code via an update that appears legitimate

### Cyber Kill Chain

- Intrusion
- Exploitation
- Privilege Escalation
- Lateral Movement
- Obfuscation (Anti-Forensics)
- Denial of Service
- Exfiltration
- Reconaissance

#### Intrusion

Brute Force Attacks

#### Exploitation

Activity from blacklisted geolocations

#### Privilege Escalations

Failed privilege escalation detected

#### Lateral Movement

Dormant service account reactivated

#### Obfuscation/Anti Forensics

Unusual amount of messages marked unread

#### Denial of Service

Unusual number of GDPR files deleted

#### Exfiltration

Unusual amount of data uploaded to external sites

#### Reconnaissance

Abnormal DNS reverse lookup requests

## Block 5: Vulnerability Management

### Identification Methods

ID Methods help locate. identify, and document security flaws in an organizations digital eco system

Key methods are vulnerability scans and software composition analysis

### Vulnerability Scan Tools

- Static Application Security Testing (SAST): Analyze source code or binaries without executing the program
- Dynamic Application Security Testing (DAST): Test apps while running to find vulnerabilities not visible in the code
- Interactive Application Security Testing (IAST): Combine SAST and DAST for comprehensive analysis
- Threat Intelligence Platforms (TIPs): Gather data from various sources to provide threat insights
- Security Information and Event Management (SIEM) Systems

### Applications Security

Identifying and mitigating vulnerabilities in software applications

- Static Analysis (SAST): Examines source code or binaries without execution, enabling early identification and resolution of security flaws
- Dynamic Analysis (DAST): Tests applications during operation, simulating attacks to uncover vulnerabilities that static anlaysis might miss
- Package Monitoring: Continously surveils third party software packages and libraries for security vulnerabilities

### Threat Feeds and Databases

#### Threat Feed

Real time repository and transmission channel for data points that indicate cyber threats

#### Proprietary/Third-Party Feed

Specialized channel of threat feeds. typically requiring subscription

#### Open Source Intelligence Threats (OSINT)

Threats shared in public forums, databases, and code repositories

#### Information Sharing and Analysis Centers (ISACs)

Repositories for organizations to share threats received and learn about others; organized by industry

### Penetration Testing

Pentesting is the simulation of cyber attacks to identify vulnerabilities

- Planning
- Recon
- Exploitation
- Post-exploitation
- Reporting

#### Types of Pentests

- Physical: Targets physical barriers such as doors and locks
- Offensive (Red Teaming): Mimics the actions of threat actors to identify vulnerabilities
- Defensive (Blue Teaming): Focuses on managing simulated attacks to evaluate defensive strategies
- Integrated (Purple Teaming): Combines offensive and defensive methodologies
- Known environment (White Box): Testers have comprehensive info about the system architecture
- Partially Known environment (Grey Box):
- Unknown environment (Black Box):

### Responsible Disclosure Program

Responsible Disclosure Program: Framework encouraging the ethical reporting of security vulnerabilities

- Outline secure procedures for external researchers to report discovered vulnerabilities
- Incentives include monetary rewards and public recognition

### Bug Bounty Program

Bug Bounty Programs offer financial incentives for discovering and reporting

### Analysis

Analysis transforms raw data about vulnerabilities and threats into comprehensive insights

#### Common Vulnerability Scoring System (CVSS)

Industry standard tool for evaluating severity and urgency of vulnerabilities; scores from 0-10

#### Common Vulnerability Enumeration (CVE)

Standardized system for cataloging security flaws; provides historical data about remediation

#### Vulnerability Classification

#### Exposure Factor (EF)

Percentage of loss that a company would experience if a specific asset were compromised

#### Environmental Variables

Specific conditions or factors within an organization's context influencing the impact and exploitability of vulnerabilities

#### Industry/Organizational Impact

Potential consequences of vulnerabilities beyond an organization's boundaries

#### Risk Tolerance

The extent to which an organization is willing to accept exposure to threats

### Message Based

Message based communication poses significant security risks due to its widespread use, users' trust in platforms, and the potential for immediate damage

### Image Based

Involve using digital images to exploit vulnerabilities in software and systems

### File Based

File based threats leverage common file formats to conceal harmful scripts and execute malicious activities

### Voice Call

Voice call threats involve malicious activities conducted through phone calls. Attackers aim to decieve or manipulate individuals into disclosing information by pretending to be trusted entities

### Removable Device

Removable device threats involve using portable storage devices that transmit malware. Examples include data storage devices that are infected with malicious code and spread malware to connected systems,

### Vulnerable Software

Vulnerable software has exploitable flaws or weaknesses in its code or design

- Client based security: involves installing software agents on client devices for active monitoring and protection
- Agentless security: centralized, it enables monitoring and protection without installing software on individual client devices

### Unsupported Systems and Applications

Software tools or platforms lacking regular updates, security patches, or technical support from developers or vendors. May occur when software reaches its official end of life or a company goes out of business

### Unsecure Network

Unsecure networks lack appropriate security measures. They expose individuals and organizations to cyber threats such as data theft, unauthorized access, and remote device control.

Examples:

- Wireless networks: Vulnerable to unauthorized access and eavesdropping if improperly configures or lacking encryption
- Wired networks: More secure than wireless but vulnerable without proper segmentation and access controls
- BLuetooth networks: Exploitable if devices are set to "Discoverable" mode or if bluetooth vulnerabilities are not patched

### Open Service Ports

Open service ports are network communication endpoints that are accessible and unguarded

### Default Credentials

Simple default passwords that ship with hardware or software

### Supply Chain

A supply chain is a network of organizations, resources, and processes involved in creating, producing, and delivering products or services

- Managed Service Providers (MSPs): Organizations that manage IT services for other companies, offering efficiency but potentially introducing risks
- Vendors: Companies providing products or services to other businesses
- Suppliers: Providers of raw materials or components used in manufacturing

### Zero Day Vulnerabilities

A flaw that's disclosed before its patch is released; an exploit being used before the organization/developer is aware of it.

Zero day protection is a collective term for the related preventative measures:

- Use a new OS with built-in protections
- Use multiple firewall layers
- Use approved application lists
- Install updates/patches regularly

## Block 6: Wireless and Mobile Security

### Wireless Devices

Wireless devices operate without a physical wired connection. They use wi-fi, bluetooth, and cell networks to communicate.

- Site surveys: assess the current wireless environment and plan for wi-fi network optimization
- Heat maps: visualize wireless activity to determine optimal access point placement for coverage and performance

### Mobile Solutions

Mobile Device Management (MDM) is crucial for successful implementation of bring your own device (BYOD) policies.

### Connection Methods

- Bluetooth
- Wi-Fi
- Cellular
- GPS and geolocation
- Satelletite Communication (SATCOM)
- Infrared and wireless USB receivers

### Unsecure Networks

Unsecure networks lack appropriate security measures. They expose individuals and organizations to cyber threats such as data theft, unauthorized access, and remote device control.

These include:

- wireless networks
- wired networks
- bluetooth networks

### Wireless Security Settings

#### WiFi Protected Access 3 (WPA3)

 uses Simultaneous Authentication of Equals (SAE) to replace the vulnerable preshared key (PSK) system.

#### RADIUS Federation

RADIUS = Remote Authentication Dial In User Service
enables secure communication among multiple RADIUS servers

#### Cryptographic Protocols

WPA3-Personal and WPA3-Enterprise offer robust encryption methods like AES-CCMP and HMAC-SHA for data protection

AES-CCMP = Advanced Encryption Service

### Mobile Device

#### Side Loading

Installing applications from sources outside the official app store.

#### Jailbreaking

Refers to removing restrictions imposed by the manufacturer or carrier.

#### Authentication Protocols

LDAP, Kerberos, and 802.1X are authentication methods tailored to various environments

Kerberos = AAA for MS AD; uses tickers to grant authentication

## Day Two Summary

## Block 1: Enterprise Security Architecture

### Zero Trust

Zero trust is a network security concept centered on not trusting any entity or device by default

- Allows access based on various known factors rather than relying on inherent trust
- Establishes trust through mechanisms such as authentication, authorization, and validation of security posture

### Zero Trust - Control Plane

- Adaptive Identity
- Threat Scope Reduction
- Policy-driven Access Control
- Secured Zone
- Policy Engine
- Policy Administrator

### Zero Trust - Data Plane

- Subject/System
- Policy enforcement point (PEP)
- Implicit trust zones

### Cloud

Cloud computing offers on demand services that extend computer or network capabilities

### IaC

Infrastructure as Code involves managing and provisioning computer data centers through machine readable definition files.

### Internet of Things (IoT)

IoT encompasses interconnected physical devices that exchange data over the internet or other networks

Components:

- Sensors
- Smart Devices
- Wearables
- Facility Automation

Weak Defaults

### Industrial Control Systems (ICS) / Supervisory Control and Data Acquisition (SCADA)

ICS and SCADA enable organizations to monitor equipment processes, collect data, perform analysis, and remotely control devices and processes.

- Play a crucial role in maintaining efficiency, enabling data driven decsions, and mitigating downtime in industrial settings
- To defend against cyberattacks, SCADA networks should be isolated from coroporate networks

### Real Time Operating Systems (RTOS)

A Real Time Operating System rapidly switches between tasks, giving the illusion of simultaneous execution of multiple programs on a single processing core.

Provides hard real time responses with fast and deterministic reactions to external events.

Security measures:

- Minimize the attack surface by disabling unnecessary features, services, and access
- Assume that external systems are insecure

### Embedded Systems

Embedded systems are specialized computer systems designed for specific functions within larger systems, often with significant design constraints

- Constraints include cost, long lifecycle, real time requirements, and reliability needs
- Often optimized for lifecycle and business driven factors rather than security or maximum computing throughput

### High Availability (HA)

Refers to operational performance, usually uptime. It ensures ability to access a system or service without interruptions.

#### Considerations

##### Availability

Ensuring continous business operations with redundant components, load balancing, failover mechanisms

##### Resilience

Building comprehensive measures and recovery strategies to withstand failures and attacks

##### Cost

Balancing expenses in acquisition, implementation, operation, and maintainence while optimizing resource utilization

##### Responsiveness

Optimizing performance and automating tasks to efficiently meet user demands

##### Scalability

Designing systems capable of growing or shrinking in response to demand

##### Ease of Deployment

##### Risk Transferance

Strategically shifting risks to other parties while maintaining accountability

##### Ease of Recovery

Establishing robust disaster recovery and business continuity plans to minimize downtime

##### Patch Availability

Ensuring timely access to software updates and fixes

##### Inability to Patch

The challenge of being unable to apply critical security updates, often because of legacy systems or technical constraints

##### Power Optimization

Optimizing energy efficiency and resilience against power based attacks across the entire network

##### Computing Resources

Effectively distributing and optimizing hardware and software components for data processing and computation

### Secure Access Service Edge (SASE)

Secure access service edge is a cybersecurity and networking framework. It converges network security functions with WAN capabilities into a single cloud delivered service model

SASE delivers secure, optimized access to users regardless of location by combining network connectivity and security services from the cloud

## Block 2: Secure Network Design

### Virtual Private Network (VPN)

A virtual private network establishes a secure connection between two or more devices over the internet, even if they are not on the same private network

### Remote Access

Remote access allows authorized users to connect to a network, system, or application from a location outside the organization's physical premises.

Remote Access Technologies:

- Remote Access Service (RAS)
- Virtual Private Networks (VPN)

### Tunneling

Tunneling creates a secure pathway for data transmission across networks via encapsulation

Protocols like Transport Layer Security (TLS) and Internet Protocol Security (IPSec) enhance the security of tunneling by providing encryption and integrity mechanisms

Internet Key Exchange (IKE), the key management protocol for IPSec, has two phases. Phase 1 negotiates the ISAKMP SA, and Phase 2 negotiates the IPSec Sas.

### Network Access Control (NAC)

NAC is a method to enforce policy-driven security solutions at the network entry level.

### Micro-Segmentation

Micro segmentation divides the network into very small, isolated segments - down to individual workloads or applications.

## Block 3: Identity and Access Management (IAM)

### Inter-operability

#### Single-Sign-On (SSO)

SSO enables one set of credentials for access to multiple services or applications

SSO Protocols:

- LDAP = Lightweight Directory Access Protocol
- OAuth = Open Authorization
- SAML = Security Assertion Markup Language

#### Federation and SSO

### Types of Standards

Password standards define rules for creating, managing, and storing passwords.

Access Control Standards determine who has access to specific resources within the organization's network and systems.

#### Access Control Types

- Attribute Based Access Control (ABAC)
- Role Based Access Control (RBAC)
- Discretionary Access Control (DAC)
- Mandatory Access Control (MAC)

## Block 4: Endpoint Security Solutions

### Data Loss Prevention (DLP)

Data loss prevention is a comprehensive approach to preventing users from sending sensitive or critical information outside the corporate network.

### NAC

Network access control is a method to enforce policy driven security solutions at the network entry level

- Checks if devices comply with predefined security rules before granting access to the network

### Endpoint Detection and Response (EDR) and Extended Detection and Response (XDR)

Endpoint detection and response (EDR) systems monitor endpoints such as desktops, laptops, mobile devices; detect and respond to signs of malicious activity.

Extended detection respon

### User Behavior Analysis

User behavior analytics use machine learning algorithms to track, collect, and assess user behavior on a network.

### Secure Baselines

Secure baselines are standardized sets of minum configurations and security controls for systems and software.

- Asset Tagging: Assigning unique identifiers to each asset for easier tracking
- Version Control:
- Manual Review: a human reviews data, logs, and systems to help prioritize vulnerabilities based on actual organizational risk. Human judgment and intuition can identify issues that automated tools miss.
- Disable unneccessary services: Turn off services and features not required for the system's primary function
- Validation Testing: confrim that the baseline settings do not disrupt necessary functions
- Rollback plan: have a plan to revert changges in the event of unforeseen issues during deployment
- Patch management: Regurlarly update software and sytems to patch known vulnerabilities
- Review and update: Periodically review the secure baseline to ensure that it aligns with current best practices in cybersecurity

### Hardening Targets

### Containerization and Virtualization

## Block 5: Secure Communications

### Software Defined Wide Area Network (SD-WAN)

SD-WAN is a networking architecture that uses software based controls to optimize and manage data traffic across a wide are network.

- Enhances network manaegement flexibility by

### SASE

Cloud native architecture that manages network security functions with WAN capabilities

### Implementation of Secure Protocols

The implementation of secure protocols refers to creating encrypted pathways

### Email Security

Email security involves measures used to secure the access and content of email accounts or services

#### Domain Based Message Authentication, Reporting and Conformance (DMARC)

Domain based message authentication, reporting, and conformance helps receivers verify the authenticity of emails from specific domains

DMARC Process:

- SPF Check
- DKIM check
- DMARC policy retrieval
- Policy Enforcement
- Reporting

## Block 6: Application Security

### Code Signing

Code signing digitally signs executables and scripts to verify authenticity and integrity

### Sandboxing

Creates a confined execution environment for running untrusted or suspicious code safely

### Integrations and APIs

Application Programming Interfaces (API)

### Secure SDLC & DevSecOps

## Block 1: Monitoring and Computing Resources

### Log Aggregation

log aggregation involves gathering log data from various sources into a centralized repository for examination

- A critical process
- Helps turn isolated data points into a coherent narrative

Log aggregation tools and processes:

- SIEM
- syslog

### Alerting

Alerting is the early warning system for security infrastructure

- Using predefined rules, alerts indicate when immediate attention is required
- Alert tuning refers to setting alert sensitivity

### Security Information and Event Management (SIEM)

A SIEM system is a specialized device or software for security monitoring. It collects, correlates and analyzes logs from multiple systems.

SIEM Functions:

- log collection
- log normalization
- log aggregation
- log correlation
- reporting

### NetFlow

NetFlow is a protocol that collects and monitors network traffic data; it provides various traffic insights:

- Source
- Destination
- Volume
- Paths

### Simple Network Management Protocol (SNMP) Traps

SNMPv3 is a popular protocol for managing and monitoring networks. SNMP traps are alerts from SNMP enabled devices when they have status changes. This facilitates speedy response.

Optional SNMPv3 features:

- Authentication: Verifies the legitimacy of trap sources, preventing unauthorized devices from sending false alerts
- Encryption: Offers encryption to maintain confidentiality of trap contents

### Vulnerability Scanners

Vulnerability scanners automate the identification of weaknesses in sytems and networks

### Deception and Disruption Technology

Deception technology involves the use of decoys, traps, and other deceptive measures to mislead and thwart attackers.

Disruption Technology

#### Honeypot

A honeypot is a decoy system or network segment designed to attract and trap potential attackers-mimcs legitimate systems or services to lure attackers into interacting with it, allowing security teams to monitor and analyze behavior

#### Honeynet

A network of interconnected honeypots and other decoy systems designed to deceive and trap potential attackers

#### Honeyfile

Honey files are files created to serve as bait for potential attackers designed to lure them into interaction

#### Honeytokens

Honeytokens are pieces of faake or fabricated data placed within a system or network to detect unauthorized access or activity

## Block 2: Incident Response Procedures

### Incident Response Process

- Preparation
- Detection

### Post Incident Activity

Post incident activity is the "lessons learned" phase of incident response

- Meet within two weeks
- Complete documentation about the incident
- Discuss response process
- Change response process if needed

### Training

Training equips teams with the knowledge and protocols for effectively managing security incidents

Role based training for individuals and departments
Tabletop exercises and simulations for practice responding

### Testing

Testing is the rigorous examination of incident response procedures

#### Tabletop Exercises

Simulate hypothetical situations that mirror real world threats

- Each participant plays a role corresponding to their actual emergency responsibilities
- Time pressure helps simulate the urgency of real incidents
- Decision points pause the action for strategic discussions about how to proceed
- Detailed records are kept of every action, decision, and discussion

#### Simulation Exercises

Simulation exercises build upon tabletop exercises with simulated tech environments such as sandboxed or isolated replicas of networks

Tips for conducting simulations:

- Define key performance indicators (KPIs) to evaluate response effectiveness
- Introduce unexpected elements to test teams adaptibility
- Include post exercise discussion to identify gaps and discuss improvements

### Root Cause Analysis

Root cause analysis is criticial for identifying the reasons underlying security incidents

- Data collection

### Threat Hunting

Proactive search through networks and data sets to detect and isolate advanced threats

- Targets threats that evade traditional reactive security measures
- Involves setting a specific type of threat, such as lateral moves or data exfiltration
- Discoveries may lead to threat remediation and updated security measures

## Block 3: Digital Forensics and Investigation

### Digital Forensics

A multi-disciplinary approach to collecting, analyzing, and preserving data.

- Involves the electronic data relevant to investigations or legal proceedings

### Legal Hold and Chain of Custody

Legal hold is the process of preserving electronic evidence related to a legal case or investigation. It prevents the alteration or deletion of a specific data

Chain of Custody documents the path that evidence takes from acquisition to disposal.

### Acquisition

Acquisition is the systematic collection of digital evidence meant to maintain its authenticity

#### Order of Volatility

- CPU Cache and registers
- RAM
- bit-by-bit image of hard drive
- network traffic and logs
- Residual data (system settings)

### Reporting

Reporting is the documentation of activities and findings throughout the forensic process

### Preservation

Preservation involves safeguarding evidence from identification to the end of its lifecycle

### E-Discovery

Involves identifying, collecting, and producing electronically stored information in response to a legal request

- Subject to specific rules and protocols
- Uses specialized software for searching, identifying, and collecting information

### Log Data

Log data is the systematically recorded information that's generated by hardware, software, and operating systems

- Captures events, transactions, and other activities within a system or network

### Firewall Logs

Help IT monitor traffic allowed and denied by a firewall

### Endpoint Logs

Endpoint logs give detailed information about activities on individual devices connected to a network

### OS Specific Security Logs

Operating System security logs

### IPS and IDS Logs

Logs produced by Intrusion Prevention/Detection Systems

### Network Logs

capture data traffic across the network infrastructure

### Metadata

### Packet Captures

Give a detailed view of network activity

## Block 4: Business Continuity and Disaster Recovery

### HA (High Availability)

High availability ensures that a system or application remains accessible and operational over an extended period

#### Redundant Hardware

Multiple instances of critical hardware components eliminates a single point of failure

### Site Considerations

#### Hot Site

A near duplicate of the organization's original site that can be up and running within minutes

#### Warm Site

Contains computers, phones, and servers but may require configuration before use

#### Cold Site

Provides basic office infrastructure, but extensive computer configuration and data restoration would be needed before use

#### Geographically Distant Site

A computing environment, such as a data center, located at least 50 miles from the main compute campus data center

### Platform Diversity

Platform diversity is the implementation of varies hardware or software platforms within an organization's IT environment

- Reduces systemic risks associated with a single point of failure
- Increased ability to withstand security incidents and technical failures
- Improved capacity to recover from incidents due to diversified platforms

### Continuity of Operations

Continuity of operations planning (COOP) is a federal initiative encouraging organizations to plan for the continuation of critical operations under various emergency circumstances

### Capacity Planning

Capacity planning is the process of determining future resource requirements such as people, technology, and infrastructure

### Backups

A backup is a duplicate copy of data and system configuration

## Block 5: Automation and Orchestration

## Block 6: Vulnerability Management Operations

## Day 4 Summary

## Block 1: Governance and Risk Management

### Risk Identification

Systematically recognizing, documenting, and understanding potential threats, vulnerabilities, and hazards that could impact an organization

### Risk Assessment

Identifying risks to determine their potential likelihood and impact

- Ad hoc
- Recurring
- One time
- Continous

### Risk analysis

Delving deep into each identified risk, examining specific details and characteristics

A risk register is useful for tracking issues and remedies

### Qualitative Risk Analysis vs Quantitative Risk Analysis

Qualitative: Assigns numeric value based on probability and impact of risks without assigning monnetary values
Quantitative: Assigns exact monetary value to risks

### Quantitative Risk Calculations

Three key values used in quantitative risk calculations:

- Single Loss Expwctancy (SLE): The loss of value in dollars based on a single incident of a given type
- Annualized Rate of Occurence (ARO): The number of times per year that the type of incident occurs
- Annualized Loss Expectancy (ALE): Total loss in dollars per year from a type of incident

SLE*ARO=ALE

### Exposure Factor (EF)

Exposure Factor is the percentage of loss that an asset would experience if a threat materialized. It helps calculate Single Loss Expectancy (SLE).

SLE=Asset Value* Exposere Factor

### Probability vs Likelihood

Probability quantifies the likelihood of a risk occurring. It's often expressed as percentage, and can be used in calculations

Likelihood qualitatively describes the chance of an event occurring, often with a term

### Risk Register

Centralized repository for recording identified risks, their characteristics, and management plans. Each risk receives a risk ID for easy tracking

- Key Risk Indicators (KRIs): Metrics for measuring the potential impact and likelihood of identified risks
- Risk Owners: Individuals or departments responsible for managing specific risks
- Risk threshold:

### Risk Tolerance

The amount of risk an organization is willing to accept as it pursues objectives

### Risk Appetite

Level of risk an organization iw willing to accept to pursue its objectives

- Expansionary: willing to accept higher risk in exchange for rapid growth
- Conservative: Prefers lower level risks, prioritizing stability and sustainable growth
- Neutral: Balanced approach; accept risk but not at the expense of stability

### Risk Management Strategies

Systematic approaches to managing and mitigating risks:

- Accept some or all consequences of the risk
- Mitigate the risk
- Transfer the risk to a third party
- Avoid the risk

### Business Impact Analysis

BIA determines potential impacts of interrrupting critical processes

- Recovery Time Objective (RTO): Time by which a process should be restored to avoid unacceptable consequences
- Recovery Point Objective (RPO): Maximum amount of data that can be lost due to a disruption
- Mean Time to Repair (MTTR): Average time required to repair a failed device or system
- Mean Time Between Failures (MTBF): Expected average time between failures for a system or component

### Types of Policies

Acceptable Use Policy
Information Security Policy
Business Continuity Policy
Disaster Recovery Policy
Incident Response Policy
Software Development Lifecycle Policy
Change Management Policy

### Standards

### Procedures

Implement policies and standards through specific, detailed instructions

### Types of Governance

Board
Committee
Government Entities

## Block 2:

## Block 3:

## Block 4: