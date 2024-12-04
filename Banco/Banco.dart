
import 'usuario.dart';

class Banco {
  int? _id_banco;
  String? _nombre_banco;
  String? _telefono_banco;
  List<Usuario>? listaUsuarios;

  Banco(this._id_banco, this._nombre_banco, this._telefono_banco){
    this._id_banco;
    this._nombre_banco;  
    this._telefono_banco;
  }

  //metodos
  set idbanco(int? _id_banco) {
    this._id_banco = _id_banco;
  }

  set nombrebanco(String? _nombre_banco) {
    this._nombre_banco = _nombre_banco;
  }

  set telefono(String? telefono) {
    this._telefono_banco = telefono;
  }
  int? get idbanco {
    return _id_banco;
  }
  String? get nombrebanco {
    return _nombre_banco;
  }
  String? get telefono {
    return _telefono_banco;
  }
}