import 'dart:io';

class Pasajero {
  String id;
  String nombres;
  String apellidos;
  String email;

  Pasajero(this.id, this.nombres, this.apellidos, this.email);

  String obtenerDatos() {
    return 'ID: $id, Nombre: $nombres $apellidos, Email: $email';
  }
}

class Vuelo {
  String numero;
  DateTime fecha;
  String ciudadOrigen;
  String ciudadDestino;
  List<Pasajero> pasajeros = [];

  Vuelo(this.numero, String fechaStr, this.ciudadOrigen, this.ciudadDestino) {
    try {
      fecha = DateTime.parse(fechaStr);
    } catch (e) {
      throw FormatException("Formato de fecha incorrecto. Use YYYY-MM-DD.");
    }
  }

  void agregarPasajero(Pasajero pasajero) {
    if (pasajeros.any((p) => p.id == pasajero.id)) {
      throw Exception('Pasajero con esta identificación ya existe en este vuelo.');
    }
    pasajeros.add(pasajero);
  }

  List<String> listarPasajeros() {
    return pasajeros.map((p) => p.obtenerDatos()).toList();
  }

  String obtenerDatos() {
    return 'Vuelo $numero, Fecha: ${fecha.toIso8601String().split('T').first}, Origen: $ciudadOrigen, Destino: $ciudadDestino';
  }
}

List<Vuelo> vuelos = [];

void crearVuelo() {
  stdout.write('Ingrese el número de vuelo: ');
  String? numero = stdin.readLineSync()?.trim();
  if (numero == null || numero.isEmpty) {
    print('Error: El número de vuelo no puede estar vacío.');
    return;
  }
  if (vuelos.any((v) => v.numero == numero)) {
    print('Error: El número de vuelo ya existe.');
    return;
  }

  stdout.write('Ingrese la fecha del vuelo (YYYY-MM-DD): ');
  String? fecha = stdin.readLineSync()?.trim();
  if (fecha == null || fecha.isEmpty) {
    print('Error: La fecha no puede estar vacía.');
    return;
  }

  stdout.write('Ingrese la ciudad de origen: ');
  String? ciudadOrigen = stdin.readLineSync()?.trim();
  if (ciudadOrigen == null || ciudadOrigen.isEmpty) {
    print('Error: La ciudad de origen no puede estar vacía.');
    return;
  }

  stdout.write('Ingrese la ciudad de destino: ');
  String? ciudadDestino = stdin.readLineSync()?.trim();
  if (ciudadDestino == null || ciudadDestino.isEmpty) {
    print('Error: La ciudad de destino no puede estar vacía.');
    return;
  }

  try {
    Vuelo vuelo = Vuelo(numero, fecha, ciudadOrigen, ciudadDestino);
    vuelos.add(vuelo);
    print('Vuelo creado exitosamente.');
  } on FormatException catch (e) {
    print('Error: ${e.message}');
  }
}

void listarVuelos() {
  if (vuelos.isEmpty) {
    print('No hay vuelos registrados para el día.');
    return;
  }
  for (var vuelo in vuelos) {
    print(vuelo.obtenerDatos());
  }
}

void agregarPasajeroAVuelo() {
  stdout.write('Ingrese el número del vuelo: ');
  String? numeroVuelo = stdin.readLineSync()?.trim();
  if (numeroVuelo == null || numeroVuelo.isEmpty) {
    print('Error: El número de vuelo no puede estar vacío.');
    return;
  }

  Vuelo? vuelo = vuelos.firstWhere(
    (v) => v.numero == numeroVuelo,
    orElse: () => null,
  );

  if (vuelo == null) {
    print('Error: Vuelo no encontrado.');
    return;
  }

  stdout.write('Ingrese la identificación del pasajero: ');
  String? idPasajero = stdin.readLineSync()?.trim();
  if (idPasajero == null || idPasajero.isEmpty) {
    print('Error: La identificación del pasajero no puede estar vacía.');
    return;
  }

  if (vuelo.pasajeros.any((p) => p.id == idPasajero)) {
    print('Error: Pasajero con esta identificación ya existe en este vuelo.');
    return;
  }

  stdout.write('Ingrese los nombres del pasajero: ');
  String? nombres = stdin.readLineSync()?.trim();
  if (nombres == null || nombres.isEmpty) {
    print('Error: Los nombres del pasajero no pueden estar vacíos.');
    return;
  }

  stdout.write('Ingrese los apellidos del pasajero: ');
  String? apellidos = stdin.readLineSync()?.trim();
  if (apellidos == null || apellidos.isEmpty) {
    print('Error: Los apellidos del pasajero no pueden estar vacíos.');
    return;
  }

  stdout.write('Ingrese el correo electrónico del pasajero: ');
  String? email = stdin.readLineSync()?.trim();
  if (email == null || email.isEmpty) {
    print('Error: El correo electrónico del pasajero no puede estar vacío.');
    return;
  }

  Pasajero pasajero = Pasajero(idPasajero, nombres, apellidos, email);
  try {
    vuelo.agregarPasajero(pasajero);
    print('Pasajero agregado exitosamente.');
  } catch (e) {
    print('Error: ${e.toString()}');
  }
}

void listarPasajerosDeVuelo() {
  stdout.write('Ingrese el número del vuelo: ');
  String? numeroVuelo = stdin.readLineSync()?.trim();
  if (numeroVuelo == null || numeroVuelo.isEmpty) {
    print('Error: El número de vuelo no puede estar vacío.');
    return;
  }

  Vuelo? vuelo = vuelos.firstWhere(
    (v) => v.numero == numeroVuelo,
    orElse: () => null,
  );

  if (vuelo == null) {
    print('Error: Vuelo no encontrado.');
    return;
  }

  if (vuelo.pasajeros.isEmpty) {
    print('No hay pasajeros registrados para este vuelo.');
    return;
  }

  for (var pasajero in vuelo.listarPasajeros()) {
    print(pasajero);
  }
}

void mostrarMenu() {
  while (true) {
    print("\nMenú de opciones");
    print("1. Crear un vuelo");
    print("2. Listar todos los datos de los vuelos del día");
    print("3. Agregar pasajero a un vuelo");
    print("4. Listar todos los datos de los pasajeros de un vuelo");
    print("5. Salir");
    stdout.write("Seleccione una opción: ");
    String? opcion = stdin.readLineSync()?.trim();

    switch (opcion) {
      case '1':
        crearVuelo();
        break;
      case '2':
        listarVuelos();
        break;
      case '3':
        agregarPasajeroAVuelo();
        break;
      case '4':
        listarPasajerosDeVuelo();
        break;
      case '5':
        print("Saliendo del programa.");
        return;
      default:
        print("Opción no válida. Intente de nuevo.");
    }
  }
}

void main() {
  mostrarMenu();
}
