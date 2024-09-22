n = gets.chomp.to_i
res = 0

while n > 0
    pepper = gets.chomp
    if pepper == 'Poblano'
        res += 1500
    elsif pepper == 'Mirasol'
        res += 6000
    elsif pepper == 'Serrano'
        res += 15500
    elsif pepper == 'Cayenne'
        res += 40000
    elsif pepper == 'Thai'
        res += 75000
    else
        res += 125000
    end
    n -= 1
end

puts res