# AWS公式よりPython 3.11 環境を利用
FROM public.ecr.aws/lambda/python:3.11
# アプリケーションコードをコピー
COPY lambda_function.py requirements.txt ./
# 依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt
# ハンドラを設定
CMD ["lambda_function.lambda_handler"]
