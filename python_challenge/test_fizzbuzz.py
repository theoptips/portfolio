import fizzbuzz
#unit test with pytest

def test_fizzbuzz():
	result = fizzbuzz.fizzbuzz(300)
	assert result == "FizzBuzz"

	result = fizzbuzz.fizzbuzz(35)
	assert result == "Buzz"
	
