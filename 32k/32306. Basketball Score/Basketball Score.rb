a, b, c = gets.chomp.split.map(&:to_i)
d, e, f = gets.chomp.split.map(&:to_i)
s1 = a*10 + b*20 + c*30
s2 = d*10 + e*20 + f*30
if s1 == s2
    puts 0
elsif s1 > s2
    puts 1
else
    puts 2
end