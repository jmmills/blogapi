

all: image

image:
	docker build -t jmmills/blogapi:latest .

test: image
	docker run -v $(PWD):/source blogapi nosetests --with-coverage --cover-package=blog/ --cover-branches --cover-erase --cover-xml --cover-xml-file=/source/coverage.xml test/units/



