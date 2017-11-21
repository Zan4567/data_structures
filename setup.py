from setuptools import setup

setup(
    name='bst',
    description='Module for a binary search tree',
    package_dir={'': 'src'},
    author=' Kevin Robinson',
    author_email='...',
    py_modules=[],
    install_requires=[],
    extras_require={
        'testing': ['pytest', 'pytest-cov', 'pytest-watch', 'tox'],
        'development': ['ipython']
    },
    entry_points={
        'console_scripts': {
            'bst=bst:main'
        }
    }
)
