import pandas as pd
import re

def ReadRpt(RptPath:str) -> list[str]:
    with open(RptPath, 'r') as f:
        lines = f.readlines()
    return lines

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