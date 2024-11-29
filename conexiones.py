import tkinter as tk
import math

# Variables globales para entradas dinámicas
entry_lado1_habitacion = []
entry_lado2_habitacion = []
entry_lado1_bano = []
entry_lado2_bano = []

def calcular_puntos():
    try:
        # Leer entradas principales
        num_habitaciones = int(entry_num_habitaciones.get())
        num_banos = int(entry_num_banos.get())
        area_total = float(entry_area_total.get())
        demanda_consumo = float(entry_demandas.get())
        watts_bombillos = int(entry_watts_bombillos.get())
        iluminacion_incandescente = bool(int(entry_iluminacion.get()))  # Convertir a booleano
        
        # Inicializar variables totales
        puntos_luz_habitacion_total = 0
        puntos_tomas_habitacion_total = 0
        consumo_luz_habitacion_total = 0
        consumo_tomas_habitacion_total = 0
        area_habitacion_total = 0
        perimetro_habitacion_total = 0
        
        puntos_luz_bano_total = 0
        puntos_tomas_bano_total = 0
        consumo_luz_bano_total = 0
        consumo_tomas_bano_total = 0
        area_bano_total = 0
        perimetro_bano_total = 0
        
        resultados = []

        # Determinar la densidad de carga según el nivel de consumo
        def nivel_consumo(area_total, demanda_consumo):
            if area_total <= 80 or demanda_consumo <= 3000:
                return "Mínimo"
            elif 80 < area_total <= 140 or 3000 < demanda_consumo <= 7000:
                return "Medio"
            else:
                return "Elevado"

        densidad_carga = nivel_consumo(area_total, demanda_consumo)
        val_iluminacion = 10 if densidad_carga == "Mínimo" else (15 if densidad_carga == "Medio" else 20)
        if not iluminacion_incandescente:
            val_iluminacion = 6 if densidad_carga in ["Mínimo", "Medio"] else 8

        # Procesar habitaciones
        for i in range(num_habitaciones):
            lado_h1 = float(entry_lado1_habitacion[i].get())
            lado_h2 = float(entry_lado2_habitacion[i].get())
            area_habitacion = lado_h1 * lado_h2
            perimetro_habitacion = 2 * (lado_h1 + lado_h2)

            # Calcular puntos de luz
            if area_habitacion <= 6:
                consumo_luz = 60
            elif 6 < area_habitacion <= 15:
                consumo_luz = 100
            else:
                consumo_luz = area_habitacion * val_iluminacion * 1.8
            puntos_luz = math.ceil(consumo_luz / watts_bombillos)
            puntos_luz_habitacion_total += puntos_luz
            consumo_luz_habitacion_total += consumo_luz

            # Calcular tomas
            puntos_tomas_area = math.ceil(area_habitacion / 10)
            puntos_tomas_perimetro = math.ceil(perimetro_habitacion / 5)
            puntos_tomas = max(puntos_tomas_area, puntos_tomas_perimetro)
            puntos_tomas_habitacion_total += puntos_tomas
            consumo_tomas_habitacion_total += puntos_tomas * 200

            resultados.append(f"Habitación {i+1}: {puntos_luz} puntos de luz, {puntos_tomas} tomas")

        # Procesar baños
        for i in range(num_banos):
            lado_b1 = float(entry_lado1_bano[i].get())
            lado_b2 = float(entry_lado2_bano[i].get())
            area_bano = lado_b1 * lado_b2

            # Calcular puntos de luz
            consumo_luz_bano = 60  # Siempre mínimo 60 W en baños
            puntos_luz_bano = math.ceil(consumo_luz_bano / watts_bombillos)
            puntos_luz_bano_total += puntos_luz_bano
            consumo_luz_bano_total += consumo_luz_bano

            # Calcular tomas (siempre 1 por baño)
            puntos_tomas_bano = 1
            puntos_tomas_bano_total += puntos_tomas_bano
            consumo_tomas_bano_total += puntos_tomas_bano * 200

            resultados.append(f"Baño {i+1}: {puntos_luz_bano} puntos de luz, {puntos_tomas_bano} tomas")

        # Calcular totales
        puntos_luz_total = puntos_luz_habitacion_total + puntos_luz_bano_total
        puntos_tomas_total = puntos_tomas_habitacion_total + puntos_tomas_bano_total
        consumo_total = consumo_luz_habitacion_total + consumo_tomas_habitacion_total + consumo_luz_bano_total + consumo_tomas_bano_total

        resultados.append("\n--- Totales ---")
        resultados.append(f"Puntos de luz: {puntos_luz_total}")
        resultados.append(f"Puntos de tomas: {puntos_tomas_total}")
        resultados.append(f"Consumo total: {consumo_total} W")

        # Mostrar resultados
        resultados_text.delete(1.0, tk.END)
        resultados_text.insert(tk.END, "\n".join(resultados))

    except ValueError:
        resultados_text.delete(1.0, tk.END)
        resultados_text.insert(tk.END, "Error: Verifique que los datos ingresados sean correctos.\n")
