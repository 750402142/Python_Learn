
a=  int(input("请输入任意一个数字:"))

nums = []
n = 1
while n<=a:
    nums.append(n)
    n+=1
lucky = []
for i in nums:
    if i %6 == 0:
        lucky.append(i)
print(nums)
print(lucky)

