from collections import deque

def solve():
    N, M = map(int, input().split())
    
    # 그래프 초기화
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    # 모든 정점에서의 최단 거리 계산
    distances = [[0] * (N+1) for _ in range(N+1)]



    for start in range(1, N+1):

        visited = [False] * (N+1)

        q = deque([(start, 0)])
        visited[start] = True

        while q:
            current, dist = q.popleft()
            
            distances[start][current] = dist
            for neighbor in graph[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append((neighbor, dist + 1))

    result = list(map(sum, distances[1:]))

    min_distance = min(result)

    for idx in range(len(result)):
        if result[idx] == min_distance:
            print(idx+1)
            break
if __name__ == "__main__":
    solve()

