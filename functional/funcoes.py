from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd


def inserir_registros(_browser):

    arquivo = r"C:\Users\fabiano.beraldi\Documents\BDD\bdd-RPAChanllenge\functional\challenge.xlsx"

    df_registros = pd.read_excel(arquivo)
    print(df_registros.head())

    for i, r in df_registros.iterrows():
        role = r['Role in Company']
        email = r['Email']
        first_name = r['First Name']
        last_name = r['Last Name']
        phone = r['Phone Number']
        company = r['Company Name']
        address = r['Address']

        print(first_name)

        # LOGIN
        print("Writing role...")
        textbox = _browser.find_element_by_xpath(
            "//input[@ng-reflect-name='labelRole']")
        textbox.clear()
        textbox.send_keys(role)
        # time.sleep(0.5)

        print("Writing email...")
        textbox = _browser.find_element_by_xpath(
            "//input[@ng-reflect-name='labelEmail']")
        textbox.clear()
        textbox.send_keys(email)
        # time.sleep(0.5)

        print("Writing first name...")
        textbox = _browser.find_element_by_xpath(
            "//input[@ng-reflect-name='labelFirstName']")
        textbox.clear()
        textbox.send_keys(first_name)
        # time.sleep(0.5)

        print("Writing last name...")
        textbox = _browser.find_element_by_xpath(
            "//input[@ng-reflect-name='labelLastName']")
        textbox.clear()
        textbox.send_keys(last_name)
        # time.sleep(0.5)

        print("Writing phone...")
        textbox = _browser.find_element_by_xpath(
            "//input[@ng-reflect-name='labelPhone']")
        textbox.clear()
        textbox.send_keys(phone)
        # time.sleep(0.5)

        print("Writing address...")
        textbox = _browser.find_element_by_xpath(
            "//input[@ng-reflect-name='labelAddress']")
        textbox.clear()
        textbox.send_keys(address)
        # time.sleep(0.5)

        print("Writing company...")
        textbox = _browser.find_element_by_xpath(
            "//input[@ng-reflect-name='labelCompanyName']")
        textbox.clear()
        textbox.send_keys(company)
        # time.sleep(0.5)

        print('Submit...')
        botao = _browser.find_element_by_xpath("//input[@type='submit']")
        botao.click()
        time.sleep(0.5)

    print('Processo finalizado')
