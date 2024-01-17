# plot 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

years = [2016, 2017, 2018, 2019, 2020, 2021, 2022]
publications = [597, 692, 703, 750, 747, 902, 1067]

plt.plot(years, publications,'o-')
plt.title('Search Results for "Robot Assisted" from 2016 to 2022 on IEEE Xplore')
plt.xlabel("Year")
plt.ylabel("Number of Publications")
plt.grid(alpha=0.25)
plt.savefig("/Users/noor/Bot4BACS/publications.pdf", format="pdf", bbox_inches="tight")
plt.show()
