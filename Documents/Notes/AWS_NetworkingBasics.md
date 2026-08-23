0+c# AWS Networking Basics

## Open Systems Interconnection (OSI) Model

### Layer 1: Physical Layer

The physical layer defines standards for transmitting raw data (bits) over transmission media to connect network nodes. The physical layer provides an electrical, mechanical, and procedural interface to the transmission medium.

### Layer 2: Data Link Layer

The data link layer defines standards for transferring data between adjacent network nodes in a wide area network (WAN) or between nodes on the same local area network (LAN) segment.

This layer can provide the means to detect and possibly correct errors that might occur in the physical layer.

### Layer 3: Network Layer

The network layer is responsible for communication across different networks. It provides the means of transferring variable-length network packets from a source to a destination host through one or more networks.

### Layer 4: Transport Layer

The transport layer provides transparent transfer of data between users, and it provides reliable data transfer services to the upper layers. The transport layer controls the reliability of a given link through flow control, segmentation and desegmentation, and error control.

This layer also provides the acknowledgement of the successful data transmission and sends the next data if no errors occurred.

### Layer 5: Session Layer

The session layer provides the mechanism for opening, closing, and managing a session between user application processes.

Communication sessions consist of requests and responses that occur between applications.

### Layer 6: Presentation Layer

The presentation layer is responsible for formatting and delivering information to the application layer for further processing or display. It translates data based on the syntax that the application accepts.

### Layer 7: Application Layer

The application layer is closest to the user, which means that both the OSI application layer and the user interact directly with the software application.

Application layer functions typically include identifying communication partners, determining resource availability, and synchronizing communications.
