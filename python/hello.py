import pandas as avm
import matplotlib.pyplot as vicky
vs = avm.read_csv('gender_submission.csv')
print(vicky)
Total_Pass = vs["Survived"].value_counts()
total = len(vs)
a = Total_Pass[0]
perc = (a/total)* 100
print(f"Percentage of non-survivors is: {perc:.2f}%")
Total_Pass.plot(kind= 'bar',color=["blue", "Green"])
vicky.xlabel("servived people")
vicky.ylabel("non-servived people")
vicky.title("servived passenger in the flight")
vicky.xticks(rotation=0)
vicky.show()
