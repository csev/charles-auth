import argparse

from authentication import makepw, secret

parser = argparse.ArgumentParser(description='Charles Auth')

parser.add_argument('username')

args = parser.parse_args()


print(makepw(args.username, secret))
