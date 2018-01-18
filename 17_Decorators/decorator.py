import argparse
from functools import wraps



cli = argparse.ArgumentParser()
subparsers = cli.add_subparsers(dest="subcommand")

def argument(*args, **kwargs):
    return ([*args], kwargs)

def subcommand(args=[], parent=subparsers):
    def decorator(func):
        parser = parent.add_parser(func.__name__, description=func.__doc__)
        for arg in args:
            parser.add_argument(*arg[0], **arg[1])
        parser.set_defaults(func=func)
    return decorator


@subcommand()
def nothing(args):
    print("Nothing special")

@subcommand([argument("-c", "--caps", help="Makes uppercase")])
def caps(args):
    word = args.caps
    print(word.upper())

@subcommand([argument("lowerc", help="Makes lowercase")])
def lowerc(args):
    word = args.lowerc
    print(word.lower())

if __name__ ==  "__main__":
    args = cli.parse_args()
    if args.subcommand is None:
        cli.print_help()
    else:
        args.func(args)