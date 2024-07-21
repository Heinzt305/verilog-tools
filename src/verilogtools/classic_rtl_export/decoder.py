# import numpy as np

def decoder(filename:str, sigIn:str, sigOut:str, widthIn:int, indent:int=0): # for example, 3-8decoder
    head = '\t'*indent
    widthOut = 2**(widthIn)
    with open(filename, 'w') as f:
        f.write(head+f'always @(*) begin\n')
        f.write(head+f'\tcase ( {sigIn} )\n')
        for case in range(widthOut):
            f.write(head+f'\t\t{widthIn}\'d{case}: {sigOut} = {widthOut}\'b{2**(case):0{widthOut}b};\n')
        f.write(head+f'\t\tdefault: {sigOut} = {widthOut}\'b{0:0{widthOut}b};\n')
        f.write(head+f'\tendcase\n')
        f.write(head+f'end')

def decoder2(filename:str, sigIn:str, sigOut:str, widthIn:int, indent:int=0):
    head = '\t'*indent
    widthOut = 2**(widthIn)
    with open(filename, 'w') as f:
        f.write(head+f'always @(*) begin\n')
        f.write(head+f'\tcase ( {sigIn} )\n')
        for case in range(widthOut):
            f.write(head+f'\t\t{widthIn}\'d{case}: {sigOut} = {widthOut}\'b{2**(case+1)-1:0{widthOut}b};\n')
        f.write(head+f'\t\tdefault: {sigOut} = {widthOut}\'b{0:0{widthOut}b};\n')
        f.write(head+f'\tendcase\n')
        f.write(head+f'end')