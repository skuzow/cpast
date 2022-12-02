import sys
from argparse import ArgumentParser

from cpast.cpast import run


parser = ArgumentParser(prog='cpast', description='Cpast CLI')
parser.add_argument('-d', '--date',
                    help='Commit date, example: 2021-12-25',
                    required=True, type=str, default=None)
parser.add_argument('-t', '--time',
                    help='Commit time, example: 22:13:05',
                    required=True, type=str, default=None)
parser.add_argument('-m', '--message',
                    help='Commit message, example: "init :)"',
                    required=True, type=str, default=None)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        parser.print_help()
    else:
        args = parser.parse_args()
        run(args.date, args.time, args.message)
