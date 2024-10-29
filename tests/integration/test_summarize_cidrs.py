#!/usr/bin/env python
"""
Test summarization of IPv4 CIDRs
"""

import subprocess
import sys


def test_cidr_summarization():
    """Test summarize_cidr script"""
    # Define the input and expected output
    input_data = "192.168.0.0/24\n192.168.1.0/24\n192.168.2.0/24\n192.168.0.0/25\n"
    expected_output = "192.168.0.0/23\n192.168.2.0/24\n"

    # Run the script with subprocess and pass the input data
    process = subprocess.Popen(
        [sys.executable, "app/summarize_cidrs.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    # Feed the input data to the process
    stdout, stderr = process.communicate(input=input_data)

    # Assert no error messages and that the output matches the expected output
    assert stderr == "", f"Expected no stderr, but got: {stderr}"
    assert (
        stdout == expected_output
    ), f"Expected output: {expected_output}, but got: {stdout}"
