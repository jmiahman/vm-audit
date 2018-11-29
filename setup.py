from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='vmaudit',
      version='0.0.2',
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
      data_files=[('/etc', ['vmaudit/vm-audit.cfg']),
                  ('/usr/bin', ['vmaudit/vm-audit']),
                  ('/var/cache/vm-audit', []),
                  ('/var/log/vm-audit', [])]
      )
