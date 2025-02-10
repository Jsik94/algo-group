
if __name__=="__main__":


    input_cnt = int(input())

    input_list = list(map(int,input().split(' ')) )


    # length = 0 
    # for idx in range(0,input_cnt-1):
    #     len+= abs(input_list[idx]-input_list[idx+1])

    # len += abs(input_list[-1] - input_list[0])

    input_list.sort()
    
    length = abs(input_list[-1]-input_list[0])*2


    print(length)