#include <msp430.h> 

/*
 * Input Switches to Application:
 * 1 - Stove
 * 2 - Lights
 * 3 - Door
 * 4 - Windows
 * 5 - Garage Door
 * 6 -
 * 7 -
 * 8 -
 */

/*
 * Input Switches to Pins:
 * 1 - P6.0
 * 2 - P6.1
 * 3 - P6.2
 * 4 - P6.3
 * 5 - P6.4
 * 6 - P7.0
 * 7 - P3.6
 * 8 - P3.5
 *
 */


int main(void) {
    WDTCTL = WDTPW | WDTHOLD;	// Stop watchdog timer
	
    //Input = 0; Output = 1;
    P6DIR &= 0b11100000;		//Sets certain pins to be inputs
    P7DIR &= 0b11111110;
    P3DIR &= 0b00000000;

    if ()	//Test to check if the input switches work




	return 0;
}
