import sys
import getopt
import os
import base64
from abc import ABCMeta, abstractmethod

placeholder = "REPLACEME"
placeholder2 = "CONTROLLERNAME"

class TS:
    name = ""

    templateApp = "aW1wb3J0IGV4cHJlc3MgZnJvbSAiZXhwcmVzcyI7CmltcG9ydCBjb3JzIGZyb20gImNvcnMiOwpp" \
                  "bXBvcnQgYm9keVBhcnNlciBmcm9tICJib2R5LXBhcnNlciI7CmltcG9ydCBtb3JnYW4gZnJvbSAi" \
                  "bW9yZ2FuIjsKLy9wcm9qZWN0LWltcG9ydHMKaW1wb3J0ICogYXMgUkVQTEFDRU1FUm91dGVzIGZy" \
                  "b20gIi4vcm91dGVzL1JFUExBQ0VNRS5yb3V0ZSI7CmltcG9ydCB7IHBvcnQsIHByZWZpeCB9IGZy" \
                  "b20gIi4vY29uZmlncy9hcGkuY29uZmlnIjsKCmNvbnN0IHNlcnZlciA9IGV4cHJlc3MoKTsKc2Vy" \
                  "dmVyLnVzZShjb3JzKCkpOwpzZXJ2ZXIudXNlKGJvZHlQYXJzZXIuanNvbigpKTsKc2VydmVyLnVz" \
                  "ZShtb3JnYW4oImRldiIpKTsKLy9kZWZpbGUtcm91dGVzCnNlcnZlci51c2UocHJlZml4LCBSRVBM" \
                  "QUNFTUVSb3V0ZXMucm91dGVyKTsKCnNlcnZlci5saXN0ZW4ocG9ydCwgKCkgPT4KICBjb25zb2xl" \
                  "LmxvZygiQVBJLUVORFBPSU5UIGFyZSBydW5uaW5nICg6IiArIHBvcnQgKyAiKSIpCik7Cg=="
    tsconfig = "ewogICJjb21waWxlck9wdGlvbnMiOiB7CiAgICAidGFyZ2V0IjogImVzNSIsCiAgICAibW9kdWxl" \
               "IjogImNvbW1vbmpzIiwKICAgICJkZWNsYXJhdGlvbiI6IGZhbHNlLAogICAgIm91dERpciI6ICIu" \
               "L2Rpc3QiLAogICAgInN0cmljdCI6IHRydWUsCiAgICAibW9kdWxlUmVzb2x1dGlvbiI6ICJub2Rl" \
               "IiwKICAgICJhbGxvd1N5bnRoZXRpY0RlZmF1bHRJbXBvcnRzIjogdHJ1ZSwKICAgICJlc01vZHVs" \
               "ZUludGVyb3AiOiB0cnVlLAogICAgImV4cGVyaW1lbnRhbERlY29yYXRvcnMiOiB0cnVlLAogICAg" \
               "ImVtaXREZWNvcmF0b3JNZXRhZGF0YSI6IHRydWUsCiAgICAic2tpcExpYkNoZWNrIjogdHJ1ZSwK" \
               "ICAgICJmb3JjZUNvbnNpc3RlbnRDYXNpbmdJbkZpbGVOYW1lcyI6IHRydWUKICB9LAogICJpbmNs" \
               "dWRlIjogWwogICAgInNyYy8qKi8qIgogIF0sCiAgImV4Y2x1ZGUiOiBbCiAgICAibm9kZV9tb2R1" \
               "bGVzIiwKICAgICIqKi8qLnNwZWMudHMiCiAgXQp9"
    templateRoute = "aW1wb3J0IGV4cHJlc3MgZnJvbSAiZXhwcmVzcyI7CmltcG9ydCB7IHByZWZpeCB9IGZyb20gIi4u" \
                    "L2NvbmZpZ3MvUkVQTEFDRU1FLmNvbmZpZyI7CmNvbnN0IHJvdXRlciA9IGV4cHJlc3MuUm91dGVy" \
                    "KCk7CnJvdXRlci5nZXQocHJlZml4LCBhc3luYyAocmVxLCByZXMpID0+IHsKICByZXR1cm4gcmVz" \
                    "LnN0YXR1cygyMDApLmpzb24oKS5lbmQoKTsKfSk7CnJvdXRlci5nZXQocHJlZml4ICsgIi86aWQi" \
                    "LCBhc3luYyAocmVxLCByZXMpID0+IHsKICBpZiAoIXJlcS5wYXJhbXMuaWQpIHsKICAgIHJldHVy" \
                    "biByZXMuc3RhdHVzKDQwNCkuZW5kKCk7CiAgfQogIHJldHVybiByZXMuc3RhdHVzKDIwMCkuanNv" \
                    "bigpLmVuZCgpOwp9KTsKcm91dGVyLnBvc3QocHJlZml4LCBhc3luYyAocmVxLCByZXMpID0+IHsK" \
                    "ICBpZiAoIXJlcS5ib2R5KSB7CiAgICByZXR1cm4gcmVzLnN0YXR1cyg0MDQpLmVuZCgpOwogIH0K" \
                    "ICByZXR1cm4gcmVzLnN0YXR1cygyMDApLmpzb24oKS5lbmQoKTsKfSk7CnJvdXRlci5wdXQocHJl" \
                    "Zml4LCBhc3luYyAocmVxLCByZXMpID0+IHt9KTsKcm91dGVyLmRlbGV0ZShwcmVmaXgsIGFzeW5j" \
                    "IChyZXEsIHJlcykgPT4ge30pOwpleHBvcnQgeyByb3V0ZXIgfTsK"
    templateController = "YXN5bmMgZnVuY3Rpb24gZ2V0UkVQTEFDRU1FcygpOiBhbnlbXSB7CiAgcmV0dXJuIG5ldyBQcm9t" \
                         "aXNlPGFueT4oKTsKfQphc3luYyBmdW5jdGlvbiBnZXRSRVBMQUNFTUUoaWQ6IHN0cmluZyk6IGFu" \
                         "eSB7CiAgcmV0dXJuIG5ldyBQcm9taXNlPGFueT4oKTsKfQphc3luYyBmdW5jdGlvbiBkZWxldGVS" \
                         "RVBMQUNFTUUoaWQ6IHN0cmluZyk6IGJvb2xlYW4gewogIHJldHVybiBuZXcgUHJvbWlzZTxib29s" \
                         "ZWFuPigpOwp9CmFzeW5jIGZ1bmN0aW9uIHVwZGF0ZVJFUExBQ0VNRShvYmo6IGFueSk6IGJvb2xl" \
                         "YW4gewogIHJldHVybiBuZXcgUHJvbWlzZTxib29sZWFuPigpOwp9CmFzeW5jIGZ1bmN0aW9uIGNy" \
                         "ZWF0ZVJFUExBQ0VNRShvYmo6IGFueSk6IHN0cmluZyB7CiAgcmV0dXJuIG5ldyBQcm9taXNlPGJv" \
                         "b2xlYW4+KCk7Cn0KCmV4cG9ydCB7CiAgZ2V0UkVQTEFDRU1FLAogIGdldFJFUExBQ0VNRXMsCiAg" \
                         "ZGVsZXRlUkVQTEFDRU1FLAogIHVwZGF0ZVJFUExBQ0VNRSwKICBjcmVhdGVSRVBMQUNFTUUsCn07" \
                         "Cg=="
    templateConfig = "Y29uc3QgcHJlZml4ID0gIi9SRVBMQUNFTUUiOwpleHBvcnQgeyBwcmVmaXggfTsK"
    packageJSON = "ewogICJkZXBlbmRlbmNpZXMiOiB7CiAgICAiYm9keS1wYXJzZXIiOiAiXjEuMTkuMCIsCiAgICAi" \
                  "Y29ycyI6ICJeMi44LjUiLAogICAgImRvdGVudiI6ICJeOC4yLjAiLAogICAgImV4cHJlc3MiOiAi" \
                  "XjQuMTcuMSIsCiAgICAibW9yZ2FuIjogIl4xLjEwLjAiLAogICAgInBnIjogIl44LjUuMSIKICB9" \
                  "LAogICJkZXZEZXBlbmRlbmNpZXMiOiB7CiAgICAiQHR5cGVzL2JvZHktcGFyc2VyIjogIl4xLjE5" \
                  "LjAiLAogICAgIkB0eXBlcy9jb3JzIjogIl4yLjguMTAiLAogICAgIkB0eXBlcy9kb3RlbnYiOiAi" \
                  "XjguMi4wIiwKICAgICJAdHlwZXMvZXhwcmVzcyI6ICJeNC4xNy4xMSIsCiAgICAiQHR5cGVzL21v" \
                  "cmdhbiI6ICJeMS45LjIiLAogICAgIkB0eXBlcy9wZyI6ICJeNy4xNC4xMSIKICB9LAogICJuYW1l" \
                  "IjogInRzIiwKICAidmVyc2lvbiI6ICIxLjAuMCIsCiAgIm1haW4iOiAiZGlzdC9hcHAuanMiLAog" \
                  "ICJzY3JpcHRzIjogewogICAgImJ1aWxkIjogInRzYyIsCiAgICAic3RhcnQiOiAidHMtbm9kZSBh" \
                  "cHAudHMiCiAgfSwKICAia2V5d29yZHMiOiBbXSwKICAiYXV0aG9yIjogIiIsCiAgImxpY2Vuc2Ui" \
                  "OiAiSVNDIiwKICAiZGVzY3JpcHRpb24iOiAiIgp9Cg=="
    appconfig = "Y29uc3QgcHJlZml4ID0gIi9hcGkiOwpjb25zdCBwb3J0ID0gMzAwOwpleHBvcnQgeyBwcmVmaXgs" \
                "IHBvcnQgfTsK"

    def __init__(self, name):
        self.name = name

    def getRoute(self):
        return self.decode(self.templateRoute).replace(placeholder, self.name).replace(placeholder2, self.name.capitalize())

    def getController(self):
        return self.decode(self.templateController).replace(placeholder, self.name).replace(placeholder2, self.name.capitalize())

    def getConfig(self):
        return self.decode(self.templateConfig).replace(placeholder, self.name).replace(placeholder2, self.name.capitalize())

    def getApp(self):
        return self.decode(self.templateApp).replace(placeholder, self.name).replace(placeholder2, self.name.capitalize())

    def getPackage(self):
        return self.decode(self.packageJSON).replace(placeholder, self.name)

    def getTsconfig(self):
        return self.decode(self.tsconfig).replace(placeholder, self.name)

    def getAppConfig(self):
        return self.decode(self.appconfig).replace(placeholder2, self.name.capitalize())

    def decode(self, c):
        base64_bytes = c.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        return message_bytes.decode('ascii')


class JS:
    name = ""

    templateRoute = "Y29uc3QgZXhwcmVzcyA9IHJlcXVpcmUoImV4cHJlc3MiKTsKY29uc3QgY29uZmlnID0gcmVxdWly" \
                    "ZSgiLi4vY29uZmlncy9SRVBMQUNFTUUuY29uZmlnIik7CmNvbnN0IHJvdXRlciA9IGV4cHJlc3Mu" \
                    "Um91dGVyKCk7CnJvdXRlci5nZXQoY29uZmlnLnByZWZpeCwgYXN5bmMgKHJlcSwgcmVzKSA9PiB7" \
                    "CiAgcmV0dXJuIHJlcy5zdGF0dXMoMjAwKS5qc29uKCkuZW5kKCk7Cn0pOwpyb3V0ZXIuZ2V0KGNv" \
                    "bmZpZy5wcmVmaXggKyAiLzppZCIsIGFzeW5jIChyZXEsIHJlcykgPT4gewogIGlmICghcmVxLnBh" \
                    "cmFtcy5pZCkgewogICAgcmV0dXJuIHJlcy5zdGF0dXMoNDA0KS5lbmQoKTsKICB9CiAgcmV0dXJu" \
                    "IHJlcy5zdGF0dXMoMjAwKS5qc29uKCkuZW5kKCk7Cn0pOwpyb3V0ZXIucG9zdChjb25maWcucHJl" \
                    "Zml4LCBhc3luYyAocmVxLCByZXMpID0+IHsKICBpZiAoIXJlcS5ib2R5KSB7CiAgICByZXR1cm4g" \
                    "cmVzLnN0YXR1cyg0MDQpLmVuZCgpOwogIH0KICByZXR1cm4gcmVzLnN0YXR1cygyMDApLmpzb24o" \
                    "KS5lbmQoKTsKfSk7CnJvdXRlci5wdXQoY29uZmlnLnByZWZpeCwgYXN5bmMgKHJlcSwgcmVzKSA9" \
                    "PiB7fSk7CnJvdXRlci5kZWxldGUoY29uZmlnLnByZWZpeCwgYXN5bmMgKHJlcSwgcmVzKSA9PiB7" \
                    "fSk7Cm1vZHVsZS5leHBvcnRzID0gcm91dGVyOwo="
    templateController = "YXN5bmMgZnVuY3Rpb24gZ2V0Q09OVFJPTExFUk5BTUVzKCkgewp9CmFzeW5jIGZ1bmN0aW9uIGdl" \
                         "dENPTlRST0xMRVJOQU1FKGlkKSB7Cn0KYXN5bmMgZnVuY3Rpb24gZGVsZXRlQ09OVFJPTExFUk5B" \
                         "TUUoaWQpIHsKfQphc3luYyBmdW5jdGlvbiB1cGRhdGVDT05UUk9MTEVSTkFNRShvYmopIHsKfQph" \
                         "c3luYyBmdW5jdGlvbiBjcmVhdGVDT05UUk9MTEVSTkFNRShvYmopIHsKfQoKbW9kdWxlLmV4cG9y" \
                         "dHMgPSB7CiAgICBnZXRDT05UUk9MTEVSTkFNRXMsCiAgICBnZXRDT05UUk9MTEVSTkFNRSwKICAg" \
                         "IGRlbGV0ZUNPTlRST0xMRVJOQU1FLAogICAgdXBkYXRlQ09OVFJPTExFUk5BTUUsCiAgICBjcmVh" \
                         "dGVDT05UUk9MTEVSTkFNRQp9"
    templateConfig = "Y29uc3QgcHJlZml4ID0gIi9SRVBMQUNFTUUiOwptb2R1bGUuZXhwb3J0cyA9IHsgcHJlZml4IH07" \
                     "Cg=="
    templateApp = "Y29uc3QgZXhwcmVzcyA9IHJlcXVpcmUoJ2V4cHJlc3MnKTsKY29uc3QgY29ycyA9IHJlcXVpcmUo" \
                  "J2NvcnMnKTsKY29uc3QgYm9keVBhcnNlciA9IHJlcXVpcmUoJ2JvZHktcGFyc2VyJyk7CmNvbnN0" \
                  "IG1vcmdhbiA9IHJlcXVpcmUoJ21vcmdhbicpOwpjb25zdCBjb25maWcgPSByZXF1aXJlKCcuL2Nv" \
                  "bmZpZ3MvYXBwLmNvbmZpZycpOwovL3Byb2plY3QtaW1wb3J0cwpjb25zdCBSRVBMQUNFTUVSb3V0" \
                  "ZSA9IHJlcXVpcmUoIi4vcm91dGVzL1JFUExBQ0VNRS5yb3V0ZS5qcyIpOwoKY29uc3Qgc2VydmVy" \
                  "ID0gZXhwcmVzcygpOwpzZXJ2ZXIudXNlKGNvcnMoKSk7CnNlcnZlci51c2UoYm9keVBhcnNlci5q" \
                  "c29uKCkpOwpzZXJ2ZXIudXNlKG1vcmdhbignZGV2JykpOwovL2RlZmlsZS1yb3V0ZXMKc2VydmVy" \
                  "LnVzZShjb25maWcucHJlZml4LCBSRVBMQUNFTUVSb3V0ZSkKCnNlcnZlci5saXN0ZW4oY29uZmln" \
                  "LnBvcnQsICgpID0+CiAgY29uc29sZS5sb2coJ0FQSS1FTkRQT0lOVCBhcmUgcnVubmluZyAoOicg" \
                  "KyBjb25maWcucG9ydCArICcpJykKKTsK"
    packageJson = "ewogICJuYW1lIjogImpzIiwKICAidmVyc2lvbiI6ICIxLjAuMCIsCiAgIm1haW4iOiAiYXBwLmpz" \
                  "IiwKICAic2NyaXB0cyI6IHsKICAgICJzdGFydCI6ICJub2RlIGFwcC5qcyIKICB9LAogICJrZXl3" \
                  "b3JkcyI6IFtdLAogICJhdXRob3IiOiAiIiwKICAibGljZW5zZSI6ICJJU0MiLAogICJkZXNjcmlw" \
                  "dGlvbiI6ICIiLAogICJkZXBlbmRlbmNpZXMiOiB7CiAgICAiYm9keS1wYXJzZXIiOiAiXjEuMTku" \
                  "MCIsCiAgICAiY29ycyI6ICJeMi44LjUiLAogICAgImV4cHJlc3MiOiAiXjQuMTcuMSIsCiAgICAi" \
                  "bW9yZ2FuIjogIl4xLjEwLjAiCiAgfQp9Cg=="
    appconfig = "Y29uc3QgcHJlZml4ID0gIi9hcGkiOwpjb25zdCBwb3J0ID0gMzAwMDsKbW9kdWxlLmV4cG9ydHMg" \
                "PSB7IHByZWZpeCwgcG9ydCB9Owo="

    def __init__(self, name):
        self.name = name

    def getRoute(self):
        return self.decode(self.templateRoute).replace(placeholder, self.name).replace(placeholder2, self.name.capitalize())

    def getController(self):
        return self.decode(self.templateController).replace(placeholder, self.name).replace(placeholder2, self.name.capitalize())

    def getConfig(self):
        return self.decode(self.templateConfig).replace(placeholder, self.name).replace(placeholder2, self.name.capitalize())

    def getApp(self):
        return self.decode(self.templateApp).replace(placeholder, self.name).replace(placeholder2, self.name.capitalize())

    def getPackage(self):
        return self.decode(self.packageJson).replace(placeholder, self.name)

    def getAppConfig(self):
        return self.decode(self.appconfig).replace(placeholder2, self.name.capitalize())

    def decode(self, c):
        base64_bytes = c.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        return message_bytes.decode('ascii')


def prepareEnv(p):
    if not os.path.exists(p):
        os.makedirs(p)


def saveFile(path, content):
    text_file = open(path, "w")
    text_file.write(content)
    text_file.close()


def generate(name, type):
    basePath = "./src"

    pathController = '{}/controllers'.format(basePath)
    pathConfig = '{}/configs'.format(basePath)
    pathRoute = '{}/routes'.format(basePath)
    pathDriver = '{}/drivers'.format(basePath)
    pathModels = '{}/models'.format(basePath)

    prepareEnv(pathController)
    prepareEnv(pathConfig)
    prepareEnv(pathRoute)
    prepareEnv(pathDriver)
    prepareEnv(pathModels)

    if type == "ts":
        ts = TS(name)
        ctr = ts.getController()
        cfg = ts.getConfig()
        rt = ts.getRoute()
        appconfig = ts.getAppConfig()
        tsconfig = ts.getTsconfig()
        packagejson = ts.getPackage()

        if os.path.isfile("{}/app.ts".format(basePath)):
            f = open("{}/app.ts".format(basePath), 'r')
            app = f.read()
        else:
            app = ts.getApp()

        imports = '//project-imports\nimport * as {}Routes from `./routes/{}.route`;'.format(name, name)
        middlewares = '//defile-routes\nserver.use(prefix, {}Routes.router);'.format(name)

        app = app.replace('//project-imports', imports).replace('//defile-routes', middlewares)
        saveFile("{}{}".format(basePath, '/app.ts'), app)
        saveFile("{}{}".format(basePath, '/package.json'), packagejson)
        saveFile("{}{}".format(basePath, '/tsconfig.json'), tsconfig)
        saveFile("{}{}".format(pathConfig, "/{}".format('app.config.ts')), appconfig)
        saveFile("{}{}".format(pathController, "/{}{}".format(name, '.controller.ts')), ctr)
        saveFile("{}{}".format(pathConfig, "/{}{}".format(name, '.config.ts')), cfg)
        saveFile("{}{}".format(pathRoute, "/{}{}".format(name, '.route.ts')), rt)
    elif type == "js":
        js = JS(name)
        ctr = js.getController()
        cfg = js.getConfig()
        rt = js.getRoute()
        appconfig = js.getAppConfig()
        packagejson = js.getPackage()

        if os.path.isfile("{}/app.js".format(basePath)):
            f = open("{}/app.js".format(basePath), 'r')
            app = f.read()
        else:
            app = js.getApp()

        imports = '//project-imports\nconst {}Routes = required(`./routes/{}.route`);'.format(name, name)
        middlewares = '//defile-routes\nserver.use(config.prefix, {}Routes.router);'.format(name)

        app = app.replace('//project-imports', imports).replace('//defile-routes', middlewares)
        saveFile("{}{}".format(basePath, '/app.js'), app)
        saveFile("{}{}".format(basePath, '/package.json'), packagejson)
        saveFile("{}{}".format(pathConfig, "/{}".format('app.config.js')), appconfig)
        saveFile("{}{}".format(pathController, "/{}{}".format(name, '.controller.js')), ctr)
        saveFile("{}{}".format(pathConfig, "/{}{}".format(name, '.config.js')), cfg)
        saveFile("{}{}".format(pathRoute, "/{}{}".format(name, '.route.js')), rt)
    else:
        return


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hn:t:", ["name=", "type="])
    except getopt.GetoptError:
        print('apigenerator.py -n <api name> -t <code type>')
        sys.exit(2)

    name = ""
    codeType = ""

    for opt, arg in opts:
        if opt == '-h':
            print('test.py -n <api name> --type [ts,js]')
            sys.exit()
        elif opt in ("-n", "--name"):
            name = arg
        elif opt in ("-t", "--type"):
            codeType = arg

    if name == "":
        print("name is empty")
        return
    if codeType == "":
        print("name is empty")
        return

    generate(name, codeType)


if __name__ == "__main__":
    main(sys.argv[1:])
