const Sequelize = require('sequelize');

var sequelize = new Sequelize(null, null, null, {
    dialect: "sqlite",
    storage: './oriondb.sqlite',
    operatorsAliases: false,
    logging: false,
    define: {
        freezeTableName: true,
        timestamps: false
    }
});

var usersTable = sequelize.define('users', {
    username: {
        type: Sequelize.TEXT,
        primaryKey: true
    },
    password: Sequelize.TEXT,
    score: Sequelize.INTEGER
});

class Ranking {
    read(place) {
        return sequelize.sync().then(function () {
            return usersTable.findAll({
                attributes: ["username", "score"],
                order: [
                    ["score", "DESC"]
                ],
                limit: 10
            }).then(function (users) {
                if (place == undefined) {
                    return users;
                } else {
                    for (let i = 0; i < users.length; i++) {
                        return users[place - 1];
                    }
                }
            });
        });
    }

    find(username) {
        return this.read().then(function (users) {
            for (let i = 0; i < users.length; i++) {
                if (users[i].username == username) {
                    return {
                        pos: i + 1
                    }
                }
            }
        });
    }
}

module.exports = Ranking;