# Introduction

![Python](https://img.shields.io/badge/-Python-9cf?logo=python&style=plastic&logoColor=000066&labelColor=white) ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/msr8/snapmail?style=plastic) ![Lines of code](https://img.shields.io/tokei/lines/github/msr8/snapmail?style=plastic) ![GitHub issues](https://img.shields.io/github/issues/msr8/snapmail?style=plastic) ![GitHub Repo stars](https://img.shields.io/github/stars/msr8/snapmail?style=plastic) 

<!-- <br> -->

Snapmail is a mail service which deletes the mails once the recipent has opened them. This project is based around privacy and security and thus, anybody anywhere in the world with an internet connection can make an account and start recieving and sending emails

<br>

# Requirements

You should have preinstalled python, pip, and git. You can install python and pip together in the latest version of [python](https://www.python.org/downloads/). As for git, you can download it from [here](https://git-scm.com/). If you are on Mac, you can simply run `git --version` in terminal. If you are on Linux, you can simply run `sudo apt install git` in the terminal

<br>

# Installation

To install the program, enter the following commands in your command prompt/terminal:

```
git clone https://github.com/msr8/snapmail
cd snapmail
pip install -r requirements.txt
python client.py
```

<br>

# TOR

**NOTE: This section is highly technical. If you aren't familliar with the onion routing protocol, I would recommend you skip this section**

<br>

If you want, you can route all the traffic through the TOR network and send requests to our .onion mirror to get even more privacy and security. However, this will slow down the program and it requires the tor command line utility to be running

<br>

## Using TOR


How the client works is it makes a proxy through port 9051 and sends requests through there. By default, TOR uses that port for a SOCKS proxy. It can be configured in the line `SOCKSPort 9050` in your torrc file. Make sure that it is configured to port 9051

Then, start tor and when running snapmail, do

```
$ python client.py -t
```

You can also use `--tor` instead of `-t`

If everything goes good, you should see `TOR: Enabled` along with the onion address below the logo. If you dont see it but the home logo is there, that means that you didnt give the tor argument in the CLI correctly. If you get the following error-

```
Failed to establish a new connection: [Errno 61] Connection refused
```

It means that TOR is not running and/or is not configured to run at port 9050



