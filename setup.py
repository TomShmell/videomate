from setuptools import setup, find_packages
import videomate


setup(
    name='videomate',
    version=videomate.__version__,
    description='Cheap Zoom clone',
    long_description=videomate.__doc__.strip(),
    url='https://github.com/TomShmell/videomate',
    download_url='https://github.com/TomShmell/videomate',
    author=videomate.__author__,
    author_email='dmitry1demetrius@gmail.com',
    license=videomate.__licence__,
    packages=find_packages(),
    extras_require={},
    install_requires=open('requirements.txt', 'r').readlines(),
    tests_require=open('requirements.txt', 'r').readlines(),
    classifiers=[
        'Programming Language :: Python',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development',
        'Topic :: Utilities'
    ]
)
