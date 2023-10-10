import usuarios.usuario as modelo
import notas.acciones


class Acciones:

    def registro(self):
        print("\nOk!! Vamos a registrarte en el sistema...")
        nombre = input("¿Cual es tu nombre?: ")
        apellidos = input("¿Cual son tus apellidos?: ")
        email = input("¿Cual es tu email?: ")
        password = input("¿Cual es tu contraseña?: ")

        usuario = modelo.Usuario(nombre, apellidos,email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"Perfecto {registro[1].nombre} te has registrado correctamente con el email {registro[1].email}")
        else:
            print("no te has registrado correctamente")

    def login(self):
        print("Vale!! Identificate en el sistema...")

        try:
            email = input("Introduce tu email: ")
            password = input("Introduce tu contraseña: ")

            usuario = modelo.Usuario('', '', email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"Bienvenido {login[1]}, te has registrado en el sistema el {login[5]}")
                self.proximasAcciones(login)
        except Exception as e:
            #print(type(e))
            #print(type(e).__name__)
            print(f"Login incorrecto!! Inténtalo más tarde")

    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles:
        - Crear nota (crear)
        - Mostrar tus notas (mostrar)
        - Eliminar nota (eliminar)
        - Salir (salir)
        """)

        accion = input("¿Qué acción quieres realizar?: ")
        hazEl = notas.acciones.Acciones()

        if accion == "crear":
            print("Vamos a crear")
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)
        elif accion == "mostrar":
            print("Vamosa  mostrar")
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == "eliminar":
            hazEl.borrar(usuario)
            print("vamos a eliminar")
            self.proximasAcciones(usuario)
        elif accion == "salir":
            print(f"Hasta pronto {usuario[1]}")
            exit()
