def get_count(input_str):
	count = 0
	vowels = "aeiou"
	for char in input_str:
		if char in vowels:
			count +=1
		return count
print(get_count("Hello world"))