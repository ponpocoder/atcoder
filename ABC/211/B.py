s1 = input()
s2 = input()
s3 = input()
s4 = input()

res = (s1 != s2) and (s1 != s3) and(s1 != s4) and (s2 != s3) and (s2 != s4) and (s3 != s4)
if res:
    print("Yes")
else:
    print("No")