# se_com_opts
## 常用的selenium-webdriver设置

## 更新
* 1.0.5 2021/11/16
    * 对注释和部分参数名进行修改，减少使用时引用的参数错误。

## 介绍
常用的selenium webdriver chrome options配置项设置工具。

## 属性
* options: 根据设置的参数所返回的chrome_options。

## 参数
* localdata_path: 浏览器本地文件的地址，默认为None，可赋值'default'来导入本地文件的默认地址。
* extension_dir：存放浏览器插件的【文件夹地址】，默认为None，插件必须为打包好的crx格式，【不能】与无窗口模式同时使用。
* headless: 无窗口模式，默认为False。
* pic: 无图模式，默认为False。
* js: 不加载Javascript，默认为False。
* css：不加载CSS，默认为False。

## 用例
* SetChromeOptions(webdriver).options: 返回最基础的设置项。
* SetChromeOptions(webdriver,localdata_path = ’default').options: 返回使用默认本地*文件地址的设置项。
* SetChromeOptions(webdriverm, extension_dir = <extension_dir>).options: 返回使用crx插件的设置项。
