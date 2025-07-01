# Prime Number Checker Tool

A simple and efficient command-line tool to check if a number is prime or not. Can also add multiple integers and check if their sum is prime.

## Features

- Check if a single number is prime
- Add two or more numbers and check if their sum is prime
- Supports any number of integer inputs
- Clean, easy-to-use command-line interface

## Usage

### Single Number Mode
Check if a single number is prime:
```bash
python prime_checker.py <number>
```

Example:
```bash
python prime_checker.py 17
# Output: 17 is a prime number.
```

### Multiple Numbers Mode
Add multiple numbers and check if their sum is prime:
```bash
python prime_checker.py <number1> <number2> [number3] [...]
```

Examples:
```bash
python prime_checker.py 5 7
# Output: 5 + 7 = 12
#         12 is not a prime number.

python prime_checker.py 2 3 5
# Output: 2 + 3 + 5 = 10
#         10 is not a prime number.

python prime_checker.py 1 2 4 8
# Output: 1 + 2 + 4 + 8 = 15
#         15 is not a prime number.
```

## Algorithm

The tool uses an optimized prime checking algorithm:
- Returns `False` for numbers less than 2
- Returns `True` for 2 (the only even prime)
- Returns `False` for other even numbers
- Checks odd divisors up to √n for efficiency

## Requirements

- Python 3.6 or higher
- No external dependencies required

## Installation

1. Clone this repository or download the `prime_checker.py` file
2. Make sure Python 3 is installed on your system
3. Run the tool using the usage examples above

## Error Handling

The tool handles various error cases:
- Invalid input (non-integers)
- Negative numbers (for single number mode)
- Missing arguments

## Examples Output

```bash
$ python prime_checker.py 13
13 is a prime number.

$ python prime_checker.py 15
15 is not a prime number.

$ python prime_checker.py 3 4
3 + 4 = 7
7 is a prime number.

$ python prime_checker.py 10 20 30
10 + 20 + 30 = 60
60 is not a prime number.
```