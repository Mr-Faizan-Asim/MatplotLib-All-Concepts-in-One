from matplotlib import pyplot as plt
import numpy as np
import random 

class_name = ["AI","PF","OOP","DSA","DB"]
class_one_marks = np.random.randint(30,90,5)

# to make one piece far
explode = [0,0,0.2,0,0.2]

plt.pie(class_one_marks,labels=class_name,explode = explode,autopct="%0.1f%%",shadow=True)