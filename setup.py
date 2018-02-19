from setuptools import setup, find_packages

__version__ = '1.0.0'

setup(
    version=__version__,
    name='aeroexpress_sdk',
    packages=find_packages(),

    install_requires=[
        'zeep'
    ],

    description='Aeroexpress SDK',

    author='Travel Managment Consulting',
    author_email='otd@tm-consulting.ru',

    url='https://github.com/tmconsulting/aeroexpress-sdk',
    download_url='https://github.com/tmconsulting/aeroexpress-sdk/archive/%s.tar.gz' % __version__,

    license='MIT License',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
