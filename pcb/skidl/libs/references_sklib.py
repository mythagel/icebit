from skidl import Pin, Part, SchLib, SKIDL, TEMPLATE

SKIDL_lib_version = '0.0.1'

references = SchLib(tool=SKIDL).add_parts(*[
        Part(name='CJ432',dest=TEMPLATE,tool=SKIDL,keywords='diode device shunt regulator',description='Shunt Regulator, SOT-23',ref_prefix='D',num_units=1,fplist=['SOT*23*'],do_erc=True,pins=[
            Pin(num='1',name='REF',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='K',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='A',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='ISL21070DIH306Z-TK',dest=TEMPLATE,tool=SKIDL,keywords='Micropower Voltage Reference 0.6V',description='ISL201070 Series, 0.6V 25μA Micropower Voltage Reference, SOT-23',ref_prefix='U',num_units=1,fplist=['SOT-23*'],do_erc=True,aliases=['ISL21070CIH320Z-TK', 'ISL21070CIH325Z-TK'],pins=[
            Pin(num='1',name='Vin',func=Pin.PWRIN,do_erc=True),
            Pin(num='2',name='Vout',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='GND',func=Pin.PWRIN,do_erc=True)]),
        Part(name='LM134H/NOPB',dest=TEMPLATE,tool=SKIDL,keywords='Adjustable Current Source 10mA',description='LM134H, 1μA to 10mA 3-Terminal Adjustable Current Source, TO-46',ref_prefix='U',num_units=1,fplist=['TO?46*'],do_erc=True,pins=[
            Pin(num='1',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='~',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='LM285D-1.2',dest=TEMPLATE,tool=SKIDL,keywords='diode device voltage reference',description='2.500V Micropower Voltage Reference Diodes, SO-8',ref_prefix='D',num_units=1,fplist=['SOIC*3.9x4.9m*_Pitch1.27mm*'],do_erc=True,aliases=['LM285D-2.5', 'LM385D-1.2', 'LM385D-2.5'],pins=[
            Pin(num='1',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='2',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='3',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='4',name='A',func=Pin.PASSIVE,do_erc=True),
            Pin(num='5',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='6',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='7',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='8',name='K',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='LM285M-ADJ',dest=TEMPLATE,tool=SKIDL,keywords='diode device voltage reference',description='Adjustable Micropower Voltage Reference Diodes, SO-8',ref_prefix='D',num_units=1,fplist=['SOIC*3.9x4.9m*_Pitch1.27mm*'],do_erc=True,aliases=['LM385M-ADJ'],pins=[
            Pin(num='1',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='2',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='3',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='4',name='A',func=Pin.PASSIVE,do_erc=True),
            Pin(num='5',name='FB',do_erc=True),
            Pin(num='6',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='7',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='8',name='K',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='LM285S-1.2',dest=TEMPLATE,tool=SKIDL,keywords='diode device voltage reference',description='2.500V Micropower Voltage Reference Diodes, SO-8',ref_prefix='D',num_units=1,fplist=['SOIC*3.9x4.9m*_Pitch1.27mm*'],do_erc=True,aliases=['LM385S-1.2', 'LM285S-2.5', 'LM385S-2.5'],pins=[
            Pin(num='1',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='2',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='3',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='4',name='A',func=Pin.PASSIVE,do_erc=True),
            Pin(num='5',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='6',name='K',func=Pin.PASSIVE,do_erc=True),
            Pin(num='7',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='8',name='K',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='LM285Z-2.5',dest=TEMPLATE,tool=SKIDL,keywords='diode device voltage reference',description='1.235V Micropower Voltage Reference Diodes, TO-92',ref_prefix='D',num_units=1,fplist=['TO?92*'],do_erc=True,aliases=['LM285Z-1.2', 'LM385Z-1.2', 'LM358Z-2.5', 'LM385BZ-2.5', 'LM385BZ-1.2'],pins=[
            Pin(num='1',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='2',name='K',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='A',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='LM285Z-ADJ',dest=TEMPLATE,tool=SKIDL,keywords='diode device voltage reference',description='Adjustable Micropower Voltage Reference Diodes, TO-92',ref_prefix='D',num_units=1,fplist=['TO?92*'],do_erc=True,aliases=['LM385Z-ADJ'],pins=[
            Pin(num='1',name='FB',do_erc=True),
            Pin(num='2',name='K',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='A',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='LM334M/NOPB',dest=TEMPLATE,tool=SKIDL,keywords='Adjustable Current Source 10mA',description='LM334M, 1μA to 10mA 3-Terminal Adjustable Current Source, SO-8',ref_prefix='U',num_units=1,fplist=['SOIC*3.9x4.9m*_Pitch1.27mm*'],do_erc=True,pins=[
            Pin(num='1',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='4',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='5',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='6',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='7',name='~',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='LM334SM/NOPB',dest=TEMPLATE,tool=SKIDL,keywords='Adjustable Current Source 10mA',description='LM334SM, 1μA to 10mA 3-Terminal Adjustable Current Source, SO-8 Alternate',ref_prefix='U',num_units=1,fplist=['SOIC*3.9x4.9m*_Pitch1.27mm*'],do_erc=True,pins=[
            Pin(num='1',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='~',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='LM334Z/NOPB',dest=TEMPLATE,tool=SKIDL,keywords='Adjustable Current Source 10mA',description='LM334Z, 1μA to 10mA 3-Terminal Adjustable Current Source, TO-92',ref_prefix='U',num_units=1,fplist=['TO?92*'],do_erc=True,aliases=['LM334Z/LFT1', 'LM234Z-3/NOPB', 'LM234Z-6/NOPB'],pins=[
            Pin(num='1',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='~',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='LM4030-4.096',dest=TEMPLATE,tool=SKIDL,keywords='diode device voltage reference shunt',description='4.096V Ultra-High Precision Shunt Voltage Reference, SOT-23-5',ref_prefix='D',num_units=1,fplist=['SOT?23*'],do_erc=True,aliases=['LM4030-2.5'],pins=[
            Pin(num='1',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='2',name='NC_GND',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='3',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='4',name='K',func=Pin.PASSIVE,do_erc=True),
            Pin(num='5',name='A',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='LM4040DBZ-2.0',dest=TEMPLATE,tool=SKIDL,keywords='diode device voltage reference shunt',description='8.192V Precision Micropower Shunt Voltage Reference, SOT-23',ref_prefix='D',num_units=1,fplist=['SOT?*23'],do_erc=True,aliases=['LM4040DBZ-2.5', 'LM4040DBZ-3', 'LM4040DBZ-4.1', 'LM4040DBZ-5', 'LM4040DBZ-8.2', 'LM4040DBZ-10'],pins=[
            Pin(num='1',name='K',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='A',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='NC',func=Pin.NOCONNECT,do_erc=True)]),
        Part(name='LM4040DCK-2.0',dest=TEMPLATE,tool=SKIDL,keywords='diode device voltage reference shunt',description='8.192V Precision Micropower Shunt Voltage Reference, SC-70',ref_prefix='D',num_units=1,fplist=['SC?70*'],do_erc=True,aliases=['LM4040DCK-2.5', 'LM4040DCK-3', 'LM4040DCK-4.1', 'LM4040DCK-5', 'LM4040DCK-8.2', 'LM4040DCK-10'],pins=[
            Pin(num='1',name='A',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='3',name='K',func=Pin.PASSIVE,do_erc=True),
            Pin(num='4',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='5',name='NC',func=Pin.NOCONNECT,do_erc=True)]),
        Part(name='LM4040LP-2.0',dest=TEMPLATE,tool=SKIDL,keywords='diode device voltage reference shunt',description='8.192V Precision Micropower Shunt Voltage Reference, TO-92',ref_prefix='D',num_units=1,fplist=['TO?92*'],do_erc=True,aliases=['LM4040LP-2.5', 'LM4040LP-3', 'LM4040LP-4.1', 'LM4040LP-5', 'LM4040LP-8.2', 'LM4040LP-10'],pins=[
            Pin(num='1',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='2',name='K',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='A',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='LM4125AIM5-2.5/NOPB',dest=TEMPLATE,tool=SKIDL,keywords='Precision Micropower Low Dropout Voltage Reference 2.5V',description='LM4125-2.5, 2.5V ±0.5% Precision Micropower Low Dropout Voltage Reference, SOT-23-5',ref_prefix='U',num_units=1,fplist=['SOT-23*'],do_erc=True,aliases=['LM4125IM5-2.0/NOPB', 'LM4125IM5-2.5/NOPB'],pins=[
            Pin(num='1',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='2',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='3',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='4',name='Vin',func=Pin.PASSIVE,do_erc=True),
            Pin(num='5',name='Vout',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='LT6657AHMS8-2.5',dest=TEMPLATE,tool=SKIDL,keywords='voltage reference vref',description='Precision voltage reference, 40V input, 10mA output, 3.0ppm/C drift, 5.0V output',ref_prefix='U',num_units=1,fplist=['MSOP*3x3mm*Pitch0.65mm*'],do_erc=True,aliases=['LT6657BHMS8-2.5', 'LT6657AHMS8-3', 'LT6657BHMS8-3', 'LT6657AHMS8-5', 'LT6657BHMS8-5'],pins=[
            Pin(num='1',name='DNC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='2',name='Vin',func=Pin.PWRIN,do_erc=True),
            Pin(num='3',name='~SHDN',do_erc=True),
            Pin(num='4',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='5',name='DNC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='6',name='OUT',func=Pin.PWROUT,do_erc=True),
            Pin(num='7',name='DNC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='8',name='DNC',func=Pin.NOCONNECT,do_erc=True)]),
        Part(name='MAX6100',dest=TEMPLATE,tool=SKIDL,keywords='voltage reference ldo',description='Low-dropout high current voltage reference, 4.500V, ±0.4% accuracy, SOT-23 package',ref_prefix='U',num_units=1,fplist=['SOT-23*'],do_erc=True,aliases=['MAX6101', 'MAX6102', 'MAX6103', 'MAX6104', 'MAX6105', 'MAX6106', 'MAX6107'],pins=[
            Pin(num='1',name='IN',func=Pin.PWRIN,do_erc=True),
            Pin(num='2',name='OUT',func=Pin.PWROUT,do_erc=True),
            Pin(num='3',name='GND',func=Pin.PWRIN,do_erc=True)]),
        Part(name='MCP1525T-I/TO',dest=TEMPLATE,tool=SKIDL,keywords='Voltage Reference 4.096V',description='MCP1541, 4.096V Voltage Reference, TO-92',ref_prefix='U',num_units=1,fplist=['TO-92*'],do_erc=True,aliases=['MCP1541T-I/TO'],pins=[
            Pin(num='1',name='Vin',func=Pin.PWRIN,do_erc=True),
            Pin(num='2',name='Vout',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='VSS',func=Pin.PWRIN,do_erc=True)]),
        Part(name='MCP1525T-I/TT',dest=TEMPLATE,tool=SKIDL,keywords='Voltage Reference 4.096V',description='MCP1541, 4.096V Voltage Reference, SOT-23',ref_prefix='U',num_units=1,fplist=['SOT-23*'],do_erc=True,aliases=['MCP1541-I/TT'],pins=[
            Pin(num='1',name='Vin',func=Pin.PWRIN,do_erc=True),
            Pin(num='2',name='Vout',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='VSS',func=Pin.PWRIN,do_erc=True)]),
        Part(name='REF02AP',dest=TEMPLATE,tool=SKIDL,keywords='Precision Voltage Reference 5V',description='5V ±10mV Precision Voltage Reference, PDIP-8',ref_prefix='U',num_units=1,fplist=['DIP*W7.62mm*'],do_erc=True,aliases=['REF02BP'],pins=[
            Pin(num='1',name='NC',func=Pin.PWRIN,do_erc=True),
            Pin(num='2',name='Vin',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='TEMP',func=Pin.PASSIVE,do_erc=True),
            Pin(num='4',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='5',name='TRIM',func=Pin.PASSIVE,do_erc=True),
            Pin(num='6',name='Vout',func=Pin.PASSIVE,do_erc=True),
            Pin(num='7',name='NC',func=Pin.PWRIN,do_erc=True),
            Pin(num='8',name='NC',func=Pin.PWRIN,do_erc=True)]),
        Part(name='REF02AU',dest=TEMPLATE,tool=SKIDL,keywords='Precision Voltage Reference 5V',description='5V ±10mV Precision Voltage Reference, SO8',ref_prefix='U',num_units=1,fplist=['SOIC*3.9x4.9m*_Pitch1.27mm*'],do_erc=True,aliases=['REF02BU'],pins=[
            Pin(num='1',name='NC',func=Pin.PWRIN,do_erc=True),
            Pin(num='2',name='Vin',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='TEMP',func=Pin.PASSIVE,do_erc=True),
            Pin(num='4',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='5',name='TRIM',func=Pin.PASSIVE,do_erc=True),
            Pin(num='6',name='Vout',func=Pin.PASSIVE,do_erc=True),
            Pin(num='7',name='NC',func=Pin.PWRIN,do_erc=True),
            Pin(num='8',name='NC',func=Pin.PWRIN,do_erc=True)]),
        Part(name='REF102AP',dest=TEMPLATE,tool=SKIDL,keywords='Precision Voltage Reference 10V',description='10V ±2.5mV Precision Voltage Reference, PDIP-8',ref_prefix='U',num_units=1,fplist=['DIP*W7.62mm*'],do_erc=True,aliases=['REF102BP', 'REF102CP'],pins=[
            Pin(num='1',name='NC',func=Pin.PWRIN,do_erc=True),
            Pin(num='2',name='Vin',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='TEMP',func=Pin.PASSIVE,do_erc=True),
            Pin(num='4',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='5',name='TRIM',func=Pin.PASSIVE,do_erc=True),
            Pin(num='6',name='Vout',func=Pin.PASSIVE,do_erc=True),
            Pin(num='7',name='NC',func=Pin.PWRIN,do_erc=True),
            Pin(num='8',name='NR',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='REF102AU',dest=TEMPLATE,tool=SKIDL,keywords='Precision Voltage Reference 10V',description='10V ±2.5mV Precision Voltage Reference, SO8',ref_prefix='U',num_units=1,fplist=['SOIC*3.9x4.9m*_Pitch1.27mm*'],do_erc=True,aliases=['REF102BU', 'REF102CU'],pins=[
            Pin(num='1',name='NC',func=Pin.PWRIN,do_erc=True),
            Pin(num='2',name='Vin',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='TEMP',func=Pin.PASSIVE,do_erc=True),
            Pin(num='4',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='5',name='TRIM',func=Pin.PASSIVE,do_erc=True),
            Pin(num='6',name='Vout',func=Pin.PASSIVE,do_erc=True),
            Pin(num='7',name='NC',func=Pin.PWRIN,do_erc=True),
            Pin(num='8',name='NR',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='REF191',dest=TEMPLATE,tool=SKIDL,description='Precision voltage references 4.096V',ref_prefix='U',num_units=1,fplist=['DIP*W7.62mm*', 'SOIC*3.9x4.9m*_Pitch1.27mm*', 'TSSOP*4.4x3mm*Pitch0.65mm*'],do_erc=True,aliases=['REF192', 'REF193', 'REF194', 'REF195', 'REF196', 'REF198'],pins=[
            Pin(num='1',name='TP',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='2',name='Vin',func=Pin.PWRIN,do_erc=True),
            Pin(num='3',name='~Sleep~',do_erc=True),
            Pin(num='4',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='5',name='TP',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='6',name='Vout',func=Pin.OUTPUT,do_erc=True),
            Pin(num='7',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='8',name='NC',func=Pin.NOCONNECT,do_erc=True)]),
        Part(name='REF3012',dest=TEMPLATE,tool=SKIDL,keywords='voltage reference',description='4.096V 50-ppm/°C Max, 50-μA, CMOS Voltage Reference in SOT-23-3',ref_prefix='U',num_units=1,fplist=['SOT-23*'],do_erc=True,aliases=['REF3020', 'REF3025', 'REF3030', 'REF3033', 'REF3040'],pins=[
            Pin(num='1',name='IN',func=Pin.PWRIN,do_erc=True),
            Pin(num='2',name='OUT',func=Pin.PWROUT,do_erc=True),
            Pin(num='3',name='GND',func=Pin.PWRIN,do_erc=True)]),
        Part(name='REF3212AMDBVREP',dest=TEMPLATE,tool=SKIDL,keywords='Micropower Prevision Voltage Reference 4.096V',description='REF3240A, 4.096V 100μA Micropower Precision Voltage Reference, SOT-23-6',ref_prefix='U',num_units=1,fplist=['SOT-23*'],do_erc=True,aliases=['REF3220AMDBVREP', 'REF3225AMDBVREP', 'REF3230AMDBVREP', 'REF3233AMDBVREP', 'REF3240AMDBVREP'],pins=[
            Pin(num='1',name='GND_F',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='GND_S',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='ENABLE',do_erc=True),
            Pin(num='4',name='IN',func=Pin.PASSIVE,do_erc=True),
            Pin(num='5',name='OUT_S',func=Pin.PASSIVE,do_erc=True),
            Pin(num='6',name='OUT_F',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='REF5020AD',dest=TEMPLATE,tool=SKIDL,keywords='Low Noise Precision Voltage Reference 5V',description='5V 0.05% 10mA Low Noise Precision Voltage Reference, SO8',ref_prefix='U',num_units=1,fplist=['SOIC*3.9x4.9m*_Pitch1.27mm*'],do_erc=True,aliases=['REF5025AD', 'REF5030AD', 'REF5040AD', 'REF5045AD', 'REF5050AD', 'REF5010AD', 'REF5020ID', 'REF5025ID', 'REF5030ID', 'REF5040ID', 'REF5045ID', 'REF5050ID', 'REF5010ID'],pins=[
            Pin(num='1',name='DNC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='2',name='Vin',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='Temp',func=Pin.PASSIVE,do_erc=True),
            Pin(num='4',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='5',name='Trim/NR',func=Pin.PASSIVE,do_erc=True),
            Pin(num='6',name='Vout',func=Pin.PASSIVE,do_erc=True),
            Pin(num='7',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='8',name='DNC',func=Pin.NOCONNECT,do_erc=True)]),
        Part(name='REF5020ADGK',dest=TEMPLATE,tool=SKIDL,keywords='Low Noise Precision Voltage Reference 5V',description='5V 0.05% 10mA Low Noise Precision Voltage Reference, MSOP-8',ref_prefix='U',num_units=1,fplist=['MSOP*3x3mm*Pitch0.65mm*'],do_erc=True,aliases=['REF5025ADGK', 'REF5030ADGK', 'REF5040ADGK', 'REF5045ADGK', 'REF5050ADGK', 'REF5010ADGK', 'REF5020IDGK', 'REF5025IDGK', 'REF5030IDGK', 'REF5040IDGK', 'REF5045IDGK', 'REF5050IDGK', 'REF5010IDGK'],pins=[
            Pin(num='1',name='DNC',func=Pin.PWRIN,do_erc=True),
            Pin(num='2',name='Vin',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='Temp',func=Pin.PASSIVE,do_erc=True),
            Pin(num='4',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='5',name='Trim/NR',func=Pin.PASSIVE,do_erc=True),
            Pin(num='6',name='Vout',func=Pin.PASSIVE,do_erc=True),
            Pin(num='7',name='NC',func=Pin.PWRIN,do_erc=True),
            Pin(num='8',name='DNC',func=Pin.PWRIN,do_erc=True)]),
        Part(name='TL431D',dest=TEMPLATE,tool=SKIDL,keywords='diode device shunt regulator',description='Shunt Regulator, SO8',ref_prefix='D',num_units=1,fplist=['SOIC*3.9x4.9m*_Pitch1.27mm*'],do_erc=True,pins=[
            Pin(num='1',name='K',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='A',do_erc=True),
            Pin(num='3',name='A',func=Pin.PASSIVE,do_erc=True),
            Pin(num='4',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='5',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='6',name='A',func=Pin.PASSIVE,do_erc=True),
            Pin(num='7',name='A',func=Pin.PASSIVE,do_erc=True),
            Pin(num='8',name='REF',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='TL431DBV',dest=TEMPLATE,tool=SKIDL,keywords='diode device shunt regulator',description='Shunt Regulator, SOT-23-5',ref_prefix='D',num_units=1,fplist=['SOT-23*'],do_erc=True,pins=[
            Pin(num='1',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='2',name='NC_SUBSTRATE',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='3',name='K',func=Pin.PASSIVE,do_erc=True),
            Pin(num='4',name='REF',func=Pin.PASSIVE,do_erc=True),
            Pin(num='5',name='A',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='TL431DBZ',dest=TEMPLATE,tool=SKIDL,keywords='diode device shunt regulator',description='Shunt Regulator, SOT-23',ref_prefix='D',num_units=1,fplist=['SOT*23*'],do_erc=True,pins=[
            Pin(num='1',name='K',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='REF',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='A',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='TL431DCK',dest=TEMPLATE,tool=SKIDL,keywords='diode device shunt regulator',description='Shunt Regulator, SC-70',ref_prefix='D',num_units=1,fplist=['SC-70*'],do_erc=True,pins=[
            Pin(num='1',name='K',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='REF',func=Pin.PASSIVE,do_erc=True),
            Pin(num='6',name='A',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='TL431KTP',dest=TEMPLATE,tool=SKIDL,keywords='diode device shunt regulator',description='Shunt Regulator, TO-252',ref_prefix='D',num_units=1,fplist=['TO*252'],do_erc=True,pins=[
            Pin(num='1',name='REF',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='A',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='K',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='TL431LP',dest=TEMPLATE,tool=SKIDL,keywords='diode device regulator shunt',description='Shunt Regulator, TO-92',ref_prefix='D',num_units=1,fplist=['TO*'],do_erc=True,pins=[
            Pin(num='1',name='REF',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='A',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='K',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='TL431P',dest=TEMPLATE,tool=SKIDL,keywords='diode device shunt regulator',description='Shunt Regulator, PDIP-8',ref_prefix='D',num_units=1,fplist=['DIP*W7.62mm*'],do_erc=True,pins=[
            Pin(num='1',name='K',func=Pin.PASSIVE,do_erc=True),
            Pin(num='6',name='A',func=Pin.PASSIVE,do_erc=True),
            Pin(num='8',name='REF',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='TL431PK',dest=TEMPLATE,tool=SKIDL,keywords='diode device shunt regulator',description='Shunt Regulator, SOT-89',ref_prefix='D',num_units=1,fplist=['SOT*89*'],do_erc=True,pins=[
            Pin(num='1',name='REF',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='A',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='K',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='TL431PS',dest=TEMPLATE,tool=SKIDL,keywords='diode device shunt regulator',description='Shunt Regulator, MSOP-8',ref_prefix='D',num_units=1,fplist=['MSOP*'],do_erc=True,pins=[
            Pin(num='1',name='K',func=Pin.PASSIVE,do_erc=True),
            Pin(num='6',name='A',func=Pin.PASSIVE,do_erc=True),
            Pin(num='8',name='REF',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='TL431PW',dest=TEMPLATE,tool=SKIDL,keywords='diode device shunt regulator',description='Shunt Regulator, TSSOP-8',ref_prefix='D',num_units=1,fplist=['TSSOP*'],do_erc=True,pins=[
            Pin(num='1',name='K',func=Pin.PASSIVE,do_erc=True),
            Pin(num='6',name='A',func=Pin.PASSIVE,do_erc=True),
            Pin(num='8',name='REF',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='TL432DBV',dest=TEMPLATE,tool=SKIDL,keywords='diode device shunt regulator',description='Shunt Regulator, SOT-23-5',ref_prefix='D',num_units=1,fplist=['SOT?23*'],do_erc=True,pins=[
            Pin(num='1',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='2',name='A',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='4',name='K',func=Pin.PASSIVE,do_erc=True),
            Pin(num='5',name='REF',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='TL432DBZ',dest=TEMPLATE,tool=SKIDL,keywords='diode device shunt regulator',description='Shunt Regulator, SOT-23',ref_prefix='D',num_units=1,fplist=['SOT*23*'],do_erc=True,pins=[
            Pin(num='1',name='REF',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='K',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='A',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='TL432PK',dest=TEMPLATE,tool=SKIDL,keywords='diode device shunt regulator',description='Shunt Regulator, SOT-89',ref_prefix='D',num_units=1,fplist=['SOT*89*'],do_erc=True,pins=[
            Pin(num='1',name='K',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='A',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='REF',func=Pin.PASSIVE,do_erc=True)])])