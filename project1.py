# order_it.py

import sys
from bisect import bisect_left

def min_operations(shuffled, original):
    """
    Compute the minimum number of cut-and-insert operations
    required to transform shuffled into original.
    """
    # Map each instruction in original to its index
    pos = {instr: i for i, instr in enumerate(original)}

    # Convert shuffled list into indices according to original order
    mapped = [pos[instr] for instr in shuffled]

    # Find length of Longest Increasing Subsequence (LIS)
    lis = []
    for x in mapped:
        idx = bisect_left(lis, x)
        if idx == len(lis):
            lis.append(x)
        else:
            lis[idx] = x

    # Minimum operations = N - LIS length
    return len(shuffled) - len(lis)

def main():
    input_lines = sys.stdin.read().splitlines()
    N = int(input_lines[0].strip())

    shuffled_start = input_lines.index("shuffled") + 1
    original_start = input_lines.index("original") + 1

    shuffled = input_lines[shuffled_start:shuffled_start + N]
    original = input_lines[original_start:original_start + N]

    result = min_operations(shuffled, original)
    print(result)

if __name__ == "__main__":
    main()
