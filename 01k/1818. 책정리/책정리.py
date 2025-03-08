from bisect import bisect_left

n = int(input())
books = [0] + list(map(int, input().split()))
mv = [0]

for i in range(1, n+1):
    book = books[i]
    idx = bisect_left(mv, book)
    if idx == len(mv):
        mv.append(book)
    else:
        mv[idx] = book

print(n-len(mv)+1)