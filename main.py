def celsius_to_fahrenheit(celsius):
    """
    Convert a temperature from Celsius to Fahrenheit.

    Args:
        celsius (float): The temperature in Celsius.

    Returns:
        float: The temperature in Fahrenheit.
    """
    return (celsius * 9 / 5) + 32
def fahrenheit_to_celsius(fahrenheit):
    """
    Convert a temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit (float): The temperature in Fahrenheit.

    Returns:
        float: The temperature in Celsius.
    """
    return (fahrenheit - 32) * 5 / 9
    
def test_should_return_celsius_to_fahrenheit():
    celsius = 25
    fahrenheit = celsius_to_fahrenheit(celsius)
    assert fahrenheit == 77 

def test_should_return_fahrenheit_to_celsius():
    fahrenheit = 77
    celsius = fahrenheit_to_celsius(fahrenheit)
    assert round(celsius, 2) == 25

def test_should_return_is_even():
    number = 42
    assert is_even(number) is True
