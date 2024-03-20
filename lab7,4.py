import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time
import random
import math


#задания 1

# def calculate_time(func):
#     def wrapper(*args,**kwargs):
#         begin = time.perf_counter()
#         func(*args,**kwargs)
#         stop = time.perf_counter()
#         print(f'execution time for {func.__name__}: {stop - begin}')
#     return wrapper

# list_1 = [random.random()*100 for i in range(1000000)]
# list_2 = [random.random()*100 for i in range(1000000)]
# arr_1 = np.array([random.random()*100 for i in range(0, 1000000)])
# arr_2 = np.array([random.random()*100 for i in range(0, 1000000)])

# @calculate_time
# def standard_list(list1, list2):
#     list_all = []
#     for i in range(len(list_1)):
#         list_all.append(list_1[i]*list_2[i])

# standard_list(list_1, list_2)

# @calculate_time
# def nump_py(arr_1,arr_2):
#     multi= np.multiply(arr_1,arr_2)

# nump_py(arr_1,arr_2)


#задания 2


# data = np.genfromtxt('data2.csv', delimiter = ',')
# col_2 = data[:,1]

# mean = np.nanmean(col_2)
# std_dev= np.nanstd(col_2)

# upp_bound = mean + std_dev
# low_bound = mean - std_dev

# plt.figure(figsize=(6,4))

# plt.hist(col_2, bins=17, color='black', edgecolor='black', alpha= 0.7)
# plt.axhline(mean, linestyle='--', color='red', label= f'Среднеквадратичное отклонение')
# plt.axhline(upp_bound, color='g', linestyle ='--', label= 'среднее + отклонение')
# plt.axhline(low_bound, color='b', linestyle='--', label= 'среднее - отклонение')
# plt.fill_between([0, len(col_2)], upp_bound, low_bound, color='yellow', alpha=0.3,  label='Диапазон')
# plt.legend()

# plt.title('Выровненная (эквализированная) гистограмма')
# plt.xlabel('значения')
# plt.ylabel('частота')
# plt.show()



 
#задания 3

# x = np.linspace(-5,5)
# y = np.linspace(-5,5)
# z = np.sin(pow(x, y))

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.plot(x, y, z, c='green')
# ax.set_xlabel("x")
# ax.set_ylabel("y")
# ax.set_zlabel("z")
# plt.show()