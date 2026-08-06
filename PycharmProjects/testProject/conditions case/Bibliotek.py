from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import random

# 📧 E-Mail ayarları
absender = "formessages77@gmail.com"
password = "ugzu tgix hazj lbru"

def send_email(text):
    msg = MIMEMultipart()
    msg["From"] = absender
    recipients = ["lilikhmelnitskaya@ukr.net", "abdullayevelmar758@gmail.com"]
    msg["To"] = ", ".join(recipients)
    msg["Subject"] = "Neue Wohnung"
    msg.attach(MIMEText(text, "plain"))

    try:
        mail = smtplib.SMTP("smtp.gmail.com", 587)
        mail.starttls()
        mail.login(absender, password)
        mail.sendmail(msg["From"], recipients, msg.as_string())
        mail.quit()
        print("📨 Mail gönderildi.")
    except Exception as e:
        print("❌ Mail hatası:", e)

# ✅ Daha gerçekçi scroll işlemi (sonsuz scroll destekli)
def human_scroll(driver, scroll_pause_time=1.0):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause_time)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

# ✅ Chrome ayarları
chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument(r"--user-data-dir=C:\Users\abdul\AppData\Local\Google\Chrome\default")

# 🔧 Service
service = Service()

# 🌐 URL
url = "https://www.immobilienscout24.de/Suche/de/hamburg/hamburg/wohnung-mieten?numberofrooms=2.5-5&price=300.0-950.0&livingspace=60.0-110.0&exclusioncriteria=swapflat&pricetype=rentpermonth&sorting=2"

# 🧠 Son başlık
last_title = ""

# 🚀 Driver başlat
driver = webdriver.Chrome(service=service, options=chrome_options)
actions = ActionChains(driver)

# 🔁 Ana döngü
while True:
    try:
        driver.get(url)
        print("🌍 Sayfa yükleniyor...")

        human_scroll(driver)

        # 📦 İçeriği al
        soup = BeautifulSoup(driver.page_source, "html.parser")
        data = soup.find("h2", attrs={"data-testid": "headline"})

        if data:
            title = data.text.strip()
            print("🔍 Bulunan başlık:", title)

            if title != last_title:
                last_title = title
                send_email(f"Neue Wohnung gefunden: {title}")
            else:
                print("⚠️ Yeni ev yok.")
        else:
            print("⚠️ Başlık bulunamadı (CAPTCHA olabilir)")
            send_email("Problem  Problem Problem Problem Problem Problem Problem Problem Problem")

    except Exception as e:
        print("🚨 Hata:", e)

    # 🔁 Rastgele 10 saniye gecikme (anti-bot)
    time.sleep(random.uniform(9.0, 11.0))
