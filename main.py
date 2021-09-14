#!/usr/bin/python3

"""
Code written by Gustav Larsson
Generating IP traffic with Scapy
"""

from logging_handler import logger
from scapy.all import *

def format_logs(level, message_type, message):
    """
    Helper function to format error messages
    """

    info = {"type": message_type,
                "message": message
    }

    logger.log(level, info)

def ping(ip_address="8.8.8.8"):

    packet = IP(dst=ip_address)/ICMP()

    try:
        exec = send(packet, loop=1, inter=0.2, count=50)
        format_logs(10, "ping", f"sent ping to {ip_address}")

    except OSError as error:
        format_logs(40, "test", error)

def send_multicast(ip_address="239.0.1.2"):

    packet = IP(dst=ip_address)/UDP()

    try:
        exec = send(packet, loop=1, inter=0.2, count=50)
        format_logs(10, "ping", f"sent ping to {ip_address}")

    except OSError as error:
        format_logs(40, "test", error)

if __name__ == "__main__":

    #ping()
    send_multicast()
