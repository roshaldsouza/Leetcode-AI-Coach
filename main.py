from fetch_data import fetch
from analyzer import analyze
from visualizer import plot

data = fetch()
stats = analyze(data)

print(stats)

plot(stats)