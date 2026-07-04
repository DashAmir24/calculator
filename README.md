# 🧮 Streamlit Calculator

A simple and interactive calculator built with **Python** and **Streamlit**. The application provides a clean graphical interface for performing basic arithmetic operations while maintaining a history of previous calculations.

---

## ✨ Features

- ➕ Addition
- ➖ Subtraction
- ✖️ Multiplication
- ➗ Division
- 🔢 Decimal number support
- 📜 Stores the last 10 calculation results
- ⌫ Backspace functionality
- 🧹 Clear calculator state
- π One-click insertion of the value of Pi
- ⚡ Continuous calculations without restarting
- 💾 State management using `st.session_state`

---

## 📂 Project Structure

```text
.
├── app.py          # Streamlit user interface
├── main.py         # Calculation logic
└── README.md

```
---

## 📋 Requirements

- Python 3.9 or later
- Streamlit

Install Streamlit:

```bash
pip install streamlit
```

Or install all dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Application

Run the application using:

```bash
streamlit run app.py
```

After executing the command, Streamlit will automatically launch the application in your default web browser.

---

## 📖 How to Use

1. Enter the first number using the numeric buttons.
2. Select an arithmetic operator (`+`, `-`, `*`, or `/`).
3. Enter the second number.
4. Click the **=** button to display the result.
5. Continue calculating or clear the calculator using the **C** button.

---

## 🔘 Button Reference

| Button | Function |
|---------|----------|
| `0-9` | Enter numbers |
| `.` | Decimal point |
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `=` | Calculate the result |
| `C` | Clear calculator |
| `<-` | Delete the last entered character |
| `H` | View previous calculation results |
| `Pi` | Insert the value of π |

---

## 📜 Calculation History

The calculator automatically stores the **last 10 calculation results**.

Press the **H** button repeatedly to browse through the stored history.

---

## ⚙️ How It Works

The application uses **Streamlit Session State** to maintain:

- Current input
- First operand
- Second operand
- Selected operator
- Calculation history
- Operation status

All arithmetic operations are handled by the `calculate()` function defined in `main.py`.

---

## 🛠️ Technologies Used

- Python
- Streamlit

---

## 📈 Future Improvements

- Scientific calculator functions
- Keyboard input support
- Parentheses support
- Square root and exponent operations
- Percentage calculations
- Persistent history stored in a file or database
- Dark mode
- Responsive UI improvements

---

## 🤝 Contributing

Contributions are welcome!

If you would like to improve this project:

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Open a Pull Request.

---

## 📄 License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this project under the terms of the MIT License.

---

## 👨‍💻 Author

**Mohamad Amir Mohamadi**

- GitHub: https://github.com/dashamir24