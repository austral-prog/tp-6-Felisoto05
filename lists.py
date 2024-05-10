def remove_elements(lista):
    if len(lista)>=6:
        del lista[0]
        del lista[3]
        del lista[3]
        return lista
    else:
        if len(lista)==5:
            del lista[0]
            del lista[4]
            return lista
        else:
            del lista[0]
            return lista
print(remove_elements(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']))

def add_elements(list_add_elements):
    list_add_elements.append("Yellow")
    list_add_elements.insert(0,"Pink")
    return print(list_add_elements)
add_elements(['Red', 'Green', 'White', 'Black'])

def is_empty(list_to_check):
    if list_to_check ==[]:
        return True
    else:
        return False
print(is_empty([]))

def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1)>=3 and len(list_to_compare2)>=3:
        if list_to_compare1[2]==list_to_compare2[2]:
            return True
        else:
            return False
    else:
        return False
print(check_lists(['Black', 'Pink', 'Yellow', 'Red', 'Green', 'White'],['Red', 'Green', 'Yellow', 'White', 'Black', 'Pink']))

def lists_of_lists(list_of_lists_to_modify):
    if len(list_of_lists_to_modify[0])>=2 and len(list_of_lists_to_modify[1])>=4 and len(list_of_lists_to_modify[2])>=2:
        list_of_lists_to_modify[0]= list_of_lists_to_modify[0][0:2]
        list_of_lists_to_modify[1]=list_of_lists_to_modify[1][1:4]
        list_of_lists_to_modify[2]=list_of_lists_to_modify[2][-2:]
        return list_of_lists_to_modify
print(lists_of_lists([[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12]]))
