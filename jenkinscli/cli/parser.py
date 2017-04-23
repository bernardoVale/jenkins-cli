import argparse
from .run import run
from .ping import ping
from .list import list_jobs

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

ping_parser = subparsers.add_parser('ping')
ping_parser.set_defaults(func=ping)


run_parser = subparsers.add_parser('run')
run_parser.add_argument('job')
run_parser.set_defaults(func=run)


list_parser = subparsers.add_parser('ls')
list_parser.add_argument('pattern', metavar='pattern', help='Search for jobs that contains the given string'
                                                            ' will ignore case by default')
list_parser.add_argument('--view', metavar='view_name',
                         help='Search for jobs that belongs to the given view', default=None)
list_parser.set_defaults(func=list_jobs)
