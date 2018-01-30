#!/usr/bin/env python3
import ldap3
import getpass
import argparse
import sys


## Argparse arguments

## Main parser and arguments:

main_parser = argparse.ArgumentParser()

main_parser.add_argument('--domain', help='Active Directory domain to work with', metavar='AD.DOMAIN.COM')
main_parser.add_argument('--aduser', help='Active Directory admin user', metavar='USERNAME')

subparsers = main_parser.add_subparsers(help='commands', dest='command')

## Query parser and arguments:
parser_query = subparsers.add_parser('query', help='query AD domain for information')
parser_query.add_argument('--username', help='lookup username(s)', nargs='+', metavar='USERNAME(s)')

## Edit parser and arguments:
parser_edit = subparsers.add_parser('edit', help='edit AD information')
parser_edit.add_argument('--username', help='edit user information', metavar='USERNAME')
parser_edit.add_argument('--password', help='reset user password', action='store_true')

args = main_parser.parse_args()

def init():

    global username
    if args.aduser:
        username = args.aduser
    else:
        username = input('Admin username: ')

    password = getpass.getpass(username + ' password: ')

    global domain
    if args.domain:
        domain = args.domain
    else:
        domain = input('AD Domain: ')

    server = ldap3.Server(domain)
    username = domain + '\\' + username

    global conn
    conn = ldap3.Connection(server, user="%s" % username, password='%s' % password, authentication=ldap3.NTLM, auto_bind=True)
    conn.start_tls()

    ## Code for getting proper dn for AD domain
    bases = domain.split('.')
    bases_total = len(bases)
    global base_domain
    base_domain = ''
    run = 0
    for base in bases:
        if run == 0:
            base_domain = 'dc=' + str(base)
        elif bases.index(base) == bases_total - 1:
            base_domain+='dc=' + str(base)
        else:
            base_domain+=',dc=' + str(base) + ','
        run = run + 1


def edit_user(x):
    if args.username and args.password:
        get_user_dn(x)
        new_pass = getpass.getpass(x + ' new password: ')
        print(final_dn)
        change_user_pass(final_dn, new_pass)

def get_user_dn(x):
    conn.search(base_domain, '(&(objectclass=person)(sAMAccountName=%s))'  % x, attributes=['sn'])
    results = conn.entries[0]
    results = str(results)
    trim1 = results[4:]
    trim2 = trim1.split('-')[0]
    #trim3 = trim2.rsplit
    #trim4 = trim3.replace("', '", " ")
    global final_dn
    final_dn = trim2
    #dn = str(trim3)
    #final_dn = trim4.strip('[]\'')

def change_user_pass(x, y):
    conn.extend.microsoft.modify_password(x, new_password='%s' % y)
    print(conn.result)


def main():
    init()
    if main_parser.parse_args(["edit"]):
        edit_user(args.username)

main()
