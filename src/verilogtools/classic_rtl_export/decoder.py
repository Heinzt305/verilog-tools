from typing import Literal

def decoder(
    filename: str,
    mode: Literal["onehot", "bitmask"],
    sigIn: str,
    sigOut: str,
    widthIn: int,
    reverse: bool = False,
    indent_num: int=0,
) -> None:
    """Write a decoder instance to the file with verilog language.
    
    Decoder contains several types, which are changed here by parameters.

    Parameters
    ----------
    filename : string
        Write path and file name.

    mode : {'onehot', 'bitmask'}
        'onehot' is used to generate general decoder, output one-hot code,
        such as 3-8 decoder.

        example : `010->00000100`

        'bitmask' is used to generate the output mask decoder, the output
        mask is defaulted to high 0 and low 1, and the mask can also be
        flipped by `reverse`.
        
        example(`reverse=False`) : `010->00000111`
    
    sigIn : string
        The Decoder's input signal name, also known as the selector signal.
        
    sigOut : string
        Decoder's output signal name.
        
    widthIn : int
        The width of the Decoder's input signal.

    reverse : bool, default False
        `reverse` is used in 'bitmask' mode, when True outputs bitmask with
        high 1 and low 0, when False outputs bitmask with high 0 and low 1.
        It cannot be used in 'onehot' mode.
        
    indent_num : int, default 0
        The size of the entire code block indentation, default is 0."""
    head = '\t'*indent_num
    widthOut = 2**(widthIn)
    with open(filename, 'w') as f:
        f.write(head+f'always @(*) begin\n')
        f.write(head+f'\tcase ( {sigIn} )\n')
        for case in range(widthOut):
            if mode == 'onehot':
                f.write(head+f'\t\t{widthIn}\'d{case}: {sigOut} = {widthOut}\'b{2**(case):0{widthOut}b};\n')
            elif mode == 'bitmask':
                if reverse == True:
                    f.write(head+f'\t\t{widthIn}\'d{case}: {sigOut} = {widthOut}\'b{2**(widthOut)-2**(case):0{widthOut}b};\n')
                else:
                    f.write(head+f'\t\t{widthIn}\'d{case}: {sigOut} = {widthOut}\'b{2**(case+1)-1:0{widthOut}b};\n')
        f.write(head+f'\t\tdefault: {sigOut} = {widthOut}\'b{0:0{widthOut}b};\n')
        f.write(head+f'\tendcase\n')
        f.write(head+f'end')