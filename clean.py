import pandas as pd

#处理面积数据
def parse_info(row):
    return row.strip().split('平米')[0]

#处理房屋数量数据
def parse_info2(row):
    beds = row.strip().split('室')[0]
    rooms_temp = row.strip().split('室')[1]
    rooms = rooms_temp.strip().split('厅')[0]
    return int(beds) + int(rooms)
#处理地区数据
def change(row):
    dist = row.strip()
    if dist=='furong':
        return 0
    elif dist=='kaifu':
        return 1
    elif dist=='tianxin':
        return 2
    elif dist=='yuelu':
        return 3
    elif dist=='yuhua':
        return 4
    else:
        return 5
#加工数据函数
def cleanData():
    df = pd.read_csv("./out.csv", names=["cs_size", "cs_type", "cs_rent", "cs_dist"])
    df['cs_size'] = df['cs_size'].apply(parse_info)
    df['cs_type'] = df['cs_type'].apply(parse_info2)
    df['cs_dist'] = df['cs_dist'].apply(change)
    df.to_csv("clean.csv",index=False,sep=',')
    

cleanData()