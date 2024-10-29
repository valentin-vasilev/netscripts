#!/usr/bin/env python
"""
This is test module including unit test for validating
sorting of CIDRs
"""

import ipaddress

import pytest

from app.handlers import sort_cidrs


@pytest.mark.parametrize(
    "unsorted_cidrs, expected",
    [
        (
            [
                ipaddress.IPv4Network("192.168.1.0/24"),
                ipaddress.IPv4Network("192.168.2.0/24"),
                ipaddress.IPv4Network("192.168.0.0/24"),
            ],
            [
                ipaddress.IPv4Network("192.168.0.0/24"),
                ipaddress.IPv4Network("192.168.1.0/24"),
                ipaddress.IPv4Network("192.168.2.0/24"),
            ],
        ),
        (
            [
                ipaddress.IPv4Network("192.168.1.0/24"),
                ipaddress.IPv4Network("192.168.1.0/25"),
                ipaddress.IPv4Network("192.168.0.0/24"),
            ],
            [
                ipaddress.IPv4Network("192.168.0.0/24"),
                ipaddress.IPv4Network("192.168.1.0/24"),
                ipaddress.IPv4Network("192.168.1.0/25"),
            ],
        ),
    ],
)
def test_sort_cidrs(unsorted_cidrs, expected) -> None:
    """Test sort_cidr() function"""
    assert sort_cidrs(unsorted_cidrs) == expected
