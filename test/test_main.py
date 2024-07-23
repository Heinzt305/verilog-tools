import sys
sys.path.append("src")
from typing import Literal
import verilogtools
import pandas as pd
import torch

def main():
    df1 = verilogtools.eda_rpt_analyze.EdaReport("./test/top_module.mapped.area.rpt")
    df2 = verilogtools.eda_rpt_analyze.EdaReport("./test/top_module.mapped.power.rpt")
    df = pd.concat([df1.data['Dataframe'], df2.data['Dataframe'].drop(index=["Module_name"])], axis=0).transpose()
    # df = pd.concat([df1.data['Dataframe'], df2.data['Dataframe']], axis=1).transpose()
    df.to_excel("example.xlsx")
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