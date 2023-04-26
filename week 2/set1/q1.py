list1 = [1,2,3,4,5,6]
list2 = [4,6,12,3,2,1]
input_list = [4,2,8,3,2,1]


result_list = list(map(lambda x, y: x+y, list1, list2))


final_list = list(map(lambda x, y: x*y, result_list, input_list))

print(final_list)