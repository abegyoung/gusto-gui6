Booting Linux on physical CPU 0x0
Linux version 5.10.170 (root@30b03bf3317f) (arm-linux-gnueabihf-gcc (Debian 12.2.0-14) 12.2.0, GNU ld (GNU Binutils for Debian) 2.40) #1 SMP PREEMPT Mon Aug 7 18:07:05 UTC 2023
CPU: ARMv7 Processor [412fc09a] revision 10 (ARMv7), cr=10c5387d
CPU: PIPT / VIPT nonaliasing data cache, VIPT aliasing instruction cache
OF: fdt: Machine model: embeddedTS i.MX6 Quad TS-4900 (Default Device Tree)
Memory policy: Data cache writealloc
efi: UEFI not found.
cma: Reserved 64 MiB at 0x8c000000
Zone ranges:
  Normal   [mem 0x0000000010000000-0x000000003fffffff]
  HighMem  [mem 0x0000000040000000-0x000000008fffffff]
Movable zone start for each node
Early memory node ranges
  node   0: [mem 0x0000000010000000-0x000000008fffffff]
Initmem setup node 0 [mem 0x0000000010000000-0x000000008fffffff]
On node 0 totalpages: 524288
  Normal zone: 1728 pages used for memmap
  Normal zone: 0 pages reserved
  Normal zone: 196608 pages, LIFO batch:63
  HighMem zone: 327680 pages, LIFO batch:63
percpu: Embedded 16 pages/cpu s33804 r8192 d23540 u65536
pcpu-alloc: s33804 r8192 d23540 u65536 alloc=16*4096
pcpu-alloc: [0] 0 [0] 1 [0] 2 [0] 3 
Built 1 zonelists, mobility grouping on.  Total pages: 522560
Kernel command line: root=/dev/mmcblk1p1 rootwait rw console=ttymxc0,115200 ro init=/sbin/init
Dentry cache hash table entries: 131072 (order: 7, 524288 bytes, linear)
Inode-cache hash table entries: 65536 (order: 6, 262144 bytes, linear)
mem auto-init: stack:all(zero), heap alloc:off, heap free:off
Memory: 1996084K/2097152K available (9216K kernel code, 1123K rwdata, 2988K rodata, 1024K init, 421K bss, 35532K reserved, 65536K cma-reserved, 1245184K highmem)
SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=4, Nodes=1
rcu: Preemptible hierarchical RCU implementation.
rcu: 	RCU event tracing is enabled.
	Trampoline variant of Tasks RCU enabled.
	Tracing variant of Tasks RCU enabled.
rcu: RCU calculated value of scheduler-enlistment delay is 10 jiffies.
NR_IRQS: 16, nr_irqs: 16, preallocated irqs: 16
L2C: DT/platform modifies aux control register: 0x32070000 -> 0x32470000
L2C-310 errata 752271 769419 enabled
L2C-310 enabling early BRESP for Cortex-A9
L2C-310 full line of zeros enabled for Cortex-A9
L2C-310 ID prefetch enabled, offset 16 lines
L2C-310 dynamic clock gating enabled, standby mode enabled
L2C-310 cache controller enabled, 16 ways, 1024 kB
L2C-310: CACHE_ID 0x410000c7, AUX_CTRL 0x76470001
Switching to timer-based delay loop, resolution 333ns
sched_clock: 32 bits at 3000kHz, resolution 333ns, wraps every 715827882841ns
clocksource: mxc_timer1: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 637086815595 ns
Console: colour dummy device 80x30
Calibrating delay loop (skipped), value calculated using timer frequency.. 6.00 BogoMIPS (lpj=30000)
pid_max: default: 32768 minimum: 301
Mount-cache hash table entries: 2048 (order: 1, 8192 bytes, linear)
Mountpoint-cache hash table entries: 2048 (order: 1, 8192 bytes, linear)
CPU: Testing write buffer coherency: ok
CPU0: Spectre v2: using BPIALL workaround
CPU0: thread -1, cpu 0, socket 0, mpidr 80000000
Setting up static identity map for 0x10100000 - 0x10100060
rcu: Hierarchical SRCU implementation.
EFI services will not be available.
smp: Bringing up secondary CPUs ...
CPU1: thread -1, cpu 1, socket 0, mpidr 80000001
CPU1: Spectre v2: using BPIALL workaround
CPU2: thread -1, cpu 2, socket 0, mpidr 80000002
CPU2: Spectre v2: using BPIALL workaround
CPU3: thread -1, cpu 3, socket 0, mpidr 80000003
CPU3: Spectre v2: using BPIALL workaround
smp: Brought up 1 node, 4 CPUs
SMP: Total of 4 processors activated (24.00 BogoMIPS).
CPU: All CPU(s) started in SVC mode.
devtmpfs: initialized
VFP support v0.3: implementor 41 architecture 3 part 30 variant 9 rev 4
clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604462750000 ns
futex hash table entries: 1024 (order: 4, 65536 bytes, linear)
pinctrl core: initialized pinctrl subsystem
DMI not present or invalid.
NET: Registered protocol family 16
DMA: preallocated 256 KiB pool for atomic coherent allocations
thermal_sys: Registered thermal governor 'step_wise'
cpuidle: using governor menu
CPU identified as i.MX6Q, silicon rev 1.6
vdd1p1: supplied by regulator-dummy
vdd3p0: supplied by regulator-dummy
vdd2p5: supplied by regulator-dummy
vddarm: supplied by regulator-dummy
vddpu: supplied by regulator-dummy
vddsoc: supplied by regulator-dummy
No ATAGs?
hw-breakpoint: found 5 (+1 reserved) breakpoint and 1 watchpoint registers.
hw-breakpoint: maximum watchpoint size is 4 bytes.
imx6q-pinctrl 20e0000.pinctrl: initialized IMX pinctrl driver
vgaarb: loaded
SCSI subsystem initialized
libata version 3.00 loaded.
usbcore: registered new interface driver usbfs
usbcore: registered new interface driver hub
usbcore: registered new device driver usb
usb_phy_generic usbphynop1: supply vcc not found, using dummy regulator
usb_phy_generic usbphynop1: dummy supplies not allowed for exclusive requests
usb_phy_generic usbphynop2: supply vcc not found, using dummy regulator
usb_phy_generic usbphynop2: dummy supplies not allowed for exclusive requests
i2c i2c-0: IMX I2C adapter registered
i2c i2c-1: IMX I2C adapter registered
pps_core: LinuxPPS API ver. 1 registered
pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
PTP clock support registered
clocksource: Switched to clocksource mxc_timer1
VFS: Disk quotas dquot_6.6.0
VFS: Dquot-cache hash table entries: 1024 (order 0, 4096 bytes)
NET: Registered protocol family 2
IP idents hash table entries: 16384 (order: 5, 131072 bytes, linear)
tcp_listen_portaddr_hash hash table entries: 512 (order: 0, 6144 bytes, linear)
TCP established hash table entries: 8192 (order: 3, 32768 bytes, linear)
TCP bind hash table entries: 8192 (order: 4, 65536 bytes, linear)
TCP: Hash tables configured (established 8192 bind 8192)
MPTCP token hash table entries: 1024 (order: 2, 16384 bytes, linear)
UDP hash table entries: 512 (order: 2, 16384 bytes, linear)
UDP-Lite hash table entries: 512 (order: 2, 16384 bytes, linear)
NET: Registered protocol family 1
RPC: Registered named UNIX socket transport module.
RPC: Registered udp transport module.
RPC: Registered tcp transport module.
RPC: Registered tcp NFSv4.1 backchannel transport module.
NET: Registered protocol family 44
PCI: CLS 0 bytes, default 64
hw perfevents: no interrupt-affinity property for /pmu, guessing.
hw perfevents: enabled with armv7_cortex_a9 PMU driver, 7 counters available
Initialise system trusted keyrings
workingset: timestamp_bits=14 max_order=19 bucket_order=5
Key type asymmetric registered
Asymmetric key parser 'x509' registered
bounce: pool size: 64 pages
Block layer SCSI generic (bsg) driver version 0.4 loaded (major 248)
io scheduler mq-deadline registered
io scheduler kyber registered
imx6q-pcie 1ffc000.pcie: host bridge /soc/pcie@1ffc000 ranges:
imx6q-pcie 1ffc000.pcie:       IO 0x0001f80000..0x0001f8ffff -> 0x0000000000
imx6q-pcie 1ffc000.pcie:      MEM 0x0001000000..0x0001efffff -> 0x0001000000
imx-sdma 20ec000.dma-controller: loaded firmware 3.5
2020000.serial: ttymxc0 at MMIO 0x2020000 (irq = 34, base_baud = 5000000) is a IMX
printk: console [ttymxc0] enabled
21e8000.serial: ttymxc1 at MMIO 0x21e8000 (irq = 72, base_baud = 5000000) is a IMX
21ec000.serial: ttymxc2 at MMIO 0x21ec000 (irq = 73, base_baud = 5000000) is a IMX
21f0000.serial: ttymxc3 at MMIO 0x21f0000 (irq = 74, base_baud = 5000000) is a IMX
21f4000.serial: ttymxc4 at MMIO 0x21f4000 (irq = 75, base_baud = 5000000) is a IMX
etnaviv etnaviv: bound 130000.gpu (ops gpu_ops)
etnaviv etnaviv: bound 134000.gpu (ops gpu_ops)
etnaviv etnaviv: bound 2204000.gpu (ops gpu_ops)
etnaviv-gpu 130000.gpu: model: GC2000, revision: 5108
etnaviv-gpu 134000.gpu: model: GC320, revision: 5007
etnaviv-gpu 2204000.gpu: model: GC355, revision: 1215
etnaviv-gpu 2204000.gpu: Ignoring GPU with VG and FE2.0
[drm] Initialized etnaviv 1.3.0 20151214 for etnaviv on minor 0
imx-ipuv3 2400000.ipu: IPUv3H probed
imx-drm display-subsystem: bound imx-ipuv3-crtc.2 (ops ipu_crtc_ops)
imx-drm display-subsystem: bound imx-ipuv3-crtc.3 (ops ipu_crtc_ops)
imx-drm display-subsystem: bound imx-ipuv3-crtc.6 (ops ipu_crtc_ops)
imx-drm display-subsystem: bound imx-ipuv3-crtc.7 (ops ipu_crtc_ops)
[drm] Initialized imx-drm 1.0.0 20120507 for display-subsystem on minor 1
imx-ipuv3 2800000.ipu: IPUv3H probed
brd: module loaded
loop: module loaded
at24 0-0057: supply vcc not found, using dummy regulator
at24 0-0057: 128 byte 24c01 EEPROM, writable, 128 bytes/write
ahci-imx 2200000.sata: fsl,transmit-level-mV not specified, using 00000024
ahci-imx 2200000.sata: fsl,transmit-boost-mdB not specified, using 00000480
ahci-imx 2200000.sata: fsl,transmit-atten-16ths not specified, using 00002000
ahci-imx 2200000.sata: fsl,receive-eq-mdB not specified, using 05000000
ahci-imx 2200000.sata: supply ahci not found, using dummy regulator
ahci-imx 2200000.sata: supply phy not found, using dummy regulator
ahci-imx 2200000.sata: supply target not found, using dummy regulator
ahci-imx 2200000.sata: SSS flag set, parallel bus scan disabled
ahci-imx 2200000.sata: AHCI 0001.0300 32 slots 1 ports 3 Gbps 0x1 impl platform mode
ahci-imx 2200000.sata: flags: ncq sntf stag pm led clo only pmp pio slum part ccc apst 
scsi host0: ahci-imx
ata1: SATA max UDMA/133 mmio [mem 0x02200000-0x02203fff] port 0x100 irq 78
spi-nor spi0.0: is25lp064 (8192 Kbytes)
pps pps0: new PPS source ptp0
fec 2188000.ethernet eth0: registered PHC device 0
ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
ehci-pci: EHCI PCI platform driver
ehci-mxc: Freescale On-Chip EHCI Host driver
usbcore: registered new interface driver usb-storage
hwmon hwmon0: temp1_input not attached to any thermal zone
rtc-isl12022 0-006f: Total power failure, RTC data is invalid.
rtc-isl12022 0-006f: registered as rtc0
rtc-isl12022 0-006f: Total power failure, RTC data is invalid.
rtc-isl12022 0-006f: hctosys: unable to read the hardware clock
i2c /dev entries driver
sdhci: Secure Digital Host Controller Interface driver
sdhci: Copyright(c) Pierre Ossman
sdhci-pltfm: SDHCI platform and OF driver helper
caam 2100000.crypto: Entropy delay = 3200
mmc1: SDHCI controller on 2194000.mmc [2194000.mmc] using ADMA
imx6q-pcie 1ffc000.pcie: Phy link never came up
mmc2: SDHCI controller on 2198000.mmc [2198000.mmc] using ADMA
imx6q-pcie 1ffc000.pcie: PCI host bridge to bus 0000:00
pci_bus 0000:00: root bus resource [bus 00-ff]
pci_bus 0000:00: root bus resource [io  0x0000-0xffff]
caam 2100000.crypto: Instantiated RNG4 SH0
pci_bus 0000:00: root bus resource [mem 0x01000000-0x01efffff]
pci 0000:00:00.0: [16c3:abcd] type 01 class 0x060400
pci 0000:00:00.0: reg 0x10: [mem 0x00000000-0x000fffff]
pci 0000:00:00.0: reg 0x38: [mem 0x00000000-0x0000ffff pref]
pci 0000:00:00.0: Limiting cfg_size to 512
pci 0000:00:00.0: supports D1
pci 0000:00:00.0: PME# supported from D0 D1 D3hot D3cold
PCI: bus0: Fast back to back transfers disabled
caam 2100000.crypto: Instantiated RNG4 SH1
PCI: bus1: Fast back to back transfers enabled
caam 2100000.crypto: device ID = 0x0a16010000000000 (Era 4)
caam 2100000.crypto: job rings = 2, qi = 0
caam algorithms registered in /proc/crypto
pci 0000:00:00.0: BAR 0: assigned [mem 0x01000000-0x010fffff]
caam 2100000.crypto: registering rng-caam
pci 0000:00:00.0: BAR 6: assigned [mem 0x01100000-0x0110ffff pref]
pci 0000:00:00.0: PCI bridge to [bus 01-ff]
usbcore: registered new interface driver usbhid
usbhid: USB HID core driver
NET: Registered protocol family 10
Segment Routing with IPv6
mmc2: new DDR MMC card at address 0001
RPL Segment Routing with IPv6
mmcblk2: mmc2:0001 Q2J54A 3.59 GiB 
NET: Registered protocol family 17
mmcblk2boot0: mmc2:0001 Q2J54A partition 1 16.0 MiB
Key type dns_resolver registered
mmcblk2boot1: mmc2:0001 Q2J54A partition 2 16.0 MiB
mmcblk2rpmb: mmc2:0001 Q2J54A partition 3 512 KiB, chardev (245:0)
Registering SWP/SWPB emulation handler
 mmcblk2: p1 p2
Loading compiled-in X.509 certificates
ci_hdrc ci_hdrc.1: EHCI Host Controller
ci_hdrc ci_hdrc.1: new USB bus registered, assigned bus number 1
ci_hdrc ci_hdrc.1: USB 2.0 started, EHCI 1.00
usb usb1: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 5.10
mmc1: new high speed SDHC card at address 0001
usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
usb usb1: Product: EHCI Host Controller
mmcblk1: mmc1:0001 0008G 7.54 GiB 
usb usb1: Manufacturer: Linux 5.10.170 ehci_hcd
ata1: SATA link up 3.0 Gbps (SStatus 123 SControl 300)
ata1.00: ATA-10: INTEL SSDSC2KG960G8, XCV10100, max UDMA/133
ata1.00: 1875385008 sectors, multi 1: LBA48 NCQ (depth 32)
ata1.00: configured for UDMA/133
scsi 0:0:0:0: Direct-Access     ATA      INTEL SSDSC2KG96 0100 PQ: 0 ANSI: 5
ata1.00: Enabling discard_zeroes_data
random: crng init done
usb usb1: SerialNumber: ci_hdrc.1
sd 0:0:0:0: [sda] 1875385008 512-byte logical blocks: (960 GB/894 GiB)
hub 1-0:1.0: USB hub found
 mmcblk1: p1
sd 0:0:0:0: [sda] 4096-byte physical blocks
sd 0:0:0:0: [sda] Write Protect is off
sd 0:0:0:0: [sda] Mode Sense: 00 3a 00 00
sd 0:0:0:0: [sda] Write cache: enabled, read cache: enabled, doesn't support DPO or FUA
hub 1-0:1.0: 1 port detected
ata1.00: Enabling discard_zeroes_data
imx_thermal 20c8000.anatop:tempmon: Extended Commercial CPU temperature grade - max:105C critical:100C passive:95C
 sda: sda1
ata1.00: Enabling discard_zeroes_data
sd 0:0:0:0: [sda] Attached SCSI disk
mmc0: SDHCI controller on 2190000.mmc [2190000.mmc] using ADMA
EXT4-fs (mmcblk1p1): mounting ext3 file system using the ext4 subsystem
EXT4-fs (mmcblk1p1): mounted filesystem with ordered data mode. Opts: (null)
VFS: Mounted root (ext3 filesystem) readonly on device 179:25.
devtmpfs: mounted
Freeing unused kernel memory: 1024K
Run /sbin/init as init process
  with arguments:
    /sbin/init
  with environment:
    HOME=/
    TERM=linux
usb 1-1: new high-speed USB device number 2 using ci_hdrc
usb 1-1: New USB device found, idVendor=0424, idProduct=2514, bcdDevice= b.b3
usb 1-1: New USB device strings: Mfr=0, Product=0, SerialNumber=0
hub 1-1:1.0: USB hub found
hub 1-1:1.0: 4 ports detected
usb 1-1.1: new full-speed USB device number 3 using ci_hdrc
systemd[1]: System time before build time, advancing clock.
usb 1-1.1: New USB device found, idVendor=0403, idProduct=6001, bcdDevice= 6.00
usb 1-1.1: New USB device strings: Mfr=1, Product=2, SerialNumber=3
usb 1-1.1: Product: USB-RS422 Cable
usb 1-1.1: Manufacturer: FTDI
usb 1-1.1: SerialNumber: FTVWJYS0
systemd[1]: Inserted module 'autofs4'
usb 1-1.2: new full-speed USB device number 4 using ci_hdrc
systemd[1]: systemd 252.12-1~deb12u1 running in system mode (+PAM +AUDIT +SELINUX +APPARMOR +IMA +SMACK +SECCOMP +GCRYPT -GNUTLS +OPENSSL +ACL +BLKID +CURL +ELFUTILS +FIDO2 +IDN2 -IDN +IPTC +KMOD +LIBCRYPTSETUP +LIBFDISK +PCRE2 -PWQUALITY +P11KIT +QRENCODE +TPM2 +BZIP2 +LZ4 +XZ +ZLIB +ZSTD -BPF_FRAMEWORK -XKBCOMMON +UTMP +SYSVINIT default-hierarchy=unified)
systemd[1]: Detected architecture arm.
systemd[1]: Hostname set to <gusto-data>.
usb 1-1.2: New USB device found, idVendor=16c0, idProduct=0483, bcdDevice= 2.77
usb 1-1.2: New USB device strings: Mfr=1, Product=2, SerialNumber=3
usb 1-1.2: Product: USB Serial
usb 1-1.2: Manufacturer: Teensyduino
usb 1-1.2: SerialNumber: B1LO_CTRL
usb 1-1.3: new full-speed USB device number 5 using ci_hdrc
usb 1-1.3: New USB device found, idVendor=16c0, idProduct=0483, bcdDevice= 2.77
usb 1-1.3: New USB device strings: Mfr=1, Product=2, SerialNumber=3
usb 1-1.3: Product: USB Serial
usb 1-1.3: Manufacturer: Teensyduino
usb 1-1.3: SerialNumber: B2LO_CTRL
usb 1-1.4: new full-speed USB device number 6 using ci_hdrc
systemd[1]: /etc/systemd/system/fixup-nfsboot.service:7: Unknown key name 'After' in section 'Service', ignoring.
systemd[1]: /etc/systemd/system/fixup-nfsboot.service:8: Unknown key name 'Wants' in section 'Service', ignoring.
usb 1-1.4: New USB device found, idVendor=16c0, idProduct=0483, bcdDevice= 2.77
usb 1-1.4: New USB device strings: Mfr=1, Product=2, SerialNumber=3
usb 1-1.4: Product: USB Serial
usb 1-1.4: Manufacturer: Teensyduino
usb 1-1.4: SerialNumber: B3LO_CTRL
systemd[1]: Queued start job for default target graphical.target.
systemd[1]: Created slice system-modprobe.slice - Slice /system/modprobe.
systemd[1]: Created slice system-serial\x2dgetty.slice - Slice /system/serial-getty.
systemd[1]: Created slice system-systemd\x2dfsck.slice - Slice /system/systemd-fsck.
systemd[1]: Created slice user.slice - User and Session Slice.
systemd[1]: Started systemd-ask-password-console.path - Dispatch Password Requests to Console Directory Watch.
systemd[1]: Started systemd-ask-password-wall.path - Forward Password Requests to Wall Directory Watch.
systemd[1]: Set up automount proc-sys-fs-binfmt_misc.automount - Arbitrary Executable File Formats File System Automount Point.
systemd[1]: Reached target cryptsetup.target - Local Encrypted Volumes.
systemd[1]: Reached target integritysetup.target - Local Integrity Protected Volumes.
systemd[1]: Reached target nss-lookup.target - Host and Network Name Lookups.
systemd[1]: Reached target paths.target - Path Units.
systemd[1]: Reached target slices.target - Slice Units.
systemd[1]: Reached target swap.target - Swaps.
systemd[1]: Reached target veritysetup.target - Local Verity Protected Volumes.
systemd[1]: Listening on rpcbind.socket - RPCbind Server Activation Socket.
systemd[1]: Listening on systemd-fsckd.socket - fsck to fsckd communication Socket.
systemd[1]: Listening on systemd-initctl.socket - initctl Compatibility Named Pipe.
systemd[1]: systemd-journald-audit.socket - Journal Audit Socket was skipped because of an unmet condition check (ConditionSecurity=audit).
systemd[1]: Listening on systemd-journald-dev-log.socket - Journal Socket (/dev/log).
systemd[1]: Listening on systemd-journald.socket - Journal Socket.
systemd[1]: Listening on systemd-udevd-control.socket - udev Control Socket.
systemd[1]: Listening on systemd-udevd-kernel.socket - udev Kernel Socket.
systemd[1]: dev-hugepages.mount - Huge Pages File System was skipped because of an unmet condition check (ConditionPathExists=/sys/kernel/mm/hugepages).
systemd[1]: Mounting dev-mqueue.mount - POSIX Message Queue File System...
systemd[1]: Mounting proc-fs-nfsd.mount - NFSD configuration filesystem...
systemd[1]: Mounting sys-kernel-debug.mount - Kernel Debug File System...
systemd[1]: sys-kernel-tracing.mount - Kernel Trace File System was skipped because of an unmet condition check (ConditionPathExists=/sys/kernel/tracing).
systemd[1]: auth-rpcgss-module.service - Kernel Module supporting RPCSEC_GSS was skipped because of an unmet condition check (ConditionPathExists=/etc/krb5.keytab).
systemd[1]: Starting kmod-static-nodes.service - Create List of Static Device Nodes...
systemd[1]: Starting modprobe@configfs.service - Load Kernel Module configfs...
systemd[1]: Starting modprobe@dm_mod.service - Load Kernel Module dm_mod...
systemd[1]: Starting modprobe@drm.service - Load Kernel Module drm...
device-mapper: ioctl: 4.43.0-ioctl (2020-10-01) initialised: dm-devel@redhat.com
systemd[1]: Starting modprobe@efi_pstore.service - Load Kernel Module efi_pstore...
systemd[1]: Starting modprobe@fuse.service - Load Kernel Module fuse...
fuse: init (API version 7.32)
systemd[1]: Starting modprobe@loop.service - Load Kernel Module loop...
systemd[1]: Starting networking.service - Network initialization...
systemd[1]: Starting systemd-fsck-root.service - File System Check on Root Device...
systemd[1]: Starting systemd-journald.service - Journal Service...
systemd[1]: Starting systemd-modules-load.service - Load Kernel Modules...
systemd[1]: Starting systemd-udev-trigger.service - Coldplug All udev Devices...
systemd[1]: Mounted dev-mqueue.mount - POSIX Message Queue File System.
systemd[1]: proc-fs-nfsd.mount: Mount process exited, code=exited, status=32/n/a
systemd[1]: proc-fs-nfsd.mount: Failed with result 'exit-code'.
systemd[1]: Failed to mount proc-fs-nfsd.mount - NFSD configuration filesystem.
systemd[1]: Dependency failed for nfs-mountd.service - NFS Mount Daemon.
systemd[1]: Dependency failed for nfs-server.service - NFS server and services.
systemd[1]: Dependency failed for nfs-idmapd.service - NFSv4 ID-name mapping service.
systemd[1]: nfs-idmapd.service: Job nfs-idmapd.service/start failed with result 'dependency'.
systemd[1]: nfs-server.service: Job nfs-server.service/start failed with result 'dependency'.
systemd[1]: nfs-mountd.service: Job nfs-mountd.service/start failed with result 'dependency'.
systemd[1]: Dependency failed for nfsdcld.service - NFSv4 Client Tracking Daemon.
systemd[1]: nfsdcld.service: Job nfsdcld.service/start failed with result 'dependency'.
systemd[1]: Mounted sys-kernel-debug.mount - Kernel Debug File System.
systemd[1]: Finished kmod-static-nodes.service - Create List of Static Device Nodes.
systemd[1]: modprobe@configfs.service: Deactivated successfully.
systemd[1]: Finished modprobe@configfs.service - Load Kernel Module configfs.
systemd[1]: modprobe@dm_mod.service: Deactivated successfully.
systemd[1]: Finished modprobe@dm_mod.service - Load Kernel Module dm_mod.
systemd[1]: modprobe@drm.service: Deactivated successfully.
systemd[1]: Finished modprobe@drm.service - Load Kernel Module drm.
systemd[1]: modprobe@efi_pstore.service: Deactivated successfully.
systemd[1]: Finished modprobe@efi_pstore.service - Load Kernel Module efi_pstore.
systemd[1]: Started systemd-journald.service - Journal Service.
EXT4-fs (mmcblk1p1): re-mounted. Opts: (null)
systemd-journald[228]: Received client request to flush runtime journal.
systemd-journald[228]: File /var/log/journal/a8281aabb76084893e65167c64d14c75/system.journal corrupted or uncleanly shut down, renaming and replacing.
fec 2188000.ethernet end0: renamed from eth0
CAN device driver interface
mc: Linux media interface: v0.10
------------[ cut here ]------------
WARNING: CPU: 3 PID: 274 at drivers/spi/spidev.c:749 spidev_probe+0xf0/0x198 [spidev]
videodev: Linux video capture interface: v2.00
/soc/bus@2000000/spba-bus@2000000/spi@200c000/spi@1: buggy DT: spidev listed directly in DT
Modules linked in: videobuf2_vmalloc videobuf2_memops videobuf2_v4l2 videobuf2_common snd_timer snd videodev soundcore spidev(+) flexcan mc can_dev uio_pdrv_genirq uio fuse dm_mod ip_tables x_tables autofs4
CPU: 3 PID: 274 Comm: (udev-worker) Not tainted 5.10.170 #1
Hardware name: Freescale i.MX6 Quad/DualLite (Device Tree)
[<c010f200>] (unwind_backtrace) from [<c010a650>] (show_stack+0x10/0x14)
[<c010a650>] (show_stack) from [<c0988040>] (dump_stack+0x94/0xa8)
[<c0988040>] (dump_stack) from [<c09857a8>] (__warn+0x8c/0x100)
[<c09857a8>] (__warn) from [<c09858b4>] (warn_slowpath_fmt+0x98/0xcc)
[<c09858b4>] (warn_slowpath_fmt) from [<bf0ae228>] (spidev_probe+0xf0/0x198 [spidev])
[<bf0ae228>] (spidev_probe [spidev]) from [<c065d650>] (spi_drv_probe+0x84/0xac)
[<c065d650>] (spi_drv_probe) from [<c05e78e8>] (really_probe+0xf0/0x49c)
[<c05e78e8>] (really_probe) from [<c05e7fc0>] (driver_probe_device+0x5c/0xb4)
[<c05e7fc0>] (driver_probe_device) from [<c05e82bc>] (device_driver_attach+0xa8/0xb0)
[<c05e82bc>] (device_driver_attach) from [<c05e8324>] (__driver_attach+0x60/0x104)
[<c05e8324>] (__driver_attach) from [<c05e58cc>] (bus_for_each_dev+0x80/0xcc)
[<c05e58cc>] (bus_for_each_dev) from [<c05e6c68>] (bus_add_driver+0xf8/0x1e8)
[<c05e6c68>] (bus_add_driver) from [<c05e8be0>] (driver_register+0x88/0x118)
[<c05e8be0>] (driver_register) from [<bf0b4094>] (spidev_init+0x94/0x1000 [spidev])
[<bf0b4094>] (spidev_init [spidev]) from [<c0101874>] (do_one_initcall+0x68/0x1f0)
[<c0101874>] (do_one_initcall) from [<c01b6d34>] (do_init_module+0x40/0x244)
[<c01b6d34>] (do_init_module) from [<c01b9a60>] (sys_finit_module+0xb8/0xf8)
[<c01b9a60>] (sys_finit_module) from [<c01002a0>] (__sys_trace_return+0x0/0x20)
Exception stack(0xc35fdfa8 to 0xc35fdff0)
dfa0:                   b6eeec90 00b861b8 00000006 b6eedad8 00000000 b6eee7bc
dfc0: b6eeec90 00b861b8 bafc8c00 0000017b 00b80ff0 00000000 00000000 00000000
dfe0: beb72798 beb72788 b6ee8051 b6e1bdd2
coda 2040000.vpu: Direct firmware load for vpu_fw_imx6q.bin failed with error -2
coda 2040000.vpu: Direct firmware load for vpu/vpu_fw_imx6q.bin failed with error -2
coda 2040000.vpu: Direct firmware load for v4l-coda960-imx6q.bin failed with error -2
coda 2040000.vpu: firmware request failed
---[ end trace 19c0f79f26c463b6 ]---
usbcore: registered new interface driver usbserial_generic
usbserial: USB Serial support registered for generic
usbcore: registered new interface driver ftdi_sio
usbserial: USB Serial support registered for FTDI USB Serial Device
ftdi_sio 1-1.1:1.0: FTDI USB Serial Device converter detected
cdc_acm 1-1.2:1.0: ttyACM0: USB ACM device
usb 1-1.1: Detected FT232RL
usb 1-1.1: FTDI USB Serial Device converter now attached to ttyUSB0
cdc_acm 1-1.3:1.0: ttyACM1: USB ACM device
cdc_acm 1-1.4:1.0: ttyACM2: USB ACM device
usbcore: registered new interface driver cdc_acm
cdc_acm: USB Abstract Control Model driver for USB modems and ISDN adapters
EXT4-fs (sda1): mounted filesystem with ordered data mode. Opts: (null)
Micrel KSZ9031 Gigabit PHY 2188000.ethernet-1:07: attached PHY driver [Micrel KSZ9031 Gigabit PHY] (mii_bus:phy_addr=2188000.ethernet-1:07, irq=POLL)
systemd-journald[228]: Oldest entry in /var/log/journal/a8281aabb76084893e65167c64d14c75/system.journal is older than the configured file retention duration (1month), suggesting rotation.
systemd-journald[228]: /var/log/journal/a8281aabb76084893e65167c64d14c75/system.journal: Journal header limits reached or header out-of-date, rotating.
systemd-journald[228]: Failed to read journal file /var/log/journal/a8281aabb76084893e65167c64d14c75/user-1001.journal for rotation, trying to move it out of the way: Text file busy
fec 2188000.ethernet end0: Link is Up - 100Mbps/Half - flow control off
IPv6: ADDRCONF(NETDEV_CHANGE): end0: link becomes ready
