from typing import (
    Optional,
    Literal,
)
import pandas as pd
import re

class EdaReport():
    def __init__(self, rptPath: Optional[str]) -> None:
        self.data = None
        if rptPath is None:
            pass
        else:
            self.loadRpt(rptPath)

    def loadRpt(self, rptPath: str) -> dict:
        self.data = self.getReportAttributes(self.readRpt(rptPath))

    def readRpt(self, rptPath: str) -> list[str]:
        with open(rptPath, 'r') as f:
            lines = f.readlines()
        return lines
    
    def getReportAttributes(self, lines: list[str]) -> dict:
        lst = (
            'Report',
            'Design',
            'Version',
            'Date',
            'Dataframe',
        )
        idx = 0

        report = dict.fromkeys(lst)
        attri = iter(lst)

        target = next(attri, 'end')
        datalines = False
        df = pd.DataFrame()
        for line in lines:
            tokens = re.sub(r'\(|\)|\:' ,"" ,line.strip()).split()
            
            if target == 'end':
                break
            elif tokens == [] or tokens is None:
                continue
            elif target == 'Dataframe' and tokens[0] == report['Design']:
                datalines = True
            elif target == 'Dataframe' and (tokens[0][0] == '1' or tokens[0][0] == '-'):
                datalines = False

            if tokens[0] == target:
                if target == 'Date':
                    report[target] = {
                        'week': tokens[1],
                        'month': tokens[2],
                        'day': tokens[3],
                        'time': tokens[4],
                        'year': tokens[5]
                    }
                else:
                    report[target] = tokens[1]
                target = next(attri, 'end')
            elif datalines is True:
                if report['Report'] == 'area':
                    index = ["Module_name", "Area(um2)"]
                    columns = [tokens[6]]
                    df = pd.concat([df, pd.DataFrame([tokens[0], eval(tokens[1])], index=index, columns=columns)], axis=1)
                elif report['Report'] == 'power':
                    index = ["Module_name", "Power(mW)"]
                    if len(tokens) == 6:
                        columns = [tokens[0]]
                        df = pd.concat([df, pd.DataFrame([tokens[0], eval(tokens[4])], index=index, columns=columns)], axis=1)
                    else:
                        columns = [tokens[1]]
                        df = pd.concat([df, pd.DataFrame([tokens[0], eval(tokens[5])], index=index, columns=columns)], axis=1)
                else:
                    index = ["Module_name"]
                    columns = [tokens[0]]
                    df = pd.concat([df, pd.DataFrame([tokens[0]], index=index, columns=columns)], axis=1)

        report['Dataframe'] = df
        return report
    
    def concatReport(self, rpt2: "EdaReport") -> pd.DataFrame:
        pass