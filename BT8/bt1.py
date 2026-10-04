from collections import deque
import sys

class Dinic:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.edges = []

    def add_edge(self, u, v, cap):
        self.graph[u].append(len(self.edges))
        self.edges.append([u, v, cap, 0])
        self.graph[v].append(len(self.edges))
        self.edges.append([v, u, 0, 0])

    def bfs(self, s, t):
        self.level = [-1] * self.n
        self.level[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for idx in self.graph[u]:
                v, cap, flow = self.edges[idx][1], self.edges[idx][2], self.edges[idx][3]
                if self.level[v] == -1 and cap > flow:
                    self.level[v] = self.level[u] + 1
                    q.append(v)
        return self.level[t] != -1

    def dfs(self, u, t, pushed):
        if pushed == 0 or u == t:
            return pushed
        for i in range(self.ptr[u], len(self.graph[u])):
            self.ptr[u] = i
            idx = self.graph[u][i]
            v, cap, flow = self.edges[idx][1], self.edges[idx][2], self.edges[idx][3]
            if self.level[u] + 1 != self.level[v] or cap == flow:
                continue
            tr = self.dfs(v, t, min(pushed, cap - flow))
            if tr == 0:
                continue
            self.edges[idx][3] += tr
            self.edges[idx ^ 1][3] -= tr
            return tr
        return 0

    def max_flow(self, s, t):
        flow = 0
        while self.bfs(s, t):
            self.ptr = [0] * self.n
            while True:
                pushed = self.dfs(s, t, float('inf'))
                if not pushed:
                    break
                flow += pushed
        return flow

def solve_vaccine():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N, M, W, C = map(int, input_data[:4])
    idx = 4
    
    source = 0
    sink = N + 1
    dinic = Dinic(N + 2)
    
    total_demand = 0
    
    # Đọc thông tin các kho[cite: 2]
    for _ in range(W):
        u, supply = int(input_data[idx]), int(input_data[idx+1])
        dinic.add_edge(source, u, supply)
        idx += 2
        
    # Đọc thông tin các trạm y tế[cite: 2]
    for _ in range(C):
        v, demand = int(input_data[idx]), int(input_data[idx+1])
        dinic.add_edge(v, sink, demand)
        total_demand += demand
        idx += 2
        
    # Đọc các tuyến đường[cite: 2]
    for _ in range(M):
        u, v, cap = int(input_data[idx]), int(input_data[idx+1]), int(input_data[idx+2])
        dinic.add_edge(u, v, cap)
        idx += 3
        
    T = dinic.max_flow(source, sink)
    print(T)
    if T >= total_demand:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    # Bỏ comment dòng dưới để chạy Bài 1
    solve_vaccine()
    pass