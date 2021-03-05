import sys, getopt
import os
import base64

def getRoute():
    return "aW1wb3J0IGV4cHJlc3MgZnJvbSAnZXhwcmVzcyc7CmltcG9ydCB7IHByZWZpeCB9IGZyb20gJy4u" \
           "L2NvbmZpZ3MvQ09OVFJPTExFUk5BTUUuY29uZmlnJzsKY29uc3Qgcm91dGVyID0gZXhwcmVzcy5S" \
           "b3V0ZXIoKTsKcm91dGVyLmdldChwcmVmaXgsIGFzeW5jIChyZXEsIHJlcykgPT4gewogIHJldHVy" \
           "biByZXMuc3RhdHVzKDIwMCkuanNvbigpLmVuZCgpOwp9KTsKcm91dGVyLmdldChwcmVmaXggKyAn" \
           "LzppZCcsIGFzeW5jIChyZXEsIHJlcykgPT4gewogIGlmICghcmVxLnBhcmFtcy5pZCkgewogICAg" \
           "cmV0dXJuIHJlcy5zdGF0dXMoNDA0KS5lbmQoKTsKICB9CiAgcmV0dXJuIHJlcy5zdGF0dXMoMjAw" \
           "KS5qc29uKCkuZW5kKCk7Cn0pOwpyb3V0ZXIucG9zdChwcmVmaXgsIGFzeW5jIChyZXEsIHJlcykg" \
           "PT4gewogIGlmICghcmVxLmJvZHkpIHsKICAgIHJldHVybiByZXMuc3RhdHVzKDQwNCkuZW5kKCk7" \
           "CiAgfQogIHJldHVybiByZXMuc3RhdHVzKDIwMCkuanNvbigpLmVuZCgpOwp9KTsKcm91dGVyLnB1" \
           "dChwcmVmaXgsIGFzeW5jIChyZXEsIHJlcykgPT4ge30pOwpyb3V0ZXIuZGVsZXRlKHByZWZpeCwg" \
           "YXN5bmMgKHJlcSwgcmVzKSA9PiB7fSk7CmV4cG9ydCB7IHJvdXRlciB9"


def getController():
    return "YXN5bmMgZnVuY3Rpb24gZ2V0Q09OVFJPTExFUk5BTUVzKCk6IGFueVtdIHsKfQphc3luYyBmdW5j" \
           "dGlvbiBnZXRDT05UUk9MTEVSTkFNRShpZDogc3RyaW5nKTogYW55IHsKfQphc3luYyBmdW5jdGlv" \
           "biBkZWxldGVDT05UUk9MTEVSTkFNRShpZDogc3RyaW5nKTogYm9vbGVhbiB7Cn0KYXN5bmMgZnVu" \
           "Y3Rpb24gdXBkYXRlQ09OVFJPTExFUk5BTUUob2JqOiBhbnkpOiBib29sZWFuIHsKfQphc3luYyBm" \
           "dW5jdGlvbiBjcmVhdGVDT05UUk9MTEVSTkFNRShvYmo6IGFueSk6IHN0cmluZyB7Cn0= "


def getConfig():
    return "Y29uc3QgcHJlZml4ID0gJy9DT05UUk9MTEVSTkFNRSc7CmV4cG9ydCB7IHByZWZpeCB9Ow=="


def getApp():
    return "aW1wb3J0IGV4cHJlc3MgZnJvbSAnZXhwcmVzcyc7CmltcG9ydCBjb3JzIGZyb20gJ2NvcnMnOwpp" \
           "bXBvcnQgYm9keVBhcnNlciBmcm9tICdib2R5LXBhcnNlcic7CmltcG9ydCBtb3JnYW4gZnJvbSAn" \
           "bW9yZ2FuJzsKLy9wcm9qZWN0LWltcG9ydHMKaW1wb3J0IHsgcG9ydCwgcHJlZml4IH0gZnJvbSAn" \
           "Li9jb25maWdzL2FwaS5jb25maWcnOwoKY29uc3Qgc2VydmVyID0gZXhwcmVzcygpOwpzZXJ2ZXIu" \
           "dXNlKGNvcnMoKSk7CnNlcnZlci51c2UoYm9keVBhcnNlci5qc29uKCkpOwpzZXJ2ZXIudXNlKG1v" \
           "cmdhbignZGV2JykpOwovL2RlZmlsZS1yb3V0ZXMKCnNlcnZlci5saXN0ZW4ocG9ydCwgKCkgPT4K" \
           "ICBjb25zb2xlLmxvZygnQVBJLUVORFBPSU5UIGFyZSBydW5uaW5nICg6JyArIHBvcnQgKyAnKScp" \
           "Cik7Cg=="

def pgClass():
    return "aW1wb3J0IHsgSURiQ29ubmVjdGlvbiB9IGZyb20gJy4uL21vZGVscy9kYmNvbm5lY3Rpb24nOwpp"\
            "bXBvcnQgeyBQb29sIH0gZnJvbSAncGcnOwppbXBvcnQgKiBhcyBjb25uZWN0aW9uQ29uZmlncyBm"\
            "cm9tICcuLi9jb25maWdzL3BnLmNvbmZpZyc7CgpleHBvcnQgY2xhc3MgUGdDb25uZWN0aW9uIGlt"\
            "cGxlbWVudHMgSURiQ29ubmVjdGlvbiB7CiAgcHJpdmF0ZSBfcG9vbENvbm5lY3Rpb246IFBvb2w7"\
            "CgogIGNvbnN0cnVjdG9yKCkgewogICAgdGhpcy5fcG9vbENvbm5lY3Rpb24gPSBuZXcgUG9vbChj"\
            "b25uZWN0aW9uQ29uZmlncyk7CiAgfQoKICBwdWJsaWMgcXVlcnkoc3FsOiBzdHJpbmcsIHBhcmFt"\
            "cz86IGFueVtdKTogYW55IHsKICAgIHRyeSB7CiAgICAgIHJldHVybiB0aGlzLl9wb29sQ29ubmVj"\
            "dGlvbgogICAgICAgIC5jb25uZWN0KCkKICAgICAgICAudGhlbihjbGllbnQgPT4gewogICAgICAg"\
            "ICAgcmV0dXJuIGNsaWVudAogICAgICAgICAgICAucXVlcnkoc3FsLCBwYXJhbXMpCiAgICAgICAg"\
            "ICAgIC50aGVuKHJlcyA9PiB7CiAgICAgICAgICAgICAgY2xpZW50LnJlbGVhc2UoKTsKICAgICAg"\
            "ICAgICAgICByZXR1cm4gcmVzOwogICAgICAgICAgICB9KQogICAgICAgICAgICAuY2F0Y2goZSA9"\
            "PiB7CiAgICAgICAgICAgICAgY2xpZW50LnJlbGVhc2UoKTsKICAgICAgICAgICAgICB0aHJvdyBu"\
            "ZXcgRXJyb3IoZSk7CiAgICAgICAgICAgIH0pOwogICAgICAgIH0pCiAgICAgICAgLmNhdGNoKGVy"\
            "ciA9PiB7CiAgICAgICAgICB0aHJvdyBlcnI7CiAgICAgICAgfSk7CiAgICB9IGNhdGNoIChlcnJv"\
            "cikgewogICAgICBjb25zb2xlLmVycm9yKGVycm9yKTsKICAgIH0KICB9Cn0K"

def dbconnection():
    return "ZXhwb3J0IGludGVyZmFjZSBJRGJDb25uZWN0aW9uIHsKICBxdWVyeShzcWw6IHN0cmluZywgcGFy"\
            "YW1zOiBhbnlbXSk6IGFueTsKfQ=="

def simpleModel():
    return "ZXhwb3J0IGludGVyZmFjZSBDT05UUk9MTEVSTkFNRSB7CiAgCn0="

def pgConfig():
    return "aW1wb3J0IGRvdGVudiBmcm9tICdkb3RlbnYnOwpkb3RlbnYuY29uZmlnKCk7CmNvbnN0IHVzZXI6"\
            "IHN0cmluZyA9IHByb2Nlc3MuZW52LlBHX1VTRVJOQU1FIHx8ICdzaW1vbmUnOwpjb25zdCBwYXNz"\
            "d29yZDogc3RyaW5nID0gcHJvY2Vzcy5lbnYuUEdfUEFTU1dPUkQgfHwgJyc7CmNvbnN0IGRhdGFi"\
            "YXNlOiBzdHJpbmcgPSBwcm9jZXNzLmVudi5QR19EQVRBQkFTRSB8fCAnJzsKY29uc3QgaG9zdDog"\
            "c3RyaW5nID0gcHJvY2Vzcy5lbnYuUEdfSE9TVE5BTUUgfHwgJ2xvY2FsaG9zdCc7CmNvbnN0IHBv"\
            "cnQ6IG51bWJlciA9IE51bWJlcihwcm9jZXNzLmVudi5QR19QT1JUKSB8fCA1NDMyOwoKZXhwb3J0"\
            "IHsgdXNlciwgcGFzc3dvcmQsIGRhdGFiYXNlLCBob3N0LCBwb3J0IH07"

def saveFile(path, content):
    text_file = open(path, "w")
    text_file.write(content)
    text_file.close()


def decode(c):
    base64_bytes = c.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    return message_bytes.decode('ascii')


def prepareEnv(p):
    if not os.path.exists(p):
        os.makedirs(p)


def generate(controllerName):
    ctr = decode(getController()).replace('CONTROLLERNAME', controllerName)
    cfg = decode(getConfig()).replace('CONTROLLERNAME', controllerName)
    rt = decode(getRoute()).replace('CONTROLLERNAME', controllerName)
    model = decode(simpleModel()).replace('CONTROLLERNAME', controllerName)
    basePath = "./src"
    app = ""

    if os.path.isfile("{}/app.ts".format(basePath)):
        f = open("{}/app.ts".format(basePath), 'r')
        app = f.read()
    else:
        app = decode(getApp())
    
    pg = decode(pgClass())
    pgc = decode(pgConfig())
    dbconn = decode(dbconnection())

    imports = '//project-imports\nimport * as {}Routes from `./routes/{}.route`;'.format(controllerName,controllerName)
    middlewares = '//defile-routes\nserver.use(prefix, {}Routes.router);'.format(controllerName)

    app = app.replace('//project-imports', imports).replace('//defile-routes', middlewares)

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


    saveFile("{}{}".format(basePath, '/app.ts'), app)
    saveFile("{}{}".format(pathController, "/{}{}".format(controllerName, '.controller.ts')), ctr)
    saveFile("{}{}".format(pathConfig, "/{}{}".format(controllerName, '.config.ts')), cfg)
    saveFile("{}{}".format(pathRoute, "/{}{}".format(controllerName, '.route.ts')), rt)
    saveFile("{}{}".format(pathModels, "/{}.ts".format(controllerName)), model)
    
    # postgres
    saveFile("{}{}".format(pathConfig, "/pg.config.ts"), pgc)
    saveFile("{}{}".format(pathDriver, "/pg.driver.ts"), pg)
    saveFile("{}{}".format(pathModels, "/dbconnection.ts"), dbconn)


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "n:", ["name="])
    except getopt.GetoptError:
        print('apigenerator.py -n <api name>')
        sys.exit(2)
    controllerName = ""
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -n <api name>')
            sys.exit()
        elif opt in ("-n", "--name"):
            controllerName = arg

    if controllerName != "":
        generate(controllerName)


if __name__ == "__main__":
    main(sys.argv[1:])
