print("problema6")

n = 5999
print(n)
print(n%9)
print(n//9)
print(n//1000,"+",n//100%10,"+",n//10%10,"+",n%10,"=",(n//1000)+(n//100%10)+(n//10%10)+(n%10))
print(n%10,n//10%10,n//100%10,n//1000,sep="")