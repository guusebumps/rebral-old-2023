import sys
import sqlite3
import bcrypt
from PyQt5 import QtWidgets
import os
import pandas as pd

from ui.ui_login_screen import Ui_LoginScreen
from ui.ui_register_screen import Ui_RegisterScreen

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "users.db")

class LoginScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginScreen()
        self.ui.setupUi(self)
        self.ui.btn_login.clicked.connect(self.login)

    def login(self):
        username = self.ui.line_username.text().strip()
        password = self.ui.line_password.text().strip()
        self.ui.label_status.setText("")

        if not username or not password:
            self.ui.label_status.setText("Preencha todos os campos.")
            return

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT password, role FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()
        conn.close()

        if result and bcrypt.checkpw(password.encode(), result[0].encode()):
            role = result[1]
            if role == "Admin":
                self.admin_panel = AdminPanel()
                self.admin_panel.show()
            else:
                self.ui.label_status.setText("Login bem-sucedido (Usuário comum).")
            self.close()
        else:
            self.ui.label_status.setText("Usuário ou senha inválidos.")

class RegisterScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_RegisterScreen()
        self.ui.setupUi(self)
        self.ui.btn_register.clicked.connect(self.register)

    def register(self):
        username = self.ui.line_username.text().strip()
        password = self.ui.line_password.text().strip()
        confirm = self.ui.line_confirm_password.text().strip()
        role_text = self.ui.combo_role.currentText()
        role = "User" if role_text == "Usuário" else "Admin"
        self.ui.label_status.setText("")

        if not username or not password or not confirm:
            self.ui.label_status.setText("Preencha todos os campos.")
            return
        if password != confirm:
            self.ui.label_status.setText("Senhas não coincidem.")
            return

        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        try:
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, hashed, role))
            conn.commit()
            conn.close()
            self.ui.label_status.setText("Usuário cadastrado com sucesso!")
        except sqlite3.IntegrityError:
            self.ui.label_status.setText("Usuário já existe.")

class AdminPanel(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Painel do Administrador")
        self.setGeometry(100, 100, 400, 300)

        self.export_button = QtWidgets.QPushButton("Exportar usuários para Excel", self)
        self.export_button.setGeometry(80, 50, 250, 40)
        self.export_button.clicked.connect(self.export_users)

        self.import_button = QtWidgets.QPushButton("Importar usuários do Excel", self)
        self.import_button.setGeometry(80, 110, 250, 40)
        self.import_button.clicked.connect(self.import_users)

        self.register_button = QtWidgets.QPushButton("Cadastrar novo usuário", self)
        self.register_button.setGeometry(80, 170, 250, 40)
        self.register_button.clicked.connect(self.open_register)

    def export_users(self):
        conn = sqlite3.connect(DB_PATH)
        df = pd.read_sql_query("SELECT id, username, role FROM users", conn)
        conn.close()
        export_path = os.path.join(BASE_DIR, "exported_users.xlsx")
        df.to_excel(export_path, index=False)
        QtWidgets.QMessageBox.information(self, "Sucesso", f"Exportado para {export_path}")

    def import_users(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Selecionar arquivo Excel", "", "Excel Files (*.xlsx *.xls)")
        if file_path:
            try:
                df = pd.read_excel(file_path)
                conn = sqlite3.connect(DB_PATH)
                cursor = conn.cursor()
                for _, row in df.iterrows():
                    username = str(row['username']).strip()
                    password = bcrypt.hashpw(str(row['password']).encode(), bcrypt.gensalt()).decode()
                    role = str(row['role']).strip()
                    cursor.execute("INSERT OR IGNORE INTO users (username, password, role) VALUES (?, ?, ?)", (username, password, role))
                conn.commit()
                conn.close()
                QtWidgets.QMessageBox.information(self, "Sucesso", "Importação concluída.")
            except Exception as e:
                QtWidgets.QMessageBox.warning(self, "Erro", f"Falha ao importar: {str(e)}")

    def open_register(self):
        self.register_window = RegisterScreen()
        self.register_window.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login = LoginScreen()
    login.show()
    sys.exit(app.exec_())