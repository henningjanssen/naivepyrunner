from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='naivepyrunner',
      version='0.1',
      description='Naive timed execution of custom handlers in multiple threads',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities'
      ],
      url='http://github.com/henningjanssen/naivepyrunner',
      author='Henning Janßen',
      author_email='development@henning-janssen.net',
      license='MIT',
      packages=['naivepyrunner'],
      install_requires=[],  # built-ins only
      zip_safe=False)
