class Bank:
    # Class variable
    bank_name = "Generic Bank"

    @classmethod
    def change_bank_name(cls, name):
        # Class method to change the bank name
        cls.bank_name = name

    def display_bank(self):
        # Instance method to display the bank name
        print(f"Bank Name: {self.bank_name}")


# Example usage
bank1 = Bank()
bank2 = Bank()

# Display initial bank names for both instances
bank1.display_bank()  # Generic Bank
bank2.display_bank()  # Generic Bank

# Change the bank name using the class method
Bank.change_bank_name("National Bank")

# Display the updated bank name for both instances
bank1.display_bank()  # National Bank
bank2.display_bank()  # National Bank
