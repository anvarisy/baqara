
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
def main():
    print("Hello World!")


def query_contact(number: str):
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

    # Attempt to find the figure element that indicates spam or secure status
    try:
        figure_element = driver.find_element(By.CSS_SELECTOR, "figure")
        figure_style = figure_element.get_attribute('style')

        # Check if the figure's background image URL indicates a spam suspicion
        is_spam = "user-default-spam.jpg" in figure_style
    except Exception as e:
        print(f"Error finding or analyzing figure element: {e}")
        is_spam = False  # Default to False if there's an error

    # Mengambil data dari elemen setelah klik
    tags_container = driver.find_element(By.ID, "tagList")
    tags = tags_container.find_elements(By.CLASS_NAME, "rtl-item")

    # Mengumpulkan teks dari setiap tag
    tags_text = [tag.text for tag in tags]
    return tags_text, is_spam


if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_argument("--enable-chrome-browser-cloud-management")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://web.getcontact.com/")

    print("Silakan scan QR code dengan aplikasi Getcontact pada smartphone Anda.")
    sleep(20)
    print("Scan success")
    with open('phone-numbers.txt', 'r') as file:
        phones = [line.strip() for line in file.readlines()]
    results = []

    # Iterasi melalui setiap nomor telepon
    for phone in phones:
        tags, is_spam = query_contact(phone)  # Adjusted to receive is_spam
        spam_status = "Suspected Spam" if is_spam else "Secure"
        for tag in tags:
            results.append({"Nomor HP": phone, "Tag": tag, "Status": spam_status})
        sleep(3)


    # Membuat DataFrame dari hasil
    df = pd.DataFrame(results)

    # Menyimpan ke Excel
    df.to_excel('hasil_scraping.xlsx', index=False)

driver.quit()



