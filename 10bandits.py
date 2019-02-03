import gym
import gym_bandits # https://github.com/JKCooper2/gym-bandits
import random

env = gym.make("BanditTenArmedGaussian-v0")
env.reset()

epsilon = 0
epsilons = []
averages = []
slotPuppet = [[], [], [], [], [], [], [], [], [], []]
slotCounter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
highestIndex = 0
averagePerEpsilon = 0

def explore():
  whichSlot = random.randint(0, 9)
  slotPuppet[whichSlot].append(env.step(whichSlot))

def exploit():
  highest = 0
  highestIndex = 0
  slotCounterIndex = 0

  for puppet in slotPuppet:
    if puppet:
      for slot in puppet:
        slotCounter[slotCounterIndex] = slotCounter[slotCounterIndex] + slot[1]
    slotCounterIndex += 1

  for i in range (0, 9):
    if slotCounter[i] > highest:
      highest = slotCounter[i]
      highestIndex = i
  slotPuppet[highestIndex].append(env.step(highestIndex))

def greedy():
  for i in range(10):
    exploreExploit = round(random.uniform(0, 100), 1)
    if (exploreExploit > epsilon):
      explore()
    else:
      exploit()

while(epsilon <= 99.9):
  epsilon += 0.1
  greedy()
  slotPuppet = [[], [], [], [], [], [], [], [], [], []]
  for counter in slotCounter:
    averagePerEpsilon += counter
  epsilons.append(epsilon)
  averages.append(averagePerEpsilon / 10)
  slotCounter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  averagePerEpsilon = 0

print(str(epsilons[averages.index(max(averages))]) + ": " + str(max(averages)))
