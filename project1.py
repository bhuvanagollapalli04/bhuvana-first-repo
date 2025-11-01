#!/usr/bin/env python3

import sys

def min_operations(shuffled, original):
    N = len(shuffled)
    start = tuple(shuffled)
    target = tuple(original)
    if start == target:
        return 0

    visited = {start}
    queue = [(start, 0)]
    head = 0

    while head < len(queue):
        cur, cost = queue[head]
        head += 1
        cur_list = list(cur)
        for i in range(N):
            for j in range(i+1, N+1):
                segment = cur_list[i:j]
                rest = cur_list[:i] + cur_list[j:]
                for k in range(len(rest)+1):
                    new_list = rest[:k] + segment + rest[k:]
                    new_t = tuple(new_list)
                    if new_t == cur:
                        continue
                    if new_t == target:
                        return cost + 1
                    if new_t not in visited:
                        visited.add(new_t)
                        queue.append((new_t, cost+1))
    return -1

def read_nonempty_line():
    while True:
        line = sys.stdin.readline()
        if not line:
            return None
        line = line.rstrip('\n')
        if line.strip() != "":
            return line
    return None

def main():
    line = read_nonempty_line()
    if line is None:
        return
    try:
        N = int(line.strip())
    except:
        return

    while True:
        line = read_nonempty_line()
        if line is None:
            return
        if line.strip().lower() == "shuffled":
            break

    shuffled = []
    for _ in range(N):
        s = sys.stdin.readline()
        if not s:
            s = ""
        else:
            s = s.rstrip('\n')
        shuffled.append(s)

    while True:
        line = read_nonempty_line()
        if line is None:
            return
        if line.strip().lower() == "original":
            break

    original = []
    for _ in range(N):
        s = sys.stdin.readline()
        if not s:
            s = ""
        else:
            s = s.rstrip('\n')
        original.append(s)

    print(min_operations(shuffled, original))

if __name__ == "__main__":
    main()
