def palindrome():
    length_of_list = int(input("Enter length of list: "))
    li=[]
    y = 0
    for i in range(length_of_list):
        y = int(input(f"Enter value of list item {i}: "))
        li.append(y)
    ans=[]
    for i in range(length_of_list-1,-1,-1):
        ans.append(li[i])
    print(ans)
if __name__=="__main__":
    palindrome()