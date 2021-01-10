# JupyterLab-Docker

講義用

## 事前準備

まずはDockerDesktopを入れてください

https://www.docker.com/products/docker-desktop

Windowsの方はVcXsrvのインストールをお願いします。

https://demura.net/misc/16325.html

Macintoshの方はXQuartzのインストールをお願いします。

http://blog.eszett-design.com/2020/10/dockerpythontkinter.html#no_twelve

## 使用方法

cloneしてそのディレクトリ上で

```
docker-compose up -d
```

で起動します。その後ブラウザで localhost:80 にアクセスしてください

使用後は

```
docker-compose down
```

で終了です。

## 追記

Windowsの人はdocker-compose.ymlの

```
environment:
      - DISPLAY=host.docker.internal:0.0
```

から


```
environment:
      - DISPLAY=自分のPCのIPアドレス:0.0
```

に変更しないと動かないかも
