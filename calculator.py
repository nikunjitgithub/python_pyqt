import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit


class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Calculator")
        self.setGeometry(100, 100, 300, 400)

        self.layout = QVBoxLayout()

        self.result_display = QLineEdit()
        self.layout.addWidget(self.result_display)

        button_layout = QVBoxLayout()
        self.buttons = [
            "7", "8", "9", "+",
            "4", "5", "6", "-",
            "1", "2", "3", "*",
            "0", "C", "=", "/"
        ]

        for btn_text in self.buttons:
            button = QPushButton(btn_text)
            button.clicked.connect(self.button_click)
            button_layout.addWidget(button)

        self.layout.addLayout(button_layout)

        self.setLayout(self.layout)

        self.current_input = ""
        self.result = None
        self.last_operator = None

    def button_click(self):
        sender = self.sender()
        text = sender.text()

        if text.isdigit() or text == ".":
            self.current_input += text
            self.result_display.setText(self.current_input)
        elif text == "C":
            self.current_input = ""
            self.result = None
            self.last_operator = None
            self.result_display.clear()
        elif text == "=":
            if self.result is not None and self.current_input != "":
                if self.last_operator == "+":
                    self.result += float(self.current_input)
                elif self.last_operator == "-":
                    self.result -= float(self.current_input)
                elif self.last_operator == "*":
                    self.result *= float(self.current_input)
                elif self.last_operator == "/":
                    try:
                        self.result /= float(self.current_input)
                    except ZeroDivisionError:
                        self.result_display.setText("Error")
                        return

                self.result_display.setText(str(self.result))
                self.current_input = ""
                self.last_operator = None
        else:
            if self.result is None:
                self.result = float(self.current_input)
            else:
                if self.last_operator == "+":
                    self.result += float(self.current_input)
                elif self.last_operator == "-":
                    self.result -= float(self.current_input)
                elif self.last_operator == "*":
                    self.result *= float(self.current_input)
                elif self.last_operator == "/":
                    try:
                        self.result /= float(self.current_input)
                    except ZeroDivisionError:
                        self.result_display.setText("Error")
                        return

            self.current_input = ""
            self.last_operator = text


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec_())
