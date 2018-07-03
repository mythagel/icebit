from skidl import Pin, Part, SchLib, SKIDL, TEMPLATE

SKIDL_lib_version = '0.0.1'

ac_dc = SchLib(tool=SKIDL).add_parts(*[
        Part(name='FSDH321',dest=TEMPLATE,tool=SKIDL,keywords='SMPS Controller with MOSFET 17W AC-DC',description='17W SMPS Controller, 50kHz, AC-DC, PDIP-8',ref_prefix='U',num_units=1,fplist=['DIP*', 'PDIP*'],do_erc=True,aliases=['FSDL321'],pins=[
            Pin(num='1',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='2',name='VDD',func=Pin.PWRIN,do_erc=True),
            Pin(num='3',name='FB',do_erc=True),
            Pin(num='4',name='IPK',func=Pin.PASSIVE,do_erc=True),
            Pin(num='5',name='VSTR',func=Pin.PASSIVE,do_erc=True),
            Pin(num='6',name='D',func=Pin.PASSIVE,do_erc=True),
            Pin(num='7',name='D',func=Pin.PASSIVE,do_erc=True),
            Pin(num='8',name='D',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='FSDH321L',dest=TEMPLATE,tool=SKIDL,keywords='SMPS Controller with MOSFET 17W AC-DC',description='17W SMPS Controller, 50kHz, AC-DC, SMD-8',ref_prefix='U',num_units=1,fplist=['SMD*'],do_erc=True,aliases=['FSDL321L'],pins=[
            Pin(num='1',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='2',name='VDD',func=Pin.PWRIN,do_erc=True),
            Pin(num='3',name='FB',do_erc=True),
            Pin(num='4',name='IPK',func=Pin.PASSIVE,do_erc=True),
            Pin(num='5',name='VSTR',func=Pin.PASSIVE,do_erc=True),
            Pin(num='6',name='D',func=Pin.PASSIVE,do_erc=True),
            Pin(num='7',name='D',func=Pin.PASSIVE,do_erc=True),
            Pin(num='8',name='D',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='FSL136MRT',dest=TEMPLATE,tool=SKIDL,keywords='SMPS Controller 50W AC-DC',description='67kHz SMPS Controller w/ Soft Start, max. 50W AC-DC, TO-220F-6L',ref_prefix='U',num_units=1,fplist=['TO-220-6L'],do_erc=True,pins=[
            Pin(num='1',name='D',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='3',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='4',name='FB',func=Pin.PASSIVE,do_erc=True),
            Pin(num='6',name='VST',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='FSQ0565RSWDTU',dest=TEMPLATE,tool=SKIDL,keywords='Quasi Resonant SMPS Controller 80W AC-DC',description='67kHz Quasi Resonant SMPS Controller w/ Soft Start, max. 80W AC-DC, TO-220F-6L',ref_prefix='U',num_units=1,fplist=['TO-220-6L'],do_erc=True,aliases=['FSQ0565RQWDTU', 'FSQ0565RSLDTU', 'FSQ0565RQLDTU'],pins=[
            Pin(num='1',name='D',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='3',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='4',name='FB',func=Pin.PASSIVE,do_erc=True),
            Pin(num='5',name='SYNC',func=Pin.PASSIVE,do_erc=True),
            Pin(num='6',name='VST',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='HS-40003',dest=TEMPLATE,tool=SKIDL,keywords='24V 3W AC-DC module power supply',description='24V, 3W, AC-DC module power supply, Hahn',ref_prefix='U',num_units=1,fplist=['ACDC*Hahn*HS*400XX*'],do_erc=True,aliases=['HS-40005', 'HS-40009', 'HS-40012', 'HS-40015', 'HS-40018', 'HS-40024'],pins=[
            Pin(num='1',name='AC/N',func=Pin.PWRIN,do_erc=True),
            Pin(num='5',name='AC/L',func=Pin.PWRIN,do_erc=True),
            Pin(num='7',name='+Vout',func=Pin.PWROUT,do_erc=True),
            Pin(num='9',name='-Vout',func=Pin.PWROUT,do_erc=True)]),
        Part(name='IRM-02-3.3',dest=TEMPLATE,tool=SKIDL,keywords='9V 2W miniature AC-DC module-type power supply',description='9V 2W miniature AC-DC module-type power supply MeanWell',ref_prefix='U',num_units=1,fplist=['ACDC?Converter?MeanWell?IRM?02?x*'],do_erc=True,aliases=['IRM-02-5', 'IRM-02-9', 'IRM-02-12', 'IRM-02-15', 'IRM-02-24'],pins=[
            Pin(num='1',name='AC/N',func=Pin.PWRIN,do_erc=True),
            Pin(num='2',name='AC/L',func=Pin.PWRIN,do_erc=True),
            Pin(num='3',name='-Vout',func=Pin.PWROUT,do_erc=True),
            Pin(num='4',name='+Vout',func=Pin.PWROUT,do_erc=True)]),
        Part(name='IRM-03-3.3S',dest=TEMPLATE,tool=SKIDL,keywords='5V 3W AC-DC module power supply',description='5V, 3W, AC-DC module power supply, MeanWell',ref_prefix='U',num_units=1,fplist=['ACDC*MeanWell*IRM*03*'],do_erc=True,aliases=['IRM-03-5S', 'IRM-03-12S', 'IRM-03-15S', 'IRM-03-24S'],pins=[
            Pin(num='1',name='AC/L',func=Pin.PWRIN,do_erc=True),
            Pin(num='3',name='AC/N',func=Pin.PWRIN,do_erc=True),
            Pin(num='5',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='10',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='11',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='12',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='22',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='13',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='14',name='-Vout',func=Pin.PWROUT,do_erc=True),
            Pin(num='24',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='15',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='16',name='+Vout',func=Pin.PWROUT,do_erc=True),
            Pin(num='26',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='17',name='NC',func=Pin.NOCONNECT,do_erc=True)]),
        Part(name='KA5H02659RN',dest=TEMPLATE,tool=SKIDL,keywords='SMPS Controller AC-DC',description='67kHz SMPS Controller, AC-DC, PDIP-8',ref_prefix='U',num_units=1,fplist=['DIP8*'],do_erc=True,aliases=['KA5M02659RN'],pins=[
            Pin(num='1',name='D',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='3',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='4',name='FB',func=Pin.PASSIVE,do_erc=True),
            Pin(num='6',name='D',func=Pin.PASSIVE,do_erc=True),
            Pin(num='7',name='D',func=Pin.PASSIVE,do_erc=True),
            Pin(num='8',name='D',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='KA5H0265RCTU',dest=TEMPLATE,tool=SKIDL,keywords='SMPS Controller AC-DC',description='KA5H0265RCTU, 100kHz SMPS Controller w/ Soft Start, AC-DC, TO-220F-5L(Forming)',ref_prefix='U',num_units=1,fplist=['TO-220-5L'],do_erc=True,aliases=['KA5H0265RCYDTU'],pins=[
            Pin(num='1',name='D',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='3',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='4',name='FB',func=Pin.PASSIVE,do_erc=True),
            Pin(num='5',name='SS',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='KA5M0265RTU',dest=TEMPLATE,tool=SKIDL,keywords='SMPS Controller AC-DC',description='KA5M0280RTDTU, 67kHz SMPS Controller, AC-DC, TO-220F-4L(Forming)',ref_prefix='U',num_units=1,fplist=['TO-220F-4L'],do_erc=True,aliases=['KA5M0265RYDTU', 'KA5L0265RTU', 'KA5L0265RYDTU', 'KA5H0280RTU', 'KA5H0280RYDTU', 'KA5M0280RTU', 'KA5M0280RYDTU'],pins=[
            Pin(num='1',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='2',name='D',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='4',name='FB',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='NCP1200P',dest=TEMPLATE,tool=SKIDL,keywords='SMPS Controller AC-DC',description='SMPS Controller, AC-DC, PDIP-8',ref_prefix='U',num_units=1,fplist=['DIP8*', 'SOIC8*'],do_erc=True,aliases=['NCP1200D'],pins=[
            Pin(num='1',name='ADJ',do_erc=True),
            Pin(num='2',name='FB',do_erc=True),
            Pin(num='3',name='CS1',do_erc=True),
            Pin(num='4',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='5',name='DRV',func=Pin.OUTPUT,do_erc=True),
            Pin(num='6',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='8',name='HV',do_erc=True)]),
        Part(name='UC3846X-D08-T',dest=TEMPLATE,tool=SKIDL,keywords='SMPS PWM Controller',description='UC3846x-DO8-T, SMPS Flyback PWM Controller, DIP8',ref_prefix='U',num_units=1,fplist=['DIP*', 'PDIP*'],do_erc=True,pins=[
            Pin(num='1',name='GATE',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='VDD',func=Pin.PWRIN,do_erc=True),
            Pin(num='4',name='SENSE',func=Pin.PASSIVE,do_erc=True),
            Pin(num='5',name='RI',func=Pin.PASSIVE,do_erc=True),
            Pin(num='7',name='FB',func=Pin.PASSIVE,do_erc=True),
            Pin(num='8',name='GND',func=Pin.PWRIN,do_erc=True)]),
        Part(name='VIPer22ADIP-E',dest=TEMPLATE,tool=SKIDL,keywords='SMPS',description='Low power OFF-line SMPS primary switcher',ref_prefix='U',num_units=1,fplist=['DIP8*', 'SO-8*'],do_erc=True,aliases=['VIPer22ASTR-E', 'VIPer22AS-E'],pins=[
            Pin(num='1',name='S',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='S',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='FB',do_erc=True),
            Pin(num='4',name='VDD',func=Pin.PWRIN,do_erc=True),
            Pin(num='5',name='D',func=Pin.PASSIVE,do_erc=True),
            Pin(num='6',name='D',func=Pin.PASSIVE,do_erc=True),
            Pin(num='7',name='D',func=Pin.PASSIVE,do_erc=True),
            Pin(num='8',name='D',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='VIPer25LN',dest=TEMPLATE,tool=SKIDL,keywords='SMPS Controller with MOSFET 12W AC-DC',description='12W SMPS Controller, AC-DC, PDIP-7',ref_prefix='U',num_units=1,do_erc=True,aliases=['VIPer25HN'],pins=[
            Pin(num='1',name='S',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='VDD',func=Pin.PWRIN,do_erc=True),
            Pin(num='3',name='ZCD',do_erc=True),
            Pin(num='4',name='FB',do_erc=True),
            Pin(num='5',name='BR',do_erc=True),
            Pin(num='7',name='D',func=Pin.PASSIVE,do_erc=True),
            Pin(num='8',name='D',func=Pin.PASSIVE,do_erc=True)])])