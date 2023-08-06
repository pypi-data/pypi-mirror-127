Data Loader Plugin - Python
===========================

# Table of Content (ToC)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

# Overview
The
[data loader plugin](https://github.com/cloud-helpers/python-plugin-data-loader),
aims at supporting running programs (_e.g._, API service backends) when
downloading data from cloud services such as
[AWS S3](https://aws.amazon.com/s3). It provides a base Python library,
namely `data-loader-plugin`,
offering a few methods to download data files from AWS S3.

# References

## Python module
* GitHub:
  https://github.com/cloud-helpers/python-plugin-data-loader/tree/master/data_loader_plugin
* PyPi: https://pypi.org/project/data-loader-plugin/
* Read the Docs (RTD):
  https://readthedocs.org/projects/data-loader-plugin/

## Python virtual environments
* Pyenv and pipenv:
  http://github.com/machine-learning-helpers/induction-python/tree/master/installation/virtual-env

# Installation

## Clone this Git repository
```bash
$ mkdir -p ~/dev/infra && \
  git clone git@github.com:cloud-helpers/python-plugin-data-loader.git ~/dev/infra/python-plugin-data-loader
$ cd ~/dev/infra/python-plugin-data-loader
```

## Python environment
* If not already done so, install `pyenv`, Python 3.9 and, `pip` and `pipenv`
  + PyEnv:
```bash
$ git clone https://github.com/pyenv/pyenv.git ${HOME}/.pyenv
$ cat >> ~/.profile2 << _EOF

# Python
eval "\$(pyenv init --path)"

_EOF
$ cat >> ~/.bashrc << _EOF

# Python
export PYENV_ROOT="\${HOME}/.pyenv"
export PATH="\${PYENV_ROOT}/bin:\${PATH}"
. ~/.profile2
if command -v pyenv 1>/dev/null 2>&1
then
        eval "\$(pyenv init -)"
fi
if command -v pipenv 1>/dev/null 2>&1
then
        eval "\$(pipenv --completion)"
fi

_EOF
$ . ~/.bashrc
```
  + Python 3.9:
```bash
$ pyenv install 3.9.8 && pyenv local 3.9.8
```
  + `pip`:
```bash
$ python -mpip install -U pip
```
  + `pipenv`:
```bash
$ python -mpip install -U pipenv
```

# Usage

## Install the `data-loader-plugin` module
* There are at least two ways to install the `data-loader-plugin` module,
  in the Python user space with `pip` and in a dedicated virtual environment
  with `pipenv`.
  + Both options may be installed in parallel
  + The Python user space (typically, `/usr/local/opt/python@3.9` on MacOS
    or `~/.pyenv/versions/3.9.8` on Linux) may already have many other modules
	installed, parasiting a fine-grained control over the versions of every
	Python dependency. If all the versions are compatible, then that option
	is convenient as it is available from the whole user space, not just
	from this sub-directory

* In the remainder of that [Usage section](#usage), it will be assumed
  that the `data-loader-plugin` module has been installed and readily
  available from the environment, whether that environment is virtual
  or not.
  In other words, to adapt the documentation for the case where `pipenv`
  is used, just add `pipenv run` in front of every Python-related command.

### Install in the Python user space
* Install and use the `data-loader-plugin` module in the user space
  (with `pip`):
```bash
$ python -mpip uninstall data-loader-plugin
$ python -mpip install -U data-loader-plugin
```

### Installation in a dedicated Python virtual environment
* Install and use the `data-loader-plugin` module in a virtual environment:
```bash
$ pipenv shell
(python-...-JwpAHotb) ✔ python -mpip install -U data-loader-plugin
(python-...-JwpAHotb) ✔ python -mpip install -U data-loader-plugin
(python-...-JwpAHotb) ✔ exit
```

## Use `data-loader-plugin` as a module from another Python program
* Check the data file with the AWS command-line (CLI):
```bash
$ aws s3 ls --human s3://nyc-tlc/trip\ data/yellow_tripdata_2021-07.csv --no-sign-request
2021-10-29 20:44:34  249.3 MiB yellow_tripdata_2021-07.csv
```

* Module import statements:
```python
>>> import importlib
>>> from types import ModuleType
>>> from data_loader_plugin.base import DataLoaderBase
```

* Create an instance of the DataLoaderBase Python class:
```python
>>> plugin: ModuleType = importlib.import_module("data_loader_plugin.copyfile")
>>> data_loader: DataLoaderBase = plugin.DataLoader(
        local_path='/tmp/yellow_tripdata_2021-07.csv',
        external_url='s3://nyc-tlc/trip\ data/yellow_tripdata_2021-07.csv',
    )
>>> data_load_success, message = data_loader.load()
```

# Development / Contribution
* Build the source distribution and Python artifacts (wheels):
```bash
$ rm -rf _skbuild/ build/ dist/ .tox/ __pycache__/ .pytest_cache/ MANIFEST *.egg-info/
$ pipenv run python setup.py sdist bdist_wheel
```

* Upload to Test PyPi (no Linux binary wheel can be uploaded on PyPi):
```bash
$ PYPIURL="https://test.pypi.org"
$ pipenv run twine upload -u __token__ --repository-url ${PYPIURL}/legacy/ dist/*
Uploading distributions to https://test.pypi.org/legacy/
Uploading datamonitor-0.0.4-py2.py3-none-any.whl
100%|███████████████████████████████████████| 9.85k/9.85k [00:02<00:00, 4.48kB/s]
Uploading datamonitor-0.0.4.tar.gz
100%|███████████████████████████████████████| 18.8k/18.8k [00:01<00:00, 17.1kB/s]

View at:
https://test.pypi.org/project/datamonitor/0.0.4/
```

* Upload/release the Python packages onto the
  [PyPi repository](https://pypi.org):
  + Register the authentication token for access to PyPi:
```bash
$ PYPIURL="https://upload.pypi.org"
$ pipenv run keyring set ${PYPIURL}/ __token__
Password for '__token__' in '${PYPIURL}/':
```
  + Register the authentication token for access to PyPi:
```bash
$ pipenv run twine upload -u __token__ --repository-url ${PYPIURL}/legacy/ dist/*
Uploading distributions to https://upload.pypi.org/legacy/
Uploading datamonitor-0.0.4-py2.py3-none-any.whl
100%|███████████████████████████████████████| 11.5k/11.5k [00:02<00:00, 5.84kB/s]
Uploading datamonitor-0.0.4.tar.gz
100%|███████████████████████████████████████| 20.7k/20.7k [00:01<00:00, 15.8kB/s]

View at:
https://pypi.org/project/datamonitor/0.0.4/
```

* Note that the documentation is built automatically by ReadTheDocs (RTD)
  + The documentation is available from
    https://datamonitoring.readthedocs.io/en/latest/
  + The RTD project is setup on https://readthedocs.org/projects/datamonitoring/
  + As of July 2020, the documentation is built from RST files, _e.g._,
    [`README.rst`](https://github.com/infra-helpers/induction-monitoring/blob/master/python/datamonitor/README.rst)
	and documentation files in the
	[`docs` sub-directory](https://github.com/infra-helpers/induction-monitoring/blob/master/python/datamonitor/docs/).
	The author is a lot more familiar with MarkDown (MD) format,
	and would welcome help in translating the documentation generation
	configuration to use MD- rather than RST-based files.
	Do not hesitate to
	[create an issue](https://github.com/infra-helpers/induction-monitoring/issues)
	or, even better, submit a
	[pull request](https://github.com/infra-helpers/induction-monitoring/pulls)

* Build the documentation manually (with [Sphinx](http://sphinx-doc.org)):
```bash
$ pipenv run python setup.py build_sphinx
running build_sphinx
Running Sphinx v3.1.1
loading pickled environment... done
building [mo]: targets for 0 po files that are out of date
building [html]: targets for 9 source files that are out of date
updating environment: [new config] 9 added, 0 changed, 0 removed
looking for now-outdated files... none found
no targets are out of date.
build succeeded.

The HTML pages are in build/sphinx/html.
```

* Re-generate the Python dependency files (`requirements.txt`)
  for the CI/CD pipeline (currently Travis CI):
```bash
$ pipenv --rm; rm -f Pipfile.lock; pipenv install; pipenv install --dev
$ git add Pipfile.lock
$ pipenv lock -r > datamonitor/ci/requirements.txt
$ pipenv lock --dev -r > datamonitor/ci/requirements-dev.txt
$ git add datamonitor/ci/requirements.txt datamonitor/ci/requirements-dev.txt
$ git commit -m "[CI] Upgraded the Python dependencies for the Travis CI pipeline"
```

## Test the DataMonitor Python module
* The tests use [ElasticMock](https://github.com/vrcmarcos/elasticmock),
  which emulates, in a very simple and limited way, an Elasticsearch (ES)
  cluster/service.

* If ES cluster/service is already running locally on the ES default port
  (9200), it must be temporarily shutdown, as the default parameters for
  ElasticMock would otherwise have both ES services step on each other toes.
  For instance:
  + On MacOs, `brew stop elasticsearch-full` (and
    `brew start elasticsearch-full` to restart it afterwards)
  + On SystemD-based Linux distributions, `sudo systemctl stop elasticsearch`
    (and `sudo systemctl start elasticsearch` to restart afterwards)

* Enter into the `pipenv` Shell:
```bash
$ pipenv shell
(python-iVzKEypY) ✔ python -V
Python 3.8.3
```

* Uninstall any previously installed `datamonitor` module/library:
```bash
(python-iVzKEypY) ✔ python -m pip uninstall datamonitor
```

* Launch a simple test with `pytest`
```bash
(python-iVzKEypY) ✔ python -m pytest test_datamonitor.py
=================== test session starts ===========================
platform darwin -- Python 3.8.3, pytest-5.4.3, py-1.9.0, pluggy-0.13.1
rootdir: ~/dev/infra/induction-monitoring/python/datamonitor, inifile: setup.cfg
collected 1 item
datamonitor/tests/test_datamonitor.py

========================== 1 passed in 0.06s ======================
```

* Check that a document has been created on ES. When the ES service is made
  from a single node (_e.g._, on a laptop or a local installation), the status
  of the index will be yellow. That is because the documents cannot be
  replicated:
```bash
(python-iVzKEypY) ✔ curl -XGET http://localhost:9200/_cat/indices/dm-test-v0
yellow open dm-test-v0 GXEUJjtkRjev3_wSn-5HOg 1 1 1 0 3.7kb 3.7kb
```

* Drop the replication requirement:
```bash
(python-iVzKEypY) ✔ curl -XPUT http://localhost:9200/dm-test-v0/_settings -H "Content-Type: application/json" --data "@../elasticseearch/settings/kibana-read-only.json"
```

* Check again the status of the `dm-test-v0` index, which should have become
  green:
```bash
(python-iVzKEypY) ✔ curl -XGET http://localhost:9200/_cat/indices/dm-test-v0
green open dm-test-v0 GXEUJjtkRjev3_wSn-5HOg 1 0 1 0 3.8kb 3.8kb
```

* Exit the `pipenv` Shell:
```bash
(python-iVzKEypY) ✔ exit
```

* To run all the tests:
```bash
$ pipenv run tox
```

