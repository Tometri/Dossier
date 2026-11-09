# Intro

I'll be taking notes on my studying and labs in preparation for the CompTIA Linux+ Certification

## Setting Up the Labs

I'll be using KVM/labvirt to run my virtual machines. The machines I've currently set up are:

-- srv1: ubuntu 26 server
-- rocky1: rocky10
-- desk1: ubuntu 26 desktop

As this week focuses on installation and orientation the focus is on installing the virtual machines and ensuring they function.

### Installation

All machines have been set up successfully. The ISOs downloaded, the distros installed in VMs, they spin up and run. From the boot screen, I can successfully log in.

### Networking

After logging in successfully I used

```shell
ip -brief address
```
to determine the addresses of each device.

All devices show two things from 'ip -brief address': lo and enp1s0.

 lo shows unknown and 127.0.0.1/8 ::1/128 on all devices. 

srv1 enp1s0: UP 192.168.122.114/24 fe80::5054:ff:fe5c:cd5d/64
rocky1 enp1s0: UP 192.168.122.164/24 fe80::5054:ff:fed9:4507/64
desk1 enp1s0: UP  192.168.122.146/24 fe80::5054:ff:fec3:7451/64

lo is the loopback and are being ignored. The fe80:: bits are link-local ipv6, and also being ignored as of the moment.

They have one NIC each and no host-only adapter attached. For week one this isn't an issue.

#### Pinging

From srv1 I pinged the rocky1 and desk1.

For both: 3 packets transmitted, 3 received 0% packet loss

That checks off the inter-VM ping verification for week one. Meaning, the network is working.

#### DHCP

On the host machine I've run:

sudo virsh net-update default add ip-dhcp-host "<host mac='52:54:00:5c:cd:5d' name='srv1' ip='192.168.122.11'/>" --live --config
sudo virsh net-update default add ip-dhcp-host "<host mac='52:54:00:d9:45:07' name='rocky1' ip='192.168.122.31'/>" --live --config
sudo virsh net-update default add ip-dhcp-host "<host mac='52:54:00:c3:74:51' name='desk1' ip='192.168.122.21'/>" --live --config

This is to add reservations to the live network and save them, and so that they survive a reboot of the host.

Terminal output for all three says: updated network default persistent config and live state. The reservations are saved and active.

After rebooting and using:

```shell
ip -brief addr
```

The addresses show as:

-- srv1: 192.168.122.11
-- desk1: 192.168.122.21
-- rocky1: 192.168.122.31

using:
```shell
 ping -c 3 <addr>
```
I verified the commands took and the interVM network is functional.

#### TailScale

Each device was added to my tailscale mesh successfully. I successfully accessed them via cellphone with tailscale+termius.

### Snapshots and Network Diagram

Each device was snapshotted for week1. Clean installs, interVM network+tailscale mesh functions, ip reservations. A network diagram will be created in cisco packet tracer and included in this directory.
