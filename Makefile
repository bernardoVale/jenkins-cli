.PHONY: build

build:
	docker build --build-arg builder_home=/${HOME} -t jenkinscli .

release:
	python setup.py bdist_wheel
	twine upload dist/*

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf jenkinscli.egg-info/
