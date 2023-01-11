## 2023년 01월 10일 구름 스터디 알고리즘공부
## 비타알고 코딩테스트
## 알파벳 삼각 장난감 ★3
## https://k-digital.goorm.io/learn/lecture/29413/%EB%B9%84%ED%83%80%EC%95%8C%EA%B3%A0-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%B4%88%EA%B8%89%EB%B6%80%ED%84%B0-%EC%A4%91%EA%B8%89%EA%B9%8C%EC%A7%80/lesson/1454749/%EC%95%8C%ED%8C%8C%EB%B2%B3-%EC%82%BC%EA%B0%81-%EC%9E%A5%EB%82%9C%EA%B0%90-3

f = open("20230110/testcase1.txt", 'r')

length = int(f.readline())

dic = {}

for i in range(length):
	dic[i] = list(map(lambda x:ord(x)-64 , f.readline()))

for i in range(1,length):
	temp = [0]*len(dic[i])

	for key,value in enumerate(dic[i]):
		if key == 0:
			temp[key] = dic[i-1][key] + value
		else:
			if key+1 == len(dic[i]):
				temp[key] = dic[i-1][key-1] + value
			else:
				temp[key] = max(dic[i-1][key-1],dic[i-1][key]) + value
	
	dic[i] = temp

print(max(dic[length-1]))

## 구름

# length = int(input())

# dic = {}

# for i in range(length):
# 	dic[i] = list(map(lambda x:ord(x)-64 , input()))

# for i in range(1,length):
# 	temp = [0]*len(dic[i])

# 	for key,value in enumerate(dic[i]):
# 		if key == 0:
# 			temp[key] = dic[i-1][key] + value
# 		else:
# 			if key+1 == len(dic[i]):
# 				temp[key] = dic[i-1][key-1] + value
# 			else:
# 				temp[key] = max(dic[i-1][key-1],dic[i-1][key]) + value
	
# 	dic[i] = temp

# print(max(dic[length-1]))
