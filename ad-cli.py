#!/usr/bin/env python3
import ldap3
import getpass
import argparse
import sys

parser = argparse.ArgumentParser(description="Program to interact with Active Directory")

parser.add_argument('--domain', help='Active Directory Domain to work with', metavar='AD.DOMAIN.COM')
parser.add_argument('--lookup', help='lookup username(s)', nargs='+', metavar='USERNAME')

args = parser.parse_args()

def init():
    username = input('Username: ') 
    password = getpass.getpass('Password: ')

    global domain
    if args.domain:
        domain = args.domain
    else:
        domain = input('AD Domain: ')

    server = ldap3.Server(domain, get_info=ldap3.ALL)
    username = domain + '\\' + username

    conn = ldap3.Connection(server, user="%s" % username, password='%s' % password, authentication=ldap3.NTLM, auto_bind=True) 


def main():
    init()


main()
