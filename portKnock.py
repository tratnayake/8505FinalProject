from scapy.all import *
from subprocess import Popen, PIPE, call
from multiprocessing import Process
import argparse
import sys
import re
import time



#Send Port Knocks
# Inputs: Protocol, Destination Address, Destination Ports,
def sendPortKnocks(protocol,dstAddress,dports):
    if(protocol == "TCP"):
        for port in dports:
            packet = IP(dst="192.168.0.17",ttl=71)/ TCP(dport=7000, sport=80)
            send(packet)
            pass

#Listen for the response
def listenSuccess():
    print "Success"

sendPortKnocks("TCP","192.168.0.17",[8000,8001,8002]);
