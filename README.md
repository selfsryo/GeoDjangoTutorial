# GeoDjango tutorial


## 概要
- 以下参考（Docker導入および一部ソースコードをバージョンに適した内容に改変）<br>
https://homata.gitbook.io/geodjango/


## 環境構築

```sh
docker-compose up --build
```

## 管理者作成
```sh
docker exec -it  geodjango_tutorial bash
# コンテナ内で以下
python3.8 manage.py createsuperuser
```
