first_name = ['Michael', 'Dwight', 'Jim', 'Pam', 'Angela']
last_name = ['Scott', 'Schrute', 'Halpert', 'Beasley', 'Martin']

def combine_names(list_one,list_two):
    character_list = []
    for i in range(len(list_one)):
    	new_dict = {}
    	new_dict['first_name'] = list_one[i]
    	new_dict['last_name'] = list_two[i]
    	character_list.append(new_dict)
    return character_list

result = combine_names(first_name, last_name)
print(result)