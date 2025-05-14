class TemperatureConverter:
    
    @staticmethod
    def celsius_to_fahrenheit(c):
        # Static method to convert Celsius to Fahrenheit
        return (c * 9/5) + 32

# Example usage
celsius = 25
fahrenheit = TemperatureConverter.celsius_to_fahrenheit(celsius)

print(f"{celsius}°C is equal to {fahrenheit}°F")
