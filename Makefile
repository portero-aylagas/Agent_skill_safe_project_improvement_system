.PHONY: verify compile consistency

PYTHON ?= python3

verify: compile consistency

compile:
	@$(PYTHON) -m compileall -q scripts

consistency:
	@$(PYTHON) scripts/check_consistency.py
