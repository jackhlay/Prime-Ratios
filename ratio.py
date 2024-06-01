amount =1000
counter = 1
avg = 0
ratioTot = 0
ratios = []
avgs = []
diffs = []

def getRatios(amount):
    global ratioTot, avg, counter  # Declare global variables
    primes = genPrimes(amount)
    for i in range(len(primes) - 1):  # Fixed usage of genPrimes
        ratio = primes[i] / primes[i + 1]
        # print(f"Ratio of {primes[i]} to {primes[i + 1]}: {ratio}")
        ratioTot += ratio
        ratios.append(ratio)
        avg = ratioTot / counter
        avgs.append(avg)
        diff = primes[i+1] - primes[i]
        diffs.append(diff)
        # print(f"Avg ratio so far: {avg}")
        counter += 1

    return ratios, avgs, diffs

def genPrimes(max):
    primes = []
    for num in range(2, max+1):
        if isPrime(num):
            primes.append(num)
    return primes

def isPrime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    maxFactor = num ** 0.5
    for d in range(3, int(maxFactor) + 1, 2):  # Convert maxFactor to an integer
        if num % d == 0:
            return False
    return True

ratios, avgs, diffs=getRatios(amount)

import matplotlib.pyplot as plt

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('Data Points')
ax1.set_ylabel('Ratios', color=color)
ax1.plot(ratios, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  
color = 'tab:blue'
ax2.set_ylabel('Averages', color=color)
ax2.plot(avgs, color=color)
ax2.tick_params(axis='y', labelcolor=color)

# ax2 = ax1.twinx()  
# color = 'tab:green'
# ax2.set_ylabel('Differences', color=color)
# ax2.plot(diffs, color=color)
# ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  
plt.title('Ratios vs Averages on a Number Line')
plt.show()