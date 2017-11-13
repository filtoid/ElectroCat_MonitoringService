from setuptools import setup

setup(name='monitoringservice',
      version='0.1',
      description='Modules for uploading data to the Electro Cat Studios Monitoring Service',
      url='http://github.com/filtoid/ElectroCat_MonitoringService',
      author='Phil Jeffes',
      author_email='phil@electrocatstudios.com',
      license='MIT',
      packages=['monitoringservice'],
      install_requires=[
          'httplib2',
      ],
      zip_safe=False)
