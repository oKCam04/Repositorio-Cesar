
import 'ususario.dart';
class CuentaBanco {
  String codigo;
  Usuario usuario;
  double saldo;
  DateTime fecha;
  CuentaBanco(this.codigo, this.fecha, this.saldo, this.usuario);


  void consignar(double monto) {
    saldo += monto;
    print(
        'La consignación es exitosa. Tu saldo es: \$${saldo.toStringAsFixed(2)}');
  }

  
  void retirar(double monto) {
    if (monto <= saldo) {
      saldo -= monto;
      print('Tu retiro es exitoso. Tu saldo es: \$${saldo.toStringAsFixed(2)}');
    } else {
      print('Tu saldo insuficiente.');
    }
  }
}
