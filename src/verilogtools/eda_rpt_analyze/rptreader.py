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
        report = {}
        attri = iter([
            'Report',
            'Design',
            'Version',
            'Date',
            'Dataframe'
        ])

        target = next(attri, 'end')
        for line in lines:
            if target == 'end':
                break
            tokens = re.sub(r'\:' ,'' , line.strip()).split()
            if tokens is []:
                continue
            elif tokens[0] == target:
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
            else:
                pass


def InfoChoose(line:str, mode:str) -> list[str]:
    token = re.sub(r'\(.*?\)' ,"" ,line).strip().split()
    if mode == 'area':
        return [token[0], eval(token[1])]
    elif mode == 'power':
        return [token[0], eval(token[4])]
    
def NewPandas(RptPath:str, mode:str, start:int, end:int) -> pd.DataFrame:
    df = pd.DataFrame()
    lines = ReadRpt(RptPath)
    if mode == 'area':
        index = ["Module_name", "Area(um2)"]
    elif mode == 'power':
        index = ["Module_name", "Power(mW)"]
    for idx, line in enumerate(lines):
        if idx < end and idx >= start - 1:
            token = InfoChoose(line, mode)
            columns = [re.sub(r'.*?/' ,"" , token[0])]
            df = pd.concat([df, pd.DataFrame(token, index=index, columns=columns)], axis=1)
    return df