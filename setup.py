from distutils.core import setup

CURRENT_VERSION = '0.13'

setup(
  name = 'basegateway',
  version = CURRENT_VERSION,
  py_modules = ['basegateway', 'oauth2gateway'],
  description = 'A base gateway to make api calls',
  author = 'Snapsheet',
  author_email = 'technotifications@snapsheet.me',
  url = 'https://github.com/bodyshopbidsdotcom/basegateway',
  download_url = 'https://github.com/bodyshopbidsdotcom/basegateway/tarball/{0}'.format(CURRENT_VERSION),
  keywords = ['api', 'gateway', 'http', 'REST'],
  install_requires = [
    'requests>=2.9.1'
  ],
  classifiers = [
    "Topic :: Internet :: WWW/HTTP",
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
)
