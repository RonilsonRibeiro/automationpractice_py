import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 
from features.pages.login_page import Login
from features.pages.cadastro_page import Cadastro
import yaml
from pathlib import Path
import time

# Abre o arquivo com dados
data = yaml.load(open(Path('fixtures/data.yaml'), "r", encoding='utf-8'), Loader=yaml.FullLoader)

# Scenarios 
scenarios('../cadastrar_usuario.feature') 

# Steps
@given('que eu estou na area de autenticacao')
def que_eu_estou_na_area_de_autenticacao(driver):
    driver.get(data.get("set_url"))

@when('eu informo um email ainda nao cadastrado')
def eu_informo_um_email_ainda_nao_cadastrado(driver):
    login = Login(driver)
    login.criar_conta(driver, data.get("email"))
    

@when('preencho o formulario')
def preencho_o_formulario(driver):   
    cadastro = Cadastro(driver)
    cadastro.preencher_cadastro(driver, data.get("first_name"), data.get("last_name"), 
                                data.get("email"), data.get("password"), data.get("birth_day"), data.get("birth_month"), 
                                data.get("birth_year"), data.get("company"), data.get("street"), data.get("city"), 
                                data.get("state"), data.get("postcode"), data.get("mobile"), data.get("alias"))
   
@then('meu cadastro e efetuado corretamente')
def meu_cadastro_e_efetuado_corretamente(driver):  
    assert data.get("confirma_cadastro") in driver.title
   
    