#随机数版本
#
#coding=utf-8
import numpy as np
import pandas as pd
import random
import heapq
import os
import csv
import xlwings as xw

root = os.path.abspath('.')
app = xw.App(visible = False, add_book = False)
wkb = app.books.add()
sheet = wkb.sheets.active

#随机生成流数据集
def generate_S(S_num):
	S = []
	S = np.array(S)
	for i in range(S_num):
		xi = random.random()
		S = np.append(S,xi)
	
	return S
'''
def generate_S(S_num):
	S = []
	S = np.array(S)
	for i in range(S_num):
		xi = random.randint(1,20)
		S = np.append(S,xi)
	
	return S
'''

#单次数据处理获取估计topk序列D
def data_proc(S,k,n):
	#估计topk
	D = []
	D = np.array(D)
	#第i个随机独立排序器——随机抽取n个数据返回其中的前k大值
	for i in range(k):
		#print(i)
		A = np.random.choice(S,n,replace = False)
		A = np.unique(A)

		DK = heapq.nlargest(k,A)  #堆操作取前k大值

		for j in range(k):
			#print(DK[j])
			if DK[j] in D:
				continue
			D = np.append(D,DK[j])
			#print(D)
			break

	#对k个di排序获得估计topk序列
	D = np.sort(D,axis = 0,kind = 'mergesort',order = None)[::-1]
	#print(D)
	return D

#更新topk序列
def update_D(D1,D2,k):
	if D1.size == 0:
		return D2
	res = []
	res = np.array(res)
	a,b = 0,0
	for i in range(k):
		if D1[a] > D2[b]:
			res = np.append(res,D1[a])
			a+=1
		elif D1[a] == D2[b]:
			res = np.append(res,D1[a])
			a+=1
			b+=1
		else:
			res = np.append(res,D2[b])
			b+=1

	return res


#main函数1-自生成
def once(k,n,S_num,m,t):
	S_all = []
	S_all = np.array(S_all)
	D_new = []
	D_new = np.array(D_new)
	for i in range(t):
		S = generate_S(S_num)
		S_all = np.append(S_all,S)
		D = data_proc(S,k,n)
		#print(D)
		D_new = update_D(D_new,D,k)
		#print("update:")
		#print(D_new)
		x = S_all[S_all > D_new[k-1]]
		b = x.size/(S_num * (i + 1))
		sheet[m,n-140].value = b
		print(b)
	return b

#给定误差，可信度-抽样数
if __name__ == '__main__':
	k = 1
	t = 1
	#n_list = [458]
	#S_list = [100000]
	S = 100000

	e_list = [0.01]#, 0.05, 0.001] #给定误差

	for e in e_list:
		for n in range(140,200):
			T = 1000
			b_count = 0
			#filename = open(root + "/top" + str(k) + "_n" + str(j) + "_S" + str(i) + "_" + str(T) + ".txt", 'w+')
			for m in range(T):
				b = once(k,n,S,m,t)
				if b <= e:
					b_count += 1
			print("gama:",end = "")
			print(b_count/T)
			sheet[T, n-140].value = n
			sheet[T+1, n-140].value = b_count/T


		wkb.save(root + "/ds_top"+str(k)+ "_S" + str(S) +"_e" + str(e) + "_repeat" + str(T) +".xls")
	wkb.close()
