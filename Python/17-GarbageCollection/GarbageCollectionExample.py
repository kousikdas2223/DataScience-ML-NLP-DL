#Garbage collection Examples:
import sys
import gc
import tracemalloc

# Example 1:
a=[]
b=a
print(sys.getrefcount(a))
del b
print(sys.getrefcount(a))

# Example 2:

class MyClass:
    def __init__(self):
        self.name = "John"

my_object = MyClass()
print(sys.getrefcount(MyClass))
del my_object
print(sys.getrefcount(MyClass))

# Example 3:

gc.enable()
print(gc.collect())
print(gc.get_stats())

# Example 4:
print(gc.garbage)

# Profiling example

tracemalloc.start()
my_object = MyClass()
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')
print("[Top 10] Memory usage statistics:")

for stat in top_stats[:10]:
    print(f"{stat.lineno}: {stat.size} bytes ({stat.count} calls)")
    del stat
    tracemalloc.stop()
    gc.collect()
    print(gc.get_stats())
    print(gc.garbage)
    tracemalloc.start()
    del snapshot
    print(f"Total memory usage: {tracemalloc.get_traced_memory()[0]} bytes")
    del top_stats
    tracemalloc.stop()
    gc.collect()
    print(gc.get_stats())
    print(gc.garbage)
    tracemalloc.start()
    del my_object
    print(f"Total memory usage: {tracemalloc.get_traced_memory()[0]} bytes")
    del my_object
    tracemalloc.stop()
    gc.collect()
    print(gc.get_stats())
    print(gc.garbage)
    tracemalloc.start()
    



