def factorize(n, divisor=2):
    """
    Recursively factorizes the number `n` into prime factors.
    
    Parameters:
    n (int)       -> Number to be factorized
    divisor (int) -> Current divisor to check
    
    Returns:
    list          -> List of prime factors
    """
    # Base case: when n is 1, no more factors left
    if n == 1:
        return []

    # If divisor divides n, we found a factor
    if n % divisor == 0:
        return [divisor] + factorize(n // divisor, divisor)  
        # Append divisor and factorize the remaining quotient
    
    # If not divisible, check next possible divisor
    else:
        return factorize(n, divisor + 1)


# ------------------ Understanding Flow ------------------

# Example: factorize(60)
# Step 1: 60 % 2 == 0 → factor = 2 → recurse on 60/2 = 30
# Step 2: 30 % 2 == 0 → factor = 2 → recurse on 15
# Step 3: 15 % 2 != 0 → divisor = 3
# Step 4: 15 % 3 == 0 → factor = 3 → recurse on 5
# Step 5: 5 % 3 != 0 → divisor = 4 → divisor = 5
# Step 6: 5 % 5 == 0 → factor = 5 → recurse on 1 (stop)

# Final Output: [2, 2, 3, 5]

if __name__ == "__main__":
    num = 60
    factors = factorize(num)
    print(f"Prime factors of {num}: {factors}")
