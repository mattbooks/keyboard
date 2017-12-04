DEVICE = atmega32u4
MCU = atmega32u4

TEST_CFLAGS=-g -Wall
CFLAGS=-g -Wall -mcall-prologues -mmcu=$(MCU) $(DEVICE_SPECIFIC_CFLAGS) -Os -DUART_RX0_BUFFER_SIZE=256 -DUART_TX0_BUFFER_SIZE=256
CC=avr-gcc
OBJ2HEX=avr-objcopy
LDFLAGS=-Wl,-gc-sections -Wl,-relax

PORT ?= usb
TARGET=blinky
DEPS=$(wildcard *.h) $(wildcard lib/*.h)
SOURCES=$(wildcard *.c) $(wildcard lib/*.c)
TEST_SOURCES=$(wildcard tst/*.c) lib/time.c
TEST_DEPS=$(wildcard tst/*.h) lib/time.h

all: $(TARGET).hex

clean:
	rm -f *.o *.hex *.obj

%.hex: %.obj
	$(OBJ2HEX) -R .eeprom -O ihex $< $@

%.obj: $(SOURCES) $(DEPS)
	$(CC) $(CFLAGS) $^ $(LDFLAGS) -o $@

program: $(TARGET).hex
	$(AVRDUDE) -p $(AVRDUDE_DEVICE) -c usbtiny -P $(PORT) -U flash:w:$(TARGET).hex

test: $(TEST_SOURCES) $(TEST_DEPS)
	gcc $(TEST_CFLAGS) $(LDFLAGS) $^ -o test

