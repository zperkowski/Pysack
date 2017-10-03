# Pysack
Program compares greedy and dynamic algorithm of Knapsack Problem.

## Features
- Auto generating input
- Manual entering input
- Comparing calculation times and quality of results



## Getting Started
### Prerequisites

[Python3](https://www.python.org/download/releases/3.0/)

### How to use

```             
$ python3 Pysack.py -h
usage: Pysack.py [-h] [-d] [-g] -c CAPACITY {auto,manual} ...

positional arguments:
  {auto,manual}         choose between auto generated and manual set array
    auto                generate an array automatically (help: auto -h)
    manual              define your own array (help: manual -h)

optional arguments:
  -h, --help            show this help message and exit
  -d, --dynamic         dynamic algorithm
  -g, --greedy          greedy algorithm
  -c CAPACITY, --capacity CAPACITY
                        capacity of the knapsack

$ python3 Pysack.py auto -h
usage: Pysack.py auto [-h] [-q QUANTITY] [-w WEIGHT] [-v VALUE]

optional arguments:
  -h, --help            show this help message and exit
  -q QUANTITY, --quantity QUANTITY
                        quantity of elements
  -w WEIGHT, --weight WEIGHT
                        maximal weight of a single element
  -v VALUE, --value VALUE
                        maximal value of a single element

$ python3 Pysack.py manual -h
usage: Pysack.py manual [-h] [-a ARRAY [ARRAY ...]]

optional arguments:
  -h, --help            show this help message and exit
  -a ARRAY [ARRAY ...], --array ARRAY [ARRAY ...]
                        use your specified values: WEIGHT VALUE [WEIGHT VALUE
                        ...]
```

### Example
#### Auto generated - Greedy
```
$ python3 Pysack.py -g -c 8 auto -w 3 -v 5 -q 10
Generated array:
 [[3, 1], [2, 3], [2, 5], [2, 1], [2, 1], [2, 4], [3, 5], [2, 5], [3, 2], [2, 2]]
Greedy algorithm:
 [[2, 5], [2, 5], [2, 4], [2, 3]]
```
#### Auto generated - Dynamic
``` 
$ python3 Pysack.py -d -c 4 auto -w 2 -v 10 -q 7
Generated array:
 [[2, 7], [2, 1], [2, 9], [2, 2], [2, 4], [2, 6], [1, 1]]
Dynamic algorithm:
 [[2, 9], [2, 7]]
```
#### Manual entered - Greedy and Dynamic
```
$ python3 Pysack.py -d -g -c 5 manual -a 2 3 4 5 1 2 3 5 3 4
Input array:  [[2, 3], [4, 5], [1, 2], [3, 5], [3, 4]]
Tolerance (Greedy/Dynamic):	 0.875
Greedy algorithm:
 [[1, 2], [3, 5]]
Greedy algorithm time:		 0.0001 
Dynamic algorithm:
 [[3, 5], [2, 3]]
Dynamic algorithm time:		 0.0001 
```