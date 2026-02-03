#setup

python3 -m venv venv  
source venv/bin/activate  
pip install -r requirements.txt  
python3 manage.py migrate  
python3 manage.py runserver  

## React のビルド資産を Django と統合する

1. `Team-6-React-frontend/Team-6-react-frontend` で `npm run build` を実行し、`dist/` を生成します。
2. `dist/index.html` を `backend/templates/app/index.html` に、`dist/assets` を `backend/static/app/assets` にコピーします（フォルダが存在しない場合は作成済みです）。
3. Django 側で `python manage.py collectstatic` すると `staticfiles/` にハッシュ付きファイルがまとめられ、WhiteNoise から `/static/app/...` で提供できます。
4. 以後は `/api/` は Django API、`/app` 以降は React SPA（`BrowserRouter` を使うなら `basename="/app"`）として同じホスト内で共存できます。
