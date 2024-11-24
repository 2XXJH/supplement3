def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32



def test_should_return_celsius_to_fahrenheit():
    celsius = 25
    fahrenheit = celsius_to_fahrenheit(celsius)
    assert fahrenheit == 77 


