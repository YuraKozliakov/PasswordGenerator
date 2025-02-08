import tkinter as tk
from tkinter import messagebox
from password_generator.generator import PasswordGenerator
from password_generator.password_strength import PasswordStrength
from password_generator.exceptions import *


class PasswordGeneratorGUI:
    """
    Графический интерфейс для генератора паролей.
    """

    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.create_widgets()

    def create_widgets(self):
        """Создание виджетов интерфейса"""
        self.length_label = tk.Label(self.root, text="Length:")
        self.length_label.grid(row=0, column=0)

        self.length_entry = tk.Entry(self.root)
        self.length_entry.grid(row=0, column=1)

        self.use_digits_var = tk.BooleanVar()
        self.use_digits_check = tk.Checkbutton(self.root, text="Use Digits", variable=self.use_digits_var)
        self.use_digits_check.grid(row=1, column=0)

        self.use_special_chars_var = tk.BooleanVar()
        self.use_special_chars_check = tk.Checkbutton(self.root, text="Use Special Characters",
                                                      variable=self.use_special_chars_var)
        self.use_special_chars_check.grid(row=1, column=1)

        self.use_uppercase_var = tk.BooleanVar()
        self.use_uppercase_check = tk.Checkbutton(self.root, text="Use Uppercase Letters",
                                                  variable=self.use_uppercase_var)
        self.use_uppercase_check.grid(row=1, column=2)

        self.generate_button = tk.Button(self.root, text="Generate", command=self.generate_password)
        self.generate_button.grid(row=2, column=0, columnspan=3)

        self.password_label = tk.Label(self.root, text="Generated Password:")
        self.password_label.grid(row=3, column=0, columnspan=3)

        self.password_text = tk.Entry(self.root, state="readonly")
        self.password_text.grid(row=4, column=0, columnspan=3)

        self.strength_label = tk.Label(self.root, text="Password Strength:")
        self.strength_label.grid(row=5, column=0, columnspan=3)

    def generate_password(self):
        """
        Генерирует пароль и проверяет его силу.
        """
        try:
            length = int(self.length_entry.get())
            use_digits = self.use_digits_var.get()
            use_special_chars = self.use_special_chars_var.get()
            use_uppercase = self.use_uppercase_var.get()

            generator = PasswordGenerator(length, use_digits, use_special_chars, use_uppercase)
            password = generator.generate()

            self.password_text.config(state="normal")
            self.password_text.delete(0, tk.END)
            self.password_text.insert(0, password)
            self.password_text.config(state="readonly")

            strength = PasswordStrength.check_strength(password)
            self.strength_label.config(text=f"Password Strength: {strength}")

        except InvalidInputError as e:
            messagebox.showerror("Error", str(e))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for length.")
