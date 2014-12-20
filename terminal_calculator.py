#to get stuff from the terminal
import argparse

#to do math stuffffz
import math

#get class from argparse module
parser = argparse.ArgumentParser()

#Setting a bunch of different arguments that can be accepted from the terminal

parser.add_argument("-f", "--foo", help="foo",
                    action="store_true")

parser.add_argument("-s", "--squareroot", help="finds the square root of the number",
                    type=int, nargs = '*')

parser.add_argument("-a", "--add", help="adds numbers together",
                    type=int, nargs = '*')

parser.add_argument("-m", "--multiply", help="multiplies numbers together",
                    type=int, nargs = '*')

#lets check for the args now
args = parser.parse_args()

if args.foo:
    print "foo"

if args.squareroot:
    print "Taking squareroot..."
    number = args.squareroot[0]
    new_number = math.sqrt(number)
    print new_number

if args.add:
    print "Adding numbers..."
    total = 0
    #print type(args.add)
    y = len(args.add)
    for x in range (0, y):
        total = total + args.add[x]
    print total

if args.multiply:
    print "Multiplying numbers..."
    total = 1
    y = len(args.multiply)
    for x in range (0, y):
        total = total * args.multiply[x]
    print total

#print dir(args)

#help(args)
