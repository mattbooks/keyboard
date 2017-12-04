#define F_CPU 2000000UL // 16 MHz clock speed

#include <avr/io.h>
#include <util/delay.h>
#include "i2cmaster.h"

int main(void)
{
  DDRB = 0xFF; //Nakes PORTC as Output
	PORTB = 0xFF; //Turns ON All LEDs

  DDRD = 0xFF;
  PORTD = 0;

	PORTB &= ~(1<<5); //Turns ON All LEDs

  while(1) //infinite loop
  {
		PORTB = 0x00;
		_delay_ms(1000);
		PORTB = 0xFF;
		_delay_ms(1000);
  }
}
