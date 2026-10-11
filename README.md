# Pytest API Framework

API automation framework using pytest and requests, tested against jsonplaceholder.

## Setup
pip install -r requirements.txt

## Run
pytest -v
pytest -m smoke -v

## Structure
- conftest.py: shared fixtures (base_url, api_session)
- tests/: GET, POST, negative tests
- pytest.ini: markers and config