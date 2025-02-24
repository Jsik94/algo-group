
from itertools import combinations

if __name__=="__main__":

   l_c_str = input()

   l_c_list = l_c_str.split(' ')
   
   l = int(l_c_list[0])
   c = int(l_c_list[1])

   total_vowel= ['a','e','i','o','u']
   word_list = input().split(" ")

   vowel  = [v  for v in word_list if v in total_vowel ]

   consonant = [c for c in word_list if c not in vowel]

   # print(vowel,consonant)
   
   # combi = list(combinations(word_list,l))

   # for atom in combi:
   #    print(''.join([str(a) for a in list(atom)]))

   result_list = list()
   vowel_cnt = 0
   while True :
      vowel_cnt +=1 

      for vowel_case in combinations(vowel,vowel_cnt) :
         
         # print(vowel_case,end="")


         if l-vowel_cnt < 2 :
            continue

         for con_case in combinations(consonant,l-vowel_cnt):
            encryp = list(vowel_case+ con_case)
            encryp.sort()
            # print(''.join(encryp))
            result_list.append(''.join(encryp))


         # print("")

      if vowel_cnt > len(vowel):
         break


   result_list.sort()


   for result in result_list:
      print(result)