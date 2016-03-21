from setuptools import setup, find_packages

VERSION = '1.0'

requires = []

setup(name='npuzz',
      version=VERSION,
      description='n-puzzle',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      extras_require={
          'testing': testing_extras,
      },
      entry_points="""\
      [console_scripts]
      run_search = npuzz.scripts.run_search:main
      """,
      )
