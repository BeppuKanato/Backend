# Git運用(Git Workflow)

本ドキュメントでは、本プロジェクトにおけるGitブランチ運用ルールを定義します。

---

## 🌳 ブランチ構成

本プロジェクトでは、以下のブランチを使用します。

| ブランチ名 | 説明 |
| ---------- | --- |
|   `main`   |  本番環境用のブランチです。<br>リリース済みの安定したコードを管理します。 |
|  `develop` | 開発用の統合ブランチです。<br>日常的な開発のベースとなります。 |
|  `feature/*` | 機能開発・修正用のブランチです。<br>`develop`から作成します。 |
| `release/*` | リリース準備用のブランチです。<br>`develop`から作成し、ステージング環境で確認を行います。 |

---

## 🎯 基本方針

- 開発は`develop`ブランチを基準に行う
- 作業時は`develop`から`feature`ブランチを作成する
- リリース時は`develop`から`release`ブランチを作成する
- `main`ブランチへ直接コミットしない
- `develop`ブランチへ直接コミットしない
- IssueとPull Requestは関連付ける

---

## 🛠 開発フロー

通常の開発は以下の流れで行います。

1. `develop`を最新化する
2. `feature`ブランチを作成する
3. 実装・修正を行う
4. コミットする
5. `develop`向けにPull Requestを作成する

### 1. developを最新化

```bash
git checkout develop
git pull origin develop
```

### 2. featureブランチを作成

ブランチ名は、作業内容が分かる名前にしてください。

```bash
git checkout -b feature/<作業名>
```

例：
```bash
git checkout -b feature/user-login
git checkout -b feature/add-item-api
```

### 3. 実装・修正

必要な実装や修正を行います。

### 4. コミット

変更内容をコミットします。

```bash
git add .
git commit -m "✨ feat: ログイン機能を追加"
```

### 5. Pull Requestを作成

`feature/*`ブランチから`develop`ブランチへPull Requestを作成してください。

## リリースフロー

リリース時は以下の流れで行います。

1. `develop`から`release`ブランチを作成する
2. ステージング環境で動作確認を行う
3. 問題がなければ`main`にマージする
4. 必要に応じて`develop`にも反映する

### 1. releaseブランチを作成

```bash
git checkout develop
git pull origin develop
git checkout -b release/<version>
```

### 2. ステージング環境で確認

releaseブランチをステージング環境へ反映し、リリース前の最終確認を行います。

### 3. mainにマージ

ステージング環境で問題がなければ、`release`ブランチを`main`にマージします。

### 4. developに反映

リリース作業中に`release`ブランチ上で修正を加えた場合は、その変更をdevelopにも反映してください。

---

## 🎫 Issue運用

本プロジェクトでは、基本的にIssueベースで開発を行います。

- 作業前にIssueを作成する
- 1つのIssueにつき1つの目的で作成する
- Issue番号をPull Requestに紐づける

---

## 🔗 Pull RequestとIssueの連携

Pull Request作成時は、関連するIssueを必ず記載してください。

PRの説明欄に以下のように記載します。

```
closes #12
```

これにより、Pull Requestがマージされた際にIssueが自動でクローズされます。

---

## 📝 ブランチ命名ルール

ブランチ名は、用途が分かるように命名してください。

**featureブランチ**
```
feature/<作業名>
```

例：
```
feature/user-login
feature/add-mission-api
feature/fix-auth-error
```

**releaseブランチ**

```
release/<version>
```

例：
```
release/v1.0.0
release/v1.1.0
```

---

## 📦 コミットメッセージ

コミットメッセージは、以下の形式を推奨します。

- ✨`feat`: 新機能追加
- 🐛`fix`: バグ修正
- ♻️`refactor`: リファクタリング
- 📝`docs`: ドキュメント更新
- 🎨`style`: コードスタイル修正(動作に影響なし)
- 🚀`perf`: パフォーマンス改善
- ✅`test`: テスト追加・修正
- 🔧`chore`: ビルと・設定変更

例：
```bash
git commit -m "✨ feat: ユーザー登録APIを追加"
git commit -m "🐛 fix: ログイン時の例外を修正"
git commit -m "📝 docs: Git運用ルールを追加"
```

---

## 📋 Pull Request作成時の確認事項

Pull Request作成前に以下を確認してください。

- [ ] 関連するIssueがある
- [ ] 変更内容が分かるタイトルいなっている
- [ ] 動作確認を行っている
- [ ] 必要なマイグレーションを実行している
- [ ] ドキュメント更新が必要な場合は対応している

---

## ⚠️ 注意事項
- `main`に直接pushしない
- `develop`に直接pushしない
- 大きな変更は小さな単位に分けて作業する
- リリース前にはステージング環境で必ず確認する