
def check_list():
    string_list= ["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"]
    i=0
    new_list=[]
    while i<len(string_list):
        if string_list[i] not in new_list:
            new_list.append(string_list[i])
        i+=1
    print(new_list)
check_list()
#more_qs6