def main():
    import collections
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    Aset = set(A)
    
    Acnt = collections.defaultdict(int)
    for i in range(N):
        Acnt[A[i]] += 1
    
    G = collections.defaultdict(list)
    for k in Aset: # 連続している数を連結する
        if (k+1)%M in Aset:
            G[k].append((k+1)%M)
            G[(k+1)%M].append(k)
    
    visited = collections.defaultdict(int)
    for k in Aset:
        visited[k] = 1

    ans = 0 # 削れる最大
    for v_start in Aset:
        if visited[v_start]==1:
            nx = collections.deque()
            nx.append(v_start)
            visited[v_start] = 0
            tmp = v_start * Acnt[v_start]

            while nx:
                v_from = nx.popleft()

                for v_to in G[v_from]:
                    if visited[v_to]==1:
                        visited[v_to] = 0
                        tmp += v_to * Acnt[v_to]
                        nx.append(v_to)
            
            ans = max(ans, tmp)

    print(sum(A)-ans)




if __name__ == '__main__':

    main()