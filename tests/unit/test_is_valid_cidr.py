#!/usr/bin/env python

import pytest

from app.handlers import is_valid_cidr


@pytest.mark.parametrize(
    "cidr, expected",
    [
        ("192.168.1.0/24", True),
        ("10.10.10.192/26", True),
        ("1.1.1.1/24", True),
        ("266.233.765.0/56", False),
    ],
)
def test_is_valid_cidr(cidr, expected) -> None:
    """Test is_valid_cidr() function"""
    assert is_valid_cidr(cidr) is expected
