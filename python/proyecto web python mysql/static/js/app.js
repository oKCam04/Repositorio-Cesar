

function mostrarImagen(event){
    const archivos= event.target.files
    const archivo= archivos[0]
    const url=URL.createObjectURL(archivo)
    document.getElementById("imagenProducto").src=url
}

