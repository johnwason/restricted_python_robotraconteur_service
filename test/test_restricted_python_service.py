from RobotRaconteur.Client import *

test_src = """
def hello():
    print("Hello world!")

def hello_name(name):
    print("Hello " + name)
"""

client = RRN.ConnectService("rr+local:///?nodename=experimental.restricted_python&service=RestrictedPythonService")

client.run_sandbox(test_src,"hello",None)