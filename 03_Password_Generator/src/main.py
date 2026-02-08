import generador # Importamos tu lógica

def iniciar_programa():
    print("--- 🔐 GENERADOR DE CONTRASEÑAS PRO ---")
    
    while True:
        try:
            # 1. INPUTS: Aquí es donde la longitud es DINÁMICA
            longitud_input = input("\nIngrese la longitud de la contraseña: ")
            longitud = int(longitud_input)
            
            minis = input("¿Incluir Minúsculas? (S/N): ").upper()
            mayus = input("¿Incluir Mayúsculas? (S/N): ").upper()
            nums = input("¿Incluir Números? (S/N): ").upper()
            simb = input("¿Incluir Símbolos? (S/N): ").upper()
            
            # 2. PREPARACIÓN: Construimos el pool y el diccionario
            pool_usuario = generador.construir_pool(minis, mayus, nums, simb)
            
            mi_config = {
                'longitud': longitud,  # <--- Aquí va el número que escribió el usuario
                'pool': pool_usuario
            }
            
            # 3. LLAMADA: Enviamos la caja al generador
            resultado = generador.generar_password(mi_config)
            
            # 4. SALIDA: Mostramos el resultado
            print(f"\n✨ Tu contraseña es: {resultado}")
            print("-" * 30)
            
            # Preguntar si quiere salir
            continuar = input("¿Generar otra? (S/N): ").upper()
            if continuar == "N":
                print("¡Hasta luego, Ingeniero!")
                break
                
        except ValueError:
            print("❌ Error: La longitud debe ser un número entero.")

if __name__ == "__main__":
    iniciar_programa()