local/shell:
	source .venv/bin/activate

local/sync:
	uv sync

local/tests:
	uv run pytest --cov-report html  --cov=functasticpy tests/