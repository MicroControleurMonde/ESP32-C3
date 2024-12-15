# ESP32-C3 RNG
---

![Link](https://github.com/MicroControleurMonde/ESP32_RNG/blob/main/Reports/ESP32download.jpg)

A Micro-python library which provides an interface to generate a random number using the ESP32-C3's hardware RNG.


## Under Construction ...

A Micro-python library which provides an interface to generate a random number using the ESP32-C3's hardware RNG.

The code uses several hardware devices of the MCU to generate random noise values using additional entropy sources. The SAR ADC and Wi-Fi are exploited to provide quality inputs to the hardware random number generator integrated into the ESP32-C3. It reads a random value from the '**RNG_DATA_REG**' register.

This uses the same method to generate random numbers as the ESP32. Only the registry address changes (***0x600260B0***)

- Library : **esp32_c6_rng.py**
- Library test: **test_esp32_c6_rng.py**

Source: ESP32-C3 Technical Reference Manual V.1.1 - Chapter 25 Random Number Generator (RNG) - Pages 528/529 -  [link](https://www.espressif.com/sites/default/files/documentation/esp32-c3_technical_reference_manual_en.pdf)

The ESP32-C6 RNG generates random integer numbers as **32-bit values**.

    Random value #1: 	146820682
    Random value #2: 	-196285670
    Random value #3: 	-866286180
    Random value #4: 	-1000580641
    Random value #5: 	1642066338
    Random value #6: 	-1467530287
    Random value #7: 	-697217448
    Random value #8: 	-1944603219
    Random value #9: 	1952318979
    Random value #10: 	1012424606

## Platform
The code was implemented specifically for an Espressif ESP32-C3 microcontroller on a Seeed Studio XIAO ESP32C3 Module [Link](https://www.seeedstudio.com/Seeed-XIAO-ESP32C3-p-5431.html?srsltid=AfmBOoo0va9xPKzG-zCuRxoFXjVCC8uy9bMNLPEuQdSVxHsAHfRzhXAA)

Esptool indicates ESP32-C3 (QFN32) (revision v0.4)

Quad Flat No-lead 32 pins (QFN32).

    MicroPython v1.22.2 on 2024-02-22; ESP32C3 module with ESP32C3

## Performance

Time taken to generate xxxxxx values: **xx** seconds (avg)

Throughput: **xxxxxx** bytes/sec

**xxxxx** random values / sec.

## Ent Test Report

  ([www.fourmilab.ch](https://www.fourmilab.ch/random/)) John Walker
- Sample size: **xx MB**
- Total generated: **xxxxxx** values

## Dieharder Test Report

(https://webhome.phy.duke.edu/~rgb/General/dieharder.php) Robert G. Brown

Sample size: **xx MB**

Total generated: **xxxxxxx** values
