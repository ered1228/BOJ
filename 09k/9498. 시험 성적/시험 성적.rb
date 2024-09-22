score = gets.chomp.to_i
if score >= 90
    print('A')
elsif score >= 80
    print('B')
elsif score >= 70
    print('C')
elsif score >= 60
    print('D')
else
    print('F')
end