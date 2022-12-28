## 2022년 12월 28일 구름 스터디 알고리즘공부
## 비타알고 코딩테스트
## 교수님의 과제 폭탄 ★3
## https://k-digital.goorm.io/learn/lecture/29413/%EB%B9%84%ED%83%80%EC%95%8C%EA%B3%A0-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%B4%88%EA%B8%89%EB%B6%80%ED%84%B0-%EC%A4%91%EA%B8%89%EA%B9%8C%EC%A7%80/lesson/1454747/%EA%B5%90%EC%88%98%EB%8B%98%EC%9D%98-%EA%B3%BC%EC%A0%9C-%ED%8F%AD%ED%83%84-3

import math

f = open("20221228/testcase1.txt", 'r')

input_vals = f.readline()

lenth = input_vals
li = []

## 시작월 *1000000 시작일 *10000 종료월 *100 종료일 *1

for i in range(int(lenth)):
	
	x = f.readline()

	temp = 0

	x = x.split(" ")
	x[0] = x[0].split("/")
	x[1] = x[1].split("/")
	
	temp = ((int(x[0][0])*50) + int(x[0][1]) , (int(x[1][0])*50) + int(x[1][1]))
	
	li.append(temp)

li = sorted(li)
print(li)

prestart = 0
end = 650

for i in li:
	if prestart == i[0]:
		end = min(end,i[1])
	elif end >= i[1]:
		prestart = i[0]
		end = i[1]
	else:
		print("No")
		break
	print(i)
else:
	print("Yes")
					
					
					
					
					