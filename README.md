# Socialgame-Text-Backend

書籍「ソーシャルゲーム開発ガイド」を基にした  
Django + Docker構成のバックエンドAPIを構築・運用する学習用プロジェクト

---

## 🚀 クイックスタート

```bash
git clone https://github.com/BeppuKanato/Backend.git
cd Backend
cp .env.example .env.dev

docker compose --env-file .env.dev -f docker-compose.yml -f docker-compose.dev.yml up --build
```

---

## 📚 ドキュメント

- [環境構築](./docs/setup.md)
- [開発ルール](./docs/development.md)
- [デプロイ](./docs/deployment.md)
- [アーキテクチャ](./docs/architecture.md)
- [Git運用](./docs/git-workflow.md)

---

## 技術構成

- Django
- nginx
- MySQL
- Docker

---

## ディレクトリ構成

```

BACKEND/
├─ app/ # Djangoアプリケーション
├─ docs/ # ドキュメント
├─ nginx/ # nginx設定
├─ mysql/ # DB初期化スクリプト
├─ docker-compose.yml
├─ docker-compose.dev.yml
├─ docker-compose.prod.yml
├─ .env.example
├─ LICENSE
└─ README.md
```