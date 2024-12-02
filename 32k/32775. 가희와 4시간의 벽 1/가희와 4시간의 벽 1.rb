rail = gets.chomp.to_i
flight = gets.chomp.to_i

if flight < rail
    puts 'flight'
else
    puts 'high speed rail'
end