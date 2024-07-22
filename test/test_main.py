import sys
sys.path.append("src")

import verilogtools
import pandas as pd
import torch

def main():
    verilogtools.classic_rtl_export.decoder(
        filename="example.v",
        mode="bitmask",
        sigIn="x",
        sigOut="y",
        widthIn=5,
        reverse=True,
        indent_num=2,
    )

if __name__ == '__main__':
    main()