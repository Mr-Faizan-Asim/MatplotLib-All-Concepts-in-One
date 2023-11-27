from matplotlib import pyplot as plt
import numpy as np
import random


# figure is used to set the size of Histogram
plt.Figure(figsize=(16,9))

cs_student_age = np.random.randint(18,50,100)
ce_student_age = np.random.randint(20,45,100)
# it make the range on graph
bin = [15,25,35,45,55]
plt.title("Students Age Histogram")
plt.xlabel("Students Age")
plt.ylabel("No of Students")
plt.hist([cs_student_age,ce_student_age],bin,rwidth=0.8,label=["CS Student","CE Student"],color=['r','g'])
plt.legend()
plt.show()

