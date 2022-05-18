import re

import re

list = ['errr 98', 'eee eee']
newlist = []

p = re.findall('[a-z]+]','5')
print('p',len(p))
prime = []
nonPrime =[]

for e in list:
   newlist.append(e.split())
index = 0
print(newlist)
for e in newlist:
     print(e[1])
     p = re.findall('[a-z]+]', e[1])
     print('p',len(p))
     if len(p) == 0:
         nonPrime.append(list[index])

     else:
         prime.append(list[index])

     index += 1




# print(newlist)
# print(prime)
print(nonPrime)


