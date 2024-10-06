a, b, c = gets.chomp.split.map(&:to_i)
if b >= c
    puts -1
else
    if a % (c-b) == 0
        n = a / (c-b)
        n += 1
        puts n
    else
        n = (a.to_f / (c-b)).ceil
        puts n
    end
end