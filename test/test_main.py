import sys
sys.path.append("src")

import verilogtools

def main():
    df1 = verilogtools.eda_rpt_analyze.NewPandas(
        RptPath="test\\top_module.mapped.area.rpt",
        mode="area",
        start=39,
        end=8424
    )

    df1.to_excel("example.xlsx")

if __name__ == '__main__':
    main()