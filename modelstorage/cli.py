from argparse import ArgumentParser

def main():
    parser = ArgumentParser()
    parser.add_argument("mynum", type=int, help="My number to test")
    args = parser.parse_args()

    print(args.mynum)