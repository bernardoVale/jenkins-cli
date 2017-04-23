import argparse
from .run import run
from .ping import ping
from .list import list_jobs
from .info import info

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

ping_parser = subparsers.add_parser('ping')
ping_parser.set_defaults(func=ping)


run_parser = subparsers.add_parser('run')
run_parser.add_argument('job')
run_parser.add_argument('arguments', metavar='args',
                        help='Arguments to build parametrized job: arg1=value arg2=value',
                        default=None, nargs='*')
run_parser.set_defaults(func=run)


list_parser = subparsers.add_parser('ls')
list_parser.add_argument('pattern', metavar='pattern', help='Search for jobs that contains the given string'
                                                            ' will ignore case by default')
list_parser.add_argument('--view', metavar='view_name',
                         help='Search for jobs that belongs to the given view', default=None)
list_parser.set_defaults(func=list_jobs)


info_parser = subparsers.add_parser('info')
info_parser.add_argument('job', metavar='job_name', default=None,
                       help='Job name which you want to get information')
info_parser.set_defaults(func=info)
