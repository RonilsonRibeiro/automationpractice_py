Feature: Cadastrar usuario
Eu como usuario
Quero me cadastrar no site 
Para que eu possa ter acesso a area logada

    @cadastro
    Scenario: Cadastrar usuario com sucesso
    Given que eu estou na area de autenticacao
    When eu informo um email ainda nao cadastrado
    And  preencho o formulario
    Then meu cadastro e efetuado corretamente