from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in trial/__init__.py
from trial import __version__ as version

setup(
	name="trial",
	version=version,
	description="Trying to see if i have grasp frappe",
	author="Elvis Kangethe",
	author_email="elvisndegwa90@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
