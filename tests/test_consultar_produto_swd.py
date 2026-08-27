# 1 - Bibliotecas
from selenium import webdriver
from selenium.webdriver.common.by import By

# 2 - Classe (opcional)
class Teste_Produtos():

    # 2.1 Atributos
    url = "https://automationteststore.com/"    

    # 2.2 Funcoes e Métodos
    def setup_method(self, method):             
        self.driver = webdriver.Chrome()        
        self.driver.implicitly_wait(10)          

    def teardown_method(self, method):          
        self.driver.quit() 

    def test_consultar_produto(self):          
        self.driver.get(self.url) 
        self.driver.find_element(By.CSS_SELECTOR, 'a[href*="path=36"]').click() 
        self.driver.find_element(By.LINK_TEXT, "Cheeks").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "span.maintext").text == "CHEEKS"
        assert self.driver.find_element(By.CSS_SELECTOR, 'a.prdocutname[title="Skinsheen Bronzer Stick"]').text == "SKINSHEEN BRONZER STICK"  
        assert self.driver.find_element(By.CSS_SELECTOR, ".oneprice").text == "$29.50"   
        self.driver.find_element(By.CSS_SELECTOR,'a.prdocutname[title="Skinsheen Bronzer Stick"]').click()   
        assert self.driver.find_element(By.CSS_SELECTOR, ".bgnone").text == "Skinsheen Bronzer Stick"   
        assert self.driver.find_element(By.CSS_SELECTOR, ".productfilneprice").text == "$29.50"
        assert self.driver.find_element(By.ID, "product_quantity").get_attribute("value") == "1"     
        self.driver.find_element(By.CSS_SELECTOR, "a.cart").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "span.maintext").text == "SHOPPING CART"
        assert self.driver.find_element(By.LINK_TEXT, "Skinsheen Bronzer Stick").text == "Skinsheen Bronzer Stick"  
        assert self.driver.find_element(By.CSS_SELECTOR, "td.align_right").text == "$29.50"
        assert self.driver.find_element(By.ID, "cart_quantity50").get_attribute("value") == "1"
        self.driver.find_element(By.CSS_SELECTOR, "i.fa-trash-o").click()              