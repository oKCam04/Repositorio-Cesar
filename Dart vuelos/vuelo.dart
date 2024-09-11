import 'pasajero.dart';

class Vuelo {

  //atributos
  late int _numeroVuelo;
  late String _ciudadOrigen;
  late String _ciudadDestino;
  late DateTime _fecha;
  late List<Pasajero> _pasajeros;

  Vuelo (
    this._numeroVuelo, this._ciudadOrigen, this._ciudadDestino, this._fecha,
  ){this._pasajeros=[];
  }

  int getNumeroVuelo(){
    return this._numeroVuelo;
  }
  String getciudadOrigen(){
    return this._ciudadOrigen;
  }
   String getciudadDestino(){
    return this._ciudadDestino;
  }
  DateTime getfecha(){
    return this._fecha;
  }
  List<Pasajero> listarPasajeros(){
    return this._pasajeros;
  }

}
