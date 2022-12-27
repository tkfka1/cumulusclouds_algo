## 2022년 12월 27일 구름 스터디 알고리즘공부
## 비타알고 코딩테스트
## 인싸가 되고 싶은 민수 ★2
## https://k-digital.goorm.io/learn/lecture/29413/%EB%B9%84%ED%83%80%EC%95%8C%EA%B3%A0-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%B4%88%EA%B8%89%EB%B6%80%ED%84%B0-%EC%A4%91%EA%B8%89%EA%B9%8C%EC%A7%80/lesson/1454730/%EC%9D%B8%EC%8B%B8%EA%B0%80-%EB%90%98%EA%B3%A0-%EC%8B%B6%EC%9D%80-%EB%AF%BC%EC%88%98-2

import math

f = open("20221227/testcase1.txt", 'r')

input_vals = list(map(int, f.readline().split(" ")))
min_val, max_val = min(input_vals), max(input_vals)
if max_val > min_val:
	print(2)
else:
	find = False
	i = 2
	while (not find and i <= int(math.sqrt(max_val))):
		if max_val % i == 0:
			print(i)
			find = True
		i += 1
	if not find:
		print(max_val)



## 구름용

# import math

# input_vals = list(map(int, input().split(" ")))
# min_val, max_val = min(input_vals), max(input_vals)
# if max_val > min_val:
# 	print(2)
# else:
# 	find = False
# 	i = 2
# 	while (not find and i <= int(math.sqrt(max_val))):
# 		if max_val % i == 0:
# 			print(i)
# 			find = True
# 		i += 1
# 	if not find:
# 		print(max_val)




# 너무 느려서 폐기 1
# /////////////////////////////////////////////////
# import math

# input_vals = list(map(int, input().split(" ")))
# min_val, max_val = min(input_vals), max(input_vals)
# table = [0] * (max_val+1)

# for i in range(2, max_val+1):
# 	val = i * math.ceil(min_val / i)
# 	while (val <= max_val):
# 		table[i] += 1
# 		val += i

# max_num = max(table)
# index = table.index(max_num)
# print(index)
# /////////////////////////////////////////////////





## 너무 느려서 폐기 2
# f = open("20221227/testcase1.txt", 'r')

# user_input = f.readline()
# a,b = user_input.split(" ")
# #print(a,b)

# ## 소수 구하기
# def is_prime_num(n):
#     arr = [True] * (n + 1) # 특정 수가 지워졌는지 아닌지 확인하기 위한 배열
#     arr[0] = False
#     arr[1] = False

#     for i in range(2, n + 1):
#         if arr[i] == True: # 특정 수가 지워지지 않았다면 (소수여서)
#             j = 2

#             while (i * j) <= n:
#                 arr[i*j] = False # i의 배수의 값을 False로 지워준다.
#                 j += 1

#     return arr

# arr = is_prime_num(int(int(b)**(1/2))) # 0 ~ rootB 중 소수를 구하기 위한 함수
# answer = 0
# find = False
# # 소수의 개수만큼 루프
# for i in range(len(arr)):
#     #만약 i가 소수라면
#     if arr[i] == True:
#         # a~b까지 루프
#         for x in range(int(a),int(b)+1):
#             ## i 가 만약 x의 약수라면
#             if x%i == 0:
#                 arr[i] += 1
#                 if arr == int(b)-int(a)+1:
#                     find = True
#                     answer = i
#                     break
    
#     if find:
#         break

# if find:
#     print(answer)
# else:
#     print(arr.index(max(arr)))



					
					
					
					
					