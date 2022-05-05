class Persona {
    nombre
    apellido
    edad
    genero

    constructor(nombre, apellido, edad, genero){
        this.nombre = nombre;
        this.apellido = apellido;
        this.edad = edad;
        this.genero = genero;
    }

    comer(){

    }

    correr(){
        this.comer()
        this.apellido
    }
}

persona = new Persona("Luis", "Rodriguez", 40, "Masculino");

console.log(persona.apellido);