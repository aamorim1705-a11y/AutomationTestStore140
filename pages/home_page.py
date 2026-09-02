# =======================
# Bibliotecas / Imports
# =======================
from selenium.webdriver.common.by import By
from .base_page import BasePage

# =========
# Classe 
# ==========
class HomePage(BasePage):

    # =============
    # Atributos 
    # =============
    url = "https://automationteststore.com"
    
    # ====================
    # Funções e Métodos
    # ====================
    def abrir_pagina(self):
        self.driver.get(self.url)

    def acessar_makeup(self):
        self.clicar(By.CSS_SELECTOR, 'a[href*="path=36"]')

    def acessar_cheeks(self):
        self.clicar(By.LINK_TEXT, "Cheeks")