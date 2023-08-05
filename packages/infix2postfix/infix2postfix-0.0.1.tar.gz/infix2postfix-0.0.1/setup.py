from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='infix2postfix',
    version='0.0.1',
    description='Infix to post fix',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Joshua Lowe',
    author_email='copyisreal@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='infixtopostfix',
    packages=find_packages(),
    install_requires=['']
)
