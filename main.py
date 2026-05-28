from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivy.clock import Clock
import random

class DashboardScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Layout principal vertical
        layout = MDBoxLayout(orientation='vertical', padding=30, spacing=20)
        
        # Título de la App
        self.title_label = MDLabel(
            text="🛴 E-Scooter Controller",
            font_style="H4",
            halign="center",
            theme_text_color="Primary"
        )
        layout.add_widget(self.title_label)
        
        # Indicador de Velocidad
        self.speed_label = MDLabel(
            text="0\nkm/h",
            font_style="H1",
            halign="center",
            theme_text_color="Secondary"
        )
        layout.add_widget(self.speed_label)
        
        # Indicador de Batería
        self.battery_label = MDLabel(
            text="🔋 Batería: 100%",
            font_style="H5",
            halign="center"
        )
        layout.add_widget(self.battery_label)
        
        # Botón de Bloqueo (Simulación)
        self.lock_btn = MDRaisedButton(
            text="BLOQUEAR SCOOTER",
            pos_hint={"center_x": .5},
            md_bg_color=(1, 0, 0, 1) # Rojo
        )
        self.lock_btn.bind(on_press=self.toggle_lock)
        layout.add_widget(self.lock_btn)
        
        self.add_widget(layout)
        self.locked = False

        # Temporizador para simular datos en tiempo real (cada 1 segundo)
        Clock.schedule_interval(self.simular_datos_scooter, 1.0)

    def simular_datos_scooter(self, dt):
        if not self.locked:
            # Simula velocidad entre 0 y 25 km/h
            nueva_velocidad = random.randint(10, 25)
            self.speed_label.text = f"{nueva_velocidad}\nkm/h"
        else:
            self.speed_label.text = "0\nkm/h"

    def toggle_lock(self, instance):
        self.locked = not self.locked
        if self.locked:
            self.lock_btn.text = "DESBLOQUEAR SCOOTER"
            self.lock_btn.md_bg_color = (0, 0.6, 0, 1) # Verde
            self.battery_label.text = "🔒 Scooter Bloqueado"
        else:
            self.lock_btn.text = "BLOQUEAR SCOOTER"
            self.lock_btn.md_bg_color = (1, 0, 0, 1) # Rojo
            self.battery_label.text = "🔋 Batería: 95%"

class ScooterApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"  # Modo oscuro para ahorrar batería
        self.theme_cls.primary_palette = "Blue"
        return DashboardScreen()

if __name__ == "__main__":
    ScooterApp().run()