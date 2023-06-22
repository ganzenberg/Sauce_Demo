import time


class Webelements:

    input_username_id = "user-name"
    input_password_id = "password"
    btn_login_id = "login-button"
    select_product_xpath = "//select[@class='product_sort_container']"
    btn_add_cart_xpath = "//div[@class='inventory_list']/div[1]/descendant::button[1]"
    cart_xpath = "//div[@id='shopping_cart_container']"
    btn_chk_out_xpath = "//button[@id='checkout']"
    input_fname_id = "first-name"
    input_lname_id = "last-name"
    input_zip_id = "postal-code"
    btn_continue_id = "continue"
    total_value_xpath = "//div[@class='summary_info_label summary_total_label']"
    btn_finish_id = "finish"
    check_out_complete_xpath = "//h2[@class='complete-header']"

    # userdata

    act_logo = "//div[text()='Swag Labs']"
    act_error_msg = "Epic sadface: Sorry, this user has been locked out."
    value = 'Price (low to high)'
    fname = "John"
    lname = "Doe"
    zip_code = "123"
    act_value = 'Total: $8.63'
    check_out_msg = "Thank you for your order!"


    @staticmethod
    def wait(seconds):
        start_ms = time.time()
        stop_ms = start_ms + seconds
        for x in range(int(seconds * 5)):
            now_ms = time.time()
            if now_ms >= stop_ms:
                break
            time.sleep(0.2)