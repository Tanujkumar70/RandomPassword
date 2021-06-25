import random
passlen =int(input("Enter the length of passward"))
s="dfwevyu;oij'p2354657687"
p="".join(random.sample(s,passlen))
print(p)
