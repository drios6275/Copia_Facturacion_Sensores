from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
import sys
sys.path.append("src")
from model.logica_sensores import calcular_valor_factura




class FacturacionSensoresApp(App):
    def build(self):
        contenedor = GridLayout(rows = 3,cols = 2)
        etiqueta1 = Label(text = "Numero servicios")
        etiqueta2 = Label(text = "Precio Unitario")
        self.numero_servicio = TextInput()
        self.precio_unitario = TextInput()
        boton_calcular = Button(text = "Calcular factura")
        self.resultado = Label(text = "Aqui va el resultado")

        contenedor.add_widget(etiqueta1)
        contenedor.add_widget(self.numero_servicio)
        contenedor.add_widget(etiqueta2)
        contenedor.add_widget(self.precio_unitario)
        contenedor.add_widget(boton_calcular)
        contenedor.add_widget(self.resultado)


        boton_calcular.bind(on_press = self.calcular_factura)


        return contenedor


    def calcular_factura(self,sender):

        numero_servicio: int = int(self.numero_servicio.text)
        precio_unitario: float = float(self.precio_unitario.text)
        resultado = calcular_valor_factura(numero_servicio,precio_unitario)
        self.resultado.text = str(resultado)




if __name__ == "__main__":
    FacturacionSensoresApp().run()