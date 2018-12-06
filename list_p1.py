#values = ['siva', 'krishna', 'puppy', 'chinnu', 'budi']
#d = {'Name':'Siva', 'Age': 27}
#import sys

#values = (sys.argv[1],sys.argv[2])
#for x in values: 
  #  print(x)
   # f.write("\n")
#with open(myfile, 'w') as f:
 #   for key, value in a.items():
  #      f.write('%s:%s\n' % (key, value))
def name_age(namn):
    dic = {}
    age = 0
    for n in range(0, len(namn), 2):
        dic[namn[n]] = namn[n+1]
    for i in dic:
        print i, dic[i]
        age = age + dic[i]
    avg_age = age / len(dic)
    return avg_age