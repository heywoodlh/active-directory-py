##active-directory-py

## Description:

The purpose of this project is to serve as an interface to easily allow end users to interact with active directory to do common tasks such as change passwords.


### Installation:

```
git clone https://github.com/heywoodlh/active-directory-py.git
cd active-directory-py.git
sudo pip3 install -r requirements.txt
```

### Usage: 

The command is interactive and can be run simply by executing the program:

`./ad-cli.py`

If no arguments are supplied, the program will interactively prompt for base information.

```
usage: ad-cli.py [-h] [--domain AD.DOMAIN.COM]
                 [--lookup USERNAME [USERNAME ...]]
Program to interact with Active Directory
optional arguments:
  -h, --help            show this help message and exit
  --domain AD.DOMAIN.COM
                        Active Directory Domain to work with
  --lookup USERNAME [USERNAME ...]
                        lookup username(s)
```
