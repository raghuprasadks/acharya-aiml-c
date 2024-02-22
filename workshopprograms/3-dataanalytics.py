import pandas as pd
lst =[3,5,7,1,70]
seriesdata = pd.Series(lst)
print("series ")
print(seriesdata)
print("data type ",type(seriesdata))
print("shape ",seriesdata.shape)

print("pandas")
topeconomies={
    "country":["USA","CHINA","GERMANY","JAPAN","INDIA"],
    "GDP":[27,18,4.7,4.2,4.1],
    "RANK":[1,2,3,4,5]
}
df= pd.DataFrame(topeconomies)
print(df)
print("data type ",type(df))
print("shape ",df.shape)
print("columns")
print(df.columns)
print("data types")
print(df.dtypes)
print("display first 5 rows")
print(df.head())
print("display last 5 rows")
print(df.tail())
print("display 3 rows randomly")
print(df.sample(n=3))
print("display 20 percent rows")
print(df.sample(frac=.2))

import matplotlib.pyplot as plt
print("line chart")
plt.title("GDP of Top 5 Economies")
plt.xlabel("Country")
plt.ylabel("GDP")
plt.plot(df.country,df.GDP)
plt.show()

print("scatter")
plt.title("GDP of Top 5 Economies")
plt.xlabel("Country")
plt.ylabel("GDP")
plt.scatter(df.country,df.GDP)
plt.show()

print("bar")
plt.title("GDP of Top 5 Economies")
plt.xlabel("Country")
plt.ylabel("GDP")
plt.bar(df.country,df.GDP)
plt.show()
