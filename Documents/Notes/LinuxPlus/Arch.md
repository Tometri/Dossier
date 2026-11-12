# Introduction

Along side my studying and primary labs, I'll be setting up a VM with vanilla Arch in order to gain a better understanding of linux itself. I'll be following the installation guide at archlinux.org.

## Partitioning

To identify the disks I use

```shell
lsblk
```

I'll be using a 25gb disk assigned to the VM, which is listed as 'vda'.

I use:

```shell
fdisk -l
```

which shows the disk is recognized by the system: Disk /dev/vda: 25 GiB.

It also shows: Disk /dev/loop0 1.02 GiB. *The installation page insists a result ending in /loop may be ignored as well as rom, airootfs, rpmb. boot0, and boot1 endings.

The partitions required for a chosen device are:

-- One partition for the root directory
-- For booting in UEFI mode: and EFI system partition

It is suggested to use fdisk to modify the partition tables:

```shell
fdisk /dev/the_disk_to_be_partitioned
```

### Example Layout (UEFI with GPT)

Mount Point | Partition | Type | Suggested Size
/boot | /dev/efi_system_partition | EFI system partition | ~1GiB
[SWAP] | /dev/swap_partition | Linux Swap | At least 4 GiB
/ | /dev/root_partition | Linux x86-64 root (/) | Remainder of the device (At least 23-32 GiB)

### BIOS with MBR
Same as above, without boot.

-- [SWAP]
-- /

Using

```shell

test -d /sys/firmware/efi && echo UEFI || echo "Legacy BIOS"
```

returns "Legacy BIOS" on my VM.

After using

```shell
lsblk
```

It shows my partition of /dev/vda/vda1, I'm skipping swap and will add a swapfile later if needed. The partition was made using fdisk defaults.

## Format

With vda1 partitioned, I'll format it as ext4 then mount it

```shell
mkfs.ext4 /dev/vda1
mount /dev/vda1 /mnt
```

## Installation

Packages must be downloaded from mirror servers, which are defined in /etc/pacman.d/mirrorlist.

To install a basic, practical package set (base system, a kernel, common firmware, networking tools, a text editor, documentation, and ext4 utilities):

```shell
pacstrap -K /mnt base linux linux-firmware networkmanager nano man-db man-pages e2fsprogs
```
However, using

```shell
 lscpu | grep "Vendor ID"
```
shows "Vendor ID: GenuineIntel", so I'll add intel-ucode.

So the full install will be:

```shell
pacstrap -K /mnt base linux linux-firmware intel-ucode networkmanager nano man-db man-pages e2fsprogs
```
Note: Initial selection only requires what is needed for the sytem to boot; all other software can be installed or replaced post-installation. Fir a VM or container, microcode and firmware can be omitted entirely. In a container, the kernel can be left out as well.

## Configuring the system

### Fstab

To get the needed file systems mounted on startup, an fstab file with persistent block device naming needs to be generated using genfstab(8). Then check the resulting file and edit in case of errors.

### Chroot

To directly interact with the new system's environment, tools, and configurations as if booted into it, change root into the new system

```shell
genfstab -U /mnt >> /mnt/etc/fstab
cat /mnt/etc/fstab
arch-chroot -S  /mnt
```

### Time

For setting the time zone:

``` shell
ln -sf /usr/share/zoneinfo/Region/City /etc/localtime
hwclock --systohc
```
For my time zone /America/Chicago (/Region/City).

then run hwclock(8) to generate /etc/adjtime (listed above).

To prevent clock drift and ensure accurate time, time sync using NTP (Network Time Protocol) needs to be set up.

### Localization

Edit /etc/locale.gen, uncommenting the locale you want (such as en_US.UTF-8 UTF-8)

``` shell
nano /etc/locale.gen
```

then save and run:

``` shell
locale-gen
echo "LANG=en_US.UTF-8" > /etc/locale.conf
```
which generates the locales and sets the LANG variable

### Hostname

create the hostname file /etc/hostname, write the name, then save and exit the file.

### Root Password

Set root password with

```shell
passwd
```

It will need to be entered twice.

### Network Manager

enable network manager with

```shell
systemctl enable  NetworkManager
```

### Bootloader

I'll be installing the GRUB bootloader, installed to the whole disk (not just vda1)

```shell
pacman -S grub
grub-install --target=i386-pc /dev/vda
grub-mkconfig -o /boot/grub/grub.cfg
```

then exit chroot and unmount before reboot with

```shell
exit
umount -R /mnt
reboot
```

### SSH

After rebooting, I sign in with user:root/password:(the passwd set above). SSH isn't up yet so:

```shell
pacman -S openssh
systemctl enable --now sshd
```
also

```shell
systemctl status NetworkManager
```
to verify network status.

#### Ping Test

From the host

```shell
ping -c 3 192.168.122.41
```

returns 3 packets sent, 3 received, 0 loss.

### Tailscale

I installed tailscale for the VM with
```shell
curl -fsSL https://tailscale.com/install.sh | sh
```

### Creating a user account

```shell
useradd -m -G wheel -s /bin/bash <username>
passwd <user>
pacman -S sudo
EDITOR=nano visudo
```
This allows you to create a new user, set the password, enable super user privilege on the new user editing the file and removing the # from %wheel ALL=(ALL:ALL) ALL. 

With the new user created, the network functioning, ssh + tailscale enabled the VM is able to be reached remotely.
