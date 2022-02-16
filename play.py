import pandas
import random
data= pandas.read_csv("data/french_words.csv")
data_dict=data.to_dict(orient="records")
dataq=random.choice(data_dict)
value=dataq["French"]
print(value)
