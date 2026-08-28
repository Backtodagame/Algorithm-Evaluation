def task_scheduling(input_file='E:/HK9/ChuyenDe/Algorithm-Evaluation/BT3/task.inp', output_file='E:/HK9/ChuyenDe/Algorithm-Evaluation/BT3/Tasks.out'):
    # 1. Đọc toàn bộ dữ liệu an toàn
    try:
        with open(input_file, 'r') as f:
            # split() tự động bỏ qua khoảng trắng, dấu xuống dòng và gộp các chữ số của một số
            data = f.read().split() 
    except FileNotFoundError:
        print(f"Không tìm thấy file {input_file}")
        return

    if not data:
        return

    N = int(data[0])
    tasks = []

    # 2. Xây dựng danh sách nhiệm vụ
    # Mỗi nhiệm vụ lưu dưới dạng Tuple: (Độ ưu tiên P, Thời gian T, Vị trí ban đầu)
    for i in range(N):
        p = int(data[1 + i*2])
        t = int(data[2 + i*2])
        original_index = i + 1 # Đánh số từ 1 theo yêu cầu đầu ra
        tasks.append((p, t, original_index))

    # 3. Sắp xếp danh sách
    # Tham số key=lambda x: (-x[0], x[1]) giải quyết cùng lúc 2 điều kiện:
    # -x[0]: Độ ưu tiên P sắp xếp GIẢM DẦN (số càng lớn âm càng nhỏ -> lên đầu)
    # x[1] : Thời gian T sắp xếp TĂNG DẦN (nếu P bằng nhau, T nhỏ hơn sẽ lên đầu)
    tasks.sort(key=lambda x: (-x[0], x[1]))

    # 4. Ghi kết quả ra file
    with open(output_file, 'w') as f:
        for task in tasks:
            f.write(f"{task[2]}\n")

# Chạy thử chương trình
if __name__ == '__main__':
    task_scheduling()