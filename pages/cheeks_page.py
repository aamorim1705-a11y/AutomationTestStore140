# =======================
# Bibliotecas / Imports
# =======================
from selenium.webdriver.common.by import By
from .base_page import BasePage

# =========
# Classe 
# ==========
class CheeksPage(BasePage):

    # ====================
    # Funções e Métodos
    # ====================
    def validar_pagina(self):
        assert self.obter_texto(By.CSS_SELECTOR, "span.maintext") == "CHEEKS"

    def consultar_produto(self, produto, preco):
        produto_elemento = self.driver.find_element(By.CSS_SELECTOR, f'a.prdocutname[title="{produto}"]')

        assert produto_elemento.text == produto.upper()

        href = produto_elemento.get_attribute("href")

        preco_elemento = self.driver.find_element(By.CSS_SELECTOR, f'div.thumbnail:has(a[href="{href}"]) div.oneprice')

        assert preco_elemento.text == preco

    