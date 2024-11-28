import tkinter as tk

# Declarar la variable global
entries_area = []

def clasificar_iluminacion(area_total):
    if area_total < 50:
        return "Mínimo"
    elif 50 <= area_total < 100:
        return "Medio"
    else:
        return "Elevado"

def calcular_puntos():
    global entries_area
    try:
        num_habitaciones = int(entry_num_habitaciones.get())
        area_total = float(entry_area_total.get())
        demanda_consumo = float(entry_demandas.get())
        num_banos = int(entry_num_banos.get())
        
        puntos_luz_total = 0
        puntos_tomas_total = 0
        
        resultados = []
        area_habitaciones_total = 0
        
        # Cálculo por habitación
        for i in range(num_habitaciones):
            area_habitacion = float(entries_area[i].get())
            area_habitaciones_total += area_habitacion
            
            puntos_luz_habitacion = area_habitacion // 10
            puntos_tomas_habitacion = area_habitacion // 10
            
            puntos_luz_total += puntos_luz_habitacion
            puntos_tomas_total += puntos_tomas_habitacion
            
            consumo_luz_habitacion = puntos_luz_habitacion * 10
            consumo_tomas_habitacion = puntos_tomas_habitacion * 100
            
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
        consumo_luz_banos = puntos_luz_banos * 10
        consumo_tomas_banos = puntos_tomas_banos * 100
        consumo_total_banos = consumo_luz_banos + consumo_tomas_banos
        
        puntos_luz_total += puntos_luz_banos
        puntos_tomas_total += puntos_tomas_banos
        
        resultados.append(f"\nBaños: {num_banos} baños, "
                          f"{int(puntos_luz_banos)} puntos de luz, "
                          f"{int(puntos_tomas_banos)} tomas, "
                          f"Consumo: {int(consumo_total_banos)}W")
        
        # No se suman puntos de luz y tomas por número de habitaciones, corrigiendo el error anterior
        # Ajuste por demanda alta: Solo para baños, no para habitaciones
        if demanda_consumo > 1000:
            puntos_luz_total += num_banos  # Agregar 1 punto de luz por baño adicional
            puntos_tomas_total += num_banos  # Agregar 1 toma por baño adicional
        
        # Calcular consumos totales
        consumo_total_luz = puntos_luz_total * 10
        consumo_total_tomas = puntos_tomas_total * 100
        consumo_total = consumo_total_luz + consumo_total_tomas
        
        # Clasificar iluminación según área total
        clasificacion = clasificar_iluminacion(area_total)
        
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
        
        global entries_area
        entries_area = []
        
        for i in range(num_habitaciones):
            label = tk.Label(frame_habitaciones, text=f"Área de habitación {i + 1} (m²):", bg="#f5e6e8", fg="#4b4b4b")
            label.pack(anchor="w", padx=5, pady=2)
            entry_area = tk.Entry(frame_habitaciones, width=40)
            entry_area.pack(pady=2, padx=5)
            entries_area.append(entry_area)
    
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
entry_area_total = tk.Entry(frame_superior, width=15)
entry_area_total.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_superior, text="Demanda consumo (W):", bg="#f5e6e8", fg="#4b4b4b").grid(row=2, column=0, padx=5, pady=5, sticky="w")
entry_demandas = tk.Entry(frame_superior, width=15)
entry_demandas.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame_superior, text="Número de baños:", bg="#f5e6e8", fg="#4b4b4b").grid(row=3, column=0, padx=5, pady=5, sticky="w")
entry_num_banos = tk.Entry(frame_superior, width=15)
entry_num_banos.grid(row=3, column=1, padx=5, pady=5)

# Botones
boton_agregar = tk.Button(frame_superior, text="Agregar Habitaciones", command=agregar_habitaciones, bg="#6ba8a9", fg="white", width=20)
boton_agregar.grid(row=4, column=0, columnspan=2, pady=10)

boton_calcular = tk.Button(frame_superior, text="Calcular", command=calcular_puntos, bg="#6b74a8", fg="white", width=20)
boton_calcular.grid(row=5, column=0, columnspan=2, pady=10)

# Widget de texto para resultados en el frame de resultados
resultados_text = tk.Text(frame_resultados, height=20, bg="#fff8e6", fg="#4b4b4b")
resultados_text.pack(fill="both", expand=True, padx=5, pady=5)

ventana.mainloop()
