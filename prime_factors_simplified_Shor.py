def prime_factors(n):
    """Return a list of prime factors of the given integer n."""
    i = 2
    factors = []
    
    # Check for number of 2s that divide n
    while n % i == 0:
        factors.append(i)
        n //= i
    
    # Check for odd factors from 3 onwards
    i = 3
    while i * i <= n:
        while (n % i) == 0:
            factors.append(i)
            n //= i
        i += 2
    
    # If n becomes a prime number greater than 2
    if n > 2:
        factors.append(n)
    
    return factors

try:
    # Get user input
    number = int(input("Enter a number to find its prime factors: "))

    # Find prime factors
    factors = prime_factors(number)

    # Display the result
    print(f"Prime factors of {number} are: {factors}")

except ValueError:
    print("Invalid input! Please enter a valid integer.")
