import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import restricted_python_robotraconteur_service as res

c = res.RestrictedPythonService()

test_src = """
def hello():
    print("Hello world!")

def hello_name(name):
    print("Hello " + name)
"""

c.run_sandbox(test_src, "hello", None)