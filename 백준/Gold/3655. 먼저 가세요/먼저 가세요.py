
if __name__=="__main__":



    input_cnt = int(input())
    input_list = list()
    for _ in range(input_cnt):
        input_cnt = input()
        input_list.append((input_cnt,list(input())))

    # input_str = "AABABB"


    for input_cnt,input_row in input_list:
        input_row= list(input_row)


        last_idx_dict = dict()
        order_dict = dict()
        cnt_dict = dict()

        order_cnt = 0
        for idx in range(0,len(input_row)):

            last_idx_dict[input_row[idx]] = idx

            if input_row[len(input_row)-1-idx] not in order_dict.values():
                order_dict[order_cnt] = input_row[len(input_row)-1-idx]
                order_cnt+=1
            if input_row[idx] not in cnt_dict:
                cnt_dict[input_row[idx]] = 1
            else:
                cnt_dict[input_row[idx]] +=1


        # print(last_idx_dict,cnt)
        # print(order)

        result = 0
        current_idx = 0 
        for idx in range(order_cnt-1,-1,-1):
            
            # if idx == 0 :
            #     continue

            # print('target',order_dict[idx] )
            # print(f'5*({last_idx_dict[order_dict[idx]]}-{current_idx+cnt_dict[order_dict[idx]]-1} )*{cnt_dict[order_dict[idx]]}')
            # print(5*(last_idx_dict[order_dict[idx]]-(current_idx+cnt_dict[order_dict[idx]]-1))*cnt_dict[order_dict[idx]])
            
            result += 5*(last_idx_dict[order_dict[idx]]-(current_idx+cnt_dict[order_dict[idx]]-1))*cnt_dict[order_dict[idx]]
            current_idx+= cnt_dict[order_dict[idx]]
        # order = dict()
        # cnt = dict()

        print(result)