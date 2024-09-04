class Vuelo {
  final int numeroVuelo;
  final String fecha;
  final String ciudadOrigen;
  final String ciudadDestino;
  List<Pasajero> listaPasajeros = [];

  Vuelo({
    required this.numeroVuelo,
    required this.fecha,
    required this.ciudadOrigen,
    required this.ciudadDestino,
  });

  void agregarPasajero(Pasajero pasajero) {
    if (!listaPasajeros.any((p) => p.id == pasajero.id)) {
      listaPasajeros.add(pasajero);
    }
  }

  void listarPasajeros() {
    for (var pasajero in listaPasajeros) {
      print('ID: ${pasajero.id}, Nombre: ${pasajero.nombres}');
    }
  }
}

class Pasajero {
  final int id;
  final String nombres;
  final String apellidos;
  final String correo;

  Pasajero({
    required this.id,
    required this.nombres,
    required this.apellidos,
    required this.correo,
  });
}

void main() {
  final vuelo1 = Vuelo(
    numeroVuelo: 101,
    fecha: '2024-09-03',
    ciudadOrigen: 'Bogotá',
    ciudadDestino: 'Medellín',
  );

  final pasajero1 = Pasajero(
    id: 1,
    nombres: 'santiago',
    apellidos: 'mera',
    correo: 'santiagomera051@gmail.com',
  );

  vuelo1.agregarPasajero(pasajero1);
  vuelo1.listarPasajeros();
}