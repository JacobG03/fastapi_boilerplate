# FastAPI Boilerplate Code

## Linux Setup

### Create .env file

    touch .env
    
    Write out
    DATABASE_URL="<Database URL or leave empty string>"
    and save file.

### Create Virtual Environment

    python3 -m venv venv

### Activate Virtual Environment

    source venv/bin/activate
    
### Install dependencies
    
    pip install -r requirements.txt

### Run Initialiser

    python3 -m app.initialiser

### Run Server

    uvicorn app.main:app --reload --host=0.0.0.0

## Windows & Mac Setup

Use google if any issues occur.
