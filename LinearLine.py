from matplotlib import pyplot as plt

days = [1,2,3,4,5,6,7,8,9,10,11,12]
temperature = [37.7,30,42.7,29.3,32.7,34.9,30,31.7,34.7,37.3,31.7,47.6]

plt.axis([0,30,0,50])
plt.title("Temperature Graph")
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.plot(days,temperature)
plt.show()
         
         