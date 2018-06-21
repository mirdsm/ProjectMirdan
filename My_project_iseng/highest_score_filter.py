list=[]
student_counts = int(raw_input())
for _ in range(student_counts):
    #name = raw_input()
    #score = float(raw_input())
    temp = [ ]
    temp.append(raw_input())
    temp.append(float(raw_input()))
    list.append(temp)
def getKey(item):
    return item[1]
list = sorted(list, key=getKey)
#print list

rangking_1 =list[1]
g = 2
temp_2 = []
temp_2.append(rangking_1[0])
for i in range(student_counts):
    rangking_2 =list[g]
    if rangking_1[1] == rangking_2[1]:
        temp_2.append(rangking_2[0])
        rangking_1 = rangking_2
        g = g + 1
    else:
        None


final_name = sorted(temp_2)
#print final_name
for _ in final_name:
    print _




'''


nama_1 = rangking_1[0]
rangking_2 =list[1]
nama_2 = rangking_2[0]

print nama_1
print nama_2

'''
#element = list[0]
#print element
#print element[1]
