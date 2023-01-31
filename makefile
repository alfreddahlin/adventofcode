year=$(shell date +'%Y')
day=$(shell date +'%d')

.DEFAULT_GOAL := solve
.PHONY: init setup solve

init:
	@pip install -r requirements.txt

setup:
	@aoc/start_solving.sh ${year} ${day}

test:
	@python -m aoc.${year}.day${day} test

solve:
	@python -m aoc.${year}.day${day}
