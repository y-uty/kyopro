def main():
    N = int(input())
    T = collections.defaultdict(list)
    E = [(-1, -1)]
    for _ in range(N-1):
        a, b = map(int, sys.stdin.readline().split())
        T[a].append(b)
        T[b].append(a)
        E.append((a, b))
    
    Q = int(input())
    Add = collections.defaultdict(int)
    for _ in range(Q):
        t, e, x = map(int, sys.stdin.readline().split())
        if t==1:
            Add[(E[e][0], E[e][1])] += x
        else:
            Add[(E[e][1], E[e][0])] += x

    later = 0
    C = [0]*(N+1)
    # BFS
    nx = collections.deque()
    nx.append((1, 0))
    visited = [False]*(N+1)
    visited[1] = True

    while nx:
        v_from, c_from = nx.popleft()
        C[v_from] = c_from

        for v_to in T[v_from]:
            if not visited[v_to]:
                visited[v_to] = True
                c_to = c_from

                if Add[(v_from, v_to)] > 0:
                    c_to -= Add[(v_from, v_to)]
                    later += Add[(v_from, v_to)]

                if Add[(v_to, v_from)] > 0:
                    c_to += Add[(v_to, v_from)]

                nx.append((v_to, c_to))                


    for i in range(1, N+1):
        C[i] += later

    print(*C[1:])


if __name__ == '__main__':
    import sys
    import collections
    import itertools
    import bisect
    import heapq
    import math
    import copy

    main()