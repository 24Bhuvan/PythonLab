def linear_search(li,query):
    position = 0
    while True:
        if li[position]==query:
            return position
            break
        position +=1
        if position == len(li):
            return -1
test ={"input":{
    "li":[13,11,10,7,4,3,1,0],
    "query":7},
    "output":3}
result = linear_search(test["input"]["li"],test["input"]["query"])
if result == test["output"] : print(result)