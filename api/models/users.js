const Sequelize = require('sequelize');

var sequelize = new Sequelize(null, null, null, {
    dialect: "sqlite",
    storage: '../db.sqlite',
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

class Users {
    create(user) {
        sequelize.sync().then(function () {
            usersTable.create({
                username: user.username,
                password: user.password
            });
        })
    }

    read(username, attributes) {
        return sequelize.sync().then(function () {
            if (attributes != undefined) {
                return usersTable.findOne({
                    where: {
                        username: username
                    },
                    attributes: attributes
                }).then(function (user) {
                    return user;
                });
            } else {
                return usersTable.findOne({
                    where: {
                        username: username
                    }
                }).then(function (user) {
                    return user;
                });
            }
        });
    }

    update(username, data) {
        sequelize.sync().then(function () {
            usersTable.update(data, {
                where: {
                    username: username
                }
            });
        });
    }

    delete(username) {
        sequelize.sync().then(function () {
            usersTable.destroy({
                where: {
                    username: username
                }
            });
        });
    }
}

module.exports = Users;