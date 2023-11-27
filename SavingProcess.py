from matplotlib import pyplot as plt


plt.pie([25,6,312,34,43],shadow=True,explode=[0,0,0.2,0,0.2],autopct="%0.1f%%")
plt.savefig("SavedByProcess\pieFig")
