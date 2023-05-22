
class Conectar_BD():
    def __init__(self) -> None:
        try:
            self.conexion = mysql.connector.connect(
                host= "localhost",
                port= 3306, 
                user= "root",
                password= 'maximiliano1o1o',
                db= "bd_ejemplo_it"
            )
        except mysql.connector.Error as descriptionError: 
            print("La base de datos no se pudo conectar", descriptionError)
    
                