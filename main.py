
from unicodedata import name
from urllib import response
from pip import main

class Property:
    def __init__(self, income=0, yearly_expenses=0, name_of_property=None):
        self.income = income
        self.yearly_expenses = yearly_expenses
        # self.cash_flow = cash_flow (come back to this later, make it a new method for total cash flow instead of in the init)
        self.name_of_property = name_of_property
        self.ROI = None

    def setIncome(self):
        response = float(input('How much money do you make off this property each month?: $'))
        self.income = response

    def setYearlyExpenses(self):
        response = float(input("How much money do you spend per year to upkeep this property?: $"))
        self.yearly_expenses = response

    def setNameOfProperty(self):
        response = input("What would you like to set as the name of this property?: ")
        self.name_of_property = response

    def calculateROI(self):
        calculation = self.income * 12 - self.yearly_expenses  # monthly profit gain
        self.ROI = calculation

class User:
    dict_of_active_users = {}

    def __init__(self, username):
        self.username = username
        self.properties = {}
        self.dict_of_active_users[username] = self

    def addProperty(self):
        userProperty = Property()
        userProperty.setNameOfProperty()
        userProperty.setIncome()
        userProperty.setYearlyExpenses()
        userProperty.calculateROI()
        self.properties[userProperty.name_of_property] = userProperty

    def displayPropertyInfo(self):
        for key, current_property in self.properties.items():
            print(f"Name of Property: {current_property.name_of_property}")
            print(f"Property Income per Month: {current_property.income}")
            print(f"Property Expenses per Year: {current_property.yearly_expenses}")
            print(f"Yearly ROI: {current_property.ROI}\n")
        pause = input("\nPress any key to head back to main menu: ")
  

class Run:
    def login(self):
        print("Please login before viewing your rental property profile.")
        sign_in_screen = input("Do you already have an account? (Y/N): ").lower()
        if sign_in_screen == "y":
            enter_username = input("What's your username: ").lower()
            if enter_username in User.dict_of_active_users:
                self.current_user = User.dict_of_active_users[enter_username]
                self.start_program()
            else:
                print("Sorry, we couldn't find that username.")
                self.login()
        elif sign_in_screen == "n":
            create_account = input("Let's create an account for you, then! Enter your new username: ").lower()
            self.current_user = User(create_account)
            self.start_program()
        else:
            self.login()

    def start_program(self):

        done = False

        while not done:
            main_menu = input("Welcome to your Rental Income Calculator. You've got a few options, listed below. \n\n"
            " Add: Add new property \n Remove: Remove a property \n View: View Properties \n Leave: Sign off \n Exit: Exit program \n\n What would you like to do?: ").lower()
            if main_menu == "add":
                self.current_user.addProperty()
                print("\nProperty added.")
            elif main_menu == "view":
                self.current_user.displayPropertyInfo()
            elif main_menu == "remove":
                remove_property = input("Which property would you like to remove?: \n")
                del self.current_user.properties[remove_property]
                print("Property Removed. Heading back to the main menu...\n")
                # remove a rental property
            elif main_menu == "leave":
                print("Logging out...\n")
                self.login()

            elif main_menu == "exit":
                print("Thanks for using our software, goodbye!")
                done = True
                break
            else:
                print("Invald input!")

# run = Run()
# run.login()
