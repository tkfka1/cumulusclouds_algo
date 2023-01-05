## 2023년 01월 05일 구름 스터디 알고리즘공부
## 비타알고 코딩테스트
## 여름의 대삼각형 ★1
## https://k-digital.goorm.io/learn/lecture/29413/%EB%B9%84%ED%83%80%EC%95%8C%EA%B3%A0-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%B4%88%EA%B8%89%EB%B6%80%ED%84%B0-%EC%A4%91%EA%B8%89%EA%B9%8C%EC%A7%80/lesson/1454741/%EC%97%AC%EB%A6%84%EC%9D%98-%EB%8C%80%EC%82%BC%EA%B0%81%ED%98%95-1

f = open("20230105/testcase1.txt", 'r')

import math
x1,y1 = map(int,f.readline().split(" "))
x2,y2 = map(int,f.readline().split(" "))
x3,y3 = map(int,f.readline().split(" "))



# Heron's formula: A=√s(s−a)(s−b)(s−c) where s=(a+b+c)/2

a = math.sqrt(((x1-x2)**2) + ((y1-y2)**2))
b = math.sqrt(((x1-x3)**2) + ((y1-y3)**2))
c = math.sqrt(((x2-x3)**2) + ((y2-y3)**2))

s = (a+b+c)/2

print("{:.2f}".format(math.sqrt(s*(s-a)*(s-b)*(s-c))))


# # 신발끈 공식 사용
# answer = abs(x1*y2+x2*y3+x3*y1 - y1*x2 - y2*x3 - y3*x1)/2

# print("{:.2f}".format(answer))
					
					
					

## 구름

# import math
# x1,y1 = map(int,input().split(" "))
# x2,y2 = map(int,input().split(" "))
# x3,y3 = map(int,input().split(" "))



# # Heron's formula: A=√s(s−a)(s−b)(s−c) where s=(a+b+c)/2

# a = math.sqrt(((x1-x2)**2) + ((y1-y2)**2))
# b = math.sqrt(((x1-x3)**2) + ((y1-y3)**2))
# c = math.sqrt(((x2-x3)**2) + ((y2-y3)**2))

# s = (a+b+c)/2

# print("{:.2f}".format(math.sqrt(s*(s-a)*(s-b)*(s-c))))


# # # 신발끈 공식 사용
# # answer = abs(x1*y2+x2*y3+x3*y1 - y1*x2 - y2*x3 - y3*x1)/2

# # print("{:.2f}".format(answer))