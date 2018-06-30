build:
	docker-compose build

fresh:
	docker-compose build --no-cache

run:
	docker-compose run --rm econ_sim

test:
	docker-compose run --rm econ_sim -c "pip install -e . && pytest -vv -s"
