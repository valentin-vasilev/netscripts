#!/usr/bin/env python

import sys
import fileinput


def read_cidr_list() -> list:
    """Read CIDR list for stdin or file"""
    return [line.strip("  ,\n") for line in fileinput.input() if line.strip(" ,\n")]


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


def cidr_to_mask(cidr: str) -> str:
    """Converts CIDR notation to network address and subnet mask"""
    net_address: str = cidr.split("/")[0]
    prefix_length: int = int(cidr.split("/")[1])
    mask: list[str] = []
    for i in range(4):
        n: int = prefix_length if prefix_length < 8 else 8
        mask.append(str(256 - pow(2, 8 - n)))
        prefix_length -= n
    return net_address + " " + ".".join(mask)


def main() -> None:
    for cidr in read_cidr_list():
        if is_valid_cidr(cidr):
            print(cidr_to_mask(cidr))
        else:
            sys.exit(f"{cidr} is not a valid CIDR notation. Please fix input data.")


if __name__ == "__main__":
    main()
