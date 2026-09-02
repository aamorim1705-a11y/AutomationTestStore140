# =======================
# Bibliotecas / Imports
# =======================
from selenium.webdriver.common.by import By
from .base_page import BasePage

# =========
# Classe 
# ==========
class CartPage(BasePage):

    # ====================
    # Funções e Métodos
    # ====================
    def validar_pagina(self):
        assert self.obter_texto(By.CSS_SELECTOR, "span.maintext") == "SHOPPING CART"

    def visualizar_produto(self, produto):
        assert self.obter_texto(By.LINK_TEXT, produto) == produto

    def validar_produto(self, produto, preco, quantidade):
        href = self.driver.find_element(By.LINK_TEXT, produto).get_attribute("href")

        assert self.driver.find_element(By.CSS_SELECTOR, f'tr:has(a[href="{href}"]) td:nth-of-type(4)').text == preco
        assert self.driver.find_element(By.CSS_SELECTOR, f'tr:has(a[href="{href}"]) input.form-control.short').get_attribute("value") == quantidade

    def remover_produto(self, produto):
        href = self.driver.find_element(By.LINK_TEXT, produto).get_attribute("href")

        self.clicar(By.CSS_SELECTOR, f'tr:has(a[href="{href}"]) i.fa-trash-o')

    def validar_carrinho_vazio(self):
        assert self.obter_texto(By.CSS_SELECTOR, ".contentpanel").startswith("Your shopping cart is empty!")