#import os module
import os

#function to count the number of CUP using 
def get_cpu_count():
    """Gets the number of CPUs in the system."""
    #returning the CPU usagae count
    return os.cpu_count()

#calling the CPU count function 
print(get_cpu_count())