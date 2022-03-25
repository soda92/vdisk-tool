# vdisk-tool

A tool for managing virtual disks.

## 安装

Windows:

安装[scoop](https://scoop.sh/):
```
Set-ExecutionPolicy RemoteSigned -scope CurrentUser
iwr -useb get.scoop.sh | iex
```

安装sudo: `scoop install sudo`

打开管理员权限命令行：`sudo pwsh`

```
.\vdisk-tool install
.\vdisk-tool start
```

打开[localhost:5002](http://localhost:5002)即可查看。


## 卸载

```
sudo pwsh
.\vdisk-tool stop
.\vdisk-tool uninstall
```

## third party

this project use [winsw](https://github.com/winsw/winsw) for mangaing services
on Windows.
