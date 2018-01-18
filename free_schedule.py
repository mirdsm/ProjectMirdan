list_time = [(1,2),(2,4),(3,5),(6,7),(8,10)]

list_meeting_time = [(0, 1), (4, 8),(3, 5), (10, 12), (9, 10)]


for item in list_meeting_time:
    if 9 in item:
        print item


def lst_function(someList, value):
    for x,y in someList:
        if x == value:
            return x,y

result = lst_function(list_meeting_time, 8)
print result
