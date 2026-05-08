#Network Types:

Internet-> Worldwide collection of interconnected networks using common standards to exchange information.

Local Networks:
Small Home Networks-> Connect a few computers to each other and to the internet.
Small Office and Home Office Networks(SOHO)-> Allows computers in a home office or a remote office to connect to a corporate network, or access centralized, shared resources.
Medium to Large-> Can have many locations with hundreds or thousands of interconnected hosts.
World Wide Networks-> The internet is a network of networks that connects hundreds of millions of computers world wide.

Mobile Devices:
Smartphone-> Able to connect to the internet from almost anywhere. Combine functions of many products such as telephone, camera, GPS, media player, etc.
Tablet-> Similar to smartphones with additional screen size.
Smartwatch-> Can connect to a smartphone and provide alerts or messages. Additional functions such as counting steps (pedometer) or heart rate monitoring.
Smart Glasse-> Wearable computer in the form of glasses that displays information in a tiny screen similar to a Heads-Up Display (HUD).

Connected Home Devices:
Security System-> Can be monitored and configured remotely.
Appliances-> Refrigerators, ovens, dishwashers, etc which can be connected to the internet.
Smart TV-> Television with internet access
Gaming Consoles-> Console that can download games or allow playing with others via the internet.

Other Connected Devices:
Smart Cars-> Cars which connect to the internet to access maps, audio/video content, travel information. Can also connect to smartphones/tablets.
Radio Frequency Identification (RFID) Tags-> Can be placed in or on objects to track or monitor sensors for many conditions.
Sensors and Actuators-> Sensors can provide environmental data (temp., humidity, wind speed, etc) which allows actuators to trigger based on conditions relayed from sensors.
Medical Devices-> Pacemakers, insulin pumps, hospital monitors give feedback based on vital signs.

#Data Transmission

Computers and networks only communicate with binary digits (bits). A bit can only be stored/transmitted in two possible states: 1 (on) or 0 (off). Binary codes, such as those defined in ASCII (American Standard Code for Information Interchange), use bits to represent and interpret things such as letters or numbers. In ASCII each character is represented with eight bits.
Bytes are groups of eight bits.

Common methods of data transmission are electrical, optical, and wireless signals.
Electrical-> Data represented as electrical pulses on copper wire.
Optical-> Data converted into electrical signals and transmitted as pulses of light.
Wireless-> Infrared, microwave, or radio waves transmit data through the air.

Types of Data:
Volunteered-> Created and explicitly shared.
Observed-> Captured by recording the actions of individuals, such as location while using a phone.
Inferred-> Data such as a credit score, which is based on an analysis of volunteered or observed data.

#Bandwidth

Bandwidth is the capacity of a medium to carry data. Digital bandwidth measures the amount of data that can flow from one place to another in a given amount of time, and is usually measured in the number of bits that (theoretically) can be sent across the media in a second.
Common measurements are bps, Kbps, Mbps, Gbps, and Tbps.
Bits-per-second(bps)-> 1 bps = fundamental unit of bandwidth.
Kilobits-per-second(Kbps)-> 1 Kbps = 1,000 bps = 10³bps
Megabits-per-second(Mbps)-> 1 Mbps = 1,000,000 bps = 
Gigabits-per-second(Gbps)-> 1 Gbps = 1,000,000,000 bps = 
Terabits-per-second(Tbps)-> 1 Tbps = 1,000,000,000,000 bps =

#Throughput

Throughput is the measure of the transfer of bits across the media over a given period of time. Due to multiple factors, throughput does not match the specified bandwidth. These include the amount of data sent/received over a connection, types of data being transmitted, and latency created by the number of network devices encountered between source and destinations.
Latency refers to the amount of time, including delays, for data to travel from one point to another.

#Client and Server Roles:

All computers connected to a network that directly participate in network communication are classified as hosts. Hosts can send and receive messages on the network.
In modern networks, computer hosts can act as a client, a server, or both--this is determined by the software installed on the host.
Servers are hosts that have software installed which enable them to provide information, like email or web pages, to other hosts on the network.
Each service requires separate server software. Ex: a host requires a web server to provide web services to the network.
Clients are computer hosts that have software installed that enables the hosts to request and display information obtained from a server. Ex: a web browser installed on the client.
The web server runs web software. The client uses browser software to access web pages on the server.

#Peer-to-Peer Networks (P2P):

P2P networks work when many computers function as both servers and clients on the network.
The simplest version of this consists of two directly connected (wired or wirelessly), with both exchanging data as necessary with each other; acting as either a client or a server as necessary.
Multiple computers can also be connected using a network device, such as a switch, to create a larger P2P network.
The main disadvantage is that performance of a host can be slowed down if it is acting as both server and client at the same time.

Advantages:
-easy to set up
-less complex
-lower cost
-used for simple tasks such as transferring files

Disadvantages:
-No central administration
-Not as secure
-Not scalable
-All devices may act as both server and client, slowing performance

#Peer-to-Peer Applications

P2P applications allow devices to act as both client/server within the same communication. P2P apps require each end device to provide a user interface and to run a background service.

#Multiple Roles in the Network

A single computer can run multiple types of server software (file server, email server, web server, etc.), and a single computer can run multiple types of client software.
Every server software providing a service needs a client software to access the service.
With multiple clients installed a host can connect to multiple servers, allowing a user to check email in a web page while listening to radio and instant messaging.

#Network Infrastructure

Network infrastructure contains three categories of hardware components.
End Devices-> Desktop computer, laptop, printer, IP phone, wireless tablet, etc.
Intermediate Devices-> Wireless router, LAN switch, router, multilayer switch, firewall appliance.
Network Media-> Wireless media, LAN media, WAN media.

An end device (or host) is either the source or the destination od messages transmitted over a network. Addresses are used to identify hosts. When a host initiates communications it uses the address of the destination host to specify where the message should be sent.

#ISP Services:

An Internet Service Provider (ISP) provides the link between a home network and the internet. ISPs also provide additional services, these include: web hosting, FTP hosting, App and Media hosting, technical support, Voice Over IP (VOIP), POP internet access, equipment co-location, etc.

#ISP Connections:
"The interconnection of ISPs that forms the backbone of the internet is a complex web of fiber-optic cables with expensive networking switches and routers that direct the flow of information between source and destination hosts. Average home users are not aware of the infrastructure outside of their network. For a home user, connecting to the ISP is a fairly uncomplicated process."
The simplest ISP connection is: "It consists of a modem that provides a direct connection between a computer and the ISP. This option should not be used though, because your computer is not protected on the internet."
The most common type of connection uses a router: "It consists of using a wireless integrated router to connect to the ISP. The router includes a switch to connect wired hosts and a wireless AP to connect wireless hosts. The router also provides client IP addressing information and security for inside hosts."

#Cable and DSL Connections:

Cable-> "Typically offered by cable television service providers, the internet data signal is carried on the same coaxial cable that delivers cable television. It provides a high bandwidth, always on, connection to the internet. A special cable modem separates the internet data signal from the other signals carried on the cable and provides an Ethernet connection to a host computer or LAN."
Digital-Subscriber-Line(DSL)-> "Provides a high bandwidth, always on, connection to the internet. It requires a special high-speed modem that separates the DSL signal from the telephone signal and provides an Ethernet connection to a host computer or LAN. DSL runs over a telephone line, with the line split into three channels. One channel is used for voice telephone calls. This channel allows an individual to receive phone calls without disconnecting from the internet. A second channel is a faster download channel, used to receive information from the internet. The third channel is used for sending or uploading information. This channel is usually slightly slower than the download channel. The quality and speed of the DSL connection depends mainly on the quality of the phone line and the distance from the central office of your phone company The farther you are from the central office, the slower the connection."
Cellular-> "Cellular internet access uses a cell phone network to connect. Wherever you can get a cellular signal, you can get cellular internet access. Performance will be limited by the capabilities of the phone and the cell tower to which it is connected. The availability of cellular internet access is a real benefit for people in areas that would otherwise have no internet connectivity at all, or for people who are constantly on the move. The downside of cellular connectivity is that the carrier usually meters the bandwidth usage of the connection and may charge extra for bandwidth that exceeds the contract data plan."
Satellite-> "Satellite service is a good option for homes or offices that do not have access to DSL or cable. Satellite dishes (see figure) require a clear line of sight to the satellite and so might be difficult in heavily wooded areas or places with other overhead obstructions. Speeds will vary depending on the contract, though they are generally good. Equipment and installation costs can be high (although check the provider for special deals), with a moderate monthly fee thereafter. Like cellular access, the availability of satellite internet access is a real benefit in areas that would otherwise have no internet connectivity at all."
Dial-up-> "An inexpensive option that uses any phone line and a modem. To connect to the ISP, a user calls the ISP access phone number. The low bandwidth provided by a dial-up modem connection is usually not sufficient for large data transfer, although it is useful for mobile access while traveling. A modem dial-up connection should only be considered when higher speed connection options are not available."
