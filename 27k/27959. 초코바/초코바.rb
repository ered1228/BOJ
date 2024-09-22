n, m = gets.chomp.split.map(&:to_i)
if n*100 >= m
    puts "Yes"
else
    puts "No"
end