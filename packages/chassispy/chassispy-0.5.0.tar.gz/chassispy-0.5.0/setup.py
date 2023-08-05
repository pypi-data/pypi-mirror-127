from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='chassispy',
    version='0.5.0',
    author='tang xi',
    author_email='tang___xi@163.com',
    description='A small example package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/88588421/agilex_chassis',
    project_urls={
        'Bug Tracker': 'https://github.com/88588421/agilex_chassis/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        
    ],

    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=['python-can>=3.3.4'],
    python_requires='>=3.6',
)
