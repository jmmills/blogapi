

all: image

image:
	docker build -t jmmills/blogapi:latest .

test: image
	docker run -v $(PWD):/source -e COVERAGE_FILE=/source/.coverage jmmills/blogapi:latest nosetests -v --with-coverage --cover-package=blog/ --cover-branches --cover-html --cover-html-dir=/source/coverage-report test/units/

clean-coverage:
	rm .coverage
	rm -rf coverage-report/

clean: clean-coverage
	docker rmi jmmills/blogapi:latest
