IMAGE_NAME ?= manager
IMAGE_TAG ?= latest

#
#
#
all:
	/bin/echo -e "\nPlease run with 'make build'\n"

build_cached:
	docker build --cache-from=${IMAGE_NAME}:${IMAGE_TAG} -t ${IMAGE_NAME}:${IMAGE_TAG} .

build:
	docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
