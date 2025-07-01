#!/usr/bin/env python3
"""
Prime Number Checker Tool

A simple command-line tool to check if a number is prime or not.
Can also add multiple integers and check if their sum is prime.

Usage: 
  python prime_checker.py <number>
  python prime_checker.py <number1> <number2>
  python prime_checker.py <number1> <number2> <number3>
  
Examples:
  python prime_checker.py 17
  python prime_checker.py 5 7
  python prime_checker.py 2 3 5
"""

import sys
import math


def _def_is_primes(n):
    """
    Check if a number is prime.
    
    Args:
        n (int): The number to check
        
    Returns:
        bool: True if the number is prime, False otherwise
    """
    if n < 2:
        return False
    
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    
    return True


def check_sum_prime(*args):
    """
    Add multiple integers and check if their sum is prime.
    
    Args:
        *args: Variable number of integers to sum
        
    Returns:
        tuple: (sum, is_prime_result) where sum is the total and is_prime_result is boolean
    """
    sum_result = sum(args)
    return sum_result, _def_is_primes(sum_result)


def main():
    """Main function to handle command-line arguments and check prime numbers."""
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python prime_checker.py <number>")
        print("  python prime_checker.py <number1> <number2>")
        print("  python prime_checker.py <number1> <number2> <number3>")
        print("Examples:")
        print("  python prime_checker.py 17")
        print("  python prime_checker.py 5 7")
        print("  python prime_checker.py 2 3 5")
        sys.exit(1)
    
    try:
        if len(sys.argv) == 2:
            # Single number mode
            number = int(sys.argv[1])
            if number < 0:
                print("Error: Please provide a non-negative integer.")
                sys.exit(1)
            
            if _def_is_primes(number):
                print(f"{number} is a prime number.")
            else:
                print(f"{number} is not a prime number.")
        
        else:
            # Multiple numbers mode - add and check if sum is prime
            numbers = [int(arg) for arg in sys.argv[1:]]
            
            sum_result, is_sum_prime = check_sum_prime(*numbers)
            
            numbers_str = " + ".join(map(str, numbers))
            print(f"{numbers_str} = {sum_result}")
            if is_sum_prime:
                print(f"{sum_result} is a prime number.")
            else:
                print(f"{sum_result} is not a prime number.")
                
    except ValueError:
        print("Error: Please provide valid integers.")
        sys.exit(1)


if __name__ == "__main__":
    main()