#!/usr/bin/python3
from skidl import *

# local parts
local = SchLib(name='local')

# LD112 linear regulator
ldl112 = Part(name='LDL112_SO8', tool=SKIDL, dest=TEMPLATE)
ldl112.ref_prefix = 'VR'
ldl112.description = '1.2 A low quiescent current LDO'
ldl112 += Pin(num=1, name='VOUT', func=Pin.PWROUT)
ldl112 += Pin(num=2, name='GND', func=Pin.PWRIN)
ldl112 += Pin(num=3, name='GND', func=Pin.PWRIN)
ldl112 += Pin(num=4, name='VIN', func=Pin.PWRIN)
ldl112 += Pin(num=5, name='EN', func=Pin.INPUT)
ldl112 += Pin(num=6, name='GND', func=Pin.PWRIN)
ldl112 += Pin(num=7, name='GND', func=Pin.PWRIN)
ldl112 += Pin(num=8, name='NC', func=Pin.NOCONNECT)
local += ldl112

W65C816S = Part(name='W65C816S_PLCC', tool=SKIDL, dest=TEMPLATE)
W65C816S.ref_prefix = 'U'
W65C816S.description = 'W65C816S 8/16–bit Microprocessor'
W65C816S += Pin(num='1', name='VSS', func=Pin.PWRIN)
W65C816S += Pin(num='2', name='VPB', func=Pin.OUTPUT)
W65C816S += Pin(num='3', name='RDY', func=Pin.BIDIR)
W65C816S += Pin(num='4', name='ABORTB', func=Pin.INPUT)
W65C816S += Pin(num='5', name='IRQB', func=Pin.INPUT)
W65C816S += Pin(num='6', name='MLB', func=Pin.OUTPUT)
W65C816S += Pin(num='7', name='NMIB', func=Pin.INPUT)
W65C816S += Pin(num='8', name='VPA', func=Pin.OUTPUT)
W65C816S += Pin(num='9', name='VDD', func=Pin.PWRIN)
W65C816S += Pin(num='10', name='A0', func=Pin.OUTPUT)
W65C816S += Pin(num='11', name='A1', func=Pin.OUTPUT)
W65C816S += Pin(num='12', name='NC', func=Pin.NOCONNECT)
W65C816S += Pin(num='13', name='A2', func=Pin.OUTPUT)
W65C816S += Pin(num='14', name='A3', func=Pin.OUTPUT)
W65C816S += Pin(num='15', name='A4', func=Pin.OUTPUT)
W65C816S += Pin(num='16', name='A5', func=Pin.OUTPUT)
W65C816S += Pin(num='17', name='A6', func=Pin.OUTPUT)
W65C816S += Pin(num='18', name='A7', func=Pin.OUTPUT)
W65C816S += Pin(num='19', name='A8', func=Pin.OUTPUT)
W65C816S += Pin(num='20', name='A9', func=Pin.OUTPUT)
W65C816S += Pin(num='21', name='A10', func=Pin.OUTPUT)
W65C816S += Pin(num='22', name='A11', func=Pin.OUTPUT)
W65C816S += Pin(num='23', name='VSS', func=Pin.PWRIN)
W65C816S += Pin(num='24', name='VSS', func=Pin.PWRIN)
W65C816S += Pin(num='25', name='A12', func=Pin.OUTPUT)
W65C816S += Pin(num='26', name='A13', func=Pin.OUTPUT)
W65C816S += Pin(num='27', name='A14', func=Pin.OUTPUT)
W65C816S += Pin(num='28', name='A15', func=Pin.OUTPUT)
W65C816S += Pin(num='29', name='D7', func=Pin.TRISTATE)
W65C816S += Pin(num='30', name='D6', func=Pin.TRISTATE)
W65C816S += Pin(num='31', name='D5', func=Pin.TRISTATE)
W65C816S += Pin(num='32', name='D4', func=Pin.TRISTATE)
W65C816S += Pin(num='33', name='D3', func=Pin.TRISTATE)
W65C816S += Pin(num='34', name='D2', func=Pin.TRISTATE)
W65C816S += Pin(num='35', name='D1', func=Pin.TRISTATE)
W65C816S += Pin(num='36', name='D0', func=Pin.TRISTATE)
W65C816S += Pin(num='37', name='VDD', func=Pin.PWRIN)
W65C816S += Pin(num='38', name='RWB', func=Pin.OUTPUT)
W65C816S += Pin(num='39', name='E', func=Pin.OUTPUT)
W65C816S += Pin(num='40', name='BE', func=Pin.INPUT)
W65C816S += Pin(num='41', name='PHI2', func=Pin.INPUT)
W65C816S += Pin(num='42', name='MX', func=Pin.OUTPUT)
W65C816S += Pin(num='43', name='VDA', func=Pin.OUTPUT)
W65C816S += Pin(num='44', name='RESB', func=Pin.INPUT)
local += W65C816S

IS61WV = Part(name='IS61WV', tool=SKIDL, dest=TEMPLATE)
IS61WV.ref_prefix = 'U'
IS61WV.description = 'W65C816S 8/16–bit Microprocessor'
IS61WV += Pin(num='1', name='NC', func=Pin.NOCONNECT)
IS61WV += Pin(num='2', name='NC', func=Pin.NOCONNECT)
IS61WV += Pin(num='3', name='A0', func=Pin.INPUT)
IS61WV += Pin(num='4', name='A1', func=Pin.INPUT)
IS61WV += Pin(num='5', name='A2', func=Pin.INPUT)
IS61WV += Pin(num='6', name='A3', func=Pin.INPUT)
IS61WV += Pin(num='7', name='A4', func=Pin.INPUT)
IS61WV += Pin(num='8', name='CE_B', func=Pin.INPUT)
IS61WV += Pin(num='9', name='IO0', func=Pin.TRISTATE)
IS61WV += Pin(num='10', name='IO1', func=Pin.TRISTATE)
IS61WV += Pin(num='11', name='Vdd', func=Pin.PWRIN)
IS61WV += Pin(num='12', name='GND', func=Pin.PWRIN)
IS61WV += Pin(num='13', name='IO2', func=Pin.TRISTATE)
IS61WV += Pin(num='14', name='IO3', func=Pin.TRISTATE)
IS61WV += Pin(num='15', name='WE_B', func=Pin.INPUT)
IS61WV += Pin(num='16', name='A5', func=Pin.INPUT)
IS61WV += Pin(num='17', name='A6', func=Pin.INPUT)
IS61WV += Pin(num='18', name='A7', func=Pin.INPUT)
IS61WV += Pin(num='19', name='A8', func=Pin.INPUT)
IS61WV += Pin(num='20', name='A9', func=Pin.INPUT)
IS61WV += Pin(num='21', name='NC', func=Pin.NOCONNECT)
IS61WV += Pin(num='22', name='NC', func=Pin.NOCONNECT)
IS61WV += Pin(num='23', name='NC', func=Pin.NOCONNECT)
IS61WV += Pin(num='24', name='NC', func=Pin.NOCONNECT)
IS61WV += Pin(num='25', name='NC', func=Pin.NOCONNECT)
IS61WV += Pin(num='26', name='A10', func=Pin.INPUT)
IS61WV += Pin(num='27', name='A11', func=Pin.INPUT)
IS61WV += Pin(num='28', name='A12', func=Pin.INPUT)
IS61WV += Pin(num='29', name='A13', func=Pin.INPUT)
IS61WV += Pin(num='30', name='A14', func=Pin.INPUT)
IS61WV += Pin(num='31', name='IO4', func=Pin.TRISTATE)
IS61WV += Pin(num='32', name='IO5', func=Pin.TRISTATE)
IS61WV += Pin(num='33', name='Vdd', func=Pin.PWRIN)
IS61WV += Pin(num='34', name='GND', func=Pin.PWRIN)
IS61WV += Pin(num='35', name='IO6', func=Pin.TRISTATE)
IS61WV += Pin(num='36', name='IO7', func=Pin.TRISTATE)
IS61WV += Pin(num='37', name='OE_B', func=Pin.INPUT)
IS61WV += Pin(num='38', name='A15', func=Pin.INPUT)
IS61WV += Pin(num='39', name='A16', func=Pin.INPUT)
IS61WV += Pin(num='40', name='A17', func=Pin.INPUT)
IS61WV += Pin(num='41', name='A18', func=Pin.INPUT)
IS61WV += Pin(num='42', name='NC', func=Pin.NOCONNECT)
IS61WV += Pin(num='43', name='NC', func=Pin.NOCONNECT)
IS61WV += Pin(num='44', name='NC', func=Pin.NOCONNECT)
local += IS61WV

W65C22S = Part(name='W65C22S_PLCC', tool=SKIDL, dest=TEMPLATE)
W65C22S.ref_prefix = 'U'
W65C22S.description = 'Versatile Interface Adapter (VIA)'
W65C22S += Pin(num='1', name='VSS', func=Pin.PWRIN)
W65C22S += Pin(num='2', name='PA0', func=Pin.BIDIR)
W65C22S += Pin(num='3', name='PA1', func=Pin.BIDIR)
W65C22S += Pin(num='4', name='PA2', func=Pin.BIDIR)
W65C22S += Pin(num='5', name='PA3', func=Pin.BIDIR)
W65C22S += Pin(num='6', name='PA4', func=Pin.BIDIR)
W65C22S += Pin(num='7', name='PA5', func=Pin.BIDIR)
W65C22S += Pin(num='8', name='PA6', func=Pin.BIDIR)
W65C22S += Pin(num='9', name='PA7', func=Pin.BIDIR)
W65C22S += Pin(num='10', name='PB0', func=Pin.BIDIR)
W65C22S += Pin(num='11', name='NC', func=Pin.NOCONNECT)
W65C22S += Pin(num='12', name='PB1', func=Pin.BIDIR)
W65C22S += Pin(num='13', name='PB2', func=Pin.BIDIR)
W65C22S += Pin(num='14', name='PB3', func=Pin.BIDIR)
W65C22S += Pin(num='15', name='PB4', func=Pin.BIDIR)
W65C22S += Pin(num='16', name='PB5', func=Pin.BIDIR)
W65C22S += Pin(num='17', name='PB6', func=Pin.BIDIR)
W65C22S += Pin(num='18', name='PB7', func=Pin.BIDIR)
W65C22S += Pin(num='19', name='CB1', func=Pin.BIDIR)
W65C22S += Pin(num='20', name='CB2', func=Pin.BIDIR)
W65C22S += Pin(num='21', name='VDD', func=Pin.PWRIN)
W65C22S += Pin(num='22', name='NC', func=Pin.NOCONNECT)
W65C22S += Pin(num='23', name='IRQB', func=Pin.OUTPUT)
W65C22S += Pin(num='24', name='RWB', func=Pin.INPUT)
W65C22S += Pin(num='25', name='CS2B', func=Pin.INPUT)
W65C22S += Pin(num='26', name='CS1', func=Pin.INPUT)
W65C22S += Pin(num='27', name='PHI2', func=Pin.INPUT)
W65C22S += Pin(num='28', name='D7', func=Pin.BIDIR)
W65C22S += Pin(num='29', name='D6', func=Pin.BIDIR)
W65C22S += Pin(num='30', name='D5', func=Pin.BIDIR)
W65C22S += Pin(num='31', name='D4', func=Pin.BIDIR)
W65C22S += Pin(num='32', name='D3', func=Pin.BIDIR)
W65C22S += Pin(num='33', name='NC', func=Pin.NOCONNECT)
W65C22S += Pin(num='34', name='D2', func=Pin.BIDIR)
W65C22S += Pin(num='35', name='D1', func=Pin.BIDIR)
W65C22S += Pin(num='36', name='D0', func=Pin.BIDIR)
W65C22S += Pin(num='37', name='RESB', func=Pin.INPUT)
W65C22S += Pin(num='38', name='NC', func=Pin.NOCONNECT)
W65C22S += Pin(num='39', name='RS3', func=Pin.INPUT)
W65C22S += Pin(num='40', name='RS2', func=Pin.INPUT)
W65C22S += Pin(num='41', name='RS1', func=Pin.INPUT)
W65C22S += Pin(num='42', name='RS0', func=Pin.INPUT)
W65C22S += Pin(num='43', name='CA2', func=Pin.BIDIR)
W65C22S += Pin(num='44', name='CA1', func=Pin.BIDIR)
local += W65C22S

W65C51N = Part(name='W65C51N_PLCC', tool=SKIDL, dest=TEMPLATE)
W65C51N.ref_prefix = 'U'
W65C51N.description = 'Asynchrones Communications Interface Adapter'
W65C51N += Pin(num='1', name='VSS', func=Pin.PWRIN)
W65C51N += Pin(num='2', name='CS0', func=Pin.INPUT)
W65C51N += Pin(num='3', name='CS1B', func=Pin.INPUT)
W65C51N += Pin(num='4', name='RESB', func=Pin.INPUT)
W65C51N += Pin(num='5', name='RxC', func=Pin.BIDIR)
W65C51N += Pin(num='6', name='XTL1', func=Pin.INPUT)
W65C51N += Pin(num='7', name='XTL0', func=Pin.INPUT)
W65C51N += Pin(num='8', name='RTSB', func=Pin.OUTPUT)
W65C51N += Pin(num='9', name='CTSB', func=Pin.INPUT)
W65C51N += Pin(num='10', name='TxD', func=Pin.OUTPUT)
W65C51N += Pin(num='11', name='DTRB', func=Pin.OUTPUT)
W65C51N += Pin(num='12', name='RxD', func=Pin.INPUT)
W65C51N += Pin(num='13', name='RS0', func=Pin.INPUT)
W65C51N += Pin(num='14', name='RS1', func=Pin.INPUT)
W65C51N += Pin(num='15', name='VDD', func=Pin.PWRIN)
W65C51N += Pin(num='16', name='DCDB', func=Pin.INPUT)
W65C51N += Pin(num='17', name='DSRB', func=Pin.INPUT)
W65C51N += Pin(num='18', name='D0', func=Pin.BIDIR)
W65C51N += Pin(num='19', name='D1', func=Pin.BIDIR)
W65C51N += Pin(num='20', name='D2', func=Pin.BIDIR)
W65C51N += Pin(num='21', name='D3', func=Pin.BIDIR)
W65C51N += Pin(num='22', name='D4', func=Pin.BIDIR)
W65C51N += Pin(num='23', name='D5', func=Pin.BIDIR)
W65C51N += Pin(num='24', name='D6', func=Pin.BIDIR)
W65C51N += Pin(num='25', name='D7', func=Pin.BIDIR)
W65C51N += Pin(num='26', name='IRQB', func=Pin.OUTPUT)
W65C51N += Pin(num='27', name='PHI2', func=Pin.INPUT)
W65C51N += Pin(num='28', name='RWB', func=Pin.INPUT)
local += W65C51N
