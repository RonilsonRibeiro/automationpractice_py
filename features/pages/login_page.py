class Login():

    def __init__(self, driver):
        self.driver = driver
        self.email_create_id = "email_create"
        self.create_account_id = "SubmitCreate"


    
    def criar_conta(self, driver, email):
        self.driver.find_element_by_id(self.email_create_id).clear()
        self.driver.find_element_by_id(self.email_create_id).send_keys(email)
        self.driver.find_element_by_id(self.create_account_id).click()
