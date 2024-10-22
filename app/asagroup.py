#!/usr/bin/env python

import sys
import re


def read_net_list() -> list:
    """Read network list for stdin"""
    return [line.strip() for line in sys.stdin]


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


def is_valid_group_name(group_name: str) -> bool:
    """Check if string is a valid Cisco ASA object-group name"""
    pattern = re.compile(r"^[a-zA-Z0-9_-]+$")

    if pattern.match(group_name):
        return True
    else:
        return False


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Missing object group name as argument!")

    if not is_valid_group_name(sys.argv[1]):
        sys.exit("Provided object group name is invalid!")

    object_group: str = f"""
object-group network {sys.argv[1]}
 description {sys.argv[1]}"""

    print(object_group)
    for net in read_net_list():
        if is_valid_net_and_mask(net):
            if net.split(" ")[1] == "255.255.255.255":
                print(f" network-object host {net.split(' ')[0]}")
            else:
                print(f" network-object {net}")
        else:
            sys.exit(
                f"{net} is not a valid network and subnet mask notation. Please, fix input data!"
            )


if __name__ == "__main__":
    main()
