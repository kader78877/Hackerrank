def cutTheSticks(arr):
    stick_cut = []
    arr_copy = copy.deepcopy(arr)
    while len(arr_copy) != 0 :
        
        stick_cut.append(len(arr_copy))
        min_stick = min(arr_copy)
        arr_copy_bis  = copy.deepcopy(arr_copy)
        
        while min_stick in arr_copy_bis :
            arr_copy_bis.remove(min_stick)
        
        for j in range(len(arr_copy_bis)):
            arr_copy_bis[j] = arr_copy_bis[j] - min_stick
            
        arr_copy = copy.deepcopy(arr_copy_bis)
        
    return stick_cut
