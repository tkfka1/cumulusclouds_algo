## 2023년 01월 11일 구름 스터디 알고리즘공부
## 비타알고 코딩테스트
## 방 탈출하기 ★2
## https://k-digital.goorm.io/learn/lecture/29413/%EB%B9%84%ED%83%80%EC%95%8C%EA%B3%A0-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%B4%88%EA%B8%89%EB%B6%80%ED%84%B0-%EC%A4%91%EA%B8%89%EA%B9%8C%EC%A7%80/lesson/1454752/%EB%B0%A9-%ED%83%88%EC%B6%9C%ED%95%98%EA%B8%B0-2

f = open("20230111/testcase1.txt", 'r')

## 수열의 길이
n = f.readline()

## 수열
li = list(map(int,f.readline().split()))

lidic = {i for i in set(li)}

## 모니터 수열 길이
m = f.readline()

## 모니터 출력 수열
monitor = list(map(int,f.readline().split()))

for i in monitor:
	if i in lidic:
		print(1)
	else:
		print(0)

## 구름

# ## 수열의 길이
# n = input()

# ## 수열
# li = list(map(int,input().split()))

# lidic = {i for i in set(li)}

# ## 모니터 수열 길이
# m = input()

# ## 모니터 출력 수열
# monitor = list(map(int,input().split()))

# for i in monitor:
# 	if i in lidic:
# 		print(1)
# 	else:
# 		print(0)
