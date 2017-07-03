
import sys
import random

from heap import Heap

min_heap = Heap(is_max=False)
max_heap = Heap(is_max=True)


def get_running_medium_slow(a_i, a_t):
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

def get_running_medium_fast(a_i, a_t):
   global min_heap
   global max_heap

   if max_heap.peek() is None:
      max_heap.add(a_t)
      print(a_t)
      return a_t / 1

   # Check which heap to add to
   if a_t <= max_heap.peek():
      if max_heap.size() > min_heap.size():
         min_heap.add(max_heap.poll())
      max_heap.add(a_t)
   else:
      swap = True
      if min_heap.size() > max_heap.size():
         if a_t < min_heap.peek(): # this value should stay in min if it's greater than a_t
            max_heap.add(a_t)
            swap = False
         else:
            max_heap.add(min_heap.poll())

      if swap:
         min_heap.add(a_t)

   print(a_t)
   print('Max heap {2}:{0}\nMin heap {3}:{1}\n'.format(max_heap, min_heap, max_heap.size(), min_heap.size()))

   if max_heap.size() < min_heap.size():
      return min_heap.peek() / 1
   elif max_heap.size() > min_heap.size():
      return max_heap.peek() / 1
   else:
      return (max_heap.peek() + min_heap.peek()) / 2


def process_running_medium(a_i, a_t):
   print(get_running_medium_fast(a_i, a_t))


a_i = 0

# User input
def run_with_user_input():
   global a_i
   n = int(input().strip())

   for a_i in range(n):
      a_t = int(input().strip())
      process_running_medium(a_i, a_t)

# Using test case 2 from hackerank
def run_test_case_two():
   global a_i
   expected_results = []
   with open('heap_running_median_output.txt') as f:
      for item in f:
         expected_results.append(float(item))

   with open('heap_running_median_input.txt') as f:
      for index, item in enumerate(f):
         if index == 0: # skip the count
            continue

         result = get_running_medium_fast(a_i, float(item))
         if result != float(expected_results[index-1]):
            print('FUCK {0} != {1}'.format(result, expected_results[index-1]))
            break

         a_i += 1

def run_random():
   random_list = random.sample(range(1000), 1000)

   for index, item in enumerate(random_list):
      get_running_medium_fast(index, item)

   # for index, item in enumerate(random_list):
   #    get_running_medium_slow(index, item)


# Random generated test case
if __name__ == "__main__":
   run_with_user_input()
   #run_test_case_two()
   #run_random()
