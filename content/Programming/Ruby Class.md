---
tags:
  - ruby
  - programming
---
Construction of [[Class|Classes]] for [[Ruby]].
By default, it only exports methods.
To export attributes, you must use [[Ruby Attribute Accessors]]
# Boilerplate
```ruby
class myClass
	def initialize(name = "Daniel")
		@name = name
	end
	
	def say_hi
		puts "Hi #(@name)"
	end
end
```