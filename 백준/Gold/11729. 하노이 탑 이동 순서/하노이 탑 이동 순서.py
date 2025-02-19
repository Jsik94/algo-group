
def cal(n):
   
   return 2**n -1


def func(n,start,mid,end):
    

    if n == 1 :
       
       print(f'{start} {end}')
    
    else: 
       func(n-1,start=start,mid=end,end=mid)
       print(f'{start} {end}')
       func(n-1,start=mid,mid=start,end=end)




if __name__=="__main__":

    n = int(input())

    print(cal(n))
    func(n,1,2,3)
    
    pass