## 2023년 01월 06일 구름 스터디 알고리즘공부
## 비타알고 코딩테스트
## A4 용지를 만들자 ★2
## https://k-digital.goorm.io/learn/lecture/29413/%EB%B9%84%ED%83%80%EC%95%8C%EA%B3%A0-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%B4%88%EA%B8%89%EB%B6%80%ED%84%B0-%EC%A4%91%EA%B8%89%EA%B9%8C%EC%A7%80/lesson/1454744/a4-%EC%9A%A9%EC%A7%80%EB%A5%BC-%EB%A7%8C%EB%93%A4%EC%9E%90-2

f = open("20230106/testcase1.txt", 'r')
x,y = map(int,f.readline().split())
print(((x//40)*(y//20))+((y//40)*(x//20))-((x//40)*(y//40))*2)						
					

## 구름

# x,y = map(int,input().split())
# print(((x//40)*(y//20))+((y//40)*(x//20))-((x//40)*(y//40))*2)