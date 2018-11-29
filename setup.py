from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='vmaudit',
      version='0.1',
      description='Audit your vms with ease',
      long_description=readme(),
      long_description_content_type='text/markdown',
      url='https://github.com/jmiahman/webapi-fun',
      author='JMiahMan',
      author_email='JMiahMan@unity-linux.org',
      license='MIT',
      packages=['vmaudit'],
      include_package_data=True,
      zip_safe=False,
      scripts=['vmaudit/vm-audit'],
      data_files=[('/etc', ['vmaudit/vm-audit.cfg']),
                  ('/usr/bin', ['vmaudit/vm-audit'])]
      )
