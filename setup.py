import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(

	name="UNIVERSencrypt",

	version="0.0.1",

	author="EGORegor",

	author_email="egor@gmail.com",

	description="Best encrypt in the World!",
	
	long_description=long_description,

	long_description_content_type="text/markdown",
	
	url="",

	packages=setuptools.find_packages(),
	
	classifiers=[
		"Programming Language :: Python :: 3.8",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
    
	python_requires='>=3.6',
)