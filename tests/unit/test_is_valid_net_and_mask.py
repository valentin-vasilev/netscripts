#!/usr/bin/env python

import pytest

from app.handlers import is_valid_net_and_mask


@pytest.mark.parametrize(
    "net_mask, expected",
    [
        ("192.168.1.0 255.255.255.0", True),
        ("192.168.1.0255.255.255.0", False),
        ("299.1.1.0 255.0.0.0", False),
    ],
)
def test_is_valid_net_and_mask(net_mask, expected) -> None:
    """Test is_valid_net_and_mask() function"""
    assert is_valid_net_and_mask(net_mask) is expected
