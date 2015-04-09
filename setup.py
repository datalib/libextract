from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='libextract',
    version='0.0.0',
    url='https://github.com/libextract/libextract',
    license='MIT',
    description='A ridiculously simple HT/XML article-text extractor',
    packages=['libextract', 'libextract.html'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'chardet>=2.3.0',
        'lxml>=3.4.2',
    ],
    keywords='extract extraction main article text html data-extraction data\
              content-extraction content unsupervised classification',
    author='Rodrigo Palacios, ',
    author_email='rodrigopala91@gmail.com, ',
    scripts=[],
    package_data={},
    test_suite='nose.collector',
    tests_require=['nose'],
)
