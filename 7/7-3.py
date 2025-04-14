list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

# 리스트 합치기
list3 = list1 + list2
print(list3)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 리스트 반복하기
list4 = list1 * 2
print(list4)  # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

pro_list1 = [1, 2, 3]
pro_list2 = [4, 5, 6]
pro_list3 = [0,0,0]

#pro_list3 = [pro_list1[i] + pro_list2[i] for i in range(len(pro_list1))]
for i in range (len(pro_list1)):
    pro_list3[i] = pro_list1[i] + pro_list2[i]
print(pro_list3)

pro_list4= []
for i in range (len(pro_list1)):
    pro_list4.append(pro_list1[i] + pro_list2[i])
print(pro_list4)


