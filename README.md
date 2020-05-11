# Restricted Python Robot Raconteur Service

This repository contains a demo of using a [Restricted Python](https://github.com/zopefoundation/RestrictedPython) as a Robot Raconteur service. A web browser client is used as a user interface with the [ACE code editor](https://ace.c9.io/) to edit the Python code.

To run the service and frontend:

Use pip to install the required packages:

    pip install robotraconteur restrictedpython

Install firefox, and [allow fetching from local filesystem](https://discourse.mozilla.org/t/firefox-68-local-files-now-treated-as-cross-origin-1558299/42493). (This is not necessary if serving the HTML file from a server)

Run the service:

    python restricted_python_robotraconteur_service.py

Open `restricted_python_robotraconteur_service_gui.html` in Firefox

Type code in the editor, and press "Run!"