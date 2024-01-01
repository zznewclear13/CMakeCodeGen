import os
import sys
import argparse
import traceback
from pathlib import Path
from jinja2 import Environment, PackageLoader
from markupsafe import Markup, escape
import yaml

def gatherFile(folder, ext):
    return Path(folder).glob("*.{0}".format(ext))

def gatherFileR(folder, ext):
    return Path(folder).rglob("*.{0}".format(ext))

def saveFile(filePath, bytes):
    with open(filePath, "w", encoding="utf-8") as f:
        f.write(bytes)

def main(args):
    try:
        sourceDir = args.cmake_code_gen_source_dir
        modulesDir = args.cmake_code_gen_modules_dir
        jinjaEnv = Environment(loader=PackageLoader("GenClass"), autoescape=False)
        cppTemplate = jinjaEnv.get_template("modules.cpp.template")
        headerTemplate = jinjaEnv.get_template("modules.h.template")
        regAllTemplate = jinjaEnv.get_template("register_all_modules.cpp.template")

        outputStr = ""
        moduleFiles = gatherFile(modulesDir, "module")
        generatedFiles = []
        generatedFiles.extend(gatherFile(sourceDir, "cpp"))
        generatedFiles.extend(gatherFile(sourceDir, "h"))

        moduleNames = []
        moduleClassNames = []
        for moduleFile in moduleFiles:
            with open(moduleFile.as_posix(), "r", encoding="utf-8") as yamlF:
                yamlFile = yaml.safe_load(yamlF)
                moduleName = yamlFile["ModuleName"]
                if "ModuleArgument" in yamlFile:
                    moduleArg = yamlFile["ModuleArgument"]
                    yamlFile["ModuleArgument"] = "\"{0}\"".format(moduleArg)

                cppFile = cppTemplate.render(yamlFile)
                headerFile = headerTemplate.render(yamlFile)

                cppFilePath = sourceDir + "/" + moduleName + ".cpp"
                headerFilePath = sourceDir + "/" + moduleName + ".h"
                # if not os.path.exists(cppFilePath):
                saveFile(cppFilePath, cppFile)
                # if not os.path.exists(headerFilePath):
                saveFile(headerFilePath, headerFile)

                outputStr += cppFilePath + ";" + headerFilePath + ";"
                moduleNames += [moduleName]
                moduleClassNames += [yamlFile["ModuleClassName"]]

        regAllCppFile = regAllTemplate.render(ModuleNames=moduleNames, ModuleClassNames=moduleClassNames)
        saveFile(sourceDir + "/../module_system/RegisterAllModules.cpp", regAllCppFile)

        for generatedFile in generatedFiles:
            if not generatedFile.stem in moduleNames:
                generatedFile.unlink()

        sys.stdout.write(outputStr)
        return 0
    except Exception as e:
        sys.stderr.write(''.join(traceback.format_exception(e)).strip())

    return 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--cmake-code-gen-source-dir", type=str, help="CMAIKE_CODE_GEN_SOURCE_DIR")
    parser.add_argument("-m,", "--cmake-code-gen-modules-dir", type=str, help="CMAKE_CODE_GEN_MODULES_DIR")
    args = parser.parse_args()

    sys.exit(main(args))