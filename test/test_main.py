import sys
sys.path.append("src")
from typing import Literal
import verilogtools
import pandas as pd
import torch

def main():
    lst = ["a", "b", "c"]
    i = iter(lst)
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i, 'end'))
    exit()

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