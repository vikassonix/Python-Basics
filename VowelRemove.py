v="aeiouAEIOU"
s="ave"
print("Input string is : ",s)
for i in v:
    if(i in s):
        s=s.replace(i,"")
print(s)
