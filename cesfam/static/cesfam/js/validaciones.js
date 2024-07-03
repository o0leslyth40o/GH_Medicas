function loguear(){
    /**declaracion de variables */
    let name=document.getElementById("nombre").value;
    let lastname=document.getElementById("apellido").value;
    let email=document.getElementById("correo").Value;
    let password=document.getElementById("clave").Value;
    let terminos = document.getElementById('terminos').checked;

    name = "abcdefghyjklmnñopqrstuvwxyz";

    function soloTexto (texto){
       texto = texto.toLowerCase();
       for(let i=0; i<texto.length; i++){
          if (name.indexOf(texto.charAt(i),0)!=-1){
             return 1;
          }
       }
       return 0;
    }

    lastname = "abcdefghyjklmnñopqrstuvwxyz";

    function soloTexto (texto){
   texto = texto.toLowerCase();
   for(let i=0; i<texto.length; i++){
      if (lastname.indexOf(texto.charAt(i),0)!=-1){
         return 1;
      }
   }
   return 0;
}
    email = "js@example.com";

    function validarEmail(email){
    /** Verificamos si el email contiene el símbolo '@' 
     y la @ no está al inicio ni al final*/
    const atIndex = email.indexOf('@');
    if (atIndex <= 0 || atIndex === email.length - 1) {
      return false;
    }
  
    // Dividimos el email usando la '@' como separador
    const [local, domain] = email.split('@');
    
    if (!local || !domain) {
      return false;
    }
  
    // Verificamos que el dominio contenga un punto y no esté al inicio ni al final
    const dotIndex = domain.indexOf('.');
    if (dotIndex <= 0 || dotIndex === domain.length - 1) {
      return false;
    }
  
    // Comprobamos que el dominio no tenga más de un punto consecutivo
    if (domain.includes('..')) {
      return false;
    }
  
    // Comprobamos que el email no contenga caracteres inválidos 
    // Estos caracteres inválidos podrían extenderse si lo ves necesario
    const invalidChars = [' ', '!', '#', '$', '%', '&', '*', '(', ')', '+', ',', '/', ':', ';', '<', '=', '>', '?', '[', '\\', ']', '^', '`', '{', '|', '}', '~'];
    for (let char of invalidChars) {
      if (email.includes(char)) {
        return false;
      }
    }
  
    // Si estamos aquí es que todas las comprobaciones anteriores fueron correctas
    return true;
  }
    



    

}