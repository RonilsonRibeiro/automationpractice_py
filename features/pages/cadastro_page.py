import time
from selenium.webdriver.support.ui import Select

class Cadastro():

    def __init__(self, driver):
        self.driver = driver        
        self.title_id = "id_gender1"
        self.first_name_id = "customer_firstname"
        self.last_name_id = "customer_lastname"
        self.email_id = "email"
        self.password_id = "passwd"
        self.birth_day_id = "days"
        self.birth_month_id = "months"
        self.birth_year_id = "years"
        self.newsletter_id = "newsletter"
        self.address_first_name_id = "newsletter"
        self.address_last_name_id = "lastname"
        self.address_company_id = "company"
        self.address_street_id = "address1"
        self.address_city_id = "city"
        self.address_state_id = "id_state"
        self.address_postcode_id = "postcode"
        self.address_country_id = "id_country"
        self.address_phone_mobile_id = "phone_mobile"
        self.address_alias_id = "alias"
        self.register_id = "submitAccount"


    def preencher_cadastro(self, driver, first_name, last_name, email, password, birth_day, 
                birth_month, birth_year, company, street, city, state, postcode, mobile, alias): 
        #Title
        self.driver.find_element_by_id(self.title_id).click()
        #First name
        self.driver.find_element_by_id(self.first_name_id).clear()
        self.driver.find_element_by_id(self.first_name_id).send_keys(first_name)
        #Last name
        self.driver.find_element_by_id(self.last_name_id).clear()
        self.driver.find_element_by_id(self.last_name_id).send_keys(last_name)
        #Email 
        self.driver.find_element_by_id(self.email_id).clear()
        self.driver.find_element_by_id(self.email_id).send_keys(email)
        #Password 
        self.driver.find_element_by_id(self.password_id).clear()
        self.driver.find_element_by_id(self.password_id).send_keys(password) 
        #Date of Birth
        day = Select(self.driver.find_element_by_id(self.birth_day_id))
        day.select_by_value(birth_day)

        month = Select(self.driver.find_element_by_id(self.birth_month_id))
        month.select_by_value(birth_month)

        year = Select(self.driver.find_element_by_id(self.birth_year_id))
        year.select_by_value(birth_year)
        #Newsletter
        self.driver.find_element_by_id(self.newsletter_id).click()        
        #First name
        self.driver.find_element_by_id(self.address_first_name_id).send_keys(first_name)        
        #Last name
        self.driver.find_element_by_id(self.address_last_name_id).send_keys(last_name)
        #Company
        self.driver.find_element_by_id(self.address_company_id).clear()
        self.driver.find_element_by_id(self.address_company_id).send_keys(company)
        #Address 
        self.driver.find_element_by_id(self.address_street_id).clear()
        self.driver.find_element_by_id(self.address_street_id).send_keys(street)
        #City 
        self.driver.find_element_by_id(self.address_city_id).clear()
        self.driver.find_element_by_id(self.address_city_id).send_keys(city)       
        #State         
        statestr = Select(self.driver.find_element_by_id(self.address_state_id))              
        statestr.select_by_value(state)                    
        #Zip/Postal Code
        self.driver.find_element_by_id(self.address_postcode_id).clear()
        self.driver.find_element_by_id(self.address_postcode_id).send_keys(postcode) 
        #Mobile phone            
        self.driver.find_element_by_id(self.address_phone_mobile_id).send_keys(mobile)        
        #Assign an address alias for future reference
        self.driver.find_element_by_id(self.address_alias_id).clear()
        self.driver.find_element_by_id(self.address_alias_id).send_keys(alias)
        #Register
        self.driver.find_element_by_id(self.register_id).click()
        