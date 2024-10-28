from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens.home import Home
from screens.pilih_level import pilihLevel
from screens.buah_level import BuahLevel
from screens.hewan_level import HewanLevel
from screens.kendaraan_level import KendaraanLevel
from screens.splash_screen import SplashScreen
from kivy.core.window import Window

class MerangkaiKata(App):
    def build(self):
        Window.size = (360, 640)
        sm = ScreenManager()
        
        splash_screen = SplashScreen(name='splash_screen')
        home_screen = Home(name='start_screen')
        pick_level_screen = pilihLevel(name='pick_screen')
        buah_level_screen = BuahLevel(name='Buah')
        hewan_level_screen = HewanLevel(name='Hewan')
        kendaraan_level_screen = KendaraanLevel(name='Kendaraan')
        
        buah_level_screen.set_pick_screen(pick_level_screen)
        hewan_level_screen.set_pick_screen(pick_level_screen)
        
        sm.add_widget(splash_screen)
        sm.add_widget(home_screen)
        sm.add_widget(pick_level_screen)
        sm.add_widget(buah_level_screen)
        sm.add_widget(hewan_level_screen)
        sm.add_widget(kendaraan_level_screen)
        
        sm.current = 'splash_screen'
        return sm

if __name__ == '__main__':
    MerangkaiKata().run()