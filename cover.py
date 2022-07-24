import pandas as pd
import argparse,openpyxl

parser = argparse.ArgumentParser(description='help')
parser.add_argument('-i', dest='input', type=str, help='处理文件(.json)')
parser.add_argument('-o', dest='output', type=str, help='输出文件(.xlsx)')

args = parser.parse_args()

df = pd.read_json(args.input)
df.T.to_excel(args.output , sheet_name="Sheet1")
