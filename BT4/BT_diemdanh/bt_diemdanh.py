import numpy as np 

def read_file(input_path=r'E:\HK9\ChuyenDe\Algorithm-Evaluation\BT4\BT_diemdanh\Graph1.inp'):
    try :
        with open(input_path) as f:
            data =f.read().split()

    except FileNotFoundError :
        print('File Not Found')
        return 

    return data

def process_data(data):
    N,M,T = int(data[0]), int(data[1]), int(data[2])
    adj_matrix = np.zeros((N,N))
    data_list = []

    if T == 0 or T==2 : # No weight 
        for i in range(M): 
            data_list.append( ( int(data[2*(i+1)+1]) -1, int(data[2*(i+1)+2])-1))

        if T == 0 :
            for edge in data_list : 
                adj_matrix[edge[0]][edge[1]], adj_matrix[edge[1]][edge[0]] = 1,1

        else : 
            for edge in data_list:
                adj_matrix[edge[0]][edge[1]] = 1




    else : # weight
        for i in range(M): 
            data_list.append((int(data[3*(i+1)]) -1, int(data[3*(i+1)+1]) -1, int(data[3*(i+1)+2])))

        if T == 1 :
            for edge in data_list : 
                adj_matrix[edge[0]][edge[1]], adj_matrix[edge[1]][edge[0]] = edge[2], edge[2]

        else :
            for edge in data_list:
                adj_matrix[edge[0]][edge[1]] = edge[2]


    return adj_matrix, T

def write_file(adj_matrix, T, output_path=r'E:\HK9\ChuyenDe\Algorithm-Evaluation\BT4\BT_diemdanh\Graph'):
    output_path += str(T)+'.out'
    try:
        with open(output_path, 'w') as f :
            for i in range(len(adj_matrix[0])):
                for j in range(len(adj_matrix[0])):
                    f.write(f"{int(adj_matrix[i][j])} ")
                f.write(f"\n")
    except FileNotFoundError :
        print('File Not Found')


if __name__ == '__main__':
    data= read_file(r'E:\HK9\ChuyenDe\Algorithm-Evaluation\BT4\BT_diemdanh\Graph2.inp')
    adj_matrix,T = process_data(data)
    write_file(adj_matrix, T)
