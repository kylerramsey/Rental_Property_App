class Property():
    def __init__(self, income=0, yearly_expenses=0, cash_flow=None, name_of_property=None):
        self.income = income
        self.yearly_expenses = yearly_expenses
        self.cash_flow = cash_flow
        self.name_of_property = name_of_property
        self.ROI = income * 12 - yearly_expenses  # monthly profit gain

    def setIncome(self):
        response = float(input('How much money do you make?'))
        self.income = response

        

class User:
    list_of_active_users = []

    def __init__(self, username, properties=[]):
        self.username = username
        self.list_of_active_users.append(self)
        self.properties = properties

    def addProperty(self):
        userProperty = Property()
        userProperty.setIncome()
        self.properties.append(userProperty)


myUser = User('jendrix')
myUser.addProperty()
myUser.addProperty()
print(myUser.properties)
print(myUser.properties[0].income)