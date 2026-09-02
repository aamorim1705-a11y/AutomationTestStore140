# =======================
# Bibliotecas / Imports
# =======================
from datetime import datetime
import os

# =========
# Classe 
# ==========
class BasePage:

    # ====================
    # CONSTRUTOR
    # ====================
    def __init__(self, driver):
        self.driver = driver

    # ====================
    # Funções e Métodos
    # ====================
    def clicar(self, by, valor):
        self.driver.find_element(by, valor).click()

    def obter_texto(self, by, valor):
        return self.driver.find_element(by, valor).text

    def obter_data_hora(self):
        return datetime.now().strftime("%Y.%m.%d_%H.%M.%S")

    def tirar_screenshot(self, screenshot_name):
        data_hora = self.obter_data_hora()

        caminho = os.path.join("screenshots", "automationteststore", data_hora)

        os.makedirs(caminho, exist_ok=True)

        self.driver.save_screenshot(os.path.join(caminho, f"{screenshot_name}.png"))

