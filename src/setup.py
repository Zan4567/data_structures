from setuptools import setup

setup (
  #metadata keyword args
  name ="packagename",
  description="A description of what this package does",
  version=0.1,
  author="Kevin Robinson",
  author_email="arealname@thisisanemail.net",
  package_dir={'': 'src'},
  my_modules=['packagename'],
  install_requires=['other_distribution', 'another_one'],
  extras_require={
    'test': ['pytest', 'pytest-watch', 'pytest-cov'],
    'development': ['ipython']
  },
  entry_points={
    "exec_name = module_path:fn_name"
  }
)
