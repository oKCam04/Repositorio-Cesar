

import 'dart:io';

void menu() {
  int opcion = 0;

  do {
    print("1. Crear cuenta");
    print("2. Consignar Cuenta");
    print("3. Retirar Cuenta");
    print("4. Consultar Cuenta ");
    print("5. Listar Cuentas");
    print("6. Salir");
    opcion = int.parse(stdin.readLineSync().toString());

    switch (opcion){
      case 1:
      case 2:
      case 3:
      case 4:
      case 5:
      case 6:
        break;
    }
  } while (opcion != 6);


}
