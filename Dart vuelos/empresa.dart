import 'vuelo.dart';

class Empresa {
  late String _nombre;
  late int _nit;
 late List<Vuelo> _vuelos;

  //contructor 
   Empresa(this._nombre, this._nit){this._vuelos=[];
   }
  String getNombre(){
    return this._nombre;
  }
  int getNit(){
    return this._nit;
  }
  List<Vuelo> ListarVuelos(){
    return _vuelos;
  }

  void registrarVuelo(int numeroVuelo, String ciudadOrigen, String ciudadDestino, DateTime fehca){
    Vuelo vuelo= Vuelo(numeroVuelo, ciudadOrigen, ciudadDestino, fecha);
  }
}