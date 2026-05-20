.PHONY: verify compile lint consistency

PYTHON ?= python3

verify: compile lint consistency

compile:
	@$(PYTHON) -m compileall -q scripts

lint:
	@$(PYTHON) -c "import ruff" >/dev/null 2>&1 || { \
		echo "ruff is required. Install it with: python -m pip install ruff"; \
		exit 1; \
	}
	@$(PYTHON) -m ruff check .

consistency:
	@$(PYTHON) scripts/check_consistency.py
