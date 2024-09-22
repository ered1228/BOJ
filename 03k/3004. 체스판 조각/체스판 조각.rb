n = gets.chomp.to_i
if (n % 2) == 0
    puts ((n/2)+1)*((n/2)+1)
else
    if n == 1
        puts 2
    else
        n -= 1
        puts ((n/2)+1)*((n/2)+2)
    end
end 