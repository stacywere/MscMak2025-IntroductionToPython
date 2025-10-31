import sys, os                          # import sys and os modules
os.chdir("../Scripts")                  # change directory to Scripts
sys.path.append(os.getcwd())            # append the current working directory to sys.path
import my_module                        # import my_module
from my_module import greet, farewell   # import specific functions from my_module
my_module.greet("John")
my_module.farewell("John")