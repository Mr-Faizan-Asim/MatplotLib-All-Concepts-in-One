from matplotlib import pyplot as plt
import numpy as np
import random 

plt.subplot(2,2,1)
plt.Figure(figsize=(16,9))
cs_student_age = np.random.randint(18,50,100)
plt.title("Students Age Histogram")
plt.xlabel("Students Age")
plt.ylabel("No of Students")
plt.hist([cs_student_age],label=["CS Student"],color=['r'])
plt.legend()
plt.show()

plt.subplot(2,2,2)
class_name = ["AI","PF","OOP","DSA","DB"]
class_one_marks = np.random.randint(30,90,5)
# to make one piece far
explode = [0,0,0.2,0,0.2]
plt.pie(class_one_marks,labels=class_name,explode = explode,autopct="%0.1f%%",shadow=True)

plt.subplot(2,2,3)
plt.hist([1,4,6,8,3])
plt.subplot(2,2,4)
plt.plot([1,5,342,42])