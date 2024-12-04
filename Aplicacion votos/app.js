let votos = [0,0,0,0]; //inicializar votos
let div=document.querySelector("#div"); //mostar la api 
//parte de cuando vas a cerrar las votaciones
let resultados=document.getElementById("resultados");
document.querySelector("#cerrar").addEventListener("click",()=>{
  resultados.innerHTML=`
  <h1>Resultados</h1>
  <table>
    <thead>
      <tr>
        <th>Nombre</th>
        <th>Votos</th>
      </tr>
    </thead>
    <tbody>
    <tr>
      <th>Juan Perez</th>
      <th>${votos[0]}</th>
    </tr>
    <tr>
      <th>Ana Gomez</th>
      <th>${votos[1]}</th>
    </tr>
    <tr>
      <th>Carlos Marinez</th>
      <th>${votos[2]}</th>
    </tr>
    <tr>
      <th>Voto en Blanco</th>
      <th>${votos[3]}</th>
    </tr>
    </tbody>
  </table>

  `;
  votos=[0,0,0,0];
});

//componente de consumo api, mostrando todo los archivos 
fetch("https://raw.githubusercontent.com/cesarmcuellar/Elecciones/refs/heads/main/candidatos.json")
  .then(response => response.json())
  .then(candidato => {
    candidato.forEach((candi,ind) => {
        div.innerHTML+=`
        <h3>${candi.curso}</h3>
        <img src="${candi.foto}" alt="foto de ${candi.nombre}" class="mia" data-nombre="${candi.nombre}" data-id="${ind}">
        <h3>Aprendiz:${candi.nombre} ${candi.apellido}</h3>
        <h3>Ficha:${candi.ficha}</h3>
        
        `;
        
    });
 //haciendo el componente de los votos    
    img=document.querySelectorAll('.mia');
    img.forEach(im => {
        im.addEventListener("click",()=>{
          let nombre = im.getAttribute('data-nombre');
          let ind=im.getAttribute('data-id');

          let confirma= confirm('Desea votar por '+nombre);
          
          if (confirma){
            votos[ind]++;
            alert('Tu voto ha sido un éxito')
          }
          console.log(votos);
        });
    });
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


