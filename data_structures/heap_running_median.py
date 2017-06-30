
import sys
import random
import copy

from heap import Heap

min_heap = Heap()

def get_running_medium(a_i, a_t):
   global min_heap
   min_heap.add(a_t)

   # number of pops to get to medium indices
   if a_i % 2 == 0:
      medium_index = (a_i + 1) // 2
   else:
      medium_index = (a_i + 1) // 2 - 1

   polled = []
   for i in range(medium_index):
      polled.append(min_heap.poll())

   if a_i % 2 == 0:
      print(min_heap.peek() / 1)
   else:
      item = min_heap.poll()
      polled.append(item)
      print((min_heap.peek() + item) / 2)

   # add those polled back
   for item in polled:
      min_heap.add(item)

# n = int(input().strip())
# a = []
# a_i = 0

# for a_i in range(n):
#    a_t = int(input().strip())
#    get_running_medium(a_i, a_t)


if __name__ == "__main__":
   random_list = random.sample(range(1000), 1000)

   for index, item in enumerate(random_list):
      get_running_medium(index, item)
