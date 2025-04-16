
from collections import deque

def solve():
    N, M = map(int, input().split())
    campus = []
    start_x, start_y = 0, 0
    
    # 캠퍼스 정보 입력 및 도연이 위치 찾기
    for i in range(N):
        row = list(input().strip())
        campus.append(row)
        if 'I' in row:
            start_x, start_y = i, row.index('I')
    
    # 방문 여부를 체크하는 배열
    visited = [[False] * M for _ in range(N)]
    visited[start_x][start_y] = True
    
    # BFS를 위한 큐 초기화
    queue = deque([(start_x, start_y)])
    people_count = 0
    
    # 상하좌우 이동 방향
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        x, y = queue.popleft()
        
        # 현재 위치가 사람(P)인 경우 카운트
        if campus[x][y] == 'P':
            people_count += 1
        
        # 상하좌우로 이동
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # 캠퍼스 범위를 벗어나지 않고, 벽이 아니며, 방문하지 않은 경우
            if 0 <= nx < N and 0 <= ny < M:
                if campus[nx][ny] != 'X' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    
    # 결과 출력
    print(people_count if people_count > 0 else "TT")

if __name__ == "__main__":
    solve()
