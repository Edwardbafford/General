import argparse as ap

# python cli/argparse_example.py 6 abc

if __name__ == '__main__':
    parser = ap.ArgumentParser()
    parser.add_argument('number')
    parser.add_argument('string')
    args = parser.parse_args()
    print(args.number)
    print(args.string)
