import sys
import getopt
import os
import base64
from abc import ABCMeta, abstractmethod

placeholder = "REPLACEME"

class TS:
    name = ""
    template_app = open("./templates/ts/app.ts", "r").read()
    tsconfig = open("./templates/ts/tsconfig.json", "r").read()
    template_route = open("./templates/ts/src/routes/template.route.ts", "r").read()
    template_controller = open("./templates/ts/src/controllers/template.controller.ts", "r").read()
    template_config = open("./templates/ts/src/configs/template.config.ts", "r").read()
    package_json = open("./templates/ts/package.json", "r").read()
    appconfig = open("./templates/ts/src/configs/api.config.ts", "r").read()

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

    template_app = open("./templates/js/app.js", "r").read()
    template_route = open("./templates/js/src/routes/template.route.js", "r").read()
    template_controller = open("./templates/js/src/controllers/template.controller.js", "r").read()
    template_config = open("./templates/js/src/configs/template.config.js", "r").read()
    package_json = open("./templates/js/package.json", "r").read()
    appconfig = open("./templates/js/src/configs/api.config.js", "r").read()

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

        imports = "//project-imports\nimport * as {}Routes from './routes/{}.route';".format(name, name)
        middlewares = "//defile-routes\nserver.use(prefix, {}Routes.router);".format(name)

        app = app.replace("//project-imports", imports).replace("//defile-routes", middlewares)
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

        imports = "//project-imports\nconst {}Routes = required('./src/routes/{}.route');".format(name, name)
        middlewares = "//defile-routes\nserver.use(config.prefix, {}Routes.router);".format(name)

        app = app.replace("//project-imports",imports).replace("//defile-routes", middlewares)
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
