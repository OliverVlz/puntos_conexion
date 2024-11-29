import tkinter as tk
import math

# Declarar la variable global
entry_area_habitacion = []
entry_area_bano = []

def calcular_puntos():
    global entry_area_habitacion, entry_area_bano
    try:
        num_habitaciones = int(entry_num_habitaciones.get())
        num_banos = int(entry_num_banos.get())
        num_divisiones = num_habitaciones + num_banos
        demanda_consumo = float(entry_demandas.get())
        watts_bombillos = int(entry_watts_bombillos.get())
        
        puntos_luz_total = 0
        puntos_tomas_total = 0
        consumo_total_luz = 0
        consumo_total_tomas = 0
        densidad_carga = 0
        potencia_luz_habitacion = 0
        iluminacion_incandenscente = False
        iluminacion_fluorecente = False
        val_iluminacion = 0
           
        resultados = []
        area_habitaciones_total = 0

        def nivel_consumo(area_total, demanda_consumo):
                if area_total <= 80 or demanda_consumo <= 3000:
                    return "Mínimo"
                elif 80 < area_total <= 140 or 3000 < demanda_consumo <= 7000:
                    return "Medio"
                else:
                    return "Elevado"
                
        def area_individual(lado1, lado2, num_total):
            area = []
            for i in range(num_total):
                param1 = float(lado1[i].get())
                param2 = float(lado2[i].get())
                area.append(param1 * param2)
            return area

        def perimetro_individual(lado1, lado2, num_total):
            perimetro = []
            for i in range(num_total):
                param1 = float(lado1[i].get())
                param2 = float(lado2[i].get())
                perimetro.append(2 * (param1 + param2))
            return perimetro
        
        def area_total(area_habitacion, area_bano):
            
        
        def perimetro_total(perimetro_habitacion):
            return perimetro_total
        
        # Cálculo de habitaciones
        for i in range(num_habitaciones):
            lado1 = float(entry_lado1_habitacion[i].get())
            lado2 = float(entry_lado2_habitacion[i].get())
            area_habitacion = lado1 * lado2
            perimetro_habitacion = 2 * (lado1 + lado2)
            perimetro_habitacion_total += perimetro_habitacion
            area_habitacion_total += area_habitacion
            
        for i in range(num_banos):
            area_bano = float(entry_area_bano[i].get())
            area_bano_total += area_bano

        area_total = area_habitacion_total + area_bano_total 
        densidad_carga = nivel_consumo(area_total, demanda_consumo)

        if densidad_carga == "Mínimo":
            if iluminacion_incandenscente == True:
                val_iluminacion = 10
            else:
                val_iluminacion = 6
            
        elif densidad_carga == "Medio":
            if iluminacion_incandenscente == True:
                val_iluminacion = 15
            else:
                val_iluminacion = 6
        else:
            if iluminacion_incandenscente == True:
                val_iluminacion = 20
            else:
                val_iluminacion = 8

        for i in range(num_habitaciones):
            area_habitacion = float(entry_area_habitacion[i].get())
            
            # Calcular puntos de luz
            "Si no se conocen datos precisos, la potencia nominal de las luminarias"
            "debe tenerse como mínimo 1.8 veces la potencia nominal de la lámpara en vatios."
            potencia_luz_habitacion = val_iluminacion * area_habitacion * 1.8
            puntos_luz_habitacion = math.ceil(potencia_luz_habitacion / watts_bombillos)

            # Calcular tomas de corriente
            # Basado en área: 1 toma cada 10 m²
            puntos_tomas_habitacion_area = math.ceil(area_habitacion / 10)

            # Basado en perímetro (asumiendo forma cuadrada)
            lado = math.sqrt(area_habitacion)
            perimetro = 4 * lado
            puntos_tomas_habitacion_perimetro = math.ceil(perimetro / 5)

            # Tomar el mayor valor entre los dos criterios para determinar las tomas
            puntos_tomas_habitacion = max(puntos_tomas_habitacion_area, puntos_tomas_habitacion_perimetro)


        # Cálculo por divisiones
        for i in range(num_divisiones):
            
            # Calcular puntos de luz (1 punto cada 10 m², redondeando hacia arriba)
            puntos_luz_habitacion = math.ceil(area_habitacion / 10)

            # Calcular tomas de corriente
            # Basado en área: 1 toma cada 10 m²
            puntos_tomas_habitacion_area = math.ceil(area_habitacion / 10)

            # Basado en perímetro (asumiendo forma cuadrada)
            lado = math.sqrt(area_habitacion)
            perimetro = 4 * lado
            puntos_tomas_habitacion_perimetro = math.ceil(perimetro / 5)

            # Tomar el mayor valor entre los dos criterios para determinar las tomas
            puntos_tomas_habitacion = max(puntos_tomas_habitacion_area, puntos_tomas_habitacion_perimetro)

            # Actualizar los totales
            puntos_luz_total += puntos_luz_habitacion
            puntos_tomas_total += puntos_tomas_habitacion
            
            # Calcular consumo por habitación
            consumo_luz_habitacion = puntos_luz_habitacion * 10  # 10 W por punto de luz
            consumo_tomas_habitacion = puntos_tomas_habitacion * 200  # 100 W por toma
            
            # Acumular los consumos totales
            consumo_total_luz += consumo_luz_habitacion
            consumo_total_tomas += consumo_tomas_habitacion
            
            # Calcular consumo total por habitación
            consumo_total_habitacion = consumo_luz_habitacion + consumo_tomas_habitacion
            
            resultados.append(f"Habitación {i + 1}: {int(puntos_luz_habitacion)} puntos de luz, "
                              f"{int(puntos_tomas_habitacion)} tomas, "
                              f"Consumo: {int(consumo_total_habitacion)}W")
        
        # Verificar si el área total de las habitaciones excede el área disponible
        if area_habitaciones_total > area_total:
            resultados_text.delete(1.0, tk.END)
            resultados_text.insert(tk.END, "Error: El área total de las habitaciones excede el área total disponible.\n")
            return
        
        # Cálculo por baños
        puntos_luz_banos = num_banos
        puntos_tomas_banos = num_banos
        consumo_luz_banos = puntos_luz_banos * 10  # 10 W por punto de luz en baños
        consumo_tomas_banos = puntos_tomas_banos * 100  # 100 W por toma en baños
        consumo_total_banos = consumo_luz_banos + consumo_tomas_banos
        
        # Actualizar los totales
        puntos_luz_total += puntos_luz_banos
        puntos_tomas_total += puntos_tomas_banos
        consumo_total_luz += consumo_luz_banos
        consumo_total_tomas += consumo_tomas_banos
        
        resultados.append(f"\nBaños: {num_banos} baños, "
                          f"{int(puntos_luz_banos)} puntos de luz, "
                          f"{int(puntos_tomas_banos)} tomas, "
                          f"Consumo: {int(consumo_total_banos)}W")
        
        # Calcular consumo total final
        consumo_total = consumo_total_luz + consumo_total_tomas
        
        # Clasificar iluminación según área total
        clasificacion = nivel_consumo(area_total)
        
        # Agregar totales a los resultados
        resultados.append(f"\nTotal puntos de luz: {int(puntos_luz_total)}")
        resultados.append(f"Total tomas: {int(puntos_tomas_total)}")
        resultados.append(f"Clasificación: {clasificacion}")
        resultados.append(f"Consumo luces: {int(consumo_total_luz)}W")
        resultados.append(f"Consumo tomas: {int(consumo_total_tomas)}W")
        resultados.append(f"Consumo total: {int(consumo_total)}W")
        
        # Mostrar resultados en el cuadro de texto
        resultados_text.delete(1.0, tk.END)
        resultados_text.insert(tk.END, "\n".join(resultados))
    
    except ValueError:
        resultados_text.delete(1.0, tk.END)
        resultados_text.insert(tk.END, "Error: Verifique que los datos ingresados sean correctos.\n")

def agregar_habitaciones():
    try:
        num_habitaciones = int(entry_num_habitaciones.get())
        for widget in frame_habitaciones.winfo_children():
            widget.destroy()
        
        global entry_area_habitacion
        entry_area_habitacion = []
        
        for i in range(num_habitaciones):
            label = tk.Label(frame_habitaciones, text=f"Área de habitación {i + 1} (m²):", bg="#f5e6e8", fg="#4b4b4b")
            label.pack(anchor="w", padx=5, pady=2)
            entry_area = tk.Entry(frame_habitaciones, width=40)
            entry_area.pack(pady=2, padx=5)
            entry_area_habitacion.append(entry_area)
    
    except ValueError:
        resultados_text.delete(1.0, tk.END)
        resultados_text.insert(tk.END, "Error: Ingrese un número válido de habitaciones.\n")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Puntos de Luz y Tomas")
ventana.geometry("700x700")
ventana.configure(bg="#f5e6e8")

# Crear Frames
frame_superior = tk.Frame(ventana, bg="#f5e6e8", pady=10)
frame_superior.pack(fill="x")

frame_habitaciones = tk.Frame(ventana, bg="#e6f5e8", pady=10)
frame_habitaciones.pack(fill="x", padx=10, pady=10)

frame_resultados = tk.Frame(ventana, bg="#e8e6f5", pady=10)
frame_resultados.pack(fill="both", expand=True, padx=10, pady=10)

# Entradas en el frame superior
tk.Label(frame_superior, text="Número de habitaciones:", bg="#f5e6e8", fg="#4b4b4b").grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_num_habitaciones = tk.Entry(frame_superior, width=15)
entry_num_habitaciones.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_superior, text="Área total (m²):", bg="#f5e6e8", fg="#4b4b4b").grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_area_bano = tk.Entry(frame_superior, width=15)
entry_area_bano.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_superior, text="Demanda consumo (W):", bg="#f5e6e8", fg="#4b4b4b").grid(row=2, column=0, padx=5, pady=5, sticky="w")
entry_demandas = tk.Entry(frame_superior, width=15)
entry_demandas.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame_superior, text="Número de baños:", bg="#f5e6e8", fg="#4b4b4b").grid(row=3, column=0, padx=5, pady=5, sticky="w")
entry_num_banos = tk.Entry(frame_superior, width=15)
entry_num_banos.grid(row=3, column=1, padx=5, pady=5)

tk.Label(frame_superior, text="Watts por bombillo:", bg="#f5e6e8", fg="#4b4b4b").grid(row=4, column=0, padx=5, pady=5, sticky="w")
entry_watts_bombillos = tk.Entry(frame_superior, width=15)
entry_watts_bombillos.grid(row=4, column=1, padx=5, pady=5)

# Botones
boton_agregar = tk.Button(frame_superior, text="Agregar Habitaciones", command=agregar_habitaciones, bg="#6ba8a9", fg="white", width=20)
boton_agregar.grid(row=4, column=0, columnspan=2, pady=10)

boton_calcular = tk.Button(frame_superior, text="Calcular", command=calcular_puntos, bg="#6b74a8", fg="white", width=20)
boton_calcular.grid(row=5, column=0, columnspan=2, pady=10)

# Widget de texto para resultados en el frame de resultados
resultados_text = tk.Text(frame_resultados, height=20, bg="#fff8e6", fg="#4b4b4b")
resultados_text.pack(fill="both", expand=True, padx=5, pady=5)

ventana.mainloop()
