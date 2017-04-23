import sys
import jenkins
from .parser import parser

# Tries to fetch configuration from the environment
try:
    from . import DEFAULT_CONFIG
    url, username, password = DEFAULT_CONFIG
except:
    print("Cannot collect configuration from the environment")
    exit(1)


def main():

    server = jenkins.Jenkins(url, username=username, password=password, timeout=240)

    args = parser.parse_args()

    if len(sys.argv) <= 1:
        parser.print_help()
        parser.exit()

    args.func(args, server)
