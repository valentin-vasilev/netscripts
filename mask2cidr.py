#!/usr/bin/env python

import sys
import fileinput
import math


def read_net_list() -> list:
    """Read network list for stdin or file"""
    return [line.strip("  ,\n") for line in fileinput.input() if line.strip(" ,\n")]


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


def mask_to_cidr(net: str) -> str:
    """Converts network address and subnet mask to CIDR notation"""
    net_address: str = net.split(" ")[0]
    subnet_mask: str = net.split(" ")[1]
    prefix_length: int = 0
    for octet in subnet_mask.split("."):
        prefix_length += 8 - math.floor(math.log(256 - int(octet), 2))
    return f"{net_address}/{prefix_length}"


def main() -> None:
    for net in read_net_list():
        if is_valid_net_and_mask(net):
            print(mask_to_cidr(net))
        else:
            sys.exit(
                f"{net} is not a valid network and subnet mask notation. Please fix input data."
            )


if __name__ == "__main__":
    main()
