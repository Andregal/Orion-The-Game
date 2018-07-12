const router = require('express').Router();
const Ranking = require("../models/ranking.js");

router.get("/mostrar", function (req, res) {
    var ranking = new Ranking();
    ranking.read().then(function (result) {
        res.send(result)
    });
});

router.get("/mostrar/:puesto", function (req, res) {
    var ranking = new Ranking();
    ranking.read(req.params.puesto).then(function (result) {
        res.send(result)
    })
});

router.get("/posicion/:username", function (req, res) {
    var ranking = new Ranking();
    ranking.find(req.params.username).then(function (result) {
        res.send(result)
    });
});

module.exports = router;