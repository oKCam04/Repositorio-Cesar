class Pasajero {
  //Atributos
  late String _identificacion;
  late String _nombres;
  late String _apellidos;
  late String _correo;

  //contructor
  Pasajero(this._identificacion, this._nombres, this._apellidos, this._correo);
  
  
  String getIdentificacion(){
    return this._identificacion;
  }
  String getnombres(){
    return this._nombres;
  }


  
}