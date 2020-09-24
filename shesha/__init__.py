''' @package shesha
Documentation for shesha.

More details.
'''

import subprocess, sys

__version__ = "5.0.0"

def check_shesha_compass_versions():
    compass_version = subprocess.check_output('conda list compass | tail -n1',shell=True).decode(
            sys.stdout.encoding).split()[1]
    assert(__version__ == compass_version), 'SHESHA and COMPASS versions are not matching : %r != %r ' %\
                                              (__version__, compass_version)

check_shesha_compass_versions()
