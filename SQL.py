import pandas as pd
DF=pd.read_csv("speakipy.csv")
DF["User"]=["sahil","sujal"]
DF.to_csv("speakipy.csv",index=False)