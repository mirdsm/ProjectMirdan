
'''
1. Pilih angka maksimal (var: a_max)
2. Masukan ke variabel list baru (var: new_var_list)
3. Remove a_max dari list
4. Ulangi perulangan sampe 3 kali
5. Print new_var_list
'''

#new_var_list = []
def max_int_filter():
    new_var_list = []
    list = [4,-12,-9,3,-100,3]
    for i in range(0,3):
        a_max = max(list)
        #print a_max
        new_var_list.insert(0,a_max)
        list.remove(a_max)
    print new_var_list

max_int_filter()
