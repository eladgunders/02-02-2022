from kivymd.uix.screen import Screen
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
import threading
from datetime import datetime
import time


class MyThread(threading.Thread):
    def __init__(self, value):
        threading.Thread.__init__(self)
        self.value = value

    def run(self):
        while True:
            time.sleep(1)
            self.value.text = str(datetime.now().isoformat(" ", "seconds"))


class MyApp(MDApp):
    def build(self):
        screen = Screen()
        clock_label = MDLabel(text='Hello!', pos_hint={'center_x': 0.7, 'center_y': 0.5}, font_style='H1')
        screen.add_widget(clock_label)
        clock_thread = MyThread(clock_label)
        clock_thread.daemon = True
        clock_thread.start()
        return screen


if __name__ == "__main__":
    MyApp().run()
