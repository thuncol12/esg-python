str1 = 'Dog is Love'
str2 = "lalalalalalalalala"
str3 = '010-1234-5678'

# love만 출력 (slicing)
print(str1[7:])

# Dog를 Cat으로 바꿔서 출력 (replace)
new_str1 = str1.replace("Dog", 'Cat')
print(new_str1)

# str2 길이, a의 개수 출력
print(len(str2))
print(str2.count('a'))

# 하이픈 제거
print(str3.replace('-', ''))

# 두 문자열 합치기
a = 'hello'
b = 'python'
print(a+"! "+b)

# 리스트에서 특정항목삭제
my_list = ['red', 'orange', 'yellow',
           'green', 'blue', 'purple', 'black', 'white']
my_list.remove('green')
print(my_list)


# 리스트에 특정 문자 추가
my_list.insert(1, "pink")
print(my_list)


# 딕셔너리에서 a,b에 해당하는 값 출력
a = {
    "A": 90,
    "B": 80,
    "C": 70,
    "D": 60
}
print(a["B"])

# 교집합과 차집합
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1 & s2)
print(s1-s2)

# 중복이 없는 리스트로 출력하기
my_list = [1, 2, 3, 4, 4, 4, 9, 11, 11, 11, 14]
new_list = list(set(my_list))
print(new_list)
