# FastAPI で作る文書分類モデルAPI

## 事前準備
- 適当な場所にフォルダを作成する。以下そのフォルダ名を `fastapi-text-classifier` とする
- `fastapi-text-classifier` 内に `requirements.txt` を置く
- `fastapi-text-classifier` 内に `model` フォルダと `src` フォルダを作成する
- `model` フォルダにチェックポイントフォルダを置く
- `src` フォルダに `main.py` を作成する

以下のようなフォルダ構成になっていれば良い。
```text
.
├── model
│   └── checkpoint-60
├── requirements.txt
└── src
    └── main.py
```

以下、ターミナル/コマンドプロンプト/PowerShell上で作業する。カレントディレクトリが `fastapi-text-classifier` になっていることを確認すること(`VSCode` で `fastapi-text-classifier` を開けばそれで良い )。

```sh
pwd
```
> path/to/fastapi-text-classifier

> [!WARNING]
> PowerShellはデフォルトだと仮想環境を有効化するスクリプトの実行ができない。以下のスクリプトで実行を許可するか、コマンドプロンプトを利用する。
> ```sh
> Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
> ```

## 環境構築

```sh
python3 -m venv .venv
```

```sh
source .venv/bin/activate # Linux, macOS
./.venv/Scripts/activate # Windows
```

```sh
pip install -r requirements.txt
```

## サーバの立ち上げ
```sh
uvicorn main:app --reload
```