# ESP32-C3 RNG
A Micro-python library which provides an interface to generate a random number using the ESP32-C3's hardware RNG.

![Link](https://github.com/MicroControleurMonde/ESP32_RNG/blob/main/Reports/ESP32download.jpg)

## Under Construction ...

A Micro-python library which provides an interface to generate a random number using the ESP32-C3's hardware RNG.

The code uses several hardware devices of the MCU to generate random noise values using additional entropy sources. The SAR ADC and Wi-Fi are exploited to provide quality inputs to the hardware random number generator integrated into the ESP32-C3. It reads a random value from the '**RNG_DATA_REG**' register.

This uses the same method to generate random numbers as the ESP32. Only the registry address changes (***0x600260B0***)

- Library : esp32_c6_rng.py
- Library test: test_esp32_c6_rng.py
