def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_gap(low: int, high: int) -> tuple[int, int]:
    """Find the largest gap between consecutive prime numbers in a range."""
    last_prime = None
    max_gap = 0
    max_gap_pair = (None, None)

    for num in range(low, high + 1):
        if is_prime(num):
            if last_prime is not None:
                if num - last_prime >= max_gap:
                    max_gap = num - last_prime
                    max_gap_pair = (last_prime, num)
            last_prime = num

    if max_gap_pair == (None, None):
        raise ValueError("No prime numbers found in the given range.")
    return max_gap_pair

if __name__ == '__main__': # Code under this block will not run if you import the file elsewhere.
    low = 10
    high = 50
    try:
        gap = prime_gap(low, high)
        print(f"The largest prime gap between {low} and {high} is between {gap[0]} and {gap[1]}.")
    except ValueError as e:
        print(e)