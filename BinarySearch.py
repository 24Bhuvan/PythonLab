def locate_card(cards,query):
    lo, hi = 0, len(cards)-1
    while lo<=hi :
        mid = (lo+hi)//2
        mid_number=cards[mid]
        print(f"{lo}, {hi}, {mid}, {mid_number}")
        if mid_number==query:
            return mid
        elif mid_number>query:
            lo = mid+1
        elif mid_number<query:
            hi = mid-1
    return -1
if __name__=="__main__":
    n=int(input("Enter number elements: "))
    li=[]
    print("Enter Elements in descending order:")
    for i in range(n):
        x=int(input(f"Enterelement number{i}: "))
        li.append(x)
    query = int(input("Enter your query number: "))
    print(f"Position of the element is {locate_card(li,query)}")