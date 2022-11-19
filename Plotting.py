# Remeber to first install Matplotlib and numpy  using the command below
# pip install matplotlib, numpy -- Make sure you've an internet connection

#numpy for creating arrays
import numpy as np
#matplotlib for plotting
import matplotlib.pyplot as mt

# Data sets
registered = np.array([23, 34, 56, 76, 89, 29, 12, 34, 56, 89])
male = np.array([3, 14, 26, 36, 49, 59, 62, 74, 86, 98])
female = np.array([15, 74, 56, 6, 00, 39, 17, 54, 66, 77])
voted = np.array([00, 10, 20, 30, 40, 50, 60, 70, 80, 90])
year = np.array(['2001', '2006', '2011', '2016', '2021', '2026', '2031', '2036', '2041', '2046'])

# Setting Chart title, Horizontal and Vertical lables respectively
mt.title("Your Chat Title")
mt.xlabel("Election Year")
mt.ylabel("Turn Up in %age")

# To plot Line graphs
mt.plot(year, registered, marker="d", linestyle="dashed", label="Registered")
mt.plot(year, male, marker="o", linestyle="dotted", label="Male")
mt.plot(year, female, marker="s", label="Female")
mt.plot(year, voted, marker="*", label="Voted")
mt.legend()
mt.show()


# To plot  Scatter graphs
mt.scatter(year, registered, label="Registered")
mt.scatter(year, male, label="Male")
mt.scatter(year, female, label="Female")
mt.scatter(year, voted, label="Voted")
mt.legend()
mt.show()

# To plot Bar graphs
mt.bar(year, registered)
mt.legend()
mt.show()

# To plot  Pie Charts
names = ['2001', '2006', '2011', '2016', '2021', '2026', '2031', '2036', '2041', '2046']
myexplode = [0.08, 0, 0, 0, 0, 0, 0, 0, 0, 0]
mt.pie(registered, labels=names, startangle = 90, explode = myexplode)

mt.legend()
mt.show()

""" Note: 1. mt.legend() is for labeling our charts
          2. mt.show() is making our charts visible 
"""
