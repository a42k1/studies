//Crie uma lista de chamada com os estudantes.
// -João, Ana, Caio, Lara, Marjorie, Leo
// Porem Ana e Caio mudaram de escola e o Rodrigo entrou na sala, atualize a lista
const sala = ["João", "Ana", "Caio", "Lara", "Marjorie", "Leo"];
const removido = sala.splice(1, 2, "Rodrigo");

console.log(removido);
console.log(sala);
