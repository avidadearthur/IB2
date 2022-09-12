# IB2 - Iot device

Project done for the class of Engineering Experience II @ Group T - Faculty of Engineering Technology / academic year 2021-22
Alarm Clock & Coffee machine connected with Raspberry Pi.

## Description

Students typically drink a lot of coffee but preparing it in the morning while your housemates try to start their day in the kitchen can be cumbersome. 
If a student could schedule when they want their coffee and just have it there, ready, waiting for them when they wake up, life would be much easier. 
That is exactly what ICoffee proposes to do. This projects has two sides: The alarm clock part, described in this repo and the desktop application part that can
be found [here](https://github.com/avidadearthur/iCoffee).

### Alarm clock
The alarm clock part of the prject contained 4 push buttons:  SET <code>GPIO23</code>, UP <code>GPIO22</code>, DOWN <code>GPIO27</code> and RESET <code>GPIO17</code>. That were acessed by a polling routine that would alter the LCD display within 3 states: <code>0 - Clock Date & Time</code>, <code>1 - Sensors Data</code> and <code>2 - Alarm Set/Alarm Display</code>. 

When in states <code>1</code> and <code>2</code>, the program ran two threads: the Main thread would update the clock in the background and the newly created thread would either display temperature data or allow the user to view/set alarms.

The alarm clock had a LDR and a NTC sensor that were sampled by the <code>MCP3008</code> ADC converter. When it was too dark, the LDR would trigger LEDs 1,2 and 3 to light up and help the user find the interface buttons. The NTC just measured the temperature around the alarm clock.

If activated, the buzzer would start beeping and only stop when the user pressed RESET.
#### Partlist:
```
Exported from Alarm_IB2.sch at 12/21/2021 6:10 PM

EAGLE Version 9.6.2 Copyright (c) 1988-2020 Autodesk, Inc.

Assembly variant: 

Part     Value          Device                Package      Library       Sheet

LCD                     M04                   04P          con-amp-quick 1
LDR1     NSL-PHOTO-TO18 NSL-PHOTO-TO18        NSL-TO18     silonex       1
LED1                    LEDCHIP-LED0805       CHIP-LED0805 led           1
LED2                    LEDCHIP-LED0805       CHIP-LED0805 led           1
LED3                    LEDCHIP-LED0805       CHIP-LED0805 led           1
R1       100            R-EU_R0805            R0805        rcl           1
R2                      V642                  P642         ptc-ntc       1
R3       10k            R-EU_R0805            R0805        rcl           1
R5       10k            R-EU_R0805            R0805        rcl           1
R6       10k            R-EU_R0805            R0805        rcl           1
R7       10k            R-EU_R0805            R0805        rcl           1
R8       10k            R-EU_R0805            R0805        rcl           1
R9       100            R-EU_R0805            R0805        rcl           1
R10      100            R-EU_R0805            R0805        rcl           1
R11      10k            R-EU_R0805            R0805        rcl           1
S1       DTSM-6         DTSM-6                DTSM-6       switch-tact   1
S2       DTSM-6         DTSM-6                DTSM-6       switch-tact   1
S3       DTSM-6         DTSM-6                DTSM-6       switch-tact   1
S4       DTSM-6         DTSM-6                DTSM-6       switch-tact   1
SL1                     M02                   02P          con-amp-quick 1
U1                      MICROCHIP_MCP3008-I-P SO-16        P             1
X1       057-040-1      057-040-1             057-040-1    con-panduit   1
```
#### Schematic:
<img src="https://github.com/avidadearthur/IB2/blob/master/images/alarm_IB2_sch.png"></img>
#### Board:
<img src="https://github.com/avidadearthur/IB2/blob/master/images/alarm_IB2_brd.png">
#### Functionality demo during test phase:
[![thumbnail](https://github.com/avidadearthur/IB2/blob/master/images/alarm_demo_thumbnail.jpg](https://youtu.be/fZlkzTX5OxE)
