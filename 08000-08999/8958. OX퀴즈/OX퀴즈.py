import sys
input = sys.stdin.readline

T = int(input())

def score_of_quiz(quiz):
    c = quiz.count('O')
    if c == 0:
        score = 0
        return score
    else:
        score = 1
        cnt = 1
        firstOinx = quiz.index('O')
        for i in range(firstOinx, len(quiz)-1):
            tmp = quiz[i+1]
            if tmp == 'O':
                cnt += 1
                score += cnt
            else:
                cnt = 0
        return score

for _ in range(T):
    quiz = str(input())
    print(score_of_quiz(quiz))