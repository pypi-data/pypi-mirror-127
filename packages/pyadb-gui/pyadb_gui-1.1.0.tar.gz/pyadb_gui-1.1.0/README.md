# pyadb_GUI

### 介绍
使用 python 自带的 Tkinter 库编写一个通过 GUI 界面操作 adb 设备的 pip 包。


### 版本更新

1. V0.1 基础功能
   - [x] 常用遥控器按键
   - [x] 一键直达 蓝牙配对/ wifi 连接
     - [x] 调整快捷键背景色
   - [x] 一键输入文字
     - [x] 输入后清除文字
2. V0.2 设备信息界面
   - [x] 设备
     - [x] 时间
     - [x] 版本
     - [x] 获取 DSN 号
   - [x] 网络
     - [x] ip 地址
     - [x] 联网状态
   - [x] 遥控器
     - [x] mac 地址
   - [x] TreeView (列表)视图
   - [x] NoteBook 分页
   - [x] 双击复制信息
3. V0.9
   - fix: notebook 分页
   - fix: text input error
4. V1.0.1
   - 新增: 
      + 显示多蓝牙设备的名称和 mac 地址(包括但不限于遥控器，蓝牙键盘、音响、手柄)
      + 添加一键 oobe 按钮（弹窗二次确认）
      + 添加刷新按钮 Reload（ip 地址等变更后可刷新查看）
      + 添加关于页面(显示 pyadb 信息)
   - 优化: 
      + 输入框添加下拉菜单选项
      + 无设备连接时，按键后弹窗提示
      + 布局: 设备界面添加滚动条
   - 修复: 
      + 部分设备连接时显示 "UnicodeDecodeError"
5. V1.0.4
   - 修复: 
      + Factory Reset 后立即打开 pyadb 提示 "IndexError"
      + Button 页面布局字体优化
      + Information 页面
6. V1.1
   - 新增 setup 页面: 
      + dongle 线连接电视后，一键配置 ip 地址
      + adb connect 功能
      + 多设备选择功能


### 开发中

1. [ ] 视频/截图
   - [ ] 截图功能
   - [ ] 屏幕录制功能
2. log 截取(关键字)
   - [ ] adb / picus / event log
   - [ ] get_log
   - [ ] 清理 log 缓存
3. adb push 文件
4. 刷机功能
5. 布局自适应缩放 


### 安装教程

1.  `pip3 install --upgrade pyadb_gui`
2.  `pyadb`


### 可能遇到的问题

1. 报错 ModuleNotFoundError: `no module named tkinter`
> 解决方法: 找到提示文字中的 python3.7
>   - `sudo apt update`
>   - `sudo apt install python3.7-tk -y`
>   - `pyadb`


#### 参与贡献

1. 作者 : xq
2. 发布审核 : cyy
3. 功能规划 : ftq
4. 代码调试环境 : lhy
5. beta 测试：lsw
6. bug 反馈 : whb, llh,
7. 功能建议 : ljz, llw
