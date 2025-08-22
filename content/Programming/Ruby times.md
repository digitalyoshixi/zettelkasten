---
tags:
  - programming
  - ruby
---
A method to return a iterator for loops within [[Ruby Block]].
Can be captured with a [[Ruby Block Parameter]]
```ruby
5.times do
	puts "Hi"
end

# capturing with block parameter
5.times do |number|
	puts "#(number) echo!"
end
```