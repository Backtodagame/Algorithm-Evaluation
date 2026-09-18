import sys
from collections import deque

class MinCostMaxFlow:
    def __init__(self, num_nodes):
        self.n = num_nodes
        self.graph = [[] for _ in range(num_nodes)]
        self.edges = []

    def add_edge(self, u, v, cap, cost):
        # Cạnh xuôi: Sức chứa = cap, Chi phí = cost
        self.graph[u].append(len(self.edges))
        self.edges.append([u, v, cap, cost, 0])
        # Cạnh ngược: Sức chứa = 0, Chi phí = -cost (để thuật toán có thể "nhường đơn")
        self.graph[v].append(len(self.edges))
        self.edges.append([v, u, 0, -cost, 0])

    def spfa(self, s, t):
        dist = [float('inf')] * self.n
        parent_edge = [-1] * self.n
        in_queue = [False] * self.n
        
        dist[s] = 0
        queue = deque([s])
        in_queue[s] = True
        
        while queue:
            u = queue.popleft()
            in_queue[u] = False
            
            for idx in self.graph[u]:
                edge = self.edges[idx]
                v, cap, cost, flow = edge[1], edge[2], edge[3], edge[4]
                
                # Nếu cạnh còn sức chứa và tìm thấy đường đi rẻ hơn
                if cap - flow > 0 and dist[v] > dist[u] + cost:
                    dist[v] = dist[u] + cost
                    parent_edge[v] = idx
                    if not in_queue[v]:
                        queue.append(v)
                        in_queue[v] = True
                        
        return dist[t] != float('inf'), dist, parent_edge

    def solve_mcmf(self, s, t):
        max_flow = 0
        min_cost = 0
        matched_edges = []
        
        while True:
            # 1. Tìm đường tăng luồng có chi phí nhỏ nhất (SPFA)
            has_path, dist, parent_edge = self.spfa(s, t)
            if not has_path:
                break # Không còn đường nào đi từ S đến T -> Kết thúc
                
            # 2. Bơm 1 đơn vị luồng qua đường đi vừa tìm được
            push_flow = 1 
            curr = t
            while curr != s:
                idx = parent_edge[curr]
                self.edges[idx][4] += push_flow       # Cạnh xuôi tăng luồng
                self.edges[idx ^ 1][4] -= push_flow   # Cạnh ngược giảm luồng
                min_cost += push_flow * self.edges[idx][3]
                curr = self.edges[idx][0]
                
            max_flow += push_flow

        # Truy xuất kết quả các cặp đã ghép
        for i in range(0, len(self.edges), 2):
            u, v, cap, cost, flow = self.edges[i]
            if flow > 0 and u != s and v != t:
                matched_edges.append((u, v, cost))
                
        return max_flow, min_cost, matched_edges

def read_data(input_file=r"E:\HK9\ChuyenDe\source code\btso5.inp"):
    try:
        with open(input_file,'r') as f:
            
            data=f.read().split()
    except FileNotFoundError:
        print('404')
        return -1
    return data 

def main():
    # Đọc dữ liệu đầu vào
    input_data =read_data()
    if not input_data: return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Định nghĩa đỉnh Nguồn (S) = 0 và đỉnh Đích (T) = n + 1
    S = 0
    T = n + 1
    mcmf = MinCostMaxFlow(T + 1)
    
    shippers = set()
    orders = set()
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        w = float(input_data[idx+2])
        idx += 3
        
        shippers.add(u)
        orders.add(v)
        # Nối Shipper u với Đơn v, sức chứa 1, chi phí w
        mcmf.add_edge(u, v, 1, w) 
        
    # Nối Nguồn S tới tất cả Shippers
    for u in shippers:
        mcmf.add_edge(S, u, 1, 0)
    # Nối tất cả Đơn hàng tới Đích T
    for v in orders:
        mcmf.add_edge(v, T, 1, 0)
        
    # Thực thi thuật toán
    s, W, matches = mcmf.solve_mcmf(S, T)
    
    # In định dạng đầu ra[cite: 1]
    # Do w có thể là số thực (khoảng cách km), ta có thể định dạng in cho đẹp
    print(f"{s} {W if isinstance(W, int) else round(W, 2)}")
    for u, v, w in matches:
        print(f"{u} {v}")

if __name__ == '__main__':
    main()