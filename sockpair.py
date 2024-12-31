def sock_pairs(A):
    # Step 1: Count occurrences of each sock color
    sock_count = {}
    for sock in A:
        sock_count[sock] = sock_count.get(sock, 0) + 1

    # Step 2: Calculate the number of pairs
    pairs = 0
    for count in sock_count.values():
        pairs += count // 2

    return pairs


A1 = [1, 2, 3]
A2 = [2, 2, 2, 2]

print(sock_pairs(A1))  # Output: 0
print(sock_pairs(A2))  # Output: 2
