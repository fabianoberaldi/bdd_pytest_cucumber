# coding=utf-8
"""RPA Challenge I feature tests."""
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

import pytest
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import platform
import os.path
import os
import wget
from zipfile import ZipFile
import pandas as pd
import funcoes as fc

so = platform.system()

print("******* COMEÇOU ****")

if(so == "Windows"):
    path = r"C:\geckodriver\geckodriver.exe"
    binary = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    if (os.path.exists(r'C:\geckodriver') == False):
        os.mkdir("C:\\geckodriver\\")
        url = "https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-win64.zip"
        wget.download(url)

        with ZipFile('geckodriver-v0.26.0-win64.zip', 'r') as zipObj:
            zipObj.extractall('C:\\geckodriver\\')

        os.remove("geckodriver-v0.26.0-win64.zip")

elif (so == "Linux"):
    path = "/usr/bin/geckodriver"
    binary = '/usr/bin/firefox'
else:
    print("Outros")


options = webdriver.FirefoxOptions()
options.binary = binary

options.add_argument('--headless')
cap = DesiredCapabilities().FIREFOX
cap["marionette"] = True


site = "http://rpachallenge.com/"


_browser = webdriver.Firefox(
    capabilities=cap, executable_path=path)


_browser.implicitly_wait(5)
_browser.get(site)
print("*************************************")
print(_browser.current_url)
print("*************************************")


@scenario('../features/executar_challenge1.feature', 'Cadastros de registros no site RPA Challenge')
def test_cadastros_de_registros_no_site_rpa_challenge():
    """Cadastros de registros no site RPA Challenge."""


@given('Botao Start visivel')
def botao_start_visivel():
    """Botao Start visivel."""
    # segundo
    try:
        start_button = _browser.find_element_by_xpath(
            "//button[@class='waves-effect col s12 m12 l12 btn-large uiColorButton']")
    except:
        start_button = None

    assert start_button


@given('Tela inicial do Challenge 1')
def tela_inicial_do_challenge_1():
    """Tela inicial do Challenge 1."""
    # primeiro
    _url_site = "http://rpachallenge.com/"
    _current_url = _browser.current_url

    assert _current_url == _url_site


@when('Clicar no botao Start')
def clicar_no_botao_start():
    """Clicar no botao Start."""
    # terceiro
    try:
        start_button = _browser.find_element_by_xpath(
            "//button[@class='waves-effect col s12 m12 l12 btn-large uiColorButton']")
    except:
        start_button = None

    start_button.click()
    assert start_button


@then('Iniciar cadastro dos registros')
def iniciar_cadastro_dos_registros():
    """Iniciar cadastro dos registros."""
    # quarto
    result = False
    try:
        fc.inserir_registros(_browser)
        result = True
    except:
        result = False

    assert result


@then('Verificar registros inseridos com sucesso')
def verificar_registros_inseridos_com_sucesso():
    """Verificar registros inseridos com sucesso."""
    # quinto
    try:
        time.sleep(3)
        mensagem = _browser.find_element_by_xpath(
            "//div[@class='congratulations col s8 m8 l8']")
        print("Congratulations!")
    except:
        mensagem = None

    assert mensagem
