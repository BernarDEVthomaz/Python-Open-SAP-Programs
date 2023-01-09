import random
import statistics 
def gaussian_distribution():
    return [random.gauss(100, 10) for _ in range(1000)]
lists = gaussian_distribution()
print("Mean:", statistics.mean(lists))
print("Standard Deviation:", statistics.stdev(lists))
