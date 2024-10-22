#!/usr/bin/env python


def is_valid_cidr(cidr: str) -> bool:
    """Check if string is valid CIDR notation"""
    parts: list = cidr.split("/")
    if len(parts) != 2:
        return False
    net_address = parts[0]
    prefix_length = parts[1]
    if not prefix_length.isdigit() or int(prefix_length) < 0 or int(prefix_length) > 32:
        return False
    octets = net_address.split(".")
    if len(octets) != 4:
        return False
    for octet in octets:
        if not octet.isdigit() or int(octet) < 0 or int(octet) > 255:
            return False
    return True


def is_valid_net_and_mask(net: str) -> bool:
    """Check if string is valid network + subnet mask notation"""
    parts: list = net.split(" ")
    if len(parts) != 2:
        return False
    for part in parts:
        if len(part.split(".")) != 4:
            return False
        for octet in part.split("."):
            if not octet.isdigit() or int(octet) < 0 or int(octet) > 255:
                return False
    return True
