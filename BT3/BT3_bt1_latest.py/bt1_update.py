import time 

def read_file(input_file = 'D:/HK9/ChuyenDe2/Algorithm-Evaluation/BT3/BT3_bt1_latest.py/Tasks.inp'):
    try : 
        with open(input_file,'r') as f:
            data = f.read().split()

    except FileNotFoundError :
        print('File Not Found')
        return 
    
    if len(data) == 0:
        print('Content Not Found')
        return

    task_list = []
    for i in range(int(data[0])):
        # element at index 0 contains number of works: 
        # for example: i run from [0;4]

        priority_i = data[2*i+1]
        duration_i   = data[2*i+2]
        task_list.append((i+1, priority_i, duration_i))

    return task_list


def insert_sort(task_list):
    time_now = time.time()

    for i in range(1, len(task_list)):
        key = task_list[i]
        key_priority, key_duration = key[1], key[2]
        j = i - 1
        while j >= 0 :
            j_priority, j_duration = task_list[j][1], task_list[j][2]

            is_key_priority_greater =  key_priority > j_priority

            # The priority is the same but the duration is different
            is_key_duration_smaller = (key_priority == j_priority) and (key_duration < j_duration)

            if is_key_priority_greater or is_key_duration_smaller :
                task_list[j+1] = task_list[j]
            else :
                break 
            j -= 1
        task_list[j + 1] = key

    count = round(time.time() - time_now, 10)
    return task_list, count


def write_file(sorted_list, output='D:\\HK9\\ChuyenDe2\\Algorithm-Evaluation\\BT3\\BT3_bt1_latest.py\\Tasks.out'):
    try :
        with open(output,'w') as f :
            for i in sorted_list:
                f.write(f"{str(i[0])}\n")
    except FileNotFoundError:
        print('File Not Found')


if __name__ =='__main__':
    initial_task_list = read_file()
    sorted_task_list, duration = insert_sort(initial_task_list)
    write_file(sorted_task_list)


