# spyshot

定时屏幕截图，监视小屁孩用电脑

## 使用方法

* ~~修改`startup.bat`文件，指向正确的路径~~
* 创建`startup.bat`快捷方式，并放到系统自启动目录（`shell:common startup` 快捷打开）
* `telnet 127.0.0.1 8023`连接服务控制台
  * `exit`或`quit` 退出当前会话
  * `kill` 停止服务
* `python .\merge.py 20230804` 生成当日视频

## 后续更新

* 最新图片`img\screen.jpg`上传到服务器
* 服务器通过web展示最新图片
