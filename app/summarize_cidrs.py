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
import ipaddress
from typing import List

from handlers import sort_cidrs


def read_cidr_list() -> list:
    """Read CIDR list for stdin or file"""
    return [line.strip("  ,\n") for line in fileinput.input() if line.strip(" ,\n")]


def summarize_cidrs(input_cidrs: List) -> List[str]:
    """Summarize list of cidrs to the least common"""
    cidrs: List[ipaddress.IPv4Network] = [
        cidr if isinstance(cidr, ipaddress.IPv4Network) else ipaddress.IPv4Network(cidr)
        for cidr in input_cidrs
    ]
    # Sort the list of input CIDRs
    sorted_cidrs: List[ipaddress.IPv4Network] = sort_cidrs(cidrs)
    return [str(cidr) for cidr in ipaddress.collapse_addresses(sorted_cidrs)]


def main() -> None:
    """Main function"""
    for cidr in summarize_cidrs(read_cidr_list()):
        print(cidr)


if __name__ == "__main__":
    main()
