text = [('Credit Suisse', 9), ('CNBC', 6), ('FINMA', 2), ('Rohner', 2), ('Silchester International', 2)]

# Bar chart plot of words
import numpy as np                                                               
import matplotlib.pyplot as plt

top=text

words, y_ax = zip(*top)
x_as = np.arange(len(words)) 

plt.bar(x_as, y_ax, align='edge', width=0.3)

plt.xticks(x_as, words)
plt.yticks(y_ax)

plt.show()

# Pie chart plot of numbers
words = text
coverage, word_tags = [i[1] for i in words],[i[0] for i in words]
plt.pie(coverage, labels=word_tags, autopct='%1.1i%%')
plt.show()
