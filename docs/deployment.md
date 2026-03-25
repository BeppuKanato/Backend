# デプロイ手順(deployment)

このドキュメントでは、本プロジェクトをAWS EC2上へデプロイする手順を説明します。  
本番環境およびステージング環境は、基本的に同一の構成を想定しています。

---

## 🎯 対象環境

- ステージング環境
- 本番環境
  
※環境ごとの差分は主に環境変数とデータベース設定です。

---

## 🧱 構成概要

本プロジェクトの開発環境・ステージング環境・本番環境は、基本的に同一の構成を持ちます。  
各環境の違いは主にデータベースおよび環境変数にあります。  

> 構成図は[アーキテクチャ](./architecture.md)を参照してください。

---

## ⚙️ 事前準備

デプロイを実行する前に、以下を準備してください。

- AWS EC2インスタンス
  - OS：Ubuntu
  - セキュリティグループ
    - HTTP(80)
    - SSH(22) 
- AWS RDS(MySQL)インスタンス
- EC2へSSH接続するための秘密鍵(`.pem`)
- Gitでリポジトリを取得できる状態

また、RDSについては以下の情報を確認しておいてください。

- エンドポイント
- データベース名
- ユーザ名
- パスワード
- ポート番号

これらの情報は`.env.prod`に設定するために必要です。

---

## 🔑 EC2にログイン

以下のコマンドでEC2インスタンスに接続します。

```bash
ssh -i <secret-key.pem> ubuntu@<EC2のIPアドレス>
```

---

## 📦 Docker / Gitのインストール

EC2にDockerおよび関連ツールをインストールします。

```bash
sudo apt update

sudo apt install -y ca-certificates curl gnupg

sudo install -m 0755 -d /etc/apt/keyrings

sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc

sudo chmod a+r /etc/apt/keyrings/docker.asc

echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt update

sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin git
```

---

## 📥 リポジトリの取得

EC2上でリポジトリをクローンします。

```bash
git clone https://github.com/BeppuKanato/Backend.git
cd Backend
```

---

## 📝 .env.prodの作成

以下のコマンドで環境変数ファイルを作成します。

```bash
nano .env.prod
```

`.env.example`を参考に `.env.prod`を作成してください。  

本番・ステージング環境では以下の変更を行ってください。

1. `DEBUG=False`に変更する
2. `SECRET_KEY`を設定する
3. `ALLOWED_HOSTS`を設定する
4. データベース設定を本番用またはステージング環境用に変更する

環境変数の例：
```env
DEBUG=False
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=your-ec2-ip

DB_NAME=socialgame_prod
DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=your-rds-endpoint
DB_PORT=3306
```

---

## 🚀 コンテナの起動

以下のコマンドでアプリケーションを起動します。

```bash
docker compose --env-file .env.prod -f docker-compose.yml -f docker-compose.prod.yml up -d --build
```

---

## 🌐 動作確認

起動後、ブラウザで以下にアクセスしてください。

```
http://<EC2のIPアドレス>
```

---

## ⚠️ 注意事項

- この手順ではHTTPSは設定していません
- `.env.prod`はGitに含めないでください
- `DEBUG=False`を必ず設定してください
- `ALLOWED_HOSTS`にはアクセスを許可するホストを設定してください