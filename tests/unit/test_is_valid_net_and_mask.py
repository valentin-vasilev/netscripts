#!/usr/bin/env python

import pytest

from app.handlers import is_valid_net_and_mask


@pytest.mark.parametrize(
    "net_mask, expected",
    [
        ("192.168.1.0 255.255.255.0", True),
        ("192.168.1.0255.255.255.0", pytest.raises(ValueError)),
        ("299.1.1.0 255.0.0.0", pytest.raises(ValueError)),
    ],
)
def test_is_valid_net_and_mask(net_mask, expected) -> None:
    """Test is_valid_net_and_mask() function"""
    if isinstance(expected, type(pytest.raises(ValueError))):
        with expected:
            is_valid_net_and_mask(net_mask)
    else:
        assert is_valid_net_and_mask(net_mask) is expected
