# 🧠 CortexOS AI Widget

A powerful **AI-powered desktop assistant widget** built with Python and PyQt5.
It stays on top of your screen and helps you automate tasks, interact with AI, and even understand your screen content.

---

## 🚀 Features

### 🤖 AI Chat

* Chat with AI using OpenRouter API
* Fast and lightweight assistant

### 🪟 Floating Widget

* Always-on-top window
* Draggable anywhere on screen
* Minimal and modern UI

### ⚙️ Smart App Launcher

* Open apps with commands like:

  ```
  open chrome
  open vscode
  open calculator
  ```
* Fuzzy matching (even works with typos)

### 🌐 Google Search

* Instantly search anything:

  ```
  search python tutorial
  ```

### 💻 Code Runner / Calculator

* Run simple Python expressions:

  ```
  calculate 25*10
  run 100+200
  ```

### 📂 File Organizer

* Automatically organizes your Downloads folder:

  * Images → Images/
  * PDFs → PDFs/

### 🧠 Screen Reader AI

* Reads your screen using OCR
* Explains what’s on your screen using AI:

  ```
  read screen
  ```

---

## 🛠️ Installation

### 1. Clone the repository

```
git clone https://github.com/shrithannukala10/cortexos-ai-widget.git
cd cortexos-ai-widget
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Install Tesseract OCR

Download and install Tesseract OCR, then update the path in your code:

```
C:\Program Files\Tesseract-OCR\tesseract.exe
```

---

## 🔑 API Setup

This project uses OpenRouter API.

### ⚠️ IMPORTANT

Do NOT hardcode your API key.

Use environment variable:

```
set OPENROUTER_API_KEY=your_api_key_here
```

Then in Python:

```python
import os
API_KEY = os.getenv("OPENROUTER_API_KEY")
```

---

## ▶️ Run the App

```
python app.py
```

---

## 🧪 Example Commands

```
open chrome
search AI news
calculate 50*10
organize files
read screen
```

---

## 🧱 Tech Stack

* Python 🐍
* PyQt5 (GUI)
* OpenRouter API (AI)
* Tesseract OCR (Screen reading)
* PyAutoGUI (Screenshot)

---

## ⚠️ Security Notes

* Uses safe command execution (no arbitrary system commands)
* Avoid exposing API keys publicly
* Designed for local personal use

---

## 🚀 Future Improvements

* 🎤 Voice assistant
* 🖱️ Click automation
* 📌 Mini floating bubble mode
* ⚡ Startup on boot
* 🧠 Real-time screen monitoring

---

## 👨‍💻 Author

Built by you 🚀
(Feel free to customize this section)

---

## ⭐ Support

If you like this project:

* Star ⭐ the repo
* Share it with others
* Improve and build on top of it

---

## 🧠 Vision

CortexOS aims to become a **personal AI operating layer**
that enhances how you interact with your computer.

---
