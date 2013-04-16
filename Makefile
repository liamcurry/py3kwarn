all:
	@echo "Use 'make install' to install."

build:
	python setup.py build

install:
	python setup.py install

clean:
	rm -Rf build dist
	find . -name "*.pyc" -or "*.egg-info" -delete

test:
	python -m py3kwarn.tests

.PHONY: test all
