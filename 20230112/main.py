## 2023년 01월 12일 구름 스터디 알고리즘공부
## 비타알고 코딩테스트
## 숫자 블럭 쌓기 ★3
## https://k-digital.goorm.io/learn/lecture/29413/%EB%B9%84%ED%83%80%EC%95%8C%EA%B3%A0-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%B4%88%EA%B8%89%EB%B6%80%ED%84%B0-%EC%A4%91%EA%B8%89%EA%B9%8C%EC%A7%80/lesson/1454738/%EC%88%AB%EC%9E%90-%EB%B8%94%EB%9F%AD-%EC%8C%93%EA%B8%B0-3

f = open("20230112/testcase1.txt", 'r')

length = int(f.readline())

inbox = []
my = 1
change = 0
ston = 0

for i in range(length*2):
	x = f.readline()
	if x[0] == "a":
		inbox.append(int(x.split()[1]))
		if not my == int(x.split()[1]):
			ston = 0
	else:
		if inbox[-1] == my:
			inbox.pop()
			my += 1
		else:
			if ston == 0:
				change += 1
				ston = 1
			elif ston == 1:
				ston = 1
			my += 1
			
print(change)

## 구름
# length = int(input())

# inbox = []
# my = 1
# change = 0
# ston = 0

# for i in range(length*2):
# 	x = input()
# 	if x[0] == "a":
# 		inbox.append(int(x.split()[1]))
# 		if not my == int(x.split()[1]):
# 			ston = 0
# 	else:
# 		if inbox[-1] == my:
# 			inbox.pop()
# 			my += 1
# 		else:
# 			if ston == 0:
# 				change += 1
# 				ston = 1
# 			elif ston == 1:
# 				ston = 1
# 			my += 1
			
# 	# print(inbox)

# print(change)