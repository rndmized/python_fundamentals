
def merge_and_sort(list1,list2):
    #merge the two lists
    merged_list= list1 + list2
    #sort merge
    return sorted(merged_list)   

#Given two lists of unordered integers
list1 = [5,7,9,56,76]
list2 = [90,87,52,32]
#Call function to merge and sort lists
print(merge_and_sort(list1,list2))