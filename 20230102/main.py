## 2022년 12월 29일 구름 스터디 알고리즘공부
## 비타알고 코딩테스트
## 1등과 2등 ★2
## https://k-digital.goorm.io/learn/lecture/29413/%EB%B9%84%ED%83%80%EC%95%8C%EA%B3%A0-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%B4%88%EA%B8%89%EB%B6%80%ED%84%B0-%EC%A4%91%EA%B8%89%EA%B9%8C%EC%A7%80/lesson/1454731/1%EB%93%B1%EA%B3%BC-2%EB%93%B1-2


f = open("20221229/testcase1.txt", 'r')

length = int(f.readline())

li = list(map(int,f.readline().split(" ")))
sumli = [0]*length

res = 0

for i in range(0,length):
	if i == 0:
		res = li[i]
	
	sumli[i] = max(sumli[i-1] + li[i] , li[i])
	
	if sumli[i] > res:
		res = sumli[i]

print(max(sumli))
					
					
					

## 구름

# length = int(input())

# li = list(map(int,input().split(" ")))
# sumli = [0]*length

# res = 0

# for i in range(0,length):
# 	if i == 0:
# 		res = li[i]
	
# 	sumli[i] = max(sumli[i-1] + li[i] , li[i])
	
# 	if sumli[i] > res:
# 		res = sumli[i]

# print(max(sumli))