from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
from fastapi.responses import HTMLResponse

# FastAPIのアプリケーションインスタンスを作成
app = FastAPI()

tokenizer = AutoTokenizer.from_pretrained("hfunakura/bert-feedback-classifier")
model = AutoModelForSequenceClassification.from_pretrained("hfunakura/bert-feedback-classifier")

# 推論用クラスの作成
classifier = pipeline(
    "text-classification",
    model=model,  # モデル名を指定
    tokenizer=tokenizer  # トークナイザを指定
)

# リクエストボディの構造を定義
class TextInput(BaseModel):
    text: str

# シンプルなタイトル画面のエンドポイント
@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <h1>FastAPIへようこそ</h1>
    <p>このアプリはテキスト分類を行います。</p>
    <p>テキスト分類を行うには <code>/predict</code> にリクエストを送ってください。</p>
    """

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