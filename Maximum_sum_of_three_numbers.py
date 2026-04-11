def max_tri_sum(numbers):
    A_list_without_duplicatesset = set(numbers)
    Sorted_A_list_without_duplicatesset = sorted(A_list_without_duplicatesset) 
    return sum(Sorted_A_list_without_duplicatesset[-3:])