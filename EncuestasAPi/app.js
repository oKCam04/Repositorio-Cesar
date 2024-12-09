let multiple=document.getElementById("multiple");
let trufol=document.getElementById("truFal");

//preguntas consumidas api
fetch("https://raw.githubusercontent.com/cesarmcuellar/CuestionarioWeb/refs/heads/main/cuestionario.json")
.then(response=>response.json())
.then(preguntas=>{
    console.log(preguntas);
    //preguntas opcion multiple
    preguntas.multiple_choice_questions.forEach((pgt,index)=>{
        multiple.innerHTML+= `<h2>${pgt.question}</h2>`;
        pgt.options.forEach((opt)=>{    
            multiple.innerHTML+= `
            <label>
            <input type="radio" name="multiple${index}" value="${opt}">
            ${opt}
            </label><br/>
            `;
        });
    });
    //preguntas verdadero o falso
    preguntas.true_false_questions.forEach((tf,index)=>{
        trufol.innerHTML+= `
        <h2>${tf.question}</h2>
        <label>
        <label>
            <input type="radio" name="true_false_${index}" value="true">
                Verdadero
        </label><br>
        <label>
            <input type="radio" name="true_false_${index}" value="false">
            Falso
        </label><br>
        `;
    });
})

//boton reinicar
document.getElementById("reiniciar").addEventListener("click", ()=>{
    let input=document.querySelectorAll('input[type="radio"]');
    input.forEach(i=>{
        i.checked=false;
    });
});

//boton calificar
document.getElementById('enviar').addEventListener("click", ()=>{
    fetch("https://raw.githubusercontent.com/cesarmcuellar/CuestionarioWeb/refs/heads/main/cuestionario.json")
         .then(response => response.json())
         .then(respuesta => {
            let Rbien = 0;

            //opciones 
             respuesta.multiple_choice_questions.forEach((pgt, index) => {
                 let respuestas = document.querySelector(`input[name="multiple${index}"]:checked`);
                 if (respuestas && respuestas.value === pgt.correct_answer) {
                     Rbien += 1;
                 }
             });
             let pgtTotal = respuesta.multiple_choice_questions.length 
             let rta = (Rbien * 100) / pgtTotal;
             alert(`Tu resultado es: ${rta.toFixed(2)}%`);
});//fetch
});
