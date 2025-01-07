t = int(input())
for _ in range(t):
    n = int(input())
    clothes = dict()
    for _ in range(n):
        item, category = input().split()
        if category not in clothes:
            clothes[category] = set()    
        clothes[category].add(item)
    res = 1
    for key, val in clothes.items():
        res *= len(val)+1
    print(res-1)