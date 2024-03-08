from setuptools import setup, find_packages
from pathlib import Path

version = __import__("src").__version__

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
    name='auditoorai',
    version=version,
    description='auditooai',
    author='0xbepresent',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT license',
    packages=find_packages(),
    keywords = ['auditor', 'evm', 'smartcontracts'],
    include_package_data=True,
    install_requires=[
        'python-dotenv==1.0.1',
        'langchain==0.1.8',
        'langchain-community==0.0.21',
        'deeplake==3.8.21',
        'click==8.1.7',
        'rich==13.7.0',
        'langchain-openai==0.0.6',
        'pydantic==1.10.8',
    ],
    entry_points='''
        [console_scripts]
        aai=src.cli:cli
    ''',
    classifiers=[
        'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',      # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.9', 
        'Programming Language :: Python :: 3.10',
    ],
)
