import customtkinter as ctk

class AddExpense(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.title = ctk.CTkEntry(
            self,
            placeholder_text="Expense Name"
        )
        self.title.pack(pady=10)

        self.amount = ctk.CTkEntry(
            self,
            placeholder_text="Amount"
        )
        self.amount.pack(pady=10)

        self.category = ctk.CTkComboBox(
            self,
            values=[
                "Food",
                "Travel",
                "Shopping",
                "Bills"
            ]
        )
        self.category.pack(pady=10)

        save_btn = ctk.CTkButton(
            self,
            text="Save Expense"
        )
        save_btn.pack(pady=10)