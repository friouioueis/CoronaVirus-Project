//import Jasmine from 'jasmine'
var Jasmine = require("C:/Users/HP/AppData/Roaming/npm/node_modules/jasmine/lib/jasmine");

let jasmine = new Jasmine();
jasmine.loadConfigFile('./support/jasmine.json')
jasmine.execute();