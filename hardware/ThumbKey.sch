EESchema Schematic File Version 2
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:keyboard-cache
EELAYER 26 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 63 66
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
Text HLabel 2150 1550 0    60   Input ~ 0
ROW
Text HLabel 2150 1800 0    60   Input ~ 0
COL
$Comp
L SPST S61
U 1 1 5950FE13
P 2400 1550
AR Path="/5947FBED/5950DE0D/5950FE13" Ref="S61"  Part="1" 
AR Path="/5947FBED/59511757/5950FE13" Ref="S62"  Part="1" 
AR Path="/5947FBED/59512178/5950FE13" Ref="S63"  Part="1" 
AR Path="/5947FBED/595128C4/5950FE13" Ref="S64"  Part="1" 
F 0 "S64" H 2650 1500 60  0000 R CNN
F 1 "SPST" H 2250 1500 60  0000 C CNN
F 2 "keyboard-modules:CHERRY_PCB_200V" H 2400 1650 60  0001 C CNN
F 3 "" H 2400 1650 60  0001 C CNN
	1    2400 1550
	1    0    0    -1  
$EndComp
$Comp
L D_Small D61
U 1 1 5950FE1A
P 2400 1800
AR Path="/5947FBED/5950DE0D/5950FE1A" Ref="D61"  Part="1" 
AR Path="/5947FBED/59511757/5950FE1A" Ref="D62"  Part="1" 
AR Path="/5947FBED/59512178/5950FE1A" Ref="D63"  Part="1" 
AR Path="/5947FBED/595128C4/5950FE1A" Ref="D64"  Part="1" 
F 0 "D64" H 2350 1880 50  0000 L CNN
F 1 "D_Small" H 2250 1720 50  0000 L CNN
F 2 "Diodes_SMD:D_SOD-123" V 2400 1800 50  0001 C CNN
F 3 "" V 2400 1800 50  0001 C CNN
	1    2400 1800
	1    0    0    -1  
$EndComp
Wire Wire Line
	2150 1800 2300 1800
Wire Wire Line
	2650 1550 2700 1550
Wire Wire Line
	2700 1550 2700 1800
Wire Wire Line
	2700 1800 2500 1800
$EndSCHEMATC
