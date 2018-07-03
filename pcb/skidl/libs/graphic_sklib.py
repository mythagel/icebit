from skidl import Pin, Part, SchLib, SKIDL, TEMPLATE

SKIDL_lib_version = '0.0.1'

graphic = SchLib(tool=SKIDL).add_parts(*[
        Part(name='ARROW1',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='ARROW2',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='ARROW3',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='ARROW4',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='BOX1',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='BOX2',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='BOX3',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='BOX4',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='C1',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='CIRCLE1',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='CIRCLE2',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='CIRCLE3',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='CIRCLE4',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='DIAMOND1',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='DIAMOND2',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='DIAMOND3',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='DIAMOND4',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='FARROW1',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='FARROW2',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='FARROW3',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='FARROW4',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='FBOX1',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='FBOX2',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='FBOX3',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='FBOX4',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='FDIAMOND1',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='FDIAMOND2',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='FDIAMOND3',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='FDIAMOND4',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='FSQUARE1',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='FSQUARE2',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='FSQUARE3',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='FSQUARE4',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='SQUARE2',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='SQUARE3',dest=TEMPLATE,tool=SKIDL,do_erc=True),
        Part(name='SQUARE4',dest=TEMPLATE,tool=SKIDL,do_erc=True)])