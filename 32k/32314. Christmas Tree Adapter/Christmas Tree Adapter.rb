at = gets.chomp.to_i
w, v = gets.chomp.split.map(&:to_i)
aa = w / v

if aa < at
    puts 0
else
    puts 1
end