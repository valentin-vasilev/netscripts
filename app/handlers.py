#!/usr/bin/env python
"""
This module provides functions for input validation of IPv4 network
related data such as CIDR, and network and subnet mask notations.
"""

import fileinput
import ipaddress
from typing import List


def read_cidr_list() -> list:
    """Read CIDR list for stdin or file"""
    return [line.strip("  ,\n") for line in fileinput.input() if line.strip(" ,\n")]


def is_valid_cidr(cidr: str) -> bool:
    """Check if string is valid CIDR notation"""
    parts: list = cidr.split("/")
    if len(parts) != 2:
        raise ValueError(f"{cidr} is not a valid CIDR notation")
    net_address = parts[0]
    prefix_length = parts[1]
    if not prefix_length.isdigit() or int(prefix_length) < 0 or int(prefix_length) > 32:
        raise ValueError(f"{cidr} is not a valid CIDR notation")
    octets = net_address.split(".")
    if len(octets) != 4:
        raise ValueError(f"{cidr} is not a valid CIDR notation")
    for octet in octets:
        if not octet.isdigit() or int(octet) < 0 or int(octet) > 255:
            raise ValueError(f"{cidr} is not a valid CIDR notation")
    return True


def is_valid_net_and_mask(net: str) -> bool:
    """Check if string is valid network + subnet mask notation"""
    parts: list = net.split(" ")
    if len(parts) != 2:
        raise ValueError(f"{net} is not a valid net mask notation")
    for part in parts:
        if len(part.split(".")) != 4:
            raise ValueError(f"{net} is not a valid net mask notation")
        for octet in part.split("."):
            if not octet.isdigit() or int(octet) < 0 or int(octet) > 255:
                raise ValueError(f"{net} is not a valid net mask notation")
    return True


def sort_cidrs(unsorted_cidrs: List) -> List[ipaddress.IPv4Network]:
    """Sort a list of IPv4 networks in CIDR notation"""

    try:
        cidr_list: List[ipaddress.IPv4Network] = [
            (
                cidr
                if isinstance(cidr, ipaddress.IPv4Network)
                else ipaddress.IPv4Network(cidr)
            )
            for cidr in unsorted_cidrs
        ]
    except ipaddress.AddressValueError as e:
        print(f"Invalid IPv4 CIDR notation {e}")
    sorted_cidrs: List[ipaddress.IPv4Network] = sorted(
        cidr_list, key=lambda n: (int(n.network_address), n.prefixlen)
    )
    return sorted_cidrs
