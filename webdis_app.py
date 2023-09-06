import subprocess
import sys
import os
import app

project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_dir)

args = ['streamlit', 'run', 'app/main.py']
subprocess.run(args)
