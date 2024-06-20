build:
	docker build -t suds .

run:
	docker run -it --rm suds

clean:
	docker image rm suds
	docker image prune -f
go:
	make build
	make run