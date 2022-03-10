"""
Return a number
python cli/docopt_example.py 5
Usage: docopt_example.py NUMBER
"""
import docopt

if __name__ == '__main__':
    args = docopt.docopt(__doc__)
    print(args['NUMBER'])
