

if __name__=="__main__":


    input_list = list()

    for _ in range(5):
        input_list.append(int(input()))

    input_list.sort()

    print(int(sum(input_list)/len(input_list)))
    print(input_list[2])