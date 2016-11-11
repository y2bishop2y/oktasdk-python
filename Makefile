
SOURCE_DIR=okta
PACKAGE_NAME=okta

clean:
	@find . -name \*.pyc -exec rm {} \;
	@find . -name "results.xml" -exec rm {} \;
	@find . -name "pylint.log" -exec rm {} \;
	@find . -name "clonedigger.xml " -exec rm {} \;
	@find . -name \*.py,cover -exec rm {} \;
	@find . -name  *.py,cover | xargs rm -f 	
	@rm -rf .eggs *.egg *.egg-info	
	@rm -rf ./${SOURCE_DIR}/htmlcov
	@rm -rf ./${SOURCE_DIR}/coverage.xml
	@rm -rf ./${SOURCE_DIR}/.coverage
	@rm -rf ./${SOURCE_DIR}/*_uwsgi.log
	@rm -rf ./logs 
	@rm -rf ./htmlcov coverage.xml .coverage


###############################################################################
#
#	Packaging 
#
package: clean
	python setup.py sdist

install:
	pip install -r requirements/repo.txt; \
	python setup.py install

uninstall:
	pip uninstall -y requirements/repo.txt; \
	pip uninstall -y $(PACKAGE_NAME)





###############################################################################
#
#	Reporting
#
# 	pylint -f parseable -i y -r y $(SOURCE_DIR)/| \

lint:
	pylint -f parseable  -r y src/*.py src/lib/*.py src/lib/config_splunk/*.py src/lib/env/*.py src/lib/ping/*.py src/lib/shard/*.py *.py | \
		tee tests/pylint.log

flake8:
	flake8 --exit-zero  --max-complexity 12 $(SOURCE_DIR)/*.py tests/*.py *.py | \
		awk -F\: '{printf "%s:%s: [E]%s\n", $$1, $$2, $$3}' | tee tests/flake8.log

pep8: flake8

clonedigger: 
	clonedigger --output tests/clonedigger.xml --cpd-output tests/




###############################################################################
#
#	Testing
# add clonedigger
test: clean lint  
	@echo "Running unit tests"
	export PYTHONPATH=${PYTHONPATH}:${SOURCE_DIR} && \
	pytest --cov=${SOURCE_DIR} tests/ \
	    --junitxml=tests/results.xml \
	    --cov-report html \
	    --cov-report xml \
	    --cov-report annotate \
	    --cov-report term-missing


