import os
import sys
import argparse
import traceback
from jinja2 import Environment, PackageLoader

def saveFile(filePath, bytes):
    with open(filePath, "w", encoding="utf-8") as f:
        f.write(bytes)

def main(args):
    try:
        sourceDir = args.cmake_code_gen_source_dir
        newClassWatcher = args.cmake_code_gen_new_class_watcher
        jinjaEnv = Environment(loader=PackageLoader("GenClass"), autoescape=["cpp", "h"])
        cppTemplate = jinjaEnv.get_template("class.cpp.template")
        headerTemplate = jinjaEnv.get_template("class.h.template")  

        outputStr = ""
        with open(sourceDir + "/" + newClassWatcher, "r", encoding="utf-8") as f:
            lines = f.readlines()
            classDir = ""
            className = ""
            for classPath in lines:
                classPath = classPath.strip()
                if classPath == "":
                    continue

                lastSlash = classPath.rfind("/")
                if lastSlash == -1:
                    className = classPath
                else:
                    classDir = classPath[0:lastSlash]
                    className = classPath[lastSlash+1:]

                cppFile = cppTemplate.render(CLASS_NAME=className)
                headerFile = headerTemplate.render(CLASS_NAME=className)
                classDir = sourceDir + "/" + classDir
                if not os.path.exists(classDir):
                    os.mkdir(classDir)

                cppFilePath = classDir + "/" + className + ".cpp"
                headerFilePath = classDir + "/" + className + ".h"
                if not os.path.exists(cppFilePath):
                    saveFile(cppFilePath, cppFile)
                if not os.path.exists(headerFilePath):
                    saveFile(headerFilePath, headerFile)
                    
                outputStr += cppFilePath + ";" + headerFilePath + ";"
                
        sys.stdout.write(outputStr)
        return 0
    except Exception as e:
        sys.stderr.write(''.join(traceback.format_exception(e)).strip())

    return 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--cmake-code-gen-source-dir", type=str, help="CMAIKE_CODE_GEN_SOURCE_DIR")
    parser.add_argument("-n", "--cmake-code-gen-new-class-watcher", type=str, help="CMAKE_CODE_GEN_NEW_CLASS_WATCHER")
    args = parser.parse_args()

    print(args)

    sys.exit(main(args))