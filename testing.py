import unittest
from main import Property, User, Run

class propertyManagerTesting(unittest.TestCase):

    def test_property_init(self):
        myProperty = Property(1000, 4000, "Kyler's House")
        self.assertEqual(myProperty.income, 1000)
        self.assertEqual(myProperty.yearly_expenses, 4000)
        self.assertEqual(myProperty.name_of_property, "Kyler's House")
        self.assertEqual(myProperty.ROI, None)

    def test_user_init(self):
        myUser = User("kylerramsey")
        self.assertEqual(myUser.username, "kylerramsey")

    def test_add_property(self):
        myUser = User("kylerramsey")
        myProperty = Property(1000, 4000, "Kyler's House")
        myUser.properties[myProperty.name_of_property] = myProperty
        self.assertIn("Kyler's House", myUser.properties)

    def test_add_user_in_dict(self):
        myUser = User("lucaslang")
        self.assertIn("lucaslang", myUser.dict_of_active_users)

    def test_run(self):
        run = Run()
        run.login()
    
if __name__ == '__main__':
        unittest.main()
