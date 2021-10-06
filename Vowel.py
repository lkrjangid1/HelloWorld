# WAP to find the number of occurances of each vowels present in given list

s=str(input("Enter the statement : "))
v={'A','E','I','O','U','a','e','i','o','u'}
d={}
for x in s:
   if x in v:
      d[x]=d.get(x,0)+1
print(d)