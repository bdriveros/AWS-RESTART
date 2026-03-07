import json

def calcular_peso_molecular(secuencia):
    pesos_aa = {
        'A': 71.08, 'R': 156.19, 'N': 114.11, 'D': 115.09, 'C': 103.14,
        'E': 129.12, 'Q': 128.13, 'G': 57.05,  'H': 137.14, 'I': 113.16,
        'L': 113.16, 'K': 128.17, 'M': 131.20, 'F': 147.18, 'P': 97.12,
        'S': 87.08,  'T': 101.11, 'W': 186.21, 'Y': 163.18, 'V': 99.13
    }
    peso_molecular = 18.015 
    for aa in secuencia:
        if aa in pesos_aa:
            peso_molecular += pesos_aa[aa]
    return peso_molecular

def procesar_secuencia():
    secuencia = ""
    nombre_proteina = "Hemoglobina"
    
    try:
        with open('hemoglobin_analysis/hemoglobin_seq.txt', 'r') as file:
            for linea in file:
                if linea.startswith('>'):
                    nombre_proteina = linea.strip()[1:].split()[0]
                else:
                    secuencia += linea.strip().upper()
    except FileNotFoundError:
        print("No se encontró el archivo 'hemoglobin_seq.txt'")
        return

    print("EJERCICIO 4: ANALISIS:")
    print(f"LONGITUD: {len(secuencia)} aminoácidos")
    print(f"PRIMEROS 10: {secuencia[:10]}")
    print(f"ULTIMOS 10: {secuencia[-10:]}\n")

    print("EJERCICIO 5: COMPOSICION DE AMINOACIDOS")
    aminoacidos = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 
                   'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']
    
    composicion = {}
    for aa in aminoacidos:
        cantidad = secuencia.count(aa)
        if cantidad > 0:
            composicion[aa] = cantidad
            
    for aa, count in composicion.items():
        print(f"{aa}: {count}")
    print()

    print("EJERCICIO 6 Y 7: PESO MOLECULAR (FUNCION REUTILIZABLE)")
    peso_molecular = calcular_peso_molecular(secuencia)
    print(f"Peso molecular estimado: {peso_molecular} Da\n")

    print("EJERCICIO 8: GUARDAR RESULTADOS EN JSON")
    resultados = {
        "Nombre de la proteina": nombre_proteina,
        "Longitud de la secuencia": len(secuencia),
        "Conteo de aminoacidos": composicion,
        "Peso molecular calculado": peso_molecular
    }
    
    with open('hemoglobin_results.json', 'w') as json_file:
        json.dump(resultados, json_file, indent=4)
    print("Resultados guardados exitosamente en 'hemoglobin_results.json'.\n")

    print("EJERCICIO 9: PORCENTAJE DE AMINOACIDOS HIDROFOBICOS")
    hidrofobicos = ['A', 'V', 'I', 'L', 'M', 'F', 'W', 'Y']
    total_hidrofobicos = sum(secuencia.count(aa) for aa in hidrofobicos)
    porcentaje_hidrofobico = (total_hidrofobicos / len(secuencia)) * 100
    print(f"Porcentaje de aminoácidos hidrofóbicos: {porcentaje_hidrofobico}%")

if __name__ == '__main__':
    procesar_secuencia()