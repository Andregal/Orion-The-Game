//Modulos necesarios
const express = require("express"); //Express: Framework web (Similar a Django)
const users = require("./routes/users.js"); //Acceso a las rutas /usuario
const ranking = require("./routes/ranking.js"); //Acceso a las rutas /ranking

//Configuracion
const app = express();

app.use(express.json());
app.use(express.urlencoded({
    extended: true
}));

//Routes
app.use("/usuario", users);
app.use("/ranking", ranking);

//Documentacion API
app.get("/apidoc", function (req, res) {
    res.sendFile(__dirname + "/apidoc.html");
});

//Puerto del servidor
app.listen(8080);

//Para correr el servidor, ejecutar en la terminal: node index.js
//Tiene que tener instalado Node.js --> https://nodejs.org/en/download/
//Para instalar todos los modulos necesarios, ejecutar el siguientes comandos:
//   npm install

//Para probar que los metodos, se puede usar Postman --> https://www.getpostman.com/apps
//Todos los metodos funcionan correctamente
//Ejemplo: 
// (GET): localhost/ranking/mostrar