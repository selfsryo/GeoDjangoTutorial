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

## 出典
国土数値情報 ダウンロードサービス - http://nlftp.mlit.go.jp/ksj/index.html の北海道のデータを使用

- 国土交通省国土政策局「国土数値情報（行政区域データ）」 (N03-170101_01_GML)
http://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v2_3.html
- 国土交通省国土政策局「国土数値情報（小学校区データ）」 (A27-16_01_GML)
http://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-A27-v2_1.html
- 国土交通省国土政策局「国土数値情報（公共施設データ）」 (P02-06_01_GML)
http://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-P02-v4_0.html
- 国土交通省国土政策局「国土数値情報（バス停留所データ）」 (P11-10_01_GML)
http://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-P11.html
