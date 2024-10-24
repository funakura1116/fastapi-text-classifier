# FastAPI で作る文書分類モデルAPI

## 事前準備
- 適当な場所にフォルダを作成する。以下そのフォルダ名を `fastapi-text-classifier` とする
- `fastapi-text-classifier` 内に `requirements.txt` を置く
- `fastapi-text-classifier` 内に `model` フォルダと `src` フォルダを作成する
- `model` フォルダにチェックポイントフォルダを置く
- `src` フォルダに `main.py` を作成する

以下、ターミナル/コマンドプロンプト/PowerShell上で作業する。カレントディレクトリが `fastapi-text-classifier` になっていることを確認すること(`VSCode` で `fastapi-text-classifier` を開けばそれで良い )。

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