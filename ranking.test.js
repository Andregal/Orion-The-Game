const Ranking = require("./models/ranking.js");
var ranking = new Ranking();


//Test 1:
test('Mostrar ranking completo', () => {
    ranking.read().then((result) => {
        expect(Array.isArray(result)).toBe(true);
    });
});


//Test 2:
test('Mostrar el usuario segun su puesto', () => {
    ranking.read().then( (result1) => {
        ranking.read(3).then( (result2) => {
            expect(result1[2].username).toBe(result2.username);
        });
    });
});


//Test 3:
test('Mostrar el usuario segun su puesto que no existe', () => {
    ranking.read().then( (result1) => {
        ranking.read(result1.length + 1).then( (result2) => {
            expect(result2).toBe(undefined);
        });
    });
});


//Test 4:
test('Mostrar el puesto segun su usuario', () => {
    ranking.read().then( (result1) => {
        ranking.find("cesar").then(function (result2) {
            for (let i = 0; i < result1.length; i++) {
                if (result1[i].username == "cesar") {
                    expect(result1[i].score).toBe(result2);
                    break;
                } 
            }
        });
    });
});


//Test 5:
test('Mostrar el puesto segun su usuario inexistente', () => {
    ranking.find("0123456789abcdefghijklmnopqrstuvwxyz").then(function (result) {
        expect(result).toBe(undefined);
    });
});