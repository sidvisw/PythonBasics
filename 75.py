import argparse
import sys

# def calc(args):
#     if args.o=='add':
#         return args.x+args.y
#     elif args.o=='mul':
#         return args.x*args.y
#     elif args.o=='sub':
#         return args.x-args.y
#     elif args.o=='div':
#         return args.x/args.y
#     else:
#         return "Something went wrong"

#faulty calculator
def calc(args):
    if args.o=='add':
        if args.x==56 and args.y==9 or args.x==9 and args.y==56:
            return 77.0
        else:
            return args.x+args.y
    elif args.o=='mul':
        if args.x==45 and args.y==3 or args.x==3 and args.y==45:
            return 555.0
        else:
            return args.x*args.y
    elif args.o=='sub':
        return args.x-args.y
    elif args.o=='div':
        if args.x==56 and args.y==6:
            return 4.0
        else:
            return args.x/args.y
    else:
        return "Something went wrong"

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--x',type=float,default=1.0,help="Enter first number. This is a utility for calculation. Please contact Sidharth.")
    parser.add_argument('--y',type=float,default=3.0,help="Enter second number. This is a utility for calculation. Please contact Sidharth.")
    parser.add_argument('--o',type=str,default="add",help="Enter second number. This is a utility for calculation. Please contact Sidharth.")
    args=parser.parse_args()
    sys.stdout.write(str(calc(args)))
