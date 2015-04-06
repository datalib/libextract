from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='libextract',
      version='0.0.104',
      description='tiny \'autocomplete\' tool using a "hidden markov model"',
      keywords='extract extraction main article text html data-extraction data\
                content-extraction content unsupervised classification',
      author='Rodrigo Palacios, ',
      author_email='rodrigopala91@gmail.com, ',
      license='MIT',
      packages=['libextract'],
      url='https://github.com/libextract/libextract',
      scripts=[],
      package_data={},
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True,
      zip_safe=False)
