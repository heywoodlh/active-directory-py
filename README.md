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

`./ad_cli.py`

If no arguments are supplied, the program will interactively prompt for base information.

However, each needed piece of information can be supplied via arguments:

`./ad_cli.py --domain AD.NSANPETE.ORG --aduser domain.admin edit --username test.user --password`

Replacing 'domain.admin' with an AD domain admin's username and 'test.user' with the username that will have its password changed.

```
usage: ad_cli.py [-h] [--domain AD.DOMAIN.COM] [--aduser USERNAME] {edit} ...
positional arguments:
  {edit}                commands
    edit                edit AD information
optional arguments:
  -h, --help            show this help message and exit
  --domain AD.DOMAIN.COM
                        Active Directory domain to work with
  --aduser USERNAME     Active Directory admin user
```



## To Do:
1. Serve command on a web interface via Eel: https://github.com/ChrisKnott/Eel
