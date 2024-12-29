def Hcf():
    x=int(input("Enter your number1:"))
    y=int(input("Enter your number1:"))
    if x<y:
        num=x
    else:
        num=y
    while 1:
        if ((num%x==0)and(num%y==0)):
            lcm=num
            break
        num-=1
    print(f'{num} is the Highest common factor')
if __name__ == "__main__":
    Hcf()