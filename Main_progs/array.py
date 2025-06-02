from collections import defaultdict

def longest_balanced_subarray(arr):
    n = len(arr)
    max_len = 0
    count = [0] * 10
    seen = {}

    # We use a tuple of differences from count[0] to count[1-9] as a signature
    key = tuple([0] * 9)
    seen[key] = -1  # empty prefix

    for i in range(n):
        count[arr[i]] += 1
        base = count[0]
        # Create signature: differences from base count
        diff = tuple(count[d] - base for d in range(1, 10))
        
        if diff in seen:
            max_len = max(max_len, i - seen[diff])
        else:
            seen[diff] = i

    return max_len
