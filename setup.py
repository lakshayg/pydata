from setuptools import setup

setup(name = 'pydata',
      version = 0.1,
      description = 'Quickle access datasets from within python',
      url = 'https://github.com/lakshayg/pydata',
      author = 'Lakshay Garg',
      author_email = 'lakshaygarg1996@gmail.com',
      license = 'MIT',
      packages = ['pydata'],
      include_package_data=True,
      zip_safe = False,
      install_requires = [
          'pandas',
          'numpy'
      ]
)

"""
      data_files = [('pydata/data', [
          'pydata/data/banana_data.csv',
          'pydata/data/cifar10/data_batch_1',
          'pydata/data/cifar10/data_batch_2',
          'pydata/data/cifar10/data_batch_3',
          'pydata/data/cifar10/data_batch_4',
          'pydata/data/cifar10/data_batch_5',
      ])],

"""
