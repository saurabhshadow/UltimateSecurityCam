from setuptools import setup, find_packages
from codecs import open
from os import path


dir_path = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(dir_path, 'README.md'), encoding='utf-8') as f:
	long_description = f.read()

requirements = ['numpy', 'matplotlib', 'pandas', 'sklearn', 'opencv-python', 'argparse', 'pygame', 'opencv-contrib-python']

setup(
	name='Ultimate Security Cam',
	version = '1.0',
	author= 'Nitesh Chaudhry',
	author_email= 'niteshbinladen@gmail.com',
	url= 'https://github.com/NIteshx2/UltimateSecurityCam',
	description = 
'''
An easy-to-build, un-hack-able security camera which is impossible to fool.

## Step by step guide
-----------------------
- Installation of all the required depedencies is completed first. 
- The code is made to run via terminal/IDE.
- Sequence of code:
	- The code first initializes a three seconds waiting camera window.
	- The main code runs to detect movements and record the complete 
	  video footage.
	- All the configurations of the video clip are recorded (like Date 
	  and Time, camera fps, maximum object movement recorded at a time, 
	  duration, etc.)
	- The video clip and configuration data is saved for future 
	  reference and the code terminates.
''',
	long_description = long_description,
#Listing Dependencies that it has
	install_requires = requirements,
#LICENSE Info
	license= 'The MIT License 2018',
#INFO about where package can run
	classifiers=[
	'Intended Audience :: Developers and users who wish to use image filters',
	'License :: OSI Approved :: MIT License',
	'Programming Language :: Python :: 2',
	'Programming Language :: Python :: 2.7',
	'Programming Language :: Python :: 3',
	'Programming Language :: Python :: 3.3',
	'Programming Language :: Python :: 3.4',
	'Programming Language :: Python :: 3.5',
	'Operating System :: Windows',
	'Operating System :: Linux',
	]
)
