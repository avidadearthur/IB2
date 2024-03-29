# IB2 - Iot device

Project done for the class of Engineering Experience II @ Group T - Faculty of Engineering Technology / academic year 2021-22
Alarm Clock & Coffee machine connected with Raspberry Pi.

### Software Contribution:
* [@avidadearthur](https://github.com/avidadearthur)
* [@kamielsabo](https://github.com/kamielsabo)
### Hardware Contribution:
* [@avidadearthur](https://github.com/avidadearthur)
* [@kamielsabo](https://github.com/kamielsabo)
* Tomas Vermeulen
* Ruben Nuyes
* Lotte Kesteleyn
* Aymeric Baume

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
#### [Functionality demo during test phase](https://www.youtube.com/watch?v=fZlkzTX5OxE)
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
<img src="https://github.com/avidadearthur/IB2/blob/master/images/alarm_IB2_brd.png"></img>

### Coffee Machine 
For this part of the project a [Tristar coffee maker](https://www.tradeinn.com/techinn/en/tristar-cm1246-600w-drip-coffee-maker/137743253/p) was used. The ON/OFF switch was controlled with a PWM servo motor and the amount of water in the coffee machine was controlled by a pump. Under the coffee jar there was an NTC resistor to estimate the coffee temperature. All the Sensors and actuators were controlled by a Raspberry Pi that executed the coffee orders comming from a Database. Every order included the datetime info, desired volume of coffee (cl) and desired temperature (hot, medium or cold).

The coffee make module could be controlled either by the alarm clock (described above), or by the Java desktop application explained [here](https://github.com/avidadearthur/iCoffee). 

#### [Functionality demo during test phase](https://youtu.be/fZkqSkyJ20Q)
#### Partlist:
```
Exported from Coffee_IB2.sch at 26/12/2021 11:54

EAGLE Version 9.5.2 Copyright (c) 1988-2019 Autodesk, Inc.

Assembly variant: 

Part     Value          Device                Package   Library        Sheet

C3       100nF          C-EUC0805             C0805     rcl            1
C4       100 nF         C-EUC0805             C0805     rcl            1
D3                      DIODE-DO-214AC        DO-214AC  diode          1
IC2      MCP6002        MCP602SN              SO08      linear         1
PUMP                    M02                   02P       con-amp-quick  1
Q1       BC817-25SMD    BC817-25SMD           SOT23-BEC transistor-npn 1
R1       100            R-EU_R0805            R0805     rcl            1
R3                      V642                  P642      ptc-ntc        1
R8       10k            R-EU_R0805            R0805     rcl            1
R9       10k            R-EU_R0805            R0805     rcl            1
SL2                     M03                   03P       con-amp-quick  1
SL3                     M02                   02P       con-amp-quick  1
U2                      MICROCHIP_MCP3008-I-P SO-16     P              1
X1       057-040-1      057-040-1             057-040-1 con-panduit    1
```
#### Schematic:
<img src="https://github.com/avidadearthur/IB2/blob/master/images/coffee_IB2_sch.png"></img>
#### Board:
<img src="https://github.com/avidadearthur/IB2/blob/master/images/coffee_IB2_brd.png"></img>
