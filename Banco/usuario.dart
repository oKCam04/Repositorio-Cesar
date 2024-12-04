import 'cuenta_ahorros.dart';

class Usuario{
  int? _id_usuario;
  int? _identificacion;
  String? _nombre_usuario;
  String? _correo_usuario;
  List<CuentaAhorros>? _cuentaAhorros=[];

  Usuario(this._id_usuario, this._identificacion, this._correo_usuario, this._nombre_usuario){
    this._id_usuario;
    this._identificacion;
    this._correo_usuario;
    this._nombre_usuario;
  }

  set cuentaAhorros(List<CuentaAhorros>? cuentaAhorros){
    this._cuentaAhorros = cuentaAhorros;
  }
  set idUsuario(int? id_usuario){
    this._id_usuario = id_usuario;
  }
  set identificacion(int? identificacion){
    this._identificacion = identificacion;
  }
  set correoUsuario(String? correo_usuario){
    this._correo_usuario = correo_usuario;
  }
  set nombreUsuario(String? nombre_usuario){
    this._nombre_usuario = nombre_usuario;
  }

  int? get idUsuario{
    return _id_usuario;
  }
  int? get identificacion{
    return _identificacion;
  }
  String? get correoUsuario{
    return _correo_usuario;
  }
  String? get nombreUsuario{
    return _nombre_usuario;
  }
}