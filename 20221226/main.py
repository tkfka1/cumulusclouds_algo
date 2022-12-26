## 2022년 12월 26일 구름 스터디 알고리즘공부
## 비타알고 코딩테스트
## 앵무새 꼬꼬 ★1
## https://k-digital.goorm.io/learn/lecture/29413/%EB%B9%84%ED%83%80%EC%95%8C%EA%B3%A0-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%B4%88%EA%B8%89%EB%B6%80%ED%84%B0-%EC%A4%91%EA%B8%89%EA%B9%8C%EC%A7%80/lesson/1454750/%EC%95%B5%EB%AC%B4%EC%83%88-%EA%BC%AC%EA%BC%AC-1


f = open("20221226/testcase1.txt", 'r')

answer = ""
vowel = ['a','e','i','o','u','A','E','I','O','U']

# 첫째줄 문장 개수
lenth = f.readline()

# 나머지 문자열 한줄씩 받는 반복문
for i in range(int(lenth)):
	
	# 임시 저장
	temp = ""
	
	# 문자열 하나씩 비교하기
	for ii in f.readline():
		
		if ii in vowel:
			#만약 모음이라면 그값 집어 넣기
			temp += ii
	if temp:
		print(temp)
	else:
		print("???")













# 구름 IDE 용

# answer = ""
# vowel = ['a','e','i','o','u','A','E','I','O','U']

# # 첫째줄 문장 개수
# lenth = input()


# # 나머지 문자열 한줄씩 받는 반복문
# for i in range(int(lenth)):
	
# 	# 임시 저장
# 	temp = ""
	
# 	# 문자열 하나씩 비교하기
# 	for ii in input():
		
# 		if ii in vowel:
# 			#만약 모음이라면 그값 집어 넣기
# 			temp += ii
# 	if temp:
# 		print(temp)
# 	else:
# 		print("???")

