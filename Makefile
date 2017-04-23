build:
	docker build --build-arg builder_home=/${HOME} -t jenkinscli .

release:
	python setup.py bdist_wheel
	twine upload dist/*
