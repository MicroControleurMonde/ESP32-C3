#test_esp32-C3_rng_8k.py
import time
from esp32_c3_rng import ESP32RNG

# Create an instance of the ESP32RNG class
rng = ESP32RNG()

# Number of random values to generate
num_values = 8000

# Start measuring time
start_time = time.time()

print("### Demarage du générateur")
# Generate random values (no need to store them)
for _ in range(num_values):
    rng.generate_random_number()

# Calculate time taken to generate the values
end_time = time.time()
time_taken = end_time - start_time

# Calculate throughput and other metrics
bytes_per_value = 4  # Assuming each random value is a 32-bit integer (4 bytes)
total_bytes = num_values * bytes_per_value
throughput = total_bytes / time_taken  # in bytes/sec
values_per_sec = num_values / time_taken  # number of values/sec

# Display the results
print(f"Time taken to generate {num_values} values: {time_taken:.6f} seconds")
print(f"Throughput: {throughput:.2f} bytes/sec")
print(f"Number of random values per second: {values_per_sec:.2f}")

