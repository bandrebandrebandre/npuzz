from setuptools import setup, find_packages

VERSION = '1.0'

requires = ['docopt']

setup(name='npuzz',
      version=VERSION,
      description='n-puzzle',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      entry_points="""\
      [console_scripts]
      run_search_one = npuzz.scripts.run_search:run_search_one
      run_search_two = npuzz.scripts.run_search:run_search_two
      compile_stats = npuzz.scripts.run_search:compile_stats
      """,
      )
