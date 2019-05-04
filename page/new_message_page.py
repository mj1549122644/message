from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class NewMessagePage(BaseAction):

    # 接收者
    phone_edit_text = By.XPATH, "//*[@text='接收者']"
    # 键入信息
    message_edit_text = By.XPATH, "//*[@text='键入信息']"
    # 发送
    send_button = By.XPATH, "//*[@content-desc='发送']"

    def input_phone(self, content):
        self.input(self.phone_edit_text, content)

    def input_message(self, content):
        self.input(self.message_edit_text, content)

    def click_send(self):
        self.click(self.send_button)
