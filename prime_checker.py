#!/usr/bin/env python3
"""
Prime Number Checker Tool

A simple command-line tool to check if a number is prime or not.
Usage: python prime_checker.py <number>
"""

import sys
import math


def is_prime(n):
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


def main():
    """Main function to handle command-line arguments and check prime numbers."""
    if len(sys.argv) != 2:
        print("Usage: python prime_checker.py <number>")
        print("Example: python prime_checker.py 17")
        sys.exit(1)
    
    try:
        number = int(sys.argv[1])
    except ValueError:
        print("Error: Please provide a valid integer.")
        sys.exit(1)
    
    if number < 0:
        print("Error: Please provide a non-negative integer.")
        sys.exit(1)
    
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")


if __name__ == "__main__":
    main()