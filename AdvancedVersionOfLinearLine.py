import random
from matplotlib import pyplot as plt
from matplotlib import style


# ggplot used to create the raph grid
style.use("ggplot")
days = [1,2,3,4,5,6,7,8,9,10,11,12]
Lahore_temperature = [37.7,30,42.7,29.3,32.7,34.9,30,31.7,34.7,37.3,31.7,47.6]
Karachi_temperature = [round(random.uniform(30, 45)) for _ in range(12)]
plt.title("TEMPERATURE Graph")
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.plot(days,Lahore_temperature,'go-',linewidth = 3)
plt.plot(days,Karachi_temperature,'ro--',linewidth = 3)
plt.grid(color='k',linestyle='-',linewidth=2)
plt.legend(["Lahore","Karachi"])
plt.show()