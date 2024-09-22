a, b, c = gets.chomp.split.map(&:to_i)
chicken, beef, pasta = gets.chomp.split.map(&:to_i)
res = 0

if chicken > a
    res += chicken - a
end

if beef > b
    res += beef - b
end

if pasta > c
    res += pasta - c
end

puts res