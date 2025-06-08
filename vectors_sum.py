import math

def read_number_of_vectors():
    while True:
        try:
            n = int(input("Ingrese la cantidad de vectores a sumar (minimo 2):"))
            if n >= 2:
                return n
            else:
                print("Se deben ingresar minimo 2 vectores.")
        except ValueError:
            print("Entrada no valida, por favor intentelo de nuevo.")
            
def read_input_method():
    while True:
        method = input(
            "Seleccione el metodo de entrada del vector:\n"
            "  1. Magnitud y direccion\n"
            "  2. Componentes (x, y)\n"
            "Opcion:"
        )
        if method in ('1', '2'):
            return method 
        print("Opcion no valida, por favor seleccione solo 1 o 2.")
        
def read_vector_by_mag_dir():
    while True:
        try:
            magnitude =  float(input("  Magnitud del vector: "))
            angle_deg = float(input("  Direccion en grados (0 grados = eje x positivo, contrario al reloj.): "))
            angle_rad = math.radians(angle_deg)
            x = magnitude * math.cos(angle_rad)
            y = magnitude * math.sin(angle_rad)
            return x, y
        except ValueError:
            print("Por favor ingrese los numeros correctamente.")
            
def read_vector_by_components():
    while True:
        try:
            x = float(input("  Componente x:  "))
            y = float(input("  Componente y:  "))
            return x, y
        except ValueError:
            print("Por favor ingrese los numeros correctamente.")
            
def main():
    print("Suma de n vectores")
    num_vectors = read_number_of_vectors()
    total_x = 0.0
    total_y = 0.0
    
    for i in range(1, num_vectors + 1):
        print(f"\nVector {i}:")
        method = read_input_method()
        if method == '1':
            x, y = read_vector_by_mag_dir()
        else:
            x, y = read_vector_by_components()
        total_x += x
        total_y += y
        
    print("\nResultado de la suma de los vectores:")
    print(f"  Componente x total: {total_x:.4f}")
    print(f"  Componente y total: {total_y:.4f}")
    
if __name__ == "__main__":
    main()
            