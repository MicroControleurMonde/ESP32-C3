# test_esp32-C3_rng.py

from esp32_c3_rng import ESP32RNG

# Create an instance of the ESP32RNG class
rng = ESP32RNG()

# Generate and display 10 random values
for i in range(10):
    random_value = rng.generate_random_number()
    print(f"Random value #{i + 1}: \t{random_value}")
