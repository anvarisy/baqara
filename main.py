
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
def main():
    print("Hello World!")


def query_contact(number:str):
    input_field = driver.find_element(By.ID, "numberInput")
    input_field.clear()
    input_field.send_keys(number)

    # Temukan dan klik tombol submit
    submit_button = driver.find_element(By.ID, "submitButton")
    submit_button.click()

    # Tunggu hasilnya atau lakukan aksi selanjutnya
    sleep(10)
    button_collapse = driver.find_element(By.CLASS_NAME, "rbi-link")
    button_collapse.click()
    sleep(5)
    # Mengambil data dari elemen setelah klik
    tags_container = driver.find_element(By.ID, "tagList")
    tags = tags_container.find_elements(By.CLASS_NAME, "rtl-item")

    # Mengumpulkan teks dari setiap tag
    tags_text = [tag.text for tag in tags]
    return tags_text


if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_argument("--enable-chrome-browser-cloud-management")
    driver = webdriver.Chrome(options=options)
    driver.get("https://web.getcontact.com/")

    print("Silakan scan QR code dengan aplikasi Getcontact pada smartphone Anda.")
    sleep(20)
    print("Scan success")
    phones = ["8194010777","85726451070","82290352117","87876977654","82281878461"]
    results = []

    # Iterasi melalui setiap nomor telepon
    for phone in phones:
        tags = query_contact(phone)
        for tag in tags:
            results.append({"Nomor HP": phone, "Tag": tag})
        sleep(3)

    # Membuat DataFrame dari hasil
    df = pd.DataFrame(results)

    # Menyimpan ke Excel
    df.to_excel('hasil_scraping.xlsx', index=False)

driver.quit()



