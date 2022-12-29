## 2022년 12월 29일 구름 스터디 알고리즘공부
## 비타알고 코딩테스트
## 1등과 2등 ★2
## https://k-digital.goorm.io/learn/lecture/29413/%EB%B9%84%ED%83%80%EC%95%8C%EA%B3%A0-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%B4%88%EA%B8%89%EB%B6%80%ED%84%B0-%EC%A4%91%EA%B8%89%EA%B9%8C%EC%A7%80/lesson/1454731/1%EB%93%B1%EA%B3%BC-2%EB%93%B1-2


f = open("20221229/testcase1.txt", 'r')

user_input = f.readline()
answer = "No"
pre = ""
on12 = False
on21 = False

for i in user_input:

	if i == "1":
		if pre == "2":
			if not on12:
				on12 = True
				pre = ""
			else:
				pre = i
		else:
			pre = i
			
	elif i == "2":
		if pre == "1":
			if not on21:
				on21 = True
				pre = ""
			else:
				pre = i
		else:
			pre = i
	else:
		pre = i

if on12 and on21:
	answer = "Yes"

print(answer)
					
					
					

## 구름

# user_input = input()
# answer = "No"
# pre = ""
# on12 = False
# on21 = False

# for i in user_input:

# 	if i == "1":
# 		if pre == "2":
# 			if not on12:
# 				on12 = True
# 				pre = ""
# 			else:
# 				pre = i
# 		else:
# 			pre = i
			
# 	elif i == "2":
# 		if pre == "1":
# 			if not on21:
# 				on21 = True
# 				pre = ""
# 			else:
# 				pre = i
# 		else:
# 			pre = i
# 	else:
# 		pre = i

# if on12 and on21:
# 	answer = "Yes"

# print(answer)