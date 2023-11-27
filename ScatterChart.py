from matplotlib import pyplot as plt
import pandas as pd

dataSetOfPlayStore = pd.read_csv("E:\\University\Semester 3\LN\MatplotLib\DataSet\Google Play Store\googleplaystore.csv",nrows = 1500)
ratingAs_x = dataSetOfPlayStore["Rating"]
reviewAs_y = dataSetOfPlayStore["Reviews"]

plt.xlabel("Rating")
plt.ylabel("Reviews")
plt.scatter(ratingAs_x, reviewAs_y)
plt.scatter(ratingAs_x, dataSetOfPlayStore["Installs"],c ="y",marker="o")
plt.show()