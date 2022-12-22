from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

pwx = ''
emailx = ''

print("Papa John's Pizza Bot")
print()
pizza = ''

while True:
    pizza_choice = input('What pizza do you want? Enter: pepperoni or works -- ').lower()
    if pizza_choice.startswith('p'):
        pizza += 'Pepperoni'
        break
    elif pizza_choice.startswith('w'):
        pizza += 'Works'
        break
    else: 
        print('Enter a valid response..')

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get('https://www.papajohns.com/')

log_in_dd = driver.find_element_by_xpath("//li[@class='nav-utility-item show-desktop']//a[@data-track-click='top-nav|Log In']")
log_in_dd.click()
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='user']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))
username.clear()
password.clear()
username.send_keys(emailx)
password.send_keys(pwx)
log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-track-click='top-nav|Log In']"))).click()

if pizza == "Pepperoni":
    crust = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//li[@class='item col-12 col-md-6 col-lg-4 col-xl-4 col-xxl-3 m-0']//select[@id='CrustFlavorings']")))
    crust.click()
    garlic = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//li[@class='item col-12 col-md-6 col-lg-4 col-xl-4 col-xxl-3 m-0']//select[@id='CrustFlavorings']//option[@value='GarlicParmFlavoring']")))
    garlic.click()
    add_to_order = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//li[@class='item col-12 col-md-6 col-lg-4 col-xl-4 col-xxl-3 m-0']//button[@class='button button--small']")))
    add_to_order.click()
elif pizza == "Works":
    crust = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//li[@class='item col-12 col-md-6 col-lg-4 col-xl-4 col-xxl-3 m-0'][1]//select[@id='CrustFlavorings']")))
    crust.click()
    garlic = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//li[@class='item col-12 col-md-6 col-lg-4 col-xl-4 col-xxl-3 m-0'][1]//select[@id='CrustFlavorings']//option[@value='GarlicParmFlavoring']")))
    garlic.click()
    add_to_order = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//li[@class='item col-12 col-md-6 col-lg-4 col-xl-4 col-xxl-3 m-0'][1]//button[@class='button button--small']")))
    add_to_order.click()

time.sleep(1)
go_to_cart = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//li[@data-freight-target='nav-total']")))
go_to_cart.click()

driver.execute_script('''window.open("https://www.joinhoney.com/shop/papajohns/new/savings?hasOpened=1","_blank");''')
papa = driver.window_handles[0]
honey = driver.window_handles[1]
driver.switch_to.window(honey)
cs = driver.find_elements_by_class_name("copyContainer-0-2-276")

code_list = []
for x in cs: 
    code_list.append(x.text)

driver.switch_to.window(papa)

value = 0
code = ''
for code in code_list: 
    try:
        promo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='cart-summary-promo']")))
        promo.clear()
        promo.send_keys(code)
        apply = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='promo-submit']")))
        apply.click()
        discount = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "td[class='discounts-amount amount']")))
        discount = discount.text.strip('($)')
        if value < float(discount):
            value += float(discount)
    except:
        pass

print(f'You saved {value} with promo code {code}')


check_out = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='cart-summary-total']//button[@type='submit']")))
check_out.click()

cc = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='credit-card']//select[@name='creditCardPayment.cardId']")))
cc.click()
cc1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='credit-card']//select[@name='creditCardPayment.cardId']//option[@value='0']")))
cc1.click()
sc = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='input input--required']//input[@name='creditCardPayment.cvv']")))
sc.send_keys('000')
review_order = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='spacing-top-sm']//input[@value='Review Your Order']")))
review_order.click()

place_order = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='button-container']//button[@id='place-your-order']")))
place_order.click()