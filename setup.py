from setuptools import setup

setup(
    name='Linked List',
    description='Create a Linked List',
    package_dir={'': 'src'},
    author=' Kevin Robinson & Darren Haynes',
    author_email='dummy-email@zoho.com',
    py_modules=[],
    install_requires=[],
    extras_require={
        'testing': ['pytest', 'pytest-cov', 'pytest-watch', 'tox'],
        'development': ['ipython']
    },
    entry_points={
        'console_scripts': {
            'mailroom=mailroom:main'
        }
    }
)
