a, b, c = gets.chomp.split.map(&:to_i)
result = (a * c.to_f) / b.to_f
puts format("%.6f", result)

