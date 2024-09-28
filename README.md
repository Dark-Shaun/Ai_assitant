# AI Assistant Chatbot

This project is an AI-powered chatbot built with Django and the Hugging Face Transformers library. It uses the BlenderBot model to generate weird responses to user queries.

## Features

- Web-based chat interface
- AI-powered responses using the BlenderBot model
- Dark mode support
- Code highlighting for various programming languages

## Prerequisites

- Python 3.8+
- Django 3.2+
- PyTorch 1.13+
- Transformers 4.30+

## Installation

1. Clone the repository:
   ```
   git clone git_url
   cd ai-assistant-chatbot
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the project root and add the following:
   ```
   SECRET_KEY=your_django_secret_key
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```

5. Run migrations:
   ```
   python manage.py migrate
   ```

6. Start the development server:
   ```
   python manage.py runserver
   ```

7. Open your browser and navigate to `http://localhost:8000` to use the chatbot.

## Project Structure
