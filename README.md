# BDD (Behavior Driven Development)

## BDD Python: utilizando pytest, cucumber

<ul>
    <li>Geckodriver: https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-win64.zip"</li>
    <li>Selenium: https://selenium-python.readthedocs.io/</li>
    <li>Cucumber: https://cucumber.io/</li>
    <li>Site utilizado no exemplo: http://rpachallenge.com/</li>
</ul>    


### Feature: RPA Challenge I

    Feature Description
    Scenario: Cadastros de registros no site RPA Challenge
        Given Tela inicial do Challenge 1
        And Botao Start visivel
        When Clicar no botao Start
        Then Iniciar cadastro dos registros
        And Verificar registros inseridos com sucesso


