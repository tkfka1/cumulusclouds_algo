## 2022년 12월 30일 구름 스터디 알고리즘공부
## 비타알고 코딩테스트
## 알파벳 트리 장난감 ★2
## https://k-digital.goorm.io/learn/lecture/29413/%EB%B9%84%ED%83%80%EC%95%8C%EA%B3%A0-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%B4%88%EA%B8%89%EB%B6%80%ED%84%B0-%EC%A4%91%EA%B8%89%EA%B9%8C%EC%A7%80/lesson/1454739/%EC%95%8C%ED%8C%8C%EB%B2%B3-%ED%8A%B8%EB%A6%AC-%EC%9E%A5%EB%82%9C%EA%B0%90-2

f = open("20221230/testcase1.txt", 'r')

length = int(f.readline())

li = []

for i in range(length):
	x = f.readline()

	li.append(list(map(lambda s:ord(s)-64, x)))	

temp = li[0]
for i in range(1,length):
	for ii in range(len(li[i])):
		li[i][ii] += li[i-1][(ii//2)]

		
print(min(li[-1]))		
print(max(li[-1]))
					
					

## 구름

# length = int(input())

# li = []

# for i in range(length):
# 	x = input()

# 	li.append(list(map(lambda s:ord(s)-64, x)))	

# temp = li[0]
# for i in range(1,length):
# 	for ii in range(len(li[i])):
# 		li[i][ii] += li[i-1][(ii//2)]

		
# print(min(li[-1]))		
# print(max(li[-1]))