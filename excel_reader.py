from tkinter import filedialog
import pandas as pd

file = filedialog.askopenfilename(filetypes=[("Spreadsheet Files", "*.xlsx *.ods"), ("All Files", "*.*")])

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

if file.endswith('.ods'):
    df = pd.read_excel(file, engine='odf')
else:
    df = pd.read_excel(file)

print(df)