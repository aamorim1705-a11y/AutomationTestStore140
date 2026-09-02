# =======================
# Bibliotecas / Imports
# =======================
from selenium import webdriver

from pages.home_page import HomePage
from pages.cheeks_page import CheeksPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

# =======================
# Dados dos produtos
# =======================
PRODUTOS = [
        {
            "produto": "Skinsheen Bronzer Stick",
            "preco": "$29.50",
            "quantidade": "1"
        },
        {
            "produto": "Benefit Bella Bamba",
            "preco": "$28.00",
            "quantidade": "2"
        }
    ]

# =======================
# Teste
# =======================
def test_consultar_produtos():

    # =======================
    # Abrir navegador
    # =======================
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()

    # =======================
    # Instanciar as Pages
    # =======================
    home_page = HomePage(driver)
    cheeks_page = CheeksPage(driver)
    product_page = ProductPage(driver)
    cart_page = CartPage(driver)

    # =======================
    # 1 - Home
    # =======================
    home_page.abrir_pagina()
    home_page.tirar_screenshot("1-Home")

    # =======================
    #  2 - Cheeks
    # =======================
    home_page.acessar_makeup()
    home_page.acessar_cheeks()
    cheeks_page.validar_pagina()
    cheeks_page.tirar_screenshot("2-Cheeks")

    # =======================
    # 3 - Consultar produtos
    # =======================
    for produto in PRODUTOS:
        cheeks_page.consultar_produto(
            produto["produto"],
            produto["preco"]
        )

    cheeks_page.tirar_screenshot("3-Consultar_produtos")

    # ===============================
    # Adicionar produtos ao carrinho
    # ===============================
    for i, produto in enumerate(PRODUTOS):

        product_page.acessar_produto(produto["produto"])

        product_page.validar_produto(produto["produto"])
        product_page.validar_preco(produto["preco"])

        product_page.preencher_quantidade(produto["quantidade"])
        product_page.validar_quantidade(produto["quantidade"])

        product_page.tirar_screenshot(f"4-Adicionar_produtos_{i + 1}")

        product_page.adicionar_ao_carrinho()

        # Retorna para Cheeks somente se ainda houver outro produto para adicionar
        if i < len(PRODUTOS) - 1:
            driver.get("https://automationteststore.com/index.php?rt=product/category&path=36_40")

    # =======================
    # Carrinho
    # =======================
    cart_page.validar_pagina()
    cart_page.tirar_screenshot("5-Carrinho")

    # ===============================
    # Visualizar produtos no carrinho
    # ===============================
    for produto in PRODUTOS:
        cart_page.visualizar_produto(produto["produto"])

    cart_page.tirar_screenshot("6-Visualizar_produtos_carrinho")

    # ===============================
    # Validar preço e quantidade
    # ===============================
    for produto in PRODUTOS:
        cart_page.validar_produto(
        produto["produto"],
        produto["preco"],
        produto["quantidade"]
    )
        
    cart_page.tirar_screenshot("7-Validar_preco_e_quantidade")

    # ===============================
    # Remover produtos
    # ===============================
    for produto in PRODUTOS:
        cart_page.remover_produto(produto["produto"])

    cart_page.tirar_screenshot("8-Remover_produtos")

    # ===============================
    # Validar carrinho vazio
    # ===============================
    cart_page.validar_carrinho_vazio()
    cart_page.tirar_screenshot("9-Carrinho_vazio")

    # =======================
    # Fechar navegador
    # =======================
    driver.quit()