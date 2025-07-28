s = 'every subclass must implement a abstract methods unless'
count =0
new_s=''
for i in s:
    if i == ' ':
        new_s +=i
        count=0
    else:
        count +=1
        if count ==3:
            new_s =new_s+i.upper()
        else:
            new_s +=i
        
print(new_s)
