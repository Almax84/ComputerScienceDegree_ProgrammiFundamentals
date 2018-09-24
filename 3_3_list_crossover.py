def crossing_over(ls1,ls2):
    new_list=[]
    for i in range(len(ls1)):
        new_list+=[ls1[i]]
        new_list+=[ls2[i]]
    return new_list
    


#crossing_over([1, 3, 5], [2, 4, 6])
#expected result [1, 2, 3, 4, 5, 6]

