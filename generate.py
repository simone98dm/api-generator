import sys
import getopt
import os
import base64
from abc import ABCMeta, abstractmethod

placeholder = "REPLACEME"

class TS:
    name = ""
    template_app = '''import express from "express";
import cors from "cors";
import bodyParser from "body-parser";
import morgan from "morgan";
//imports
import { port, prefix } from "./src/configs/api.config";

const server = express();
server.use(cors());
server.use(bodyParser.json());
server.use(morgan("dev"));
//middlewares

server.listen(port, () =>
console.log("API-ENDPOINT are running (:" + port + ")")
);
'''
    tsconfig = '''{
  "compilerOptions": {
    "target": "es5",
    "module": "commonjs",
    "declaration": false,
    "outDir": "./dist",
    "strict": true,
    "moduleResolution": "node",
    "allowSyntheticDefaultImports": true,
    "esModuleInterop": true,
    "experimentalDecorators": true,
    "emitDecoratorMetadata": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  },
  "include": [
    "src/**/*"
  ],
  "exclude": [
    "node_modules",
    "**/*.spec.ts"
  ]
}
'''
    template_route = '''import express from "express";
import { prefix } from "../configs/REPLACEME.config";
const router = express.Router();

router.get(prefix, async (req, res) => {
  return res.status(200).json().end();
});

router.get(prefix + "/:id", async (req, res) => {
  if (!req.params.id) {
    return res.status(404).end();
  }
  return res.status(200).json().end();
});

router.post(prefix, async (req, res) => {
  if (!req.body) {
    return res.status(404).end();
  }
  return res.status(200).json().end();
});

router.put(prefix, async (req, res) => {});

router.delete(prefix, async (req, res) => {});

export { router };
'''
    template_controller = '''async function getREPLACEMEs(): any[] {
  return new Promise<any>();
}
async function getREPLACEME(id: string): any {
  return new Promise<any>();
}
async function deleteREPLACEME(id: string): boolean {
  return new Promise<boolean>();
}
async function updateREPLACEME(obj: any): boolean {
  return new Promise<boolean>();
}
async function createREPLACEME(obj: any): string {
  return new Promise<boolean>();
}

export {
  getREPLACEME,
  getREPLACEMEs,
  deleteREPLACEME,
  updateREPLACEME,
  createREPLACEME,
};
'''
    template_config ='''const prefix = "/REPLACEME";
export { prefix };
'''
    package_json = '''{
  "dependencies": {
    "body-parser": "^1.19.0",
    "cors": "^2.8.5",
    "dotenv": "^8.2.0",
    "express": "^4.17.1",
    "morgan": "^1.10.0",
    "pg": "^8.5.1"
  },
  "devDependencies": {
    "@types/body-parser": "^1.19.0",
    "@types/cors": "^2.8.10",
    "@types/dotenv": "^8.2.0",
    "@types/express": "^4.17.11",
    "@types/morgan": "^1.9.2",
    "@types/pg": "^7.14.11"
  },
  "name": "ts",
  "version": "1.0.0",
  "main": "dist/app.js",
  "scripts": {
    "build": "tsc --build",
    "start": "ts-node app.ts"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "description": ""
}
'''
    appconfig = '''const prefix = "/api";
const port = 3000;
export { prefix, port };'''

    def __init__(self, name):
        self.name = name

    def get_route(self):
        return (self.template_route).replace(placeholder, self.name).replace(placeholder, self.name.capitalize())

    def get_controller(self):
        return (self.template_controller).replace(placeholder, self.name).replace(placeholder, self.name.capitalize())

    def get_config(self):
        return (self.template_config).replace(placeholder, self.name).replace(placeholder, self.name.capitalize())

    def get_app(self):
        return (self.template_app).replace(placeholder, self.name).replace(placeholder, self.name.capitalize())

    def get_package(self):
        return (self.package_json).replace(placeholder, self.name)

    def get_tsconfig(self):
        return (self.tsconfig).replace(placeholder, self.name)

    def get_app_config(self):
        return (self.appconfig).replace(placeholder, self.name.capitalize())


class JS:
    name = ""

    template_app = '''const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const morgan = require('morgan');
const config = require('./src/configs/api.config');
//imports

const server = express();
server.use(cors());
server.use(bodyParser.json());
server.use(morgan('dev'));
//middlewares

server.listen(config.port, () =>
  console.log('API-ENDPOINT are running (:' + config.port + ')')
);
'''
    template_route = '''const express = require("express");
const config = require("../configs/REPLACEME.config");
const router = express.Router();

router.get(config.prefix, async (req, res) => {
  return res.status(200).json().end();
});

router.get(config.prefix + "/:id", async (req, res) => {
  if (!req.params.id) {
    return res.status(404).end();
  }
  return res.status(200).json().end();
});

router.post(config.prefix, async (req, res) => {
  if (!req.body) {
    return res.status(404).end();
  }
  return res.status(200).json().end();
});

router.put(config.prefix, async (req, res) => {});

router.delete(config.prefix, async (req, res) => {});

module.exports = router;
'''
    template_controller = '''async function getREPLACEMEs() {
}
async function getREPLACEME(id) {
}
async function deleteREPLACEME(id) {
}
async function updateREPLACEME(obj) {
}
async function createREPLACEME(obj) {
}

module.exports = {
    getREPLACEMEs,
    getREPLACEME,
    deleteREPLACEME,
    updateREPLACEME,
    createREPLACEME
}
'''
    template_config = '''const prefix = "/REPLACEME";
module.exports = { prefix };
'''
    package_json = '''{
  "name": "js",
  "version": "1.0.0",
  "main": "app.js",
  "scripts": {
    "start": "node app.js"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "description": "",
  "dependencies": {
    "body-parser": "^1.19.0",
    "cors": "^2.8.5",
    "express": "^4.17.1",
    "morgan": "^1.10.0"
  }
}
'''
    appconfig = '''const prefix = "/api";
const port = 3000;
module.exports = { prefix, port };
'''

    def __init__(self, name):
        self.name = name

    def get_route(self):
        return (self.template_route).replace(placeholder, self.name).replace(placeholder, self.name.capitalize())

    def get_controller(self):
        return (self.template_controller).replace(placeholder, self.name).replace(placeholder, self.name.capitalize())

    def get_config(self):
        return (self.template_config).replace(placeholder, self.name).replace(placeholder, self.name.capitalize())

    def get_app(self):
        return (self.template_app).replace(placeholder, self.name).replace(placeholder, self.name.capitalize())

    def get_package(self):
        return (self.package_json).replace(placeholder, self.name)

    def get_app_config(self):
        return (self.appconfig).replace(placeholder, self.name.capitalize())


def prepare_env(p):
    if not os.path.exists(p):
        os.makedirs(p)


def save_file(path, content):
    text_file = open(path, "w")
    text_file.write(content)
    text_file.close()


def generate(name, type, path):
    pathcontroller = "{}/src/controllers".format(path)
    pathconfig = "{}/src/configs".format(path)
    pathroute = "{}/src/routes".format(path)
    pathdriver = "{}/src/drivers".format(path)
    pathmodels = "{}/src/models".format(path)

    prepare_env(path)
    prepare_env(pathcontroller)
    prepare_env(pathconfig)
    prepare_env(pathroute)
    prepare_env(pathdriver)
    prepare_env(pathmodels)

    if type == "ts":
        ts = TS(name)
        ctr = ts.get_controller()
        cfg = ts.get_config()
        rt = ts.get_route()
        appconfig = ts.get_app_config()
        tsconfig = ts.get_tsconfig()
        packagejson = ts.get_package()

        if os.path.isfile("{}/app.ts".format(path)):
            app = open("{}/app.ts".format(path), "r").read()
        else:
            app = ts.get_app()

        imports = "//imports\nimport * as {}Routes from './routes/{}.route';".format(name, name)
        middlewares = "//middlewares\nserver.use(prefix, {}Routes.router);".format(name)

        app = app.replace("//imports", imports).replace("//middlewares", middlewares)
        save_file("{}{}".format(path, "/app.ts"), app)
        save_file("{}{}".format(path, "/package.json"), packagejson)
        save_file("{}{}".format(path, "/tsconfig.json"), tsconfig)
        save_file("{}{}".format(pathconfig, "/{}".format("app.config.ts")), appconfig)
        save_file("{}{}".format(pathcontroller, "/{}{}".format(name, ".controller.ts")), ctr)
        save_file("{}{}".format(pathconfig, "/{}{}".format(name, ".config.ts")), cfg)
        save_file("{}{}".format(pathroute, "/{}{}".format(name, ".route.ts")), rt)
    elif type == "js":
        js = JS(name)
        ctr = js.get_controller()
        cfg = js.get_config()
        rt = js.get_route()
        appconfig = js.get_app_config()
        packagejson = js.get_package()

        if os.path.isfile("{}/app.js".format(path)):
            app = open("{}/app.js".format(path), "r").read()
        else:
            app = js.get_app()

        imports = "//imports\nconst {}Routes = required('./src/routes/{}.route');".format(name, name)
        middlewares = "//middlewares\nserver.use(config.prefix, {}Routes.router);".format(name)

        app = app.replace("//imports",imports).replace("//middlewares", middlewares)
        save_file("{}{}".format(path, "/app.js"), app)
        save_file("{}{}".format(path, "/package.json"), packagejson)
        save_file("{}{}".format(pathconfig, "/{}".format("app.config.js")), appconfig)
        save_file("{}{}".format(pathcontroller, "/{}{}".format(name, ".controller.js")), ctr)
        save_file("{}{}".format(pathconfig, "/{}{}".format(name, ".config.js")), cfg)
        save_file("{}{}".format(pathroute, "/{}{}".format(name, ".route.js")), rt)
    else:
        return
    
    print("[!] Completed...")


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hn:t:p:", ["name=", "type=", "path="])
    except getopt.GetoptError:
        print("apigenerator.py -n <api name> -t <code type> -p <path>")
        sys.exit(2)

    name = ""
    code_type = ""
    path = "."

    for opt, arg in opts:
        if opt == "-h":
            print("test.py -n <api name> --type [ts,js] --path")
            sys.exit()
        elif opt in ("-n", "--name"):
            name = arg
        elif opt in ("-t", "--type"):
            code_type = arg
        elif opt in ("-p", "--path"):
            path = arg

    if name == "":
        print("name is empty")
        return
    if code_type == "":
        print("name is empty")
        return

    generate(name, code_type, path)


if __name__ == "__main__":
    main(sys.argv[1:])
