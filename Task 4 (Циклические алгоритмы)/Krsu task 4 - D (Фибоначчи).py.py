def fibonacci(n):
  if n<0:
    print("ERROR")
  else:
    count=0
    fn1=0
    fn2=1
    count=0
    if n==0 or n==1:
        return n
    while count<n:
        f=fn1+fn2
        fn2=fn1
        fn1=f
        count+=1
    print(f)

n=int(input("please input number"))
fibonacci(n)
