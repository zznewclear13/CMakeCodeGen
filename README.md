# CMake代码自动生成CMake Code Gen

一个使用CMake, Python, Jinja2, Pyyaml的自动生成代码的项目示例。A CMake code generation demo project using CMake, Python, Jinja2 and pyyaml.

## 特性Features

1. 简单地通过模板创建新的空白类。Easily create new empty class from template.
    - 在`source/CMakeNewClassWatcher.txt`中输入新类的路径和名称。Type in path and name of new class in `source/CMakeNewClassWatcher.txt`.
    - 在Visual Studio中点击`Build->Build Solution`开始构建。Click `Build->Build Solution` to start building in Visual Studio.
2. 通过模板创建模块类并自动添加到工程中。Create module class from template and add to project automatically.
    - 在`modules/module_config/`中添加或移除`*.module`文件。Add or remove `*.module` files in `modules/module_config/`.
    - 在Visual Studio中点击`Build->Build Solution`开始构建。Click `Build->Build Solution` to start building in Visual Studio.
3. 控制反转的设计来自于Ludwig Füchsl的(Boundless2D)[https://github.com/Ohjurot/Boundless2D]。The Inversion of Controll design pattern comes from (Boundless2D)[https://github.com/Ohjurot/Boundless2D] by Ludwig Füchsl.

## 使用方法Usage

1. 通过git下载本仓库。Download this repository using git.
```
git clone https://github.com/zznewclear13/CMakeCodeGen.git
```
2. 双击`configure.bat`配置VS工程。Double click `configure.bat` to configure Visual Studio project.
3. 初次构建会创建这些文件Following files will be generated during first configuration:
    - source/NewClass.cpp
    - source/NewClass.h
    - dummy.foo.cpp
    - dummy.foo.h
    - dummy.bar.cpp
    - dummy.bar.h
4. 双击`build.bat`进行构建。Double click `build.bat` to build.
5. 在`binary/Release/bin`下即可找到构建好的`CMakeCodeGen.exe`。`CMakeCodeGen.exe` will be built to `binary/Release/bin`.

## 缺陷Flaws

本项目使用了CMake中`file(GLOB CONFIGURE_DEPENDS)`来获取module的模板文件，只能检测到增加删除，而不能检测到修改。This project uses `file(GLOB CONFIGURE_DEPENDS)` to monitor template files for modules, only adding/removing can be detected, modifing any template files would not be detected.