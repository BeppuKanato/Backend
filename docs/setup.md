# 環境構築(setup)

このドキュメントでは、本プロジェクトの開発環境を構築する手順を説明します。

---

## 🧰 前提条件

以下がインストールされている必要があります。

- Git
- Docker
- Docker Compose

---

## 📥 リポジトリの取得

```bash
git clone https://github.com/BeppuKanato/Backend.git
cd Backend
```

---

## ⚙ 環境変数の設定

`.env.example`をコピーして`.env.dev`を作成します。

※Mac,Linuxの場合
```bash
cp .env.example .env.dev
```

※Windowsの場合
```bash
copy .env.example .env.dev
```

必要に応じて.env.devの内容を編集してください。

---

## 🚀 コンテナの起動

以下のコマンドで開発環境を起動します。

```bash
docker compose --env-file .env.dev -f docker-compose.yml -f docker-compose.dev.yml up --build
```

---

## 🌐 アクセス確認

起動後、以下のURLにアクセスできます。

- [アプリ](http://localhost)：(http://localhost)
- [phpMyAdmin](http://localhost:8080)：(http://localhost:8080)

---

## 🗄 データベースのマイグレーション

初回起動時やモデル変更時は、マイグレーションを実行します。

```bash
docker compose exec app python manage.py makemigrations
docker compose exec app python manage.py migrate
```

---

## 🛑 コンテナの停止

以下のコマンドでコンテナを停止できます。

```bash
docker compose down
```

---

## ❗ よくあるエラー

**ポートが使用中**

```
Error: port is already allocated
```

👉他のコンテナやアプリがポートを使用しています。  
→停止するかポート番号を変更してください。

---
**Dockerが起動していない**

```
Cannot connect to the Docker daemon
```
👉Docker Desktopを起動してください。

---

**マイグレーションエラー**

```
django.db.utils.OperationalError
```

👉DBコンテナが起動しているか確認してください。

## 💡 補足

- .env.devはGit管理されません
- 設定値は各自の環境に応じて変更してください