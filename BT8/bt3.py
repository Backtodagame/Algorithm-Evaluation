import heapq
import sys
from collections import deque
from bt1 import *

# (Sử dụng lại class Dinic từ Bài 1)

def dijkstra(start, n, adj):
    dist = {i: float('inf') for i in range(1, n + 1)}
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, t in adj[u]:
            if dist[u] + t < dist[v]:
                dist[v] = dist[u] + t
                heapq.heappush(pq, (dist[v], v))
    return dist

def solve_ambulance():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    N, M, A, P = map(int, input_data[:4])
    idx = 4
    
    ambulances = []
    for _ in range(A):
        ambulances.append(int(input_data[idx]))
        idx += 1
        
    incidents = []
    for _ in range(P):
        pos, max_time = int(input_data[idx]), int(input_data[idx+1])
        incidents.append((pos, max_time))
        idx += 2
        
    adj = {i: [] for i in range(1, N + 1)}
    for _ in range(M):
        u, v, t = int(input_data[idx]), int(input_data[idx+1]), int(input_data[idx+2])
        adj[u].append((v, t))
        adj[v].append((u, t))
        idx += 3
        
    # Mô hình hóa luồng cực đại:
    # Đỉnh: 0 (Source), 1 đến A (Xe cứu thương), A+1 đến A+P (Hiện trường), A+P+1 (Sink)
    source = 0
    sink = A + P + 1
    dinic = Dinic(sink + 1)
    
    for i in range(1, A + 1):
        dinic.add_edge(source, i, 1) # Mỗi xe chỉ nhận 1 ca[cite: 6]
        
    for j in range(1, P + 1):
        dinic.add_edge(A + j, sink, 1) # Mỗi ca chỉ cần 1 xe[cite: 6]
        
    for i in range(A):
        dist = dijkstra(ambulances[i], N, adj)
        for j in range(P):
            incident_pos, max_allowed_time = incidents[j]
            # Ràng buộc thời gian di chuyển[cite: 6]
            if dist[incident_pos] <= max_allowed_time:
                dinic.add_edge(i + 1, A + j + 1, 1)
                
    max_cases = dinic.max_flow(source, sink)
    print(max_cases)
    
    # Truy vết kết quả
    for u in range(1, A + 1):
        for edge_idx in dinic.graph[u]:
            v, cap, flow = dinic.edges[edge_idx][1], dinic.edges[edge_idx][2], dinic.edges[edge_idx][3]
            if v > A and v <= A + P and flow > 0:
                print(f"{u} {v - A}")

if __name__ == '__main__':
    # Bỏ comment dòng dưới để chạy Bài 3
    # solve_ambulance()
    pass