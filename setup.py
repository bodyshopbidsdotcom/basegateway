from distutils.core import setup

setup(
  name = 'basegateway',
  version = '0.3',
  py_modules = ['basegateway', 'oauth2gateway'],
  description = 'A base gateway to make api calls',
  author = 'Snapsheet',
  author_email = 'technotifications@snapsheet.me',
  url = 'https://github.com/bodyshopbidsdotcom/basegateway',
  download_url = 'https://github.com/bodyshopbidsdotcom/basegateway/tarball/0.3',
  keywords = ['api', 'gateway', 'http', 'REST'],
  install_requires = [
    'requests'
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
