
import 'dart:io';
import 'ususario.dart';
import 'cuentabanco.dart';
import 'banco.dart';


void mostrarMenu() {
  print('''\nMENÚ BANCO ADSO 2874057
1. Crear Cuenta
2. Consignar Cuenta
3. Retirar Cuenta
4. Consultar Cuenta Por Código
5. Listar Cuentas
6. Salir
Ingrese Opción (1-6):''');
}

void main() {
  Banco banco = Banco();

  while (true) {
    mostrarMenu();
    String? opcion = stdin.readLineSync();

    switch (opcion) {
      case '1':
        print('Ingrese su identificación:');
        String? identificacion = stdin.readLineSync();
        print('Ingrese el nombre del usuario:');
        String? nombre = stdin.readLineSync();
        print('Ingrese el correo del usuario:');
        String? correo = stdin.readLineSync();

        Usuario usuario = Usuario(identificacion!, nombre!, correo!);
        banco.crearCuenta(usuario);
        break;

      case '2':
        print('Ingrese el código asigando a la cuenta:');
        String? codigoCuenta = stdin.readLineSync();
        print('Ingrese la cantidad a consignar:');
        double montoConsignar = double.parse(stdin.readLineSync()!);
        banco.consignar(codigoCuenta!, montoConsignar);
        break;

      case '3':
        print('Ingrese el código asigando a la cuenta:');
        String? codigoCuentaRetiro = stdin.readLineSync();
        print('Ingrese la cantidad a consignar:');
        double montoRetirar = double.parse(stdin.readLineSync()!);
        banco.retirar(codigoCuentaRetiro!, montoRetirar);
        break;

      case '4':
        print('Ingrese el código asigando a la cuenta:');
        String? codigoConsulta = stdin.readLineSync();
        CuentaBanco? cuenta = banco.buscarCuenta(codigoConsulta!);
        if (cuenta != null) {
          print('Cuenta ${cuenta.codigo} - Saldo: \$${cuenta.saldo.toStringAsFixed(2)}');
        } else {
          print('La cuenta no fue encontrada.');
        }
        break;

      case '5':
        banco.listarCuentas();
        break;

      case '6':
        print('Saliendo del sistema...');
        exit(0);

      default:
        print('La opción no es válida. Intentelo nuevamente.');
    }
  }
}


