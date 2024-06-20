# Langchain test task

## Setup
1. Create a virtual environment

```cmd
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
2. Install dependencies

```cmd
pip install -r requirements.txt
```

3. Run webserver

```cmd
uvicorn main:app
```

## Test the app

```cmd
python tests\test_requests.py
```

## Whant to try other text or model?

1. If you want to try another model you have 2 ways
    - Change default value in summarizer class `model_id`
    - Specify `custom_model_id` in SimpleSummarizer constructor in summarize endpoint
2. If you want to try another text to test just change `test_text` in tests\test_requests.py file
