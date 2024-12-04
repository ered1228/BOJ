n = gets.chomp.to_i
if n < 4
    puts 0
else
    puts n*(n-1)*(n-2)*(n-3)/24
end