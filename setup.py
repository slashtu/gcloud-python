import sys


try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages


if sys.version_info <= (2, 4):
    ERROR = 'Requires Python Version 2.5 or above... exiting.'
    print >> sys.stderr, ERROR
    sys.exit(1)


REQUIREMENTS = [
    'httplib2',
    'oauth2client',
    'protobuf >= 2.5.0',
    'pycrypto',
    'pyopenssl',
    'pytz',
]

setup(
    name='gcloud',
    version='0.02.2',
    description='API Client library for Google Cloud',
    author='JJ Geewax',
    author_email='jj@geewax.org',
    scripts=[],
    url='https://github.com/GoogleCloudPlatform/gcloud-python',
    packages=find_packages(),
    license='Apache 2.0',
    platforms='Posix; MacOS X; Windows',
    package_data={'': ['gcloud/datastore/demo.key',
                       'gcloud/storage/demo.key']},
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIREMENTS,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet',
    ]
)
