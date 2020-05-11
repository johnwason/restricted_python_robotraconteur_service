from RobotRaconteur.Client import *
from js import document
from js import print_div
from js import ace
import traceback

def on_run_button_click(a):    
    function_name = document.getElementById("function_textbox").value
    editor = ace.edit("editor")
    script_src = editor.getValue()
    print_div("Running function_named: " + function_name)
    loop.call_soon(do_click(script_src,function_name))

async def do_click(script_src,function_name):
    try:
        await client.async_run_sandbox(script_src,function_name,None,None)
    except Exception as e:
        print_div(traceback.format_exc())
        

async def main():
    global client
    client = await RRN.AsyncConnectService("rr+ws://localhost:62354/?service=RestrictedPythonService",None,None,None,None)

    run_button = document.getElementById("run_button")
    run_button.onclick = on_run_button_click

loop = RR.WebLoop()
loop.call_soon(main())
    



