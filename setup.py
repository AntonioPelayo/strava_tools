from setuptools import setup, find_packages

setup(
    name='strava_tools',
    version='0.1',
    description="Tools for Strava's API",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Antonio Pelayo',
    author_email='aPelayo.py@gmail.com',
    url='https://github.com/AntonioPelayo/strava_tools',
    python_requires='>=3.9',
    packages=find_packages(),
    install_requires=[
        'python-dotenv',
        'requests',
    ],
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Intended Audience :: Developers',
    ]
)