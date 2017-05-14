import sys
import runpy

sys.path.insert(0, r'C:/kmujournal')

activate_this = '/kmujournal/venv/Scripts/activate_this.py'
runpy.run_path(activate_this)

from kmujournal import app as application