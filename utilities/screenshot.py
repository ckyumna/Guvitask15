import os
from datetime import datetime


class Screenshot:

    @staticmethod
    def capture(driver, name):

        folder = "screenshots"

        if not os.path.exists(folder):
            os.makedirs(folder)

        time_stamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        file_name = f"{name}_{time_stamp}.png"

        path = os.path.join(folder, file_name)

        driver.save_screenshot(path)

        return path