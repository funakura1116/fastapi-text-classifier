# fastapi-text-classifier

## 事前準備
- 適当な場所にフォルダを作成する。以下そのフォルダ名を `fastapi-folder` とする
- `fastapi-folder` 内に `requirements.txt` を置く
- `fastapi-folder` 内に `model` フォルダと `src` フォルダを作成する
- `model` フォルダにチェックポイントフォルダを置く
- `src` フォルダに `main.py` を作成する

```sh
pwd
```
> path/to/fastapi-text-classifier

## 環境構築

```sh
python3 -m venv .venv
```

```sh
source .venv/bin/activate
```

```sh
pip install -r requirements.txt
```

## サーバの立ち上げ
```sh
uvicorn main:app --reload
```