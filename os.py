import sys
import requests
import os
import webbrowser
import shutil
import difflib
import pyautogui
import pytesseract
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QTextEdit, QLineEdit, QPushButton
)
from PyQt5.QtCore import Qt, QPoint

# 🔑 API KEY
API_KEY = "paste_your_api_key"

url = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# 🔧 Tesseract path (CHANGE if needed)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# 🧠 APPS
APPS = {
    "chrome": "start chrome",
    "notepad": "notepad",
    "calculator": "calc",
    "cmd": "start cmd",
    "files": "explorer",
    "vscode": "code",
    "paint": "mspaint"
}

def find_app(user_input):
    matches = difflib.get_close_matches(user_input, APPS.keys(), n=1, cutoff=0.5)
    return matches[0] if matches else None

def open_app_smart(user_input):
    app_name = user_input.replace("open ", "").strip()
    match = find_app(app_name)
    if match:
        os.system(APPS[match])
        return f"⚙️ Opening {match}"
    return "❌ App not found"

# 🌐 SEARCH
def google_search(query):
    query = query.replace("search", "").strip()
    webbrowser.open(f"https://www.google.com/search?q={query}")

# 💻 CALC
def run_code(code):
    try:
        return str(eval(code))
    except:
        return "⚠️ Invalid expression"

# 📂 ORGANIZE
def organize_files():
    path = os.path.expanduser("~/Downloads")
    for file in os.listdir(path):
        full = os.path.join(path, file)
        if os.path.isfile(full):
            if file.endswith((".jpg", ".png")):
                folder = "Images"
            elif file.endswith(".pdf"):
                folder = "PDFs"
            else:
                continue
            dest = os.path.join(path, folder)
            os.makedirs(dest, exist_ok=True)
            shutil.move(full, os.path.join(dest, file))

# 🧠 SCREEN READ
def read_screen():
    screenshot = pyautogui.screenshot()
    text = pytesseract.image_to_string(screenshot)
    return text

def explain_screen(text):
    data = {
        "model": "openchat/openchat-3.5",
        "messages": [
            {"role": "system", "content": "Explain clearly what is on screen."},
            {"role": "user", "content": text[:2000]}
        ]
    }
    try:
        r = requests.post(url, headers=headers, json=data)
        res = r.json()
        return res["choices"][0]["message"]["content"]
    except:
        return "⚠️ Could not analyze screen"

# 🪟 MAIN WIDGET
class AIWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(350, 450)

        # 🔥 ALWAYS ON TOP + NO BORDER
        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint
        )

        self.old_pos = QPoint()

        layout = QVBoxLayout()

        self.chat_box = QTextEdit()
        self.chat_box.setReadOnly(True)

        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText("Ask...")

        btn = QPushButton("Send")
        btn.clicked.connect(self.send_message)

        layout.addWidget(self.chat_box)
        layout.addWidget(self.input_box)
        layout.addWidget(btn)

        self.setLayout(layout)

        # 📍 Position bottom-right
        screen = QApplication.primaryScreen().geometry()
        self.move(screen.width() - 370, screen.height() - 500)

    # 🖱️ DRAG WIDGET
    def mousePressEvent(self, event):
        self.old_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.old_pos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.old_pos = event.globalPos()

    def send_message(self):
        user = self.input_box.text().strip()
        if not user:
            return

        self.chat_box.append("🧑 " + user)
        u = user.lower()

        if "search" in u:
            google_search(user)
            self.chat_box.append("🌐 Searching...\n")

        elif u.startswith("run") or u.startswith("calculate"):
            code = u.replace("run", "").replace("calculate", "")
            self.chat_box.append("💻 " + run_code(code) + "\n")

        elif "organize files" in u:
            organize_files()
            self.chat_box.append("📂 Done!\n")

        elif u.startswith("open "):
            self.chat_box.append(open_app_smart(u) + "\n")

        elif "read screen" in u:
            text = read_screen()
            if text.strip():
                explanation = explain_screen(text)
                self.chat_box.append("🧠 " + explanation + "\n")
            else:
                self.chat_box.append("⚠️ No text detected\n")

        else:
            data = {
                "model": "openchat/openchat-3.5",
                "messages": [
                    {"role": "user", "content": user}
                ]
            }
            try:
                r = requests.post(url, headers=headers, json=data)
                res = r.json()
                reply = res["choices"][0]["message"]["content"]
            except:
                reply = "⚠️ AI Error"

            self.chat_box.append("🤖 " + reply + "\n")

        self.input_box.clear()


# 🚀 RUN
app = QApplication(sys.argv)

app.setStyleSheet("""
QWidget {
    background-color: rgba(15,23,42,230);
    color: white;
    border-radius: 15px;
}
QTextEdit, QLineEdit {
    background-color: rgba(30,41,59,200);
    border-radius: 10px;
}
QPushButton {
    background-color: #38bdf8;
    border-radius: 8px;
}
""")

window = AIWidget()
window.show()

sys.exit(app.exec_())
