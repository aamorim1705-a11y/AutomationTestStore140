# =======================
# Bibliotecas / Imports
# =======================
from selenium.webdriver.common.by import By
from .base_page import BasePage

# =========
# Classe 
# ========== 
class ProductPage(BasePage):

    ## ====================
    # Funções e Métodos
    # ====================
    def acessar_produto(self, produto):
        self.clicar(By.CSS_SELECTOR, f'a.prdocutname[title="{produto}"]')

    def validar_produto(self, produto):
        assert self.obter_texto(By.CSS_SELECTOR, ".bgnone") == produto

    def validar_preco(self, preco):
        assert self.obter_texto(By.CSS_SELECTOR, ".productfilneprice") == preco

    def preencher_quantidade(self, quantidade):
        campo_quantidade = self.driver.find_element(By.ID, "product_quantity")
        campo_quantidade.clear()
        campo_quantidade.send_keys(quantidade)

    def validar_quantidade(self, quantidade):
        assert self.driver.find_element(By.ID, "product_quantity").get_attribute("value") == quantidade

    def adicionar_ao_carrinho(self):
        self.clicar(By.CSS_SELECTOR, "a.cart")