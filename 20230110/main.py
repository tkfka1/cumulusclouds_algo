## 2023년 01월 09일 구름 스터디 알고리즘공부
## 비타알고 코딩테스트
## 1차원 뿌요뿌요 ★3
## https://k-digital.goorm.io/learn/lecture/29413/%EB%B9%84%ED%83%80%EC%95%8C%EA%B3%A0-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%B4%88%EA%B8%89%EB%B6%80%ED%84%B0-%EC%A4%91%EA%B8%89%EA%B9%8C%EC%A7%80/lesson/1454746/1%EC%B0%A8%EC%9B%90-%EB%BF%8C%EC%9A%94%EB%BF%8C%EC%9A%94-3

f = open("20230109/testcase1.txt", 'r')
n,m = map(int,f.readline().split())
li = list(map(str,f.readline()))

afterli = []

while True:
	end = li
	pre = ""
	stack = 1
	for i in range(len(li)):

		if li[i] == pre:
			stack += 1
			afterli.append(li[i])

		else:
			pre = li[i]
			if stack >= m:
				for x in range(stack):
					afterli.pop()
				afterli += li[i:]
				break
			else:
				afterli.append(li[i])

			stack = 1
	else:
		if stack >= m:
			for x in range(stack):
				afterli.pop()
	
	li = afterli
	afterli = []

	if li == end:
		if li:
			print("".join(li))
		else:
			print("CLEAR!")
		break				
					

## 구름

# n,m = map(int,input().split())
# li = list(map(str,input()))
# afterli = []


# while True:
# 	end = li
# 	pre = ""
# 	stack = 1
# 	for i in range(len(li)):

# 		if li[i] == pre:
# 			stack += 1
# 			afterli.append(li[i])

# 		else:
# 			pre = li[i]
# 			if stack >= m:
# 				for x in range(stack):
# 					afterli.pop()
# 				afterli += li[i:]
# 				break
# 			else:
# 				afterli.append(li[i])

# 			stack = 1
# 	else:
# 		if stack >= m:
# 			for x in range(stack):
# 				afterli.pop()
	
# 	li = afterli
# 	afterli = []

# 	if li == end:
# 		if li:
# 			print("".join(li))
# 		else:
# 			print("CLEAR!")
# 		break