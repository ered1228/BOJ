a, b, c = gets.chomp.split.map(&:to_i)
if c-b > b-a
    puts c-b-1
else
    puts b-a-1
end
