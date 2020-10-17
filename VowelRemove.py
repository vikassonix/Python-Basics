v="aeiouAEIOU"
s="ave"
print("Input Data: ",s)
for i in v:
    if(i in s):
        s=s.replace(i,"")
print(s)
