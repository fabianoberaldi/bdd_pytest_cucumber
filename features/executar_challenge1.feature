Feature: RPA Challenge I

    Feature Description
    Scenario: Cadastros de registros no site RPA Challenge
        Given Tela inicial do Challenge 1
        And Botao Start visivel
        When Clicar no botao Start
        Then Iniciar cadastro dos registros
        And Verificar registros inseridos com sucesso

#pytest-bdd generate features/executar_challenge1.feature > functional/test_executar_challenge1.py