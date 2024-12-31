def closest_number(N, M):
    prev, next_ = N, N
    while True:
        if prev % M == 0:
            return prev
        if next_ % M == 0:
            return next_
        prev -= 1
        next_ += 1

# Example usage
close = closest_number(13, 4)
print(close)
