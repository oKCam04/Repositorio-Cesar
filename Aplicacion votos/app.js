let div=document.querySelector("#div");

//componente de consumo api, mostrando todo los archivos 
fetch("https://raw.githubusercontent.com/cesarmcuellar/Elecciones/refs/heads/main/candidatos.json")
  .then(response => response.json())
  .then(candidato => {
    candidato.forEach(candi => {
        div.innerHTML+=`
        <h3>${candi.curso}</h3>
        <img src="${candi.foto}" alt="" class="mia">
        <h3>Aprendiz=${candi.nombre} ${candi.apellido}</h3>
        <h3>Ficha=${candi.ficha}</h3>
        
        `;
        
    });
 //haciendo el componente de los votos    
    img=document.querySelectorAll('.mia');
    
  });

  


//Login cuando te registras y todo sale bien te deja ingresar al portal para que votes
document.querySelector("#btn").addEventListener("click",()=>{
let user = document.querySelector("#usuario").value;
let contra = document.querySelector("#contrasena").value;
fetch("https://raw.githubusercontent.com/cesarmcuellar/Elecciones/refs/heads/main/administrador.json")
 .then(respuesta=>respuesta.json())
 .then (usuarios=>{
  let admin=usuarios.username;
  let pass=usuarios.password;
  if(user==admin && contra==pass){
    alert("Contraseña correcta")
    window.location.href = "./app.html";
  }else{
    alert("Contraseña incorrecta")
  }
 })
});

//parte de cuando vas a cerrar las votaciones

document.querySelector("#cerrar").addEventListener("click",()=>{

});
