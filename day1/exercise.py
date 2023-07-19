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
