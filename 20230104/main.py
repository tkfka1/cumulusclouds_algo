## 2023년 01월 03일 구름 스터디 알고리즘공부
## 비타알고 코딩테스트
## 외계인과 용돈 기입장 ★2
## https://k-digital.goorm.io/learn/lecture/29413/%EB%B9%84%ED%83%80%EC%95%8C%EA%B3%A0-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%B4%88%EA%B8%89%EB%B6%80%ED%84%B0-%EC%A4%91%EA%B8%89%EA%B9%8C%EC%A7%80/lesson/1454751/%EC%99%B8%EA%B3%84%EC%9D%B8%EA%B3%BC-%EC%9A%A9%EB%8F%88-%EA%B8%B0%EC%9E%85%EC%9E%A5-2

f = open("20230103/testcase1.txt", 'r')

length = list(map(int, f.readline().split(" ")))
#print(length)
money = list(map(int, f.readline().split(" ")))
#print(money)

for i in range(1,length[0]):
	money[i] += money[i-1]

# print(money)

for i in range(length[1]):
	x,y = map(int, f.readline().split(" "))
	if x == 1:
		su = money[y-1]
	else:
		su = money[y-1] - money[x-2]
	
	if su > 0:
		print(f"+{su}")
	else:
		print(su)
					
					
					

## 구름

# length = list(map(int, input().split(" ")))
# money = list(map(int, input().split(" ")))

# for i in range(1,length[0]):
# 	money[i] += money[i-1]

# # print(money)

# for i in range(length[1]):
# 	x,y = map(int, input().split(" "))
# 	if x == 1:
# 		su = money[y-1]
# 	else:
# 		su = money[y-1] - money[x-2]
	
# 	if su > 0:
# 		print(f"+{su}")
# 	else:
# 		print(su)