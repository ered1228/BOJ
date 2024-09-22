h, m = gets.chomp.split

h = h.to_i
m = m.to_i

time = (h - 9)*60
time += m

puts time