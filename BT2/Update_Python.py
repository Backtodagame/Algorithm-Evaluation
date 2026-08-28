import time

def insert_sort(list_n):
    time_now = time.time()
    
    for i in range(1, len(list_n)):
        key = list_n[i]
        j = i - 1
        while j >= 0 and key < list_n[j]:
            list_n[j + 1] = list_n[j]
            j -= 1
        list_n[j + 1] = key

    count = time.time() - time_now 
    return list_n, count


list_any = [9,4,3,8,10,5]
print(insert_sort(list_any))