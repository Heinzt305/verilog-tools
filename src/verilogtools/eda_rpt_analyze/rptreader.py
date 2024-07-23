from typing import (
    Optional,
    Literal,
)
import pandas as pd
import re

class EdaReport():
    def __init__(self, rptPath: Optional[str]) -> None:
        self.lines = None
        if rptPath is None:
            pass
        else:
            self.loadRpt(rptPath)

    def loadRpt(self, rptPath: str) -> list[str]: 
        self.lines = self.readRpt(rptPath)
        for line in self.lines:
            tokens = line.strip().split()

    def readRpt(self, rptPath: str) -> list[str]:
        with open(rptPath, 'r') as f:
            lines = f.readlines()
        return lines
    
    def getReportAttributes(self, lines: list[str]):
        lst = (
            'Report',
            'Design',
            'Version',
            'Date',
            'Dataframe',
        )

        report = dict.fromkeys(lst)
        attri = iter(lst)

        target = next(attri, 'end')
        datalines = False
        df = pd.DataFrame()
        for line in lines:
            tokens = re.sub(r'\(.*?\)|\:' ,"" ,line.strip()).split()

            if target == 'end':
                break
            elif tokens is [] or tokens is None:
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
                target == next(attri, 'Dataframe')
            elif datalines is True:
                columns = [re.sub(r'.*?/' ,"" , tokens[0])]
                if report['Report'] == 'area':
                    index = ["Module_name", "Area(um2)"]
                    df = pd.concat([df, pd.DataFrame([tokens[0], eval(tokens[1])], index=index, columns=columns)], axis=1)
                elif report['Report'] == 'power':
                    index = ["Module_name", "Power(mW)"]
                    df = pd.concat([df, pd.DataFrame([tokens[0], eval(tokens[4])], index=index, columns=columns)], axis=1)
                else:
                    index = ["Module_name"]
                    df = pd.concat([df, pd.DataFrame([tokens[0]], index=index, columns=columns)], axis=1)

        report['Dataframe'] = df