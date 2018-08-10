import os
import subprocess
import sys
import traceback


def run_tests():
    python_binary = next(x for x in ('venv/bin/python', 'venv/Scripts/python') if os.path.exists(x))
    def python(*args):
        subprocess.check_call([python_binary, '-m'] + list(args))

    python('pip', 'install', '-r', 'coremltools/test_requirements.pip')
    python('pytest', 'coremltools')


def main():
    if sys.version_info[:2] == (3, 7):
        print('Dependencies are unavailable for Python 3.7, tests are expected to fail')
        try:
            run_tests()
        except Exception:  # Don't fail the CI build
            traceback.print_exc()
    else:
        run_tests()

if __name__ == '__main__':
    main()
