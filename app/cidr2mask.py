#!/usr/bin/env python

import fileinput
import sys

from handlers import is_valid_cidr


def read_cidr_list() -> list:
    """Read CIDR list for stdin or file"""
    return [line.strip("  ,\n") for line in fileinput.input() if line.strip(" ,\n")]


def cidr_to_mask(cidr: str) -> str:
    """Converts CIDR notation to network address and subnet mask"""
    net_address: str = cidr.split("/")[0]
    prefix_length: int = int(cidr.split("/")[1])
    mask: list[str] = []
    for _ in range(4):
        n: int = prefix_length if prefix_length < 8 else 8
        mask.append(str(256 - pow(2, 8 - n)))
        prefix_length -= n
    return net_address + " " + ".".join(mask)


def main() -> None:
    """Main function"""
    for cidr in read_cidr_list():
        if is_valid_cidr(cidr):
            print(cidr_to_mask(cidr))
        else:
            sys.exit(f"{cidr} is not a valid CIDR notation. Please fix input data.")


if __name__ == "__main__":
    main()