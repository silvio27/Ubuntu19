# Ubuntu19
how to set a new Ubuntu19

1. Download [Ubuntu19](https://www.ubuntu.com/download/desktop)
2. use [rufus](https://rufus.ie/) burn in USB memory stick
3. if you want to use two system in one pc you may delete one disk for the Ubuntu
4. after the system setting then use 
    1. `sudo apt-get update`
    2. `sudo apt-get upgrade`
    3. change caps key to ctrl `sudo apt install gnome-tweak-tool`
        + Open Tweaks 
        + Keyboard & Mouse
        + Additional Layout Options
        + Ctrl position
        + find **Caps Lock as Ctrl**
5. Add git `sudo apt-get install git`
6. Add pycharm-community `sudo snap install pycharm-community --classic` my be you need install snap
7. Setup Firefox to login
8. download Adguard userlist from git then put in firefox
9. ~~add zsh~~ wait to test
10. install pip3 or update pip3 `pip3 install --upgrade pip`
11. pip change source
    make directory: .pip ：mkdir ~/.pip
    creat file: pip.conf ：gedit .pip/pip.conf
    ```
    [global]
    index-url = https://pypi.tuna.tsinghua.edu.cn/simple
    trusted-host = pypi.tuna.tsinghua.edu.cn
    ```
12. recommend packages
    + openpyxl
    + pyautogui
    + opencv-python
    + python-docx
    + flask
    + beautifulsoup4
    + pyecharts
        + echarts-maps

13. ready to update outdate pip `pip3 list --outdate`
    + use `pip3 install --upgrade pkgname`
