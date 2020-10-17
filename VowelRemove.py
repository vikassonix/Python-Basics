v="aeiouAEIOU"
s="avenger"
print("Input string : ",s)
for i in v:
    if(i in s):
        s=s.replace(i,"")
print(s)
