from distutils.core import setup

setup(name='vs_pbf',
      version='.1',
      description="Programmer's Best Friend Utility Extension for vs_pbf",
      author='', # Add your name here
      author_email='', # Add your e-mail here
      packages=['vs_pbf', 'vs_pbf.Commands', 'vs_pbf.templates'],
      #package_data = {'vs_pbf.templates':[]}, # Add template files
     )