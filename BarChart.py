from matplotlib import pyplot as plt
import numpy as np


class_name = ["AI","PF","OOP","DSA","DB"]

class_one_marks = np.random.randint(30,90,5)
class_two_marks = np.random.randint(20,95,5)
class_three_marks = np.random.randint(40,80,5)


plt.bar(class_name,class_one_marks,width=0.6)
plt.bar(class_name,class_two_marks,width=0.6)

plt.show()