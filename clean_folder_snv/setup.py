from setuptools import setup, find_namespace_packages

setup(name='clean_folder_snv',
      version='0.0.1',
      description='Very useful code',
      author='Nataliia Shvab',
      author_email='shnataliya77@gmail.com',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['clean_folder = clean_folder_snv.clean:main']}
      )