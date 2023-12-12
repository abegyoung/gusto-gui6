Booting Linux on physical CPU 0x0
Linux version 5.10.201-gea8959c1966f-dirty (ckulesa@supercam9) (arm-linux-gnueabihf-gcc (Debian 8.3.0-2) 8.3.0, GNU ld (GNU Binutils for Debian) 2.31.1) #3 SMP PREEMPT Mon Nov 27 12:48:20 MST 2023
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
percpu: Embedded 16 pages/cpu s32908 r8192 d24436 u65536
pcpu-alloc: s32908 r8192 d24436 u65536 alloc=16*4096
pcpu-alloc: [0] 0 [0] 1 [0] 2 [0] 3 
Built 1 zonelists, mobility grouping on.  Total pages: 522560
Kernel command line: root=/dev/mmcblk1p1 rootwait rw console=ttymxc0,115200 ro init=/sbin/init
Dentry cache hash table entries: 131072 (order: 7, 524288 bytes, linear)
Inode-cache hash table entries: 65536 (order: 6, 262144 bytes, linear)
mem auto-init: stack:off, heap alloc:off, heap free:off
Memory: 2001264K/2097152K available (6144K kernel code, 1103K rwdata, 1664K rodata, 1024K init, 383K bss, 30352K reserved, 65536K cma-reserved, 1245184K highmem)
rcu: Preemptible hierarchical RCU implementation.
	Trampoline variant of Tasks RCU enabled.
	Tracing variant of Tasks RCU enabled.
rcu: RCU calculated value of scheduler-enlistment delay is 100 jiffies.
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
Calibrating delay loop (skipped), value calculated using timer frequency.. 6.00 BogoMIPS (lpj=3000)
CPU: Testing write buffer coherency: ok
CPU0: Spectre v2: using BPIALL workaround
pid_max: default: 32768 minimum: 301
Mount-cache hash table entries: 2048 (order: 1, 8192 bytes, linear)
Mountpoint-cache hash table entries: 2048 (order: 1, 8192 bytes, linear)
CPU0: thread -1, cpu 0, socket 0, mpidr 80000000
Setting up static identity map for 0x10100000 - 0x10100078
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
clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 1911260446275000 ns
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
imx6q-pinctrl 20e0000.pinctrl: initialized IMX pinctrl driver
vgaarb: loaded
SCSI subsystem initialized
libata version 3.00 loaded.
usbcore: registered new interface driver usbfs
usbcore: registered new interface driver hub
usbcore: registered new device driver usb
i2c i2c-0: IMX I2C adapter registered
i2c i2c-1: IMX I2C adapter registered
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
NET: Registered protocol family 44
PCI: CLS 0 bytes, default 64
Initialise system trusted keyrings
workingset: timestamp_bits=14 max_order=19 bucket_order=5
Key type asymmetric registered
Asymmetric key parser 'x509' registered
bounce: pool size: 64 pages
Block layer SCSI generic (bsg) driver version 0.4 loaded (major 250)
io scheduler mq-deadline registered
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
max3100-ts spi1.0: Detected 0 uarts
------------[ cut here ]------------
WARNING: CPU: 1 PID: 1 at drivers/spi/spidev.c:752 spidev_probe+0x40/0x178
/soc/bus@2000000/spba-bus@2000000/spi@200c000/spi@1: buggy DT: spidev listed directly in DT
Modules linked in:
CPU: 1 PID: 1 Comm: swapper/0 Not tainted 5.10.201-gea8959c1966f-dirty #3
Hardware name: Freescale i.MX6 Quad/DualLite (Device Tree)
[<c010cfa0>] (unwind_backtrace) from [<c0108e44>] (show_stack+0x10/0x14)
[<c0108e44>] (show_stack) from [<c06ab564>] (dump_stack+0xbc/0xe4)
[<c06ab564>] (dump_stack) from [<c06a8f78>] (__warn+0x7c/0xb0)
[<c06a8f78>] (__warn) from [<c06a9020>] (warn_slowpath_fmt+0x74/0xa4)
[<c06a9020>] (warn_slowpath_fmt) from [<c04aa8a4>] (spidev_probe+0x40/0x178)
[<c04aa8a4>] (spidev_probe) from [<c04a5e4c>] (spi_drv_probe+0x84/0xa0)
[<c04a5e4c>] (spi_drv_probe) from [<c0452484>] (really_probe+0x22c/0x384)
[<c0452484>] (really_probe) from [<c0452880>] (driver_probe_device+0x138/0x150)
[<c0452880>] (driver_probe_device) from [<c04509e0>] (bus_for_each_drv+0xa0/0xb4)
[<c04509e0>] (bus_for_each_drv) from [<c04526b8>] (__device_attach+0xdc/0x14c)
[<c04526b8>] (__device_attach) from [<c0451618>] (bus_probe_device+0x28/0x80)
[<c0451618>] (bus_probe_device) from [<c044f788>] (device_add+0x5ac/0x6c0)
[<c044f788>] (device_add) from [<c04a757c>] (spi_add_device+0xfc/0x14c)
[<c04a757c>] (spi_add_device) from [<c04a7fc0>] (spi_register_controller+0x8e4/0x9bc)
[<c04a7fc0>] (spi_register_controller) from [<c04ab6a8>] (spi_bitbang_start+0x38/0x58)
[<c04ab6a8>] (spi_bitbang_start) from [<c04acfb0>] (spi_imx_probe+0x3d0/0x4cc)
[<c04acfb0>] (spi_imx_probe) from [<c0453f08>] (platform_drv_probe+0x48/0x94)
[<c0453f08>] (platform_drv_probe) from [<c0452484>] (really_probe+0x22c/0x384)
[<c0452484>] (really_probe) from [<c0452880>] (driver_probe_device+0x138/0x150)
[<c0452880>] (driver_probe_device) from [<c0452a2c>] (device_driver_attach+0x44/0x5c)
[<c0452a2c>] (device_driver_attach) from [<c0452b00>] (__driver_attach+0xbc/0xc4)
[<c0452b00>] (__driver_attach) from [<c04508f0>] (bus_for_each_dev+0x64/0xa0)
[<c04508f0>] (bus_for_each_dev) from [<c04517f8>] (bus_add_driver+0xac/0x1bc)
[<c04517f8>] (bus_add_driver) from [<c0453190>] (driver_register+0xac/0xf0)
[<c0453190>] (driver_register) from [<c0101820>] (do_one_initcall+0x70/0x1a4)
[<c0101820>] (do_one_initcall) from [<c0901214>] (kernel_init_freeable+0x23c/0x294)
[<c0901214>] (kernel_init_freeable) from [<c06af7d8>] (kernel_init+0x8/0x118)
[<c06af7d8>] (kernel_init) from [<c0100168>] (ret_from_fork+0x14/0x2c)
Exception stack(0xc2077fb0 to 0xc2077ff8)
7fa0:                                     00000000 00000000 00000000 00000000
7fc0: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000
7fe0: 00000000 00000000 00000000 00000000 00000013 00000000
---[ end trace f42f5135fb2449b0 ]---
ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
ehci-mxc: Freescale On-Chip EHCI Host driver
usbcore: registered new interface driver usb-storage
hwmon hwmon0: temp1_input not attached to any thermal zone
rtc-isl12022 0-006f: Total power failure, RTC data is invalid.
rtc-isl12022 0-006f: registered as rtc0
rtc-isl12022 0-006f: Total power failure, RTC data is invalid.
rtc-isl12022 0-006f: hctosys: unable to read the hardware clock
i2c /dev entries driver
sdhci: Secure Digital Host Controller Interface driver
imx6q-pcie 1ffc000.pcie: Phy link never came up
sdhci: Copyright(c) Pierre Ossman
imx6q-pcie 1ffc000.pcie: PCI host bridge to bus 0000:00
sdhci-pltfm: SDHCI platform and OF driver helper
pci_bus 0000:00: root bus resource [bus 00-ff]
pci_bus 0000:00: root bus resource [io  0x0000-0xffff]
ledtrig-cpu: registered to indicate activity on CPUs
caam 2100000.crypto: Entropy delay = 3200
pci_bus 0000:00: root bus resource [mem 0x01000000-0x01efffff]
pci 0000:00:00.0: [16c3:abcd] type 01 class 0x060400
mmc1: SDHCI controller on 2194000.mmc [2194000.mmc] using ADMA
pci 0000:00:00.0: reg 0x10: [mem 0x00000000-0x000fffff]
mmc2: SDHCI controller on 2198000.mmc [2198000.mmc] using ADMA
ata1: SATA link up 3.0 Gbps (SStatus 123 SControl 300)
pci 0000:00:00.0: reg 0x38: [mem 0x00000000-0x0000ffff pref]
ata1.00: ATA-10: INTEL SSDSC2KG960G8, XCV10100, max UDMA/133
pci 0000:00:00.0: Limiting cfg_size to 512
ata1.00: 1875385008 sectors, multi 1: LBA48 NCQ (depth 32)
pci 0000:00:00.0: imx6_pcie_quirk+0x0/0x6c took 13164 usecs
caam 2100000.crypto: Instantiated RNG4 SH0
ata1.00: configured for UDMA/133
pci 0000:00:00.0: supports D1
mmc2: new DDR MMC card at address 0001
pci 0000:00:00.0: PME# supported from D0 D1 D3hot D3cold
PCI: bus0: Fast back to back transfers disabled
mmcblk2: mmc2:0001 Q2J54A 3.59 GiB 
PCI: bus1: Fast back to back transfers enabled
mmcblk2boot0: mmc2:0001 Q2J54A partition 1 16.0 MiB
pci 0000:00:00.0: BAR 0: assigned [mem 0x01000000-0x010fffff]
mmcblk2boot1: mmc2:0001 Q2J54A partition 2 16.0 MiB
pci 0000:00:00.0: BAR 6: assigned [mem 0x01100000-0x0110ffff pref]
mmcblk2rpmb: mmc2:0001 Q2J54A partition 3 512 KiB, chardev (248:0)
caam 2100000.crypto: Instantiated RNG4 SH1
caam 2100000.crypto: device ID = 0x0a16010000000000 (Era 4)
caam 2100000.crypto: job rings = 2, qi = 0
pci 0000:00:00.0: PCI bridge to [bus 01-ff]
scsi 0:0:0:0: Direct-Access     ATA      INTEL SSDSC2KG96 0100 PQ: 0 ANSI: 5
 mmcblk2: p1 p2
ata1.00: Enabling discard_zeroes_data
caam algorithms registered in /proc/crypto
sd 0:0:0:0: [sda] 1875385008 512-byte logical blocks: (960 GB/894 GiB)
caam 2100000.crypto: registering rng-caam
sd 0:0:0:0: [sda] 4096-byte physical blocks
sd 0:0:0:0: [sda] Write Protect is off
NET: Registered protocol family 10
sd 0:0:0:0: [sda] Mode Sense: 00 3a 00 00
sd 0:0:0:0: [sda] Write cache: enabled, read cache: enabled, doesn't support DPO or FUA
Segment Routing with IPv6
RPL Segment Routing with IPv6
ata1.00: Enabling discard_zeroes_data
NET: Registered protocol family 17
 sda: sda1
ata1.00: Enabling discard_zeroes_data
Key type dns_resolver registered
sd 0:0:0:0: [sda] Attached SCSI disk
Registering SWP/SWPB emulation handler
Loading compiled-in X.509 certificates
imx_thermal 20c8000.anatop:tempmon: Extended Commercial CPU temperature grade - max:105C critical:100C passive:95C
mmc1: new high speed SDHC card at address 0001
mmcblk1: mmc1:0001 0008G 7.54 GiB 
 mmcblk1: p1
random: crng init done
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
systemd[1]: System time before build time, advancing clock.
systemd[1]: systemd 252.12-1~deb12u1 running in system mode (+PAM +AUDIT +SELINUX +APPARMOR +IMA +SMACK +SECCOMP +GCRYPT -GNUTLS +OPENSSL +ACL +BLKID +CURL +ELFUTILS +FIDO2 +IDN2 -IDN +IPTC +KMOD +LIBCRYPTSETUP +LIBFDISK +PCRE2 -PWQUALITY +P11KIT +QRENCODE +TPM2 +BZIP2 +LZ4 +XZ +ZLIB +ZSTD -BPF_FRAMEWORK -XKBCOMMON +UTMP +SYSVINIT default-hierarchy=unified)
systemd[1]: Detected architecture arm.
systemd[1]: Hostname set to <gusto-data>.
systemd[1]: /etc/systemd/system/fixup-nfsboot.service:7: Unknown key name 'After' in section 'Service', ignoring.
systemd[1]: /etc/systemd/system/fixup-nfsboot.service:8: Unknown key name 'Wants' in section 'Service', ignoring.
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
RPC: Registered named UNIX socket transport module.
RPC: Registered udp transport module.
systemd[1]: Starting modprobe@drm.service - Load Kernel Module drm...
RPC: Registered tcp transport module.
RPC: Registered tcp NFSv4.1 backchannel transport module.
systemd[1]: Starting modprobe@efi_pstore.service - Load Kernel Module efi_pstore...
device-mapper: ioctl: 4.43.0-ioctl (2020-10-01) initialised: dm-devel@redhat.com
systemd[1]: Starting modprobe@fuse.service - Load Kernel Module fuse...
systemd[1]: Starting modprobe@loop.service - Load Kernel Module loop...
systemd[1]: Starting networking.service - Network initialization...
Installing knfsd (copyright (C) 1996 okir@monad.swb.de).
systemd[1]: Starting systemd-fsck-root.service - File System Check on Root Device...
systemd[1]: Starting systemd-journald.service - Journal Service...
systemd[1]: Starting systemd-modules-load.service - Load Kernel Modules...
systemd[1]: Starting systemd-udev-trigger.service - Coldplug All udev Devices...
systemd[1]: Mounted dev-mqueue.mount - POSIX Message Queue File System.
systemd[1]: Mounted proc-fs-nfsd.mount - NFSD configuration filesystem.
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
systemd[1]: modprobe@fuse.service: Deactivated successfully.
systemd[1]: Finished modprobe@fuse.service - Load Kernel Module fuse.
systemd[1]: modprobe@loop.service: Deactivated successfully.
systemd[1]: Finished modprobe@loop.service - Load Kernel Module loop.
systemd[1]: Finished systemd-modules-load.service - Load Kernel Modules.
systemd[1]: sys-fs-fuse-connections.mount - FUSE Control File System was skipped because of an unmet condition check (ConditionPathExists=/sys/fs/fuse/connections).
systemd[1]: Mounting sys-kernel-config.mount - Kernel Configuration File System...
systemd[1]: Started systemd-fsckd.service - File System Check Daemon to report status.
systemd[1]: systemd-repart.service - Repartition Root Disk was skipped because no trigger condition checks were met.
systemd[1]: Starting systemd-sysctl.service - Apply Kernel Variables...
systemd[1]: Started systemd-journald.service - Journal Service.
EXT4-fs (mmcblk1p1): re-mounted. Opts: (null)
systemd-journald[219]: Received client request to flush runtime journal.
systemd-journald[219]: File /var/log/journal/a8281aabb76084893e65167c64d14c75/system.journal corrupted or uncleanly shut down, renaming and replacing.
fec 2188000.ethernet end0: renamed from eth0
CAN device driver interface
etnaviv etnaviv: bound 130000.gpu (ops gpu_ops [etnaviv])
etnaviv etnaviv: bound 134000.gpu (ops gpu_ops [etnaviv])
etnaviv etnaviv: bound 2204000.gpu (ops gpu_ops [etnaviv])
imx-ipuv3 2400000.ipu: IPUv3H probed
etnaviv-gpu 130000.gpu: model: GC2000, revision: 5108
imx-ipuv3 2800000.ipu: IPUv3H probed
etnaviv-gpu 134000.gpu: model: GC320, revision: 5007
etnaviv-gpu 2204000.gpu: model: GC355, revision: 1215
etnaviv-gpu 2204000.gpu: Ignoring GPU with VG and FE2.0
[drm] Initialized etnaviv 1.3.0 20151214 for etnaviv on minor 0
imx-drm display-subsystem: bound imx-ipuv3-crtc.2 (ops ipu_crtc_ops [imxdrm])
imx-drm display-subsystem: bound imx-ipuv3-crtc.3 (ops ipu_crtc_ops [imxdrm])
imx-drm display-subsystem: bound imx-ipuv3-crtc.6 (ops ipu_crtc_ops [imxdrm])
imx-drm display-subsystem: bound imx-ipuv3-crtc.7 (ops ipu_crtc_ops [imxdrm])
[drm] Initialized imx-drm 1.0.0 20120507 for display-subsystem on minor 1
ci_hdrc ci_hdrc.1: EHCI Host Controller
ci_hdrc ci_hdrc.1: new USB bus registered, assigned bus number 1
usb_phy_generic usbphynop1: supply vcc not found, using dummy regulator
ci_hdrc ci_hdrc.1: USB 2.0 started, EHCI 1.00
usb usb1: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 5.10
usb_phy_generic usbphynop1: dummy supplies not allowed for exclusive requests
usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
usb_phy_generic usbphynop2: supply vcc not found, using dummy regulator
usb_phy_generic usbphynop2: dummy supplies not allowed for exclusive requests
usb usb1: Product: EHCI Host Controller
usb usb1: Manufacturer: Linux 5.10.201-gea8959c1966f-dirty ehci_hcd
usb usb1: SerialNumber: ci_hdrc.1
hub 1-0:1.0: USB hub found
hub 1-0:1.0: 1 port detected
usb 1-1: new high-speed USB device number 2 using ci_hdrc
usb 1-1: New USB device found, idVendor=0424, idProduct=2514, bcdDevice= b.b3
usb 1-1: New USB device strings: Mfr=0, Product=0, SerialNumber=0
hub 1-1:1.0: USB hub found
hub 1-1:1.0: 4 ports detected
EXT4-fs (sda1): mounted filesystem with ordered data mode. Opts: (null)
usb 1-1.1: new full-speed USB device number 3 using ci_hdrc
usb 1-1.1: New USB device found, idVendor=0403, idProduct=6001, bcdDevice= 6.00
usb 1-1.1: New USB device strings: Mfr=1, Product=2, SerialNumber=3
usb 1-1.1: Product: USB-RS422 Cable
usb 1-1.1: Manufacturer: FTDI
usb 1-1.1: SerialNumber: FTVWJYS0
usb 1-1.2: new full-speed USB device number 4 using ci_hdrc
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
usb 1-1.4: New USB device found, idVendor=16c0, idProduct=0483, bcdDevice= 2.77
usb 1-1.4: New USB device strings: Mfr=1, Product=2, SerialNumber=3
usb 1-1.4: Product: USB Serial
usb 1-1.4: Manufacturer: Teensyduino
usb 1-1.4: SerialNumber: B3LO_CTRL
systemd-journald[219]: Oldest entry in /var/log/journal/a8281aabb76084893e65167c64d14c75/system.journal is older than the configured file retention duration (1month), suggesting rotation.
systemd-journald[219]: /var/log/journal/a8281aabb76084893e65167c64d14c75/system.journal: Journal header limits reached or header out-of-date, rotating.
usbcore: registered new interface driver usbserial_generic
usbserial: USB Serial support registered for generic
cdc_acm 1-1.2:1.0: ttyACM0: USB ACM device
usbcore: registered new interface driver ftdi_sio
cdc_acm 1-1.3:1.0: ttyACM1: USB ACM device
usbserial: USB Serial support registered for FTDI USB Serial Device
ftdi_sio 1-1.1:1.0: FTDI USB Serial Device converter detected
usb 1-1.1: Detected FT232RL
cdc_acm 1-1.4:1.0: ttyACM2: USB ACM device
usbcore: registered new interface driver cdc_acm
usb 1-1.1: FTDI USB Serial Device converter now attached to ttyUSB0
cdc_acm: USB Abstract Control Model driver for USB modems and ISDN adapters
systemd-journald[219]: Failed to read journal file /var/log/journal/a8281aabb76084893e65167c64d14c75/user-1001.journal for rotation, trying to move it out of the way: Text file busy
Micrel KSZ9031 Gigabit PHY 2188000.ethernet-1:07: attached PHY driver [Micrel KSZ9031 Gigabit PHY] (mii_bus:phy_addr=2188000.ethernet-1:07, irq=POLL)
NFSD: Using nfsdcld client tracking operations.
NFSD: no clients to reclaim, skipping NFSv4 grace period (net f0000069)
fec 2188000.ethernet end0: Link is Up - 100Mbps/Half - flow control off
IPv6: ADDRCONF(NETDEV_CHANGE): end0: link becomes ready
