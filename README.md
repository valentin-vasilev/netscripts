<h1 align="center">PrefixOps</h1>
![Tests](https://github.com/valentin-vasilev/netscripts/actions/workflows/pr_workflow.yaml/badge.svg)

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

2. Install dependencies
```bash
python -m pip install - r requirements.txt
```

3. Make scripts executable
```bash
chmod +x $HOME/code/netscripts*
```

4. (Optional) Create a symlink to a directory in your $PATH so you can run the script from anywhere.
```bash
sudo ln -s $HOME/code/netscripts/cidr2mask.py /usr/local/bin/cidr2mask
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

**Example 2: Generate Cisco ASA object group with the summarized list of public AWS IPv4 prefixes**

You are tasked to create a network object group on your Cisco ASA firewall called "aws-public-ipv4-cidrs", containing the list of AWS IPv4 prefixes. You have to keep the group's length as minimal as possible so summarization has to be done before creating the network object group with the AWS IPv4 public CIDRs. 

To start this, let's get the raw list of AWS prefixes from the API which AWS provide - [AWS Public IPv4 prefixes](https://ip-ranges.amazonaws.com/ip-ranges.json).

```bash
curl https://ip-ranges.amazonaws.com/ip-ranges.json | jq -r '.prefixes[].ip_prefix' > ~/aws-public-ipv4-ranges
```

You use `curl` to fetch the JSON formated list from AWS, then `jq` to process the JSON and filter just the IPv4 prefixes. Now that you have a file with network prefixes in CIDR format, it is time to put the prefixops tools to work and get the task completed. 

```bash
cat ~/aws-public-ipv4-ranges | summarize_cidrs | cidr2mask | asagroup aws-public-ipv4-cidrs > ~/asa-group-aws-public-ipv4-cidrs-local
```

Prefixops tools are designed to read from STDIN hence we `cat` the file you created on the previous step. Then pipe the output to `summarize_cidrs` to shrink the list as much as possible. Now you have the summarized prefix list, however the list is in CIDR notation. ASA requires prefix and subnet mask notation in the network object group. Fortunaltely, you have `cidr2mask` and piping the previous output to that will get the list in prefix subnet mask notation. Finally, you have to create the ASA network object group. For that you use `asagroup` which again reads input from STDIN and also you provide the object group name "aws-public-ipv4-cidrs" as argument. Result is redirected to a file "asa-group-aws-public-ipv4-cidrs-local" in the home dir. 

If you're a cat person like me, please avoid the `cat` abuse and do this in a one liner 😊:

```bash
curl https://ip-ranges.amazonaws.com/ip-ranges.json | jq -r '.prefixes[].ip_prefix' | summarize_cidrs | cidr2mask | asagroup aws-public-ipv4-cidrs > ~/asa-group-aws-public-ipv4-cidrs
```

As a bonus hint, you might need to compare your newly created network object group with what you already have on your ASA and see what's missing or obsolete. Assuming that you alredy have the "asa-group-aws-public-ipv4-cidrs-local" file and you downloaded the version from the ASA to "asa-group-aws-public-ipv4-cidrs-remote".

Use `diff` to compare both files. To have the correct comparison result, you need to feed `diff` with the sorted version of both files using `sort` tool. To get a list of what's "remote" is missing from "local" you can filter the results like that:

```bash
diff -u <(sort ~/asa-group-aws-public-ipv4-cidrs-local) <(sort ~/asa-group-aws-public-ipv4-cidrs-remote) | grep '^-' | sed 's/^-//'
```

Should you need a list of what's "local" missing from remote, you can alter it like that:

```bash
diff -u <(sort ~/asa-group-aws-public-ipv4-cidrs-local) <(sort ~/asa-group-aws-public-ipv4-cidrs-remote) | grep '^+' | sed 's/^+//'
```

## Contributing

:+1: Pull requests are always welcome!
