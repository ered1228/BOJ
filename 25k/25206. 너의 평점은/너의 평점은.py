total_credit = 0
total_grade = 0
for _ in range(20):
    sub, credit, grade = input().split()
    if grade == 'A+':
        credit = float(credit)
        total_credit += credit
        total_grade += 4.5 * credit
    elif grade == 'A0':
        credit = float(credit)
        total_credit += credit
        total_grade += 4.0 * credit
    elif grade == 'B+':
        credit = float(credit)
        total_credit += credit
        total_grade += 3.5 * credit
    elif grade == 'B0':
        credit = float(credit)
        total_credit += credit
        total_grade += 3.0 * credit
    elif grade == 'C+':
        credit = float(credit)
        total_credit += credit
        total_grade += 2.5 * credit
    elif grade == 'C0':
        credit = float(credit)
        total_credit += credit
        total_grade += 2.0 * credit
    elif grade == 'D+':
        credit = float(credit)
        total_credit += credit
        total_grade += 1.5 * credit
    elif grade == 'D0':
        credit = float(credit)
        total_credit += credit
        total_grade += 1.0 * credit
    elif grade == 'F':
        credit = float(credit)
        total_credit += credit
print(format(total_grade / total_credit, ".6f"))