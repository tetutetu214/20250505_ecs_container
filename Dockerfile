# 汎用的なPythonイメージを使用
FROM public.ecr.aws/docker/library/python:3.11-slim

# 作業ディレクトリを設定
WORKDIR /app

# アプリケーションをコピー
COPY app.py requirements.txt ./

# 依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt

# コンテナ起動時に実行するコマンド
CMD ["python", "app.py"]

# ECSヘルスチェック用
HEALTHCHECK --interval=30s --timeout=10s   CMD python -c "import requests; requests.get('http://localhost:8080/health').raise_for_status()"
