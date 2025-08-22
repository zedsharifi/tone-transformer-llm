# Tone Transformation Chatbot using Offline LLMs
This project is a comprehensive exploration of a tone transformation system that leverages offline, open-source Large Language Models (LLMs) to rewrite text, matching the tone and style of a reference text while preserving the original meaning.

The system is implemented as an interactive web-based chatbot using a Flask backend, allowing users to select from several powerful models and see the tone transformation in real-time.

✨ Features
Dynamic Tone Transformation: Analyzes the style (formality, emotion, etc.) of a "reference text" and applies it to a "target text."

Offline Model Support: Utilizes locally-run LLMs via the Ollama platform, ensuring privacy and removing dependency on external APIs.

Multiple LLM Integration: Allows users to compare the performance of several powerful open-source models:

Meta Llama 3 (8B)

Meta Llama 3.2 (3B)

Qwen 2.5 (7B)

Google Gemma (2B)

Advanced Prompt Engineering: Employs a Few-Shot Prompting technique with structured examples to guide the models for accurate and context-aware outputs.

Interactive Web Interface: A user-friendly chatbot interface built with HTML, CSS, and JavaScript for seamless interaction.

🤖 How It Works
The core of the project is a sophisticated prompt designed to instruct the LLM on its task. The model is given the following:

A Task Definition: It's told to act like an actor who must deliver the message of the Target Text with the emotion and style of the Reference Text.

Clear Instructions: A step-by-step guide on how to analyze tone, preserve meaning, and rewrite the text using its own vocabulary. A critical rule is that it cannot use words from the reference text.

Few-Shot Examples: Several examples demonstrate how to handle different scenarios, such as transforming a neutral statement to a negative one, or an informal sentence to a formal one.

The Flask backend receives the user's reference text, target text, and model selection. It injects this information into the prompt and sends the complete request to the selected LLM running locally via the Ollama API.

🛠️ Technology Stack
Backend: Python, Flask

LLM Platform: Ollama

Frontend: HTML, CSS, JavaScript

Models: Llama 3, Llama 3.2, Qwen 2.5, Gemma

🚀 Getting Started
Follow these instructions to set up and run the project locally.

Prerequisites
Python 3.8+

Ollama installed and running.

An active Conda environment.

1. Clone the Repository
git clone https://github.com/zedsharifi/tone-transformer-llm.git
cd tone-transformer-llm

2. Set Up Ollama and Pull Models
Ensure the Ollama application is running. Then, pull the models used in this project from the command line:

ollama pull llama3
ollama pull llama3.2:3b-instruct-q8_0
ollama pull qwen2.5:7b-instruct
ollama pull gemma:2b

3. Create Conda Environment and Install Dependencies
If you haven't already, create and activate a Conda environment for this project.

# Create a new environment
conda create --name tone-env python=3.9

# Activate the environment
conda activate tone-env

# Install the required packages from the requirements.txt file
pip install -r requirements.txt

4. Run the Application
Make sure your tone-env Conda environment is active.

python app/main.py

The application will be available at http://127.0.0.1:5000. Open this URL in your web browser to start using the chatbot.

Usage
Open the web interface in your browser.

Select your desired model from the dropdown menu.

In the "متن مرجع را وارد کنید..." (Enter Reference Text) box, type or paste the text that has the desired tone.

In the "متن هدف را وارد کنید..." (Enter Target Text) box, type or paste the text you want to rewrite.

Click the send button and wait for the model to generate the response.
