import matplotlib.pyplot as plt

def plot(stats):

    labels = list(stats.keys())
    values = list(stats.values())

    plt.bar(labels, values)
    plt.title("LeetCode Progress")
    plt.savefig("graphs/progress.png")