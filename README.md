# Filter-OPTIONS-Method
This script is a Python plugin for Burpsuite, designed to filter options methods

## 背景

想学习一下burpsuite插件的编辑，就尝试写了一下这个插件。

## 安装

要安装插件，请按照以下步骤操作：
1. 从本页面下载插件的最新版本。
2. 在Burp Suite中，导航到`Extender`标签。
3. 点击`Add`，然后选择下载的插件文件。
4. 此时插件应已安装并激活。
PS:需要正确配置jython环境才能使用此插件。

## 使用方法

安装插件后，您可以按照以下步骤使用它：

选择 proxy -> http history -> fifter -> Filter by MIME type -> untick the CSS checkbox

## 作者

flechazo

## 参考仓库

本脚本主要模仿此代码的逻辑，但是整体重构了一下。

这个老哥的想法很骚气，通过将OPTIONS方法的数据包全打上MIME类型为JSON，以此通过burpsuite自带的过滤器来进行处理。

仓库链接：https://github.com/capt-meelo/filter-options-method

## 许可证

[MIT](https://choosealicense.com/licenses/mit/)
