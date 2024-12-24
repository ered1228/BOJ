import sys
input = sys.stdin.readline

def poker(a, b, c, d, e, f):
    C = [a, b, c, d, e, f]
    d = dict()
    for card in C:
      if card in d:
        d[card] += 1
      else:
        d[card] = 1
    d = list(sorted(d.items(), key=lambda item: item[1], reverse=True))
    if len(d) == 2:
      if d[0][1] == 3:
        return "two triples"
      else:
        return "tiki pair"
    elif len(d) == 3:
      if d[0][1] == 3 and d[1][1] == 2:
        return "full house"
      elif d[0][1] == 2 and d[1][1] == 2:
        return "three pairs"
      else:
        return "tiki"
    elif len(d) == 4:
      if d[0][1] == 3:
        return "one triple"
      elif d[0][1] == 2:
        return "two pairs"
    elif len(d) == 5:
      return "one pair"
    else:
      return "single"

t = int(input())
for _ in range(t):
    a, b, c, d, e, f = map(int, input().rstrip().split())
    print(poker(a, b, c, d, e, f))