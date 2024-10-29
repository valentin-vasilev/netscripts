<h1 align="center">PrefixOps</h1>

<p align="center">
  <img src="https://github.com/valentin-vasilev/netscripts/blob/main/images/prefixops.webp" alt="PrefixOps" width="500"/>
</p>

![Linting](https://github.com/valentin-vasilev/netscripts/actions/workflows/linting.yaml/badge.svg) ![Unit Test](https://github.com/valentin-vasilev/netscripts/actions/workflows/unit_tests.yaml/badge.svg)


A collection of scripts for manipulating network address data in CLI. Each command-line tool is designed to do one thing and do it well. This follows the Unix philosophy of "do one thing and do it well."

## Table of Contents

- [Synopsis](#synopsis)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Synopsis

|Script Name    |Synopsis    |
|---------------|------------|
|cidr2mask      |Read prefixes in CIDR notation from STDIN and return them in prefix and subnet mask notation to STDOUT.|
|mask2cidr      |Read prefixes in prefix and subnet mask notation from STDIN and returns them in CIDR notation to STDOUT.|
|summarize_cidrs|Read prefixes in CIDR notation from STDIN, summarize them to least common prefix length and returns the result in CIDR notation to STDOUT.|

## Installation

1. Clone the repository

```bash
git clone git@github.com:valentin-vasilev/netscripts.git $HOME/code
cd $HOME/code/netscripts
```

2. (Optional) Install dependencies 

Addtional packages are required for development purposes only. All scripts are designed to work with the standard Python libraries.

```bash
python -m pip install - r requirements.txt
```

3. Make scripts executable
```bash
chmod +x $HOME/code/netscripts*
```

4. (Optional) Create a symlink to a directory in your $PATH so you can run the script from anywhere.
```bash
sudo ln -s $HOME/code/netscripts/app/cidr2mask.py /usr/local/bin/cidr2mask
```

## Usage

All tools are designed to read from STDIN and write to STDOUT. This makes them suitable for creating pipelines and scripts.

**Example 1: Summarize CIDRs and format conversion**

We have a list of 3 prefixes (192.168.0.0/24, 192.168.1.0/24 and 192.168.2.0/24) in CIDR notation and we need to summarize them. Additionally, we need the result in prefix and subnet mask notation to use it in a firewall configuration.

```bash
echo "192.168.0.0/24\n192.168.2.0/24\n192.168.3.0/24" | summarize_cidrs | cidr2mask
```

This will result in the following output.

```bash
192.168.0.0 255.255.255.0
192.168.2.0 255.255.254.0
```

The original list of prefixes in CIDR notation are first summarized using `summarize_cidrs`. The output of `summarize_cidrs` is again in CIDR notation, so we use `cidr2mask` to convert them to prefix and subnet mask notation.

## Contributing

:+1: Pull requests are always welcome!
