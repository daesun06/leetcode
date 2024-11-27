#You are given the heads of two sorted linked lists list1 and list2.
#Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
#Return the head of the merged linked list.

list1 = list(input("Enter some numbers (without any spaces): "))
list2 = list(input("Enter some numbers again (without any spaces): "))

for i in list2:
    list1.append(i)
    sorted_list = sorted(list1)
print(sorted_list)
