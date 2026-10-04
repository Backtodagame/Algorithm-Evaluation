from collections import deque
import sys
from bt1 import *
# (Sử dụng lại class Dinic từ Bài 1)

def extract_paths(dinic, s, t):
    paths = []
    
    def dfs_extract(u, min_flow, current_path):
        if u == t:
            return min_flow
        
        for idx in dinic.graph[u]:
            v, cap, flow = dinic.edges[idx][1], dinic.edges[idx][2], dinic.edges[idx][3]
            # Chỉ xét các cạnh thuận có lưu lượng dương
            if idx % 2 == 0 and flow > 0:
                current_path.append(v)
                pushed = dfs_extract(v, min(min_flow, flow), current_path)
                if pushed > 0:
                    dinic.edges[idx][3] -= pushed # Trừ đi lưu lượng đã trích xuất
                    return pushed
                current_path.pop()
        return 0

    while True:
        path = [s]
        pushed = dfs_extract(s, float('inf'), path)
        if pushed == 0:
            break
        paths.append((pushed, list(path)))
        
    return paths

def solve_routing():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    N, M, s, t = map(int, input_data[:4])
    dinic = Dinic(N + 1)
    
    idx = 4
    for _ in range(M):
        u, v, c = map(int, input_data[idx:idx+3])
        dinic.add_edge(u, v, c)
        idx += 3
        
    max_bandwidth = dinic.max_flow(s, t)
    print(max_bandwidth)
    
    paths = extract_paths(dinic, s, t)
    print(len(paths))
    for flow, path in paths:
        # Xuất định dạng: Luồng (F), Độ dài (L), và danh sách các nút trên đường đi[cite: 4]
        print(f"{flow} {len(path)} " + " ".join(map(str, path)))

if __name__ == '__main__':
    # Bỏ comment dòng dưới để chạy Bài 2
    # solve_routing()
    pass