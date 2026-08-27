# 1 - Bibliotecas / Imports
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

# ====================
# CONSULTAR PRODUTOS 
# ==================== 
@given(u'que acesso o site Automation Test Store')
def step_impl(context):
    context.driver = webdriver.Chrome()   
    context.driver.implicitly_wait(10)
    context.driver.delete_all_cookies()
    context.driver.get("https://automationteststore.com")
    
@when(u'acesso a sessao MAKEUP e clico na subsessao Cheeks')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, 'a[href*="path=36"]').click()
    context.driver.find_element(By.LINK_TEXT, "Cheeks").click()
    
@then(u'sou direcionado para pagina dos produtos')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "span.maintext").text == "CHEEKS"
    
@then(u'consulto os produtos:')
def step_impl(context):
    for row in context.table:
        produto = row['produto']
        preco = row['preco']

        assert context.driver.find_element(By.CSS_SELECTOR, f'a.prdocutname[title="{produto}"]').text == produto.upper()
        href = context.driver.find_element(By.CSS_SELECTOR, f'a.prdocutname[title="{produto}"]').get_attribute("href")
        assert context.driver.find_element(By.CSS_SELECTOR, f'div.thumbnail:has(a[href="{href}"]) div.oneprice').text == preco

# ===============================
# ADICIONAR PRODUTOS AO CARRINHO
# =============================== 
@when(u'adiciono os produtos ao carrinho:')
def step_impl(context):
    for i, row in enumerate(context.table):
        produto = row['produto']
        preco = row['preco']
        quantidade = row['quantidade']

        context.driver.find_element(By.CSS_SELECTOR, f'a.prdocutname[title="{produto}"]').click()
        assert context.driver.find_element(By.CSS_SELECTOR, ".bgnone").text == produto
        assert context.driver.find_element(By.CSS_SELECTOR, ".productfilneprice").text == preco
        context.driver.find_element(By.ID, "product_quantity").clear()
        context.driver.find_element(By.ID, "product_quantity").send_keys(quantidade)
        assert context.driver.find_element(By.ID, "product_quantity").get_attribute("value") == quantidade
        context.driver.find_element(By.CSS_SELECTOR, 'a.cart').click()
        if i < len(context.table.rows) - 1:
            context.driver.get("https://automationteststore.com/index.php?rt=product/category&path=36_40")

@then(u'sou direcionado para a pagina do carrinho')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "span.maintext").text == "SHOPPING CART"

# =====================
# VALIDAR PRODUTOS
# =====================
@then(u'devo visualizar os produtos adicionados no carrinho')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT, "Skinsheen Bronzer Stick").text == "Skinsheen Bronzer Stick"
    assert context.driver.find_element(By.LINK_TEXT, "Benefit Bella Bamba").text == "Benefit Bella Bamba"

@then(u'devo validar preço e quantidade dos produtos:')
def step_impl(context):
    for row in context.table:

        produto = row['produto']
        preco = row['preco']
        quantidade = row['quantidade']

        href = context.driver.find_element(By.LINK_TEXT, produto).get_attribute("href")

        assert context.driver.find_element(By.CSS_SELECTOR, f'tr:has(a[href="{href}"]) td:nth-of-type(4)').text == preco
        assert context.driver.find_element(By.CSS_SELECTOR, f'tr:has(a[href="{href}"]) input.form-control.short').get_attribute("value") == quantidade

# ====================
# REMOÇAO DOS PRODUTOS
# ====================
@when(u'removo os produtos do carrinho')
def step_impl(context):
    for row in context.table:

        produto = row['produto']

        href = context.driver.find_element(By.LINK_TEXT, produto).get_attribute("href")

        context.driver.find_element(By.CSS_SELECTOR, f'tr:has(a[href="{href}"]) i.fa-trash-o').click()

@then(u'o carrinho deve estar vazio')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".contentpanel").text.startswith("Your shopping cart is empty!")

# teardown / encerramento
def after_scenario(context, scenario):
    context.driver.quit()
        