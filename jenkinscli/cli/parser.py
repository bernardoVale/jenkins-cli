import argparse
from .run import run
from .ping import ping
from .list import list_jobs

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()


def ping_parser():
    ping_parser = subparsers.add_parser('ping')
    ping_parser.set_defaults(func=ping)


def run_parser():
    run_parser = subparsers.add_parser('run')
    run_parser.add_argument('job')
    run_parser.set_defaults(func=run)


def list_parser():
    parser = subparsers.add_parser('ls')
    parser.add_argument('pattern')
    parser.set_defaults(func=list_jobs)

run_parser()
ping_parser()
list_parser()
