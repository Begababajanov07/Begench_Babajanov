s = input()
s = s.split()
s = ''.join(s)
print(s)

if s == s[::-1]:
    print("Палиндром")
else:
    print("Не палиндром")