from setuptools import setup

with open('README.rst') as file:
    long_description = file.read()

setup(
    name='zxcvbn-covert',
    version='5.0.0',
    packages=['zxcvbn'],
    url='https://github.com/covert-encryption/zxcvbn-python',
    download_url='https://github.com/covert-encryption/zxcvbn-python/tarball/v5.0.0',
    license='MIT',
    author='Daniel Wolf',
    author_email='danielrwolf5@gmail.com',
    long_description=long_description,
    keywords=['zxcvbn', 'password', 'security'],
    entry_points={
        'console_scripts': [
            'zxcvbn = zxcvbn.__main__:cli'
         ]
    },
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Security',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
