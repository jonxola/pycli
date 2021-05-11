import argparse

def init():
    '''Get CLI arguments.'''
    parser = argparse.ArgumentParser(prog='pycli', description='A Python CLI template')
    parser.add_argument('cmd', help='A demo argument')
    parser.add_argument('-f', '--flag', help='A demo optional argument')
    return parser.parse_args()