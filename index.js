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

//Index
app.get("/apidoc", function (req, res) {
    res.send("Orion The Game");
});
//Documentacion API
app.get("/apidoc", function (req, res) {
    res.sendFile(__dirname + "/apidoc.html");
});

//Puerto del servidor
app.listen(5000);