import os
from os.path import exists

list_data = []
def get_itr_form_recursion(path):
    if os.path.exists(path):
        for i in os.listdir(path):
            new_path = path + "\\" + i
            if os.path.isdir(new_path):
                get_itr_form_recursion(new_path)
            else:
                list_data.append(i)

    else:
        return list_data
get_itr_form_recursion("D:\黑马代码\递归")
print(list_data)


