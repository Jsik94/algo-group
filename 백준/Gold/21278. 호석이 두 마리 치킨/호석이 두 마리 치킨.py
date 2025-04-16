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
    

    # N이 최대 100이므로 101 을 넘는 경우는 없음
    min_total = 101
    result = (0, 0)
    
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            total = 0
            for k in range(1, N+1):
                # k에서 가장 가까운 치킨집까지의 왕복 거리
                min_dist = min(distances[k][i], distances[k][j]) * 2
                total += min_dist
            
            if total < min_total:
                min_total = total
                result = (i, j)
            elif total == min_total:
                # 두 건물의 번호가 작은 순서대로 출력
                if i < result[0] or (i == result[0] and j < result[1]):
                    result = (i, j)
    
    print(result[0], result[1], min_total)

def solve2():
    N, M = map(int, input().split())
    
    # 플로이드-워셜을 위한 거리 배열 초기화
    INF = float('inf')
    dist = [[INF] * (N+1) for _ in range(N+1)]
    
    # 자기 자신으로의 거리는 0
    for i in range(1, N+1):
        dist[i][i] = 0
    
    # 간선 정보 입력
    for _ in range(M):
        a, b = map(int, input().split())
        dist[a][b] = 1
        dist[b][a] = 1
    
    # 플로이드-워셜 알고리즘
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    # 최적의 치킨집 위치 찾기
    min_total = float('inf')
    result = (0, 0)
    
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            total = 0
            for k in range(1, N+1):
                # k에서 가장 가까운 치킨집까지의 왕복 거리
                min_dist = min(dist[k][i], dist[k][j]) * 2
                total += min_dist
            
            if total < min_total:
                min_total = total
                result = (i, j)
            elif total == min_total:
                if i < result[0] or (i == result[0] and j < result[1]):
                    result = (i, j)
    
    print(result[0], result[1], min_total)

if __name__ == "__main__":
    solve2()

