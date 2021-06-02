# Start

1. 下载nodejs
2. 创建工程文件夹，执行npm init，工程初始化
3. 在package.json文件中的script中添加:
   ```json
   "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "electron ."
   },
   ```
4. 安装`electron：npm install --save-dev electron`，将electron作为包依赖，也可以使用`npm install -g electron`进行全局安装
   1. `npx electron -v`或者`./node_modules/.bin/electron -v`查看electron版本

5. `npx electron .`运行项目，npx会将node_module/bin加入到环境变量中，并且强制使用本地package。或者，在package.json中的script中配置start命令，可以直接使用`npm start`运行
![](img/0001-1.png)

   