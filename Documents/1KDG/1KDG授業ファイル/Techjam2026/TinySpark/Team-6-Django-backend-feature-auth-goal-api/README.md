#setup

python3 -m venv venv  
source venv/bin/activate  
pip install -r requirements.txt  
python3 manage.py migrate  
python3 manage.py runserver  

## React のビルド資産を Django と統合する

1. `Team-6-React-frontend/Team-6-react-frontend` で `npm run build` を実行し、`dist/` を生成します。
2. `dist/index.html` を `backend/templates/app/index.html` に、`dist/assets` を `backend/static/app/assets` にコピーします（フォルダーが存在しない場合は作成済みです）。
3. Django側で `python manage.py collectstatic` すると `staticfiles/` にハッシュ付きファイルがまとめられ、WhiteNoiseから `/static/app/...` で提供できます。
4. 以後は `/api/` はDjango API、`/app` 以降はReact SPA（`BrowserRouter` を使うなら `basename="/app"`）として同じホスト内で共存できます。

## React と Django のビルド/同期をまとめて実行する

`sync-react-to-django.sh` を使えばReactの `npm run build` → `dist/` のコピー → Djangoの `collectstatic` までを順に実行できます。TinySpark ルートから次のコマンドを叩いてください：

```sh
./scripts/sync-react-to-django.sh
```

最後に `python manage.py runserver 0.0.0.0:8000` を立ち上げれば、`http://localhost:8000/app` でReact SPAがDjango上で表示されます。必要があればローカルIPを使ってチームと共有してください。

Tiny SparkルートにDjango、同階層にReact、スクリプトが親ディレクトリから相対パスでReactを参照）を前提に書かれています
