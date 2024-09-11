
import 'dart:io';

import 'empresa.dart';

late Empresa miEmpresa;

void main(){
  menu();
}
void menu(){
  int opcion =0;
  do{
    print("Menu Empresa");
    print("1. Crear vuelo");
    print("2. Listar datos de vuelo");
    print("3. Agregar pasajeo a vuelo");
    print("4. Listar datos pasajeores vuelo");
    print("5. Salir");
    print("Ingrese opción de 1 a 5:");
    opcion=int.parse(stdin.readLineSync().toString());
    switch (opcion){
      case 1:
      crearVuelo();
      case 2:
      ListarDatosVuelo();
      case 3:
      agregarPasajero();
      case 4:
      ListarDatosvuelos();
      case 5:
      break;
    }

  } while(opcion!=5);
}

void ListarDatosvuelos() {
}

void agregarPasajero() {
}

void ListarDatosVuelo() {
}


void crearVuelo() {
  print("Número de vuelo:");
  int numeroVuelo=int.parse(stdin.readLineSync().toString());
  print("Ciudad Origen: ");
  String eciudadOrigen
}