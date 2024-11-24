if __name__ == "__main__":
    def test_should_return_celsius_to_fahrenheit():
    celsius = 25
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is {fahrenheit}°F")
    assert fahrenheit == 77, "Test case for celsius_to_fahrenheit failed!"
