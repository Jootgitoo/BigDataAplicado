import json
from tkinter import Tk, filedialog

# Oculta la ventana principal de Tkinter
Tk().withdraw()

# Pedir al usuario que seleccione el archivo JSON
ruta_archivo = filedialog.askopenfilename(
    title="Selecciona el archivo JSON",
    filetypes=[("Archivos JSON", "*.json"), ("Todos los archivos", "*.*")]
)

if not ruta_archivo:
    print("❌ No se seleccionó ningún archivo. Saliendo...")
    exit()

print(f"📂 Archivo seleccionado: {ruta_archivo}")

# Cargar el JSON original
with open(ruta_archivo, "r", encoding="utf-8-sig") as f:
    data = json.load(f)

# Extraer campos y registros
fields = [f["id"] for f in data["fields"]]
records = data["records"]

# Crear documentos con estructura tipo MongoDB
documentos = [{fields[i]: record[i] for i in range(len(fields))} for record in records]

# Guardar uno por línea, como el dataset de restaurantes
ruta_salida = ruta_archivo.replace(".json", "_mongo.json")

with open(ruta_salida, "w", encoding="utf-8") as f:
    for doc in documentos:
        json.dump(doc, f, ensure_ascii=False)
        f.write("\n")

print(f"✅ Archivo convertido correctamente: {ruta_salida}")
print("Puedes importarlo en MongoDB con:")
print(f"mongoimport --db tu_base --collection tu_coleccion --file \"{ruta_salida}\"")
