from celsius_fahrenheit import celsius_to_fahrenheit
def test_default():
 assert celsius_to_fahrenheit() == "Temperature in Fahrenheit: 32.0"
def test_zero():
 assert celsius_to_fahrenheit(0) == "Temperature in Fahrenheit: 32.0"
def test_positive():
 assert celsius_to_fahrenheit(100) == "Temperature in Fahrenheit: 212.0"
