# FastAPI-OpenAI-Chatbot

This project is a FastAPI application integrated with OpenAI's API for generating text responses. It demonstrates setting up a virtual environment, installing dependencies, and creating a simple API with FastAPI.

## Setup Instructions

1. **Create .env File:** 

Create a new file in this directory called `.env` and copy your OpenAI API key into an environment variable like this:

```sh
OPENAI_KEY=<<your-api-key>>
```

The `.env` file will be ignored by Git to ensure you don't check in these two values to source control.
Make sure to add .env to your .gitignore to prevent it from being pushed to your repository.

## Deployment

1. **Create a virtual environment:**
   ```bash
   python3 -m venv fastenv

2. **Activate the virtual environment:**
source fastenv/bin/activate

3. **Install the dependencies:**
pip install -r ./app/requirements.txt
