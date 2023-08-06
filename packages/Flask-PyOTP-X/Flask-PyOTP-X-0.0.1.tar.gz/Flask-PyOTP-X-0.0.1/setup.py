from setuptools import setup

setup(
    name='Flask-PyOTP-X',
    version='0.0.1',
    url='https://github.com/khub-app/flask-pyotp',
    license='MIT',
    author='Tornike Natsvlishvili',
    author_email='tornikenatsvlishvilideveloper@gmail.com',
    maintainer='Faizan Alhassan',
    maintainer_email='faizanalhassan@gmail.com',
    description='PyOTP warpper for flask.',
    long_description=__doc__,
    packages=['flask_pyotp'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask>=0.10',
        'pyotp'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',

        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Topic :: Security',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='otp mfa flask pyotp'
)
