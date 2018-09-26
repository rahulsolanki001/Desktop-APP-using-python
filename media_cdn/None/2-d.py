#2-d list
s=input("enter a string:")
print("length of string:",len(s))
x=input('which word of the string you want to search:')
for i in range (0,len(s)):
    if x==s[i]:
        print('found')
                  
                  
