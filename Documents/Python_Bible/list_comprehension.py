Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> even_number = [x for x in range(1,101) if x % 2 == 0]
>>> print(even_number)
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
>>> odd_number = [x for x in range(1,101) if x % 2 != 0]
>>> print(odd_number)
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
>>> 
>>> words = ["the", "quick", "brown", "fox", "jumps", "over"]
>>> answer = [[w.upper().w.lower(),len(w)] for w in words]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    answer = [[w.upper().w.lower(),len(w)] for w in words]
  File "<pyshell#6>", line 1, in <listcomp>
    answer = [[w.upper().w.lower(),len(w)] for w in words]
AttributeError: 'str' object has no attribute 'w'
>>> answer = [[w.upper(),w.lower(),len(w)] for w in words]
>>> print(answer)
[['THE', 'the', 3], ['QUICK', 'quick', 5], ['BROWN', 'brown', 5], ['FOX', 'fox', 3], ['JUMPS', 'jumps', 5], ['OVER', 'over', 4]]
>>> 
