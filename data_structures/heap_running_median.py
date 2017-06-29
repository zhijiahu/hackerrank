
import sys

from heap import Heap


n = int(input().strip())
a = []
a_i = 0

heap = Heap()

for a_i in range(n):
   a_t = int(input().strip())
   a.append(a_t)
   heap.add(a_t)

   # number of pops to get to medium indices
   if a_i % 2 == 0:
      medium_index = (a_i + 1) // 2
   else:
      medium_index = (a_i + 1) // 2 - 1

   polled = []
   for i in range(medium_index):
      polled.append(heap.poll())

   if a_i % 2 == 0:
      print(heap.peek() / 1)
   else:
      item = heap.poll()
      polled.append(item)
      print((heap.peek() + item) / 2)

   # add those polled back
   for item in polled:
      heap.add(item)
