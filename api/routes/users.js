const router = require('express').Router();
const Users = require("../models/users.js");

router.get("/validarExistencia/:username", function (req, res) {
    var users = new Users();
    users.read(req.params.username).then(function (result) {
        if (result != undefined) {
            res.send({
                result: true
            })
        } else {
            res.send({
                result: false
            })
        }
    });

});

router.post("/crear", function (req, res) {
    var user = req.body;
    var users = new Users();
    users.create({
        username: user.username,
        password: user.username
    });

    res.sendStatus(200);
})

router.post("/validarContrasena", function (req, res) {
    var user = req.body;

    var users = new Users();
    users.read(user.username, ["password"]).then(function (result) {
        if (user.password == result.password) {
            res.send({
                result: true
            })
        } else {
            res.send({
                result: false
            })
        }
    });
});

router.put("/actualizarContrasena", function (req, res) {
    var user = req.body;

    var users = new Users();
    users.update(user.username, {
        password: user.password
    });

    res.sendStatus(200);
})

router.get("/obtenerScore/:username", function (req, res) {
    var users = new Users();
    users.read(req.params.username, ["score"]).then(function (result) {
        res.send(result)
    });
});

router.put("/actualizarScore", function (req, res) {
    var user = req.body;

    var users = new Users();
    users.update(user.username, {
        score: user.score
    });

    res.sendStatus(200);
});

module.exports = router;