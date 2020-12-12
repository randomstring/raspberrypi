#!/usr/bin/python
import time
import struct

ldusb = file("/dev/hidraw1")

time.sleep(0.5)

pkt = ldusb.read(8)
parsed_pkt = list(struct.unpack("<BBHHH", pkt))
num_samples = parsed_pkt.pop(0)
seqno = parsed_pkt.pop(0)
for sample in range(num_samples):
    cel = parsed_pkt[sample]/128.0
    fahr = (9.0/5.0 * cel) + 32.0
    print(fahr)

