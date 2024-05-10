#!/usr/bin/env python

from netaddr import cidr_merge
import fileinput


def read_cidr_list() -> list:
    """Read CIDR list for stdin or file"""
    return [line.strip("  ,\n") for line in fileinput.input() if line.strip(" ,\n")]


def merge_cidr_list(cidr_list: list) -> list:
    """Merge CIDR list and returns merged list"""
    return cidr_merge(cidr_list)


def main() -> None:
    for cidr in merge_cidr_list(read_cidr_list()):
        print(cidr)


if __name__ == "__main__":
    main()
