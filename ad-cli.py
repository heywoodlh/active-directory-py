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
    conn.extend.standard.who_am_i()

#    bases = domain.split('.')
#    bases_total = len(bases) 
#    global base_domain

#    for base in bases:
#        if bases.index(base) == '0':
#            print(0)
#            base_domain = 'dc=' + str(base) 
#        elif bases.index(base) == bases_total - 1:
#            print(3)
#            base_domain+='dc=' + str(base)
#        else:
#            print(2)
#            base_domain+=',dc=' + str(base) + ','

#   print(base_domain)

#def search():


def main():
    init()


main()
