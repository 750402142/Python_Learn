
import numpy as np

#import pandas
#创建一维数组
#数组没有逗号,和列表的差别
list1 = [1,3,5]
list1_array = np.array(list1)
print(list1)
print(list1_array)
#创建二维数组,两个添加的数组长度必须相同
list2 = [2,3,3]
list2_array = np.array([list1,list2])
print(list2_array.shape)
print(list2_array.reshape((5,2)))
print(list2)
print(list2_array)

import numpy as np
# 创建线段型数据
data= np.linspace(1,10,20) # 开始端1，结束端10，且分割成20个数据，生成线段
print(data)
print(len(data))


#创建随机数组
import numpy as np
data = np.random.rand(3,4)
print(data)

