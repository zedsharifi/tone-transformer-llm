# 🎭 Few-Shot Prompting Tone Transformation Chatbot using Offline LLMs

This project is a comprehensive exploration of a **tone transformation system in Persian** that leverages offline, open-source **Large Language Models (LLMs)** to rewrite text, matching the tone and style of a reference text while preserving the original meaning.

The system is implemented as an **interactive web-based chatbot** using a Flask backend, allowing users to select from several powerful models and see the tone transformation in real-time.

---

## ✨ Features

* **Dynamic Tone Transformation**
  Analyzes the style (formality, emotion, etc.) of a *reference text* and applies it to a *target text*.

* **Offline Model Support**
  Utilizes locally-run LLMs via the [Ollama](https://ollama.ai) platform, ensuring privacy and removing dependency on external APIs.

* **Multiple LLM Integration**
  Compare the performance of several powerful open-source models:

  * Meta Llama 3 (8B)
  * Meta Llama 3.2 (3B)
  * Qwen 2.5 (7B)
  * Google Gemma (2B)

* **Advanced Prompt Engineering**
  Employs a *Few-Shot Prompting* technique with structured examples to guide models for accurate and context-aware outputs.

* **Interactive Web Interface**
  A user-friendly chatbot interface built with **HTML, CSS, and JavaScript** for seamless interaction.

---

## 🤖 How It Works

The core of the project is a **sophisticated prompt** designed to instruct the LLM on its task.
The model is given:

1. **Task Definition**
   It’s told to act like an actor who must deliver the message of the *Target Text* with the emotion and style of the *Reference Text*.

2. **Clear Instructions**
   A step-by-step guide on how to analyze tone, preserve meaning, and rewrite the text using its own vocabulary.
   ⚠️ **Critical rule**: The model cannot copy words from the reference text.

3. **Few-Shot Examples**
   Demonstrates how to handle different scenarios, such as:

   * Neutral → Negative
   * Informal → Formal
   * Happy → Serious

The Flask backend receives the **reference text**, **target text**, and **model selection**, then injects this information into the prompt and sends it to the locally running LLM via the Ollama API.

---

## 🛠️ Technology Stack

* **Backend:** Python, Flask
* **LLM Platform:** Ollama
* **Frontend:** HTML, CSS, JavaScript
* **Models:** Llama 3, Llama 3.2, Qwen 2.5, Gemma

---

## 🚀 Getting Started

Follow these steps to set up and run the project locally.

### Prerequisites

* Python **3.8+**
* [Ollama](https://ollama.ai) installed and running
* An active **Conda environment**

---

### 1. Clone the Repository

```
git clone https://github.com/zedsharifi/tone-transformer-llm.git
cd tone-transformer-llm
```

---

### 2. Set Up Ollama and Pull Models

Make sure Ollama is running, then pull the required models:

```
ollama pull llama3
ollama pull llama3.2:3b-instruct-q8_0
ollama pull qwen2.5:7b-instruct
ollama pull gemma:2b
```

---

### 3. Create Conda Environment and Install Dependencies

```
# Create a new environment
conda create --name tone-env python=3.9

# Activate the environment
conda activate tone-env

# Install required packages
pip install -r requirements.txt
```

---

### 4. Run the Application

Make sure your Conda environment is active, then:

```
python app/main.py
```

The app will be available at:
👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 💡 Usage

1. Open the web interface in your browser.
2. Select your desired model from the dropdown menu.
3. In the **"متن مرجع را وارد کنید..."** (*Enter Reference Text*) box, paste the text with the desired tone.
4. In the **"متن هدف را وارد کنید..."** (*Enter Target Text*) box, paste the text you want to rewrite.
5. Click the **Send** button and wait for the model to generate the response.
