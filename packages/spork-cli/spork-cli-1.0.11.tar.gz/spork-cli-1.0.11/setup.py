from setuptools import find_packages
from setuptools import setup


with open('README.md', 'r') as readme:
    LONG_DESCRIPTION = readme.read()  # use readme as long description


CLASSIFIERS = [
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'Topic :: Scientific/Engineering',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'Topic :: Scientific/Engineering :: Mathematics',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8']


URL = 'https://github.com/brandontrabucco/spork'


setup(name='spork-cli', version='1.0.11', license='MIT',
      packages=find_packages(include=['spork', 'spork.*']),
      description=('CLI For Launching '
                   'Experiments Using Singularity On Slurm'),
      long_description=LONG_DESCRIPTION, classifiers=CLASSIFIERS,
      long_description_content_type='text/markdown',
      author='Brandon Trabucco', author_email='brandon@btrabucco.com',
      url=URL, download_url=URL + '/archive/v1_0_11.tar.gz',
      keywords=['Deep Learning', 'Research', 'Management'],
      install_requires=['click', 'paramiko', 'pexpect', 'spython'],
      entry_points={'console_scripts': (
          'spork=spork.experiment_config:command_line_interface',)})
