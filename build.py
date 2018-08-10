import os
from pathlib import Path
import subprocess
import sys
import venv


class CustomEnvironment(venv.EnvBuilder):
    '''Virtual environment for the installation.

    Install wheel in the venv for packaging.
    '''
    def post_setup(self, context):
        self.python = context.env_exe
        def pip(*args):
            subprocess.check_call([self.python, '-m', 'pip', *args])
        pip('install', '-U', 'pip')
        pip('install', 'wheel')


def main():
    # Patch the original setup.py to change the project name and description
    coremltools = Path('coremltools')
    coremltools_setup = coremltools / 'setup.py'
    (coremltools_setup).rename(coremltools / 'coremltools_setup.py')
    os.link('setup.py', str(coremltools_setup))

    env = CustomEnvironment(clear=True, symlinks=True, with_pip=True)
    env.create('venv')
    subprocess.check_call([env.python, 'setup.py', 'bdist_wheel'], cwd='coremltools')

if __name__ == '__main__':
    main()
