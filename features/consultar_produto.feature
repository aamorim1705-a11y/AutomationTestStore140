Feature: Consultar Produto

    Scenario: Consultar produtos de Makeup e adicionar ao carrinho
        Given que acesso o site Automation Test Store
        When acesso a sessao MAKEUP e clico na subsessao Cheeks
        Then sou direcionado para pagina dos produtos
        And consulto os produtos:
        | produto                    | preco  |
        | Skinsheen Bronzer Stick    | $29.50 |
        | Benefit Bella Bamba        | $28.00 |

        When adiciono os produtos ao carrinho:
        | produto                 | preco   | quantidade | 
        | Skinsheen Bronzer Stick | $29.50  | 1          | 
        | Benefit Bella Bamba     | $28.00  | 2          | 
        Then sou direcionado para a pagina do carrinho
        And devo visualizar os produtos adicionados no carrinho

        And devo validar preço e quantidade dos produtos:
        | produto                 | preco   | quantidade | 
        | Skinsheen Bronzer Stick | $29.50  | 1          | 
        | Benefit Bella Bamba     | $28.00  | 2          | 

        When removo os produtos do carrinho
        | produto                    | 
        | Skinsheen Bronzer Stick    | 
        | Benefit Bella Bamba        | 
        Then o carrinho deve estar vazio