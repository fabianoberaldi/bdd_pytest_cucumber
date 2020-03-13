# BDD (Behavior Driven Development)
BDD Python: utilizando pytest, cucumber

Geckodriver: https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-win64.zip"
Selenium: https://selenium-python.readthedocs.io/
Cucumber: https://cucumber.io/

Site utilizado no exemplo: http://rpachallenge.com/

Feature: RPA Challenge I

    Feature Description
    Scenario: Cadastros de registros no site RPA Challenge
        Given Tela inicial do Challenge 1
        And Botao Start visivel
        When Clicar no botao Start
        Then Iniciar cadastro dos registros
        And Verificar registros inseridos com sucesso


