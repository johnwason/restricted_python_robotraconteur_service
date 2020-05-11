import sys

assert sys.version_info >= (3, 6), "Python version 3.6 or greater required"

import threading
import re
from RestrictedPython import compile_restricted, safe_globals
import RobotRaconteur as RR
RRN = RR.RobotRaconteurNode.s



restricted_python_service_robdef = """
service experimental.restricted_python

object RestrictedPythonService
    function varvalue run_sandbox(string script_src, string function_name, varvalue{string} params)
end

"""

_valid_name_re = re.compile('[a-zA-Z][a-zA-Z0-9_]*')

class PrintCollector:
    def __init__(self):
        self.printed = ""
    
    def __call__(self, _gettattr_=None):
        return self

    def write(self, text):
        self.printed += text

    def _call_print(self, text):
        self.printed += text
    

class RestrictedPythonService:
    def __init__(self):
        self._sandbox_running = False
        self._sandbox_lock = threading.Lock()

    def run_sandbox(self, script_src, function_name, params):
        if _valid_name_re.match(function_name) is None:
            raise RR.InvalidArgumentException("Function name is invalid")
        if params is not None:
            for k in params:
                if _valid_name_re.match(params) is None:
                    raise RR.InvalidArgumentException("Param name is invalid")
        
        loc = {}
        
        byte_code = compile_restricted(script_src, '<robotraconteur_sandbox>', 'exec')
        sandbox_globals = safe_globals.copy()
        print_collector = PrintCollector()
        sandbox_globals["_print_"] =print_collector
        exec(byte_code, sandbox_globals, loc)
        if params is None:
            res = loc[function_name]()
        else:
            res = loc[function_name](*params)

        print(print_collector.printed)

def main():

    service_obj = RestrictedPythonService()

    RRN.RegisterServiceType(restricted_python_service_robdef)
    with RR.ServerNodeSetup("experimental.restricted_python",62354):
        RRN.RegisterService("RestrictedPythonService", "experimental.restricted_python.RestrictedPythonService", service_obj)

        input("Press enter to quit")

if __name__ == '__main__':
    main()