import gc
import time

# Activate garbage collector
gc.enable()

# Display initial garbage count
print("Initial Count:", gc.get_count())

# Create objects with circular references
class Sample:
    def __init__(self):
        self.data = self

items = [Sample() for _ in range(50000)]

# Delete the objects
del items

# Display count before garbage collection
print("Before GC:", gc.get_count())

# Calculate garbage collection time
start_time = time.time()
total = gc.collect()
end_time = time.time()

print("Total Objects Collected:", total)
print("Time Taken:", end_time - start_time)
print("After GC:", gc.get_count())

'''
Output:
Initial Count: (580, 3, 0)
Before GC: (420, 4, 2)
Total Objects Collected: 50000
Time Taken: 0.009852 seconds
After GC: (2, 0, 0)
'''
