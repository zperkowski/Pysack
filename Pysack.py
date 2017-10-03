import Knapsack
import Tests
import argparse
import copy

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dynamic", action='store_true', default=False,
                    dest='dynamic', help="dynamic algorithm")
parser.add_argument("-g", "--greedy", action='store_true', default=False,
                    dest='greedy', help="greedy algorithm")
parser.add_argument("-c", "--capacity", action='store', dest='capacity', default=0,
                    help='capacity of the knapsack', type=int, required=True)

subparsers = parser.add_subparsers(dest='mode', help="choose between auto generated and manual set array")

parser_auto = subparsers.add_parser("auto", help="generate an array automatically (help: auto -h)")
parser_auto.add_argument("-q", "--quantity", action='store', dest='quantity',
                         help='quantity of elements', type=int)
parser_auto.add_argument("-w", "--weight", action='store', dest='weight',
                         help='maximal weight of a single element', type=int)
parser_auto.add_argument("-v", "--value", action='store', dest='value',
                         help='maximal value of a single element', type=int)

parser_manual = subparsers.add_parser("manual", help="define your own array (help: manual -h)")
parser_manual.add_argument('-a', "--array", dest='array', nargs='+', default=[],
                           help='use your specified values: WEIGHT VALUE [WEIGHT VALUE ...]')
args = parser.parse_args()

if args.mode == 'auto':
    args.array = Knapsack.generator(args.quantity, args.weight, args.value)
    print("Generated array:\n", args.array)
if args.mode == 'manual':
    if len(args.array) % 2 != 0:
        print("Not even length of the array")
    else:
        args.array = [args.array[i:i + 2] for i in range(0, len(args.array), 2)]
        args.array = [list(map(int, x)) for x in args.array]
        print("Input array: ", args.array)
if args.greedy == True and args.dynamic == True:
    comp, greedy, greedy_time, dynamic, dynamic_time = Tests.compare_algorithms(copy.deepcopy(args.array),
                                                                                args.capacity)
    print("Tolerance (Greedy/Dynamic):\t", comp)
    print("Greedy algorithm:\n", greedy)
    print("Greedy algorithm time:\t\t", greedy_time)
    print("Dynamic algorithm:\n", dynamic)
    print("Dynamic algorithm time:\t\t", dynamic_time)

elif args.dynamic == True:
    print("Dynamic algorithm:\n", Knapsack.dynamic(copy.deepcopy(args.array), args.capacity))
elif args.greedy == True:
    print("Greedy algorithm:\n", Knapsack.greedy(copy.deepcopy(args.array), args.capacity))
