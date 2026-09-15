# YouTube Keyword Search

A small FastAPI endpoint that searches YouTube with Selenium and returns titles from the first ten result elements.

## Overview

The route opens Chrome, submits the supplied keyword to YouTube, waits briefly, collects visible video titles, and closes the browser. It is a browser automation example; it does not use the YouTube Data API.

## Tech stack

Python, FastAPI, Selenium, ChromeDriver (through webdriver-manager), and Uvicorn.

## Structure

- `main.py` — FastAPI application.
- `api/v1/searchable.py` — search route and Selenium workflow.

## Installation and usage

Install Chrome and Python, then run:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

On Windows activate with `.venv\Scripts\activate`. Open `http://127.0.0.1:8000/docs` or request `GET /KEY_WORD_FINDER?titile=FastAPI`. The existing parameter name is `titile` (a typo kept for compatibility). Response shape is `{"result": [...]}`.

## Configuration and limitations

No API key or environment variable is read by the current code. ChromeDriver is downloaded by webdriver-manager at runtime. Search results depend on YouTube's page markup and a fixed five-second wait; dynamic content and headless/server deployment have not been verified. Exceptions are returned as error text instead of an HTTP error status.
