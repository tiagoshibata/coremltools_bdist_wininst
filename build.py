import subprocess
import venv


class CustomEnvironment(venv.EnvBuilder):
    '''Virtual environment for the installation.

    Install wheel in the venv for packaging.
    '''
    def post_setup(self, context):
        self.python = context.env_exe
        def pip(*args):
            subprocess.check_call([self.python, '-m', 'pip'] + args)
        pip('install', '-U', 'pip')
        pip('install', 'wheel')


def main():
    env = CustomEnvironment(clear=True, symlinks=True, with_pip=True)
    env.create('venv')
    subprocess.check_call([env.python, '../patched_setup.py', 'bdist_wheel'], cwd='coremltools')

if __name__ == '__main__':
    main()
