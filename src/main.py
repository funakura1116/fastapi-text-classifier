from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline

# FastAPIのアプリケーションインスタンスを作成
app = FastAPI()

# 推論用クラスの作成
classifier = pipeline(
    "text-classification",
    model="../model/checkpoint-60",  # モデル名を指定
    tokenizer="../model/checkpoint-60"  # トークナイザを指定
)

# リクエストボディの構造を定義
class TextInput(BaseModel):
    text: str

# 推論を行うエンドポイント
@app.post("/predict")
async def predict(input: TextInput):
    try:
        # テキストをモデルに渡して推論を行う
        prediction = classifier(input.text)
        return {"prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 実行方法: uvicornで実行
# uvicorn main:app --reload
