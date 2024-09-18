import 'cuentabanco.dart';
import 'ususario.dart';

class Banco {
  List<CuentaBanco> cuentas = [];
  int contadorCuentas = 1;

  void crearCuenta(Usuario usuario) {
    String anio = DateTime.now().year.toString();
    String codigo = '$anio-${contadorCuentas++}';
    CuentaBanco nuevaCuenta = CuentaBanco(codigo, DateTime.now(), 0.0, usuario);
    cuentas.add(nuevaCuenta);
    print('Cuenta creada exitosamente con el código: $codigo');
  }
  void consignar(String codigoCuenta, double monto) {
    CuentaBanco? cuenta = buscarCuenta(codigoCuenta);
    if (cuenta != null) {
      cuenta.consignar(monto);
    } else {
      print('La cuenta no fue encontrada .');
    }
  }


  void retirar(String codigoCuenta, double monto) {
    CuentaBanco? cuenta = buscarCuenta(codigoCuenta);
    if (cuenta != null) {
      cuenta.retirar(monto);
    } else {
      print('La cuenta no fue encontrada.');
    }
  }

  CuentaBanco? buscarCuenta(String codigo) {
    for (var cuenta in cuentas) {
      if (cuenta.codigo == codigo) {
        return cuenta;
      }
    }
    return null;
  }

  void listarCuentas() {
    if (cuentas.isEmpty) {
      print('No existen cuentas registradas.');
    } else {
      for (var cuenta in cuentas) {
        print(
            'Cuenta ${cuenta.codigo} - Saldo: \$${cuenta.saldo.toStringAsFixed(2)}');
      }
    }
  }
}
