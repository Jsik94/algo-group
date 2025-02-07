if __name__=="__main__":


    #입력되는 번호 길이 
    input_cnt = int(input())

    list_group = list()
    for i in range(input_cnt):
        
        input_str = list(input())
        data = sorted(input_str)

        if data not in list_group:
            list_group.append(data)


    print(len(list_group))