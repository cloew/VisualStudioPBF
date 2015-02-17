from distutils.core import setup

setup(name='pbf_vs',
      version='.2',
      description="Programmer's Best Friend Utility Extension for Visual Studio",
      author='Chris Loew',
      author_email='cloew123@gmail.com',
      packages=['pbf_vs',
                'pbf_vs.Commands',
                'pbf_vs.templates',
                'pbf_vs.helpers'],
      #package_data = {'pbf_vs.templates':[]}, # Add template files
     )