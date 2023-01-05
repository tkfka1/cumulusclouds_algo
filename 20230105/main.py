## 2023년 01월 04일 구름 스터디 알고리즘공부
## 비타알고 코딩테스트
## 불이야!! ★2
## https://k-digital.goorm.io/learn/lecture/29413/%EB%B9%84%ED%83%80%EC%95%8C%EA%B3%A0-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%B4%88%EA%B8%89%EB%B6%80%ED%84%B0-%EC%A4%91%EA%B8%89%EA%B9%8C%EC%A7%80/lesson/1454734/%EB%B6%88%EC%9D%B4%EC%95%BC-2

f = open("20230104/testcase1.txt", 'r')

y,x = map(int,f.readline().split(" "))

li = [[0]*x for _ in range(y)]

people = [(0,0)]

# 기본 초기화 &원준 ==> people 0 .빈칸 == 0 @불 == 1 #벽 == -1
for yy in range(y):
	for i,xx in enumerate(f.readline()):
		if xx == "&":
			people = [(yy,i)]
			li[yy][i] = 0
		elif xx == "@":
			li[yy][i] = 1
		elif xx == "#":
			li[yy][i] = -1

def onestep(loc):
	u,d,l,r = 1,1,1,1
	temp = []
	if loc[0] == 0:
		#위로 안함
		u = 0
	if loc[0] == y-1:
		#아래 안함
		d = 0
	if loc[1] == 0:
		#왼쪽 안함
		l = 0
	if loc[1] == x-1:
		#오른 안함
		r = 0
	if u:
		temp.append((loc[0]-1,loc[1]))
	if d:
		temp.append((loc[0]+1,loc[1]))			
	if l:
		temp.append((loc[0],loc[1]-1))				
	if r:
		temp.append((loc[0],loc[1]+1))
	return temp
					
count = 0
ans = False

while True:
	temp = []
	
	for i in people:
		if li[i[0]][i[1]] == 0:
			li[i[0]][i[1]] = 2
			temp.extend(onestep(i))
		elif li[i[0]][i[1]] == 1:
			ans = True
			break

	people = temp
	if ans:
		print(count-1)
		break
	if not people:
		print(-1)
		break
	# print(people,count)
	if count == x*y//2+x+y:
		print(-1)
		break
	
	count += 1
					
					
					

## 구름

# y,x = map(int,input().split(" "))

# li = [[0]*x for _ in range(y)]

# people = [(0,0)]

# # 기본 초기화 &원준 ==> people 0 .빈칸 == 0 @불 == 1 #벽 == -1
# for yy in range(y):
# 	for i,xx in enumerate(input()):
# 		if xx == "&":
# 			people = [(yy,i)]
# 			li[yy][i] = 0
# 		elif xx == "@":
# 			li[yy][i] = 1
# 		elif xx == "#":
# 			li[yy][i] = -1

# def onestep(loc):
# 	u,d,l,r = 1,1,1,1
# 	temp = []
# 	if loc[0] == 0:
# 		#위로 안함
# 		u = 0
# 	if loc[0] == y-1:
# 		#아래 안함
# 		d = 0
# 	if loc[1] == 0:
# 		#왼쪽 안함
# 		l = 0
# 	if loc[1] == x-1:
# 		#오른 안함
# 		r = 0
# 	if u:
# 		temp.append((loc[0]-1,loc[1]))
# 	if d:
# 		temp.append((loc[0]+1,loc[1]))			
# 	if l:
# 		temp.append((loc[0],loc[1]-1))				
# 	if r:
# 		temp.append((loc[0],loc[1]+1))
# 	return temp
					
# count = 0
# ans = False

# while True:
# 	temp = []
	
# 	for i in people:
# 		if li[i[0]][i[1]] == 0:
# 			li[i[0]][i[1]] = 2
# 			temp.extend(onestep(i))
# 		elif li[i[0]][i[1]] == 1:
# 			ans = True
# 			break

# 	people = temp
# 	if ans:
# 		print(count-1)
# 		break
# 	if not people:
# 		print(-1)
# 		break
# 	# print(people,count)
# 	if count == x*y//2+x+y:
#	print(-1)
# 		break
	
# 	count += 1