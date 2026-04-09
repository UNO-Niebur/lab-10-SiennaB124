#MapPlot.py
#Name: Sienna Bonner
#Date: 4/7/26
#Assignment: Lab 10


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("reaction_time_data.csv")

plt.plot(data["Trial"], data["ReactionTime_ms"], marker='o')

plt.xlabel("Trial")
plt.ylabel("Reaction Time (ms)")
plt.title("Reaction Time Across Trials")

plt.savefig("reaction_time_graph.png")

