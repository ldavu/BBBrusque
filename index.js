function Validar_usuario(nome){
    while(nome != "davi"){
        
        nome = prompt("digite o nome") //prompt que vai aparecer para digitar o nome
        
        if(nome == "davi"){ // validar no console o nome para saber o que foi digitado
            console.log("Nome Correto!")
        }
        else{
            console.log("Nome Digitado:", nome)
        }
    }
}

Validar_usuario()