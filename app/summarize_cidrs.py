#!/usr/bin/env python
"""
Script for summarizing IPv4 CIDRs to the least common
CIDR blocks

Example:
Input:
192.168.0.0/24
192.168.1.0/24
192.168.2.0/24
Output:
192.168.0.0/23
192.168.2.0/24
"""

import fileinput

from netaddr import cidr_merge


def read_cidr_list() -> list:
    """Read CIDR list for stdin or file"""
    return [line.strip("  ,\n") for line in fileinput.input() if line.strip(" ,\n")]


def merge_cidr_list(cidr_list: list) -> list:
    """Merge CIDR list and returns merged list"""
    return cidr_merge(cidr_list)


def main() -> None:
    """Main function"""
    for cidr in merge_cidr_list(read_cidr_list()):
        print(cidr)


if __name__ == "__main__":
    main()
