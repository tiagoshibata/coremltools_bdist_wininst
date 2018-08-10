import os
from pathlib import Path
import subprocess
import sys

# Patch the original setup.py to change the project name and description
coremltools = Path('coremltools')
coremltools_setup = coremltools / 'setup.py'
(coremltools_setup).rename(coremltools / 'coremltools_setup.py')
os.link('setup.py', str(coremltools_setup))

subprocess.check_call([sys.executable, 'setup.py', 'bdist_wininst'], cwd='coremltools')
