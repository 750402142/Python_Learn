
str1 = 'it and me'
str2 = 'itand'

print(str1.index('and'))
print(str2.index('and'))
print(str1[0])

str = "万过薪月,员序程马黑来,nohtyP学"

new_str = str[9:4:-1]

new_str2 = str.split(",")
for str in new_str2:
    print(str)
print(new_str2[1][4::-1])
get = new_str2[1].replace('来','')
print(get[::-1])


print(new_str)

my_list = ['黑马程序员','传智播客','黑马程序员','传智播客','itheima','itcast',
           'itheima','itcast','best']
my_set = set({})
for i in my_list:
    my_set.add(i)

print(my_set)

stu_score = {"帅哥":20,"美女":21}
keys = stu_score.keys()
for key in stu_score:
    print(f"学生{key}的成绩为{stu_score[key]}")