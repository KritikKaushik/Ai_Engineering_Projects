# Groq API with Python 🚀

A beginner-friendly collection of Python examples demonstrating how to use the **Groq Python SDK** for building AI-powered applications. This repository covers everything from basic chat completions to structured JSON outputs using Pydantic.

## 📌 Features

* Load API keys securely using `.env`
* Generate chat completions
* Use **System** and **User** messages
* Compare token usage
* Understand finish reasons (`stop`, `length`, etc.)
* Generate structured JSON responses
* Use **Pydantic** for schema definition
* Well-commented code for easy learning

---

## 📂 Project Structure

```text
.
├── .env                 # Stores the Groq API Key
├── basic_chat.py        # Simple chat completion example
├── system_prompt.py     # Using system prompts
├── token_usage.py       # Token usage and finish reason example
├── structured_output.py # Structured JSON output using Pydantic
├── requirements.txt
└── README.md
```

> File names are examples—rename this section if your filenames differ.

---

## ⚙️ Prerequisites

* Python 3.9+
* A Groq API Key

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/<your-repository>.git
cd <your-repository>
```

### 2. Create a virtual environment

#### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Running the Examples

Run any script using:

```bash
python filename.py
```

For example,

```bash
python basic_chat.py
```

---

## 📖 Topics Covered

### 1. Basic Chat Completion

* Sending prompts to Groq models
* Reading generated responses

---

### 2. System Prompts

Learn how to control model behavior by defining a system message.

Example:

```text
You are an extreme climate enthusiast and a weather expert.
```

---

### 3. Token Usage

Understand how many tokens are consumed for:

* Prompt Tokens
* Completion Tokens
* Total Tokens

Also learn about the completion finish reason.

Example output:

```text
Prompt Tokens: 18
Completion Tokens: 52
Total Tokens: 70
Finish Reason: stop
```

---

### 4. Structured Output

Learn how to:

* Define schemas using Pydantic
* Request JSON responses
* Parse structured AI outputs

Example schema:

```python
class CustomerTicket(BaseModel):
    name: str
    problem: str
    course_resolution: bool
    chat_support: bool
    phone_number: str
```

Example output:

```json
{
  "name": "Kritik",
  "problem": "DSA",
  "course_resolution": true,
  "chat_support": true,
  "phone_number": "898989898989"
}
```

---

## 📚 Technologies Used

* Python
* Groq Python SDK
* Pydantic
* python-dotenv

---

## 📦 Install Dependencies

```bash
pip install groq python-dotenv pydantic
```

or

```bash
pip install -r requirements.txt
```

---

## 🎯 Learning Goals

This repository is intended for developers who want to learn:

* Groq API fundamentals
* Prompt engineering basics
* System prompts
* Token accounting
* Structured outputs
* Best practices for organizing AI projects

---

## 🤝 Contributing

Contributions, improvements, and suggestions are welcome. Feel free to fork the repository and open a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you found this repository helpful, consider giving it a ⭐ on GitHub.
