import subprocess
import sys
import os

project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_dir)

if sys.platform == "win32":
    venv_streamlit = 'venv\\Scripts\\streamlit.exe'
else:
    venv_streamlit = 'venv/bin/streamlit'

args = [venv_streamlit, 'run', 'main.py']
subprocess.run(args)
