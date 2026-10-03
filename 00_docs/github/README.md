# GitHubにリポジトリをpushする手順（Git・GitHub初学者向け）

クラウドサービスへのデプロイは、多くの場合「GitHubのリポジトリと連携する」形で行います。ここでは、Git・GitHubを初めて使う人向けに、基本の考え方からローカルのプロジェクトをGitHubにpushするまでを説明します。後半では、複数人での共同作業や個人開発でも役立つ**ブランチ運用・Pull Request・変更の取り消し・SSH鍵認証**にも触れます。

## 目次

1. [GitとGitHubの違い](#1-gitとgithubの違い)
2. [基本用語](#2-基本用語)
3. [Gitの初期設定](#3-gitの初期設定パソコンごとに最初の1回だけ)
4. [ローカルでの基本的な流れ](#4-ローカルでの基本的な流れ)
5. [コミットしてはいけないファイルを除外する](#5-コミットしてはいけないファイルを除外するgitignore)
6. [GitHubでアカウントを作り、空のリポジトリを作成する](#6-githubでアカウントを作り空のリポジトリを作成する)
7. [ローカルのリポジトリとGitHubを繋いでpushする](#7-ローカルのリポジトリとgithubを繋いでpushする)
8. [2回目以降：変更を反映する](#8-2回目以降変更を反映する)
9. [ブランチを使った作業](#9-ブランチを使った作業)
10. [Pull Requestを出す](#10-pull-requestを出す)
11. [変更を取り消す](#11-変更を取り消す)
12. [SSH鍵で認証する](#12-ssh鍵で認証する)
13. [ghコマンド（GitHub CLI）を使う](#13-ghコマンドgithub-cliを使う)

---

## 用意したファイル

```
00_docs/github/
└── example/
    └── .gitignore   Flask学習プロジェクト向けの.gitignoreサンプル
```

---

## 1. GitとGitHubの違い

名前が似ていますが、役割が違う別々のものです。

| | 役割 |
|---|---|
| **Git** | ファイルの変更履歴を記録・管理する**ツール**（自分のパソコンの中だけで完結する） |
| **GitHub** | Gitのリポジトリ（後述）をインターネット上に保管し、他の人と共有できるようにする**サービス**（Webサイト） |

例えるなら、Gitは「変更履歴を保存できる高機能なフォルダ」、GitHubは「そのフォルダをアップロードしておける倉庫」です。Gitだけでも自分のパソコン内でバージョン管理はできますが、他の人と共有したり、別の場所（クラウドサービスなど）から参照したりするためにGitHubを使います。

## 2. 基本用語

| 用語 | 意味 |
|---|---|
| リポジトリ（repository） | 変更履歴ごと管理されているプロジェクトのフォルダ |
| コミット（commit） | 「この時点の変更内容」を記録するスナップショット。こまめに作る |
| ステージング（staging） | 「次のコミットに含めるファイル」を選んでおく場所 |
| リモート（remote） | 手元のリポジトリと紐づけた、GitHub上などにあるリポジトリの参照先 |
| ブランチ（branch） | 作業の分岐。特に指示がなければ`main`という名前のブランチを使う |
| push | 手元のコミットをリモート（GitHubなど）に送ること |
| pull / clone | リモートの内容を手元に持ってくること（`clone`は新規に丸ごとコピー、`pull`は既存リポジトリへの反映） |
| マージ（merge） | 別のブランチでの変更を、今いるブランチに取り込むこと |
| Pull Request（PR） | 「このブランチの変更をmainに取り込んでほしい」とGitHub上で提案し、レビュー・議論してからマージする仕組み |

## 3. Gitの初期設定（パソコンごとに最初の1回だけ）

まずGitがインストールされているか確認します。

```bash
git --version
```

バージョンが表示されればインストール済みです。表示されない場合は[公式サイト](https://git-scm.com/)からインストールしてください。

次に、コミットに記録される名前とメールアドレスを設定します（これはコミットの「作者情報」として記録されるもので、GitHubへのログイン情報とは別物です）。

```bash
git config --global user.name "あなたの名前"
git config --global user.email "your-email@example.com"
```

`--global`を付けると、このパソコン上のすべてのリポジトリで共通の設定になります。一度設定すれば、以降のプロジェクトで毎回設定し直す必要はありません。

## 4. ローカルでの基本的な流れ

GitHubに触れる前に、Git単体での基本の流れを押さえます。ファイルの状態は次の3段階で管理されています。

```
作業ディレクトリ  --git add-->  ステージング  --git commit-->  リポジトリ（コミット履歴）
（普段編集する場所）           （次のコミットの準備）          （確定した変更履歴）
```

| コマンド | 説明 |
|---|---|
| `git init` | 今いるフォルダをGitで管理し始める（最初の1回だけ） |
| `git status` | 今どのファイルが変更されている・ステージングされているかを確認する（迷ったらまずこれ） |
| `git add <ファイル名>` / `git add .` | 変更したファイルをステージングに追加する（`.`はカレントディレクトリ以下すべて） |
| `git commit -m "変更内容"` | ステージングした内容を1つの記録（コミット）として確定する |
| `git log` / `git log --oneline` | これまでのコミット履歴を確認する（`--oneline`は1コミット1行の簡易表示） |
| `git diff` | まだステージングしていない変更の差分を確認する |

```bash
cd プロジェクトのフォルダ
git init                        # このフォルダをGit管理下にする（最初の1回だけ）
git status                      # 状態を確認（すべて「Untracked files」と表示されるはず）
git add .                       # すべての変更をステージングに追加
git commit -m "Initial commit"  # 最初のコミットを作成
```

`git commit -m "..."` の`"..."`の部分は**コミットメッセージ**と呼ばれ、「何を変更したか」を短くまとめた説明文です。後で履歴を見返すときの手がかりになるので、`"fix"`のような曖昧な文言ではなく、内容が分かるように書く習慣をつけましょう。

## 5. コミットしてはいけないファイルを除外する（.gitignore）

DBファイルやキャッシュなど、環境ごとに生成される・人によって内容が変わるファイルはコミットしません。リポジトリ直下に`.gitignore`というファイルを作り、除外したいパターンを書きます。

> [example/.gitignore](example/.gitignore)

```
__pycache__/
*.pyc
*.pyo
*.db
*.sqlite
*.sqlite3
instance/
migrations/
.pytest_cache/
.env
```

```bash
cp 00_docs/github/example/.gitignore .gitignore
```

| パターン | 除外する理由 |
|---|---|
| `__pycache__/` / `*.pyc` / `*.pyo` | Pythonが自動生成するキャッシュファイル。実行するたびに再生成されるためコミット不要 |
| `*.db` / `*.sqlite` / `*.sqlite3` / `instance/` | SQLiteのDBファイル。各自の手元データであり、他人の環境に持ち込むべきではない |
| `migrations/` | `flask db init`で生成されるマイグレーション管理フォルダ。各自の手元で生成する前提のファイルであり、環境ごとに内容が変わりうるためリポジトリには含めない |
| `.env` | `SECRET_KEY`など、秘密情報を書く可能性のあるファイル |

`.gitignore`に書いたファイルは`git status`にも`git add .`にも出てこなくなります。

**注意**：すでにコミットしてしまったファイルは、後から`.gitignore`に追加しても追跡が止まりません。誤ってコミットしていた場合は次のコマンドで追跡から外します（ファイル自体は手元に残ります）。

```bash
git rm -r --cached instance migrations
```

## 6. GitHubでアカウントを作り、空のリポジトリを作成する

1. [GitHub](https://github.com/)にアクセスし、アカウントを作成（すでにお持ちならログイン）する
2. 右上の **+** → **New repository** を選ぶ
3. リポジトリ名を入力する（例: `my-flask-app`）
4. **Public**（誰でも見られる）か**Private**（自分だけ）かを選ぶ。学習用なら公開してよければPublicで問題ありません
5. **README・.gitignore・LICENSEは追加しない**（チェックを入れない）。すでに手元にあるプロジェクトをpushする場合、GitHub側で先にこれらを作ってしまうと、手元の履歴とぶつかる原因になります
6. **Create repository** をクリックする

作成が終わると、`https://github.com/<ユーザー名>/<リポジトリ名>.git` のようなURLが発行された画面が表示されます。このURLは次の手順で使うので控えておきます。

## 7. ローカルのリポジトリとGitHubを繋いでpushする

「4. ローカルでの基本的な流れ」まで終わっている（`git init`してコミット済み）前提で進めます。

```bash
git remote add origin https://github.com/<ユーザー名>/<リポジトリ名>.git
git branch -M main
git push -u origin main
```

| コマンド | 説明 |
|---|---|
| `git remote add origin <URL>` | 手元のリポジトリに「origin」という名前でGitHub上のリポジトリを紐づける（`origin`は慣習的に使われる名前） |
| `git branch -M main` | 現在のブランチ名を`main`に変更する（デフォルトブランチ名を統一する） |
| `git push -u origin main` | `main`ブランチをGitHubにpushする。`-u`を付けると、以降は`git push`だけでこの紐づけ先にpushできるようになる |

```
[作業ディレクトリ] -- add --> [ステージング] -- commit --> [手元のリポジトリ]
                                                                    |
                                                                  push
                                                                    ↓
                                                        [GitHub上のリポジトリ (origin)]
```

pushが終わったら、GitHub上のリポジトリページを再読み込みしてファイル一覧が反映されているか確認してください。

### すでにリモートが設定されているか確認する

このリポジトリのように、すでに誰か（または過去の自分）が`git remote add`を済ませている場合もあります。

```bash
git remote -v
```

`origin`が表示されればすでに連携済みです。その場合は`git remote add`をやり直す必要はなく、2回目以降と同じ手順で進められます。

## 8. 2回目以降：変更を反映する

最初のpushが終わったら、以降はファイルを変更するたびに次の3つを繰り返すだけです。

```bash
git status                    # 何が変更されたか確認（習慣にすると安心）
git add .
git commit -m "変更内容の説明"
git push
```

---

## 9. ブランチを使った作業

ここまでは`main`ブランチに直接コミットしてきましたが、新機能の開発や実験的な変更は**別のブランチ**で行い、完成してから`main`に取り込むのが一般的です。`main`を常に「動く状態」に保てるのが利点です。

```bash
git switch -c feature/add-search   # 新しいブランチを作って切り替える
# ここでファイルを編集する
git add .
git commit -m "検索機能を追加"
git push -u origin feature/add-search   # このブランチをGitHubにも送る
```

| コマンド | 説明 |
|---|---|
| `git switch -c <ブランチ名>` | 新しいブランチを作成し、そのブランチに切り替える（`git checkout -b <ブランチ名>`と同じ意味の新しい書き方） |
| `git switch <ブランチ名>` | 既存のブランチに切り替える（`main`に戻るときも使う） |
| `git branch` | ローカルに存在するブランチの一覧を表示する（`*`が付いているのが現在のブランチ） |
| `git push -u origin <ブランチ名>` | 新しいブランチを初めてGitHubに送るとき。以降は`git push`だけでよい |

ブランチ名は`feature/xxx`（新機能）・`fix/xxx`（修正）のように、何のための変更かが分かる名前を付けると、後から履歴を見返しやすくなります。

### 動作確認

| 確認する操作 | 確認したいこと |
|---|---|
| `git switch -c feature/example`の直後に`git branch` | `main`と`feature/example`の両方が表示され、`feature/example`の方に`*`が付いている |
| `git switch main`で`main`に戻る | ブランチで行った編集内容が（コミットしていなければ）見えなくなる。`git switch feature/example`で戻ると再び見える |

## 10. Pull Requestを出す

ブランチをGitHubにpushしただけでは、まだ`main`には反映されません。**Pull Request（PR）**を作成し、「この変更をmainに取り込んでほしい」と提案する形を取ります。1人で開発している場合でも、変更内容を見直す・記録に残すという点でPRを使う価値があります。

1. `git push -u origin feature/add-search`を実行すると、GitHubのリポジトリページに「Compare & pull request」というボタンが表示される（表示されない場合はリポジトリページの**Pull requests**タブ→**New pull request**から作成する）
2. タイトルと説明を書く（何を・なぜ変更したか）
3. **Create pull request** をクリックする
4. 内容を確認し、問題なければ **Merge pull request** で`main`に取り込む
5. マージ後、GitHub上で不要になったブランチを削除してよい（**Delete branch**ボタン）

マージが終わったら、手元の`main`にも反映させます。

```bash
git switch main
git pull
```

| 用語 | 意味 |
|---|---|
| Base branch | 取り込み先のブランチ（通常`main`） |
| Compare branch | 変更内容を持っているブランチ（今回の`feature/add-search`） |
| レビュー | 他の人（または未来の自分）がPRの差分を読んで、コメントを付けたり承認したりすること |
| マージ方法（Merge / Squash and merge / Rebase and merge） | GitHubのマージボタンには3種類あり、「Squash and merge」を選ぶとブランチ内の複数コミットが1つにまとめられて履歴が読みやすくなる。迷ったら「Squash and merge」でよい |

### 動作確認

| 確認する操作 | 確認したいこと |
|---|---|
| ブランチをpushした直後にGitHubのリポジトリページを開く | 「Compare & pull request」ボタンが表示されている |
| PRを作成する | 差分（Files changedタブ）に、そのブランチで変更したファイルだけが表示される |
| マージ後に手元で`git switch main && git pull` | PRで加えた変更が手元の`main`にも反映されている |

## 11. 変更を取り消す

作業中に「間違えた」「やっぱり元に戻したい」という場面はよくあります。状況に応じて使うコマンドが変わります。

| やりたいこと | コマンド | 説明 |
|---|---|---|
| 編集したがまだ`git add`していない変更を取り消す | `git restore <ファイル名>` | ファイルを直前のコミットの状態に戻す（**この変更は失われる**） |
| `git add`した内容をステージングから外す（変更自体は残す） | `git restore --staged <ファイル名>` | 「コミットに含める予定」から外すだけで、編集内容は手元に残る |
| 直前のコミットのメッセージや内容を修正する | `git commit --amend` | 直前のコミットをやり直す。**まだpushしていないコミットにだけ使う**（pushした後に使うと、他の人の手元の履歴とズレて混乱の元になる） |
| すでにpushしたコミットを打ち消したい | `git revert <コミットのハッシュ>` | 指定したコミットの内容を打ち消す、**新しいコミットを追加する**。履歴を書き換えないので、共同作業でも安全に使える |

```bash
git log --oneline           # 取り消したいコミットのハッシュ（例: a1b2c3d）を確認する
git revert a1b2c3d          # そのコミットの変更を打ち消す新しいコミットを作る
```

**注意（`git reset --hard`について）**：Web検索すると`git reset --hard`というコマンドもよく紹介されますが、これは**コミット自体を消してしまう**強力なコマンドです。一度実行すると元に戻すのが難しく、特にpush済みの履歴に対して使うと事故につながりやすいため、このカリキュラムでは扱いません。「元に戻したい」ときは、まず`git restore`（コミット前）か`git revert`（コミット後）を検討してください。

## 12. SSH鍵で認証する

GitHubへの`push`では、ユーザー名とパスワードの代わりに[Personal Access Token](https://docs.github.com/ja/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)を使う方法（HTTPS方式）が基本ですが、毎回入力するのは手間です。**SSH鍵**を使うと、一度設定するだけでパスワード入力なしに`push`/`pull`できるようになります。

```bash
ssh-keygen -t ed25519 -C "your-email@example.com"
```

質問にはすべてEnter（デフォルトのまま）で進めて構いません。`~/.ssh/id_ed25519`（秘密鍵）と`~/.ssh/id_ed25519.pub`（公開鍵）の2つのファイルが作られます。

```bash
cat ~/.ssh/id_ed25519.pub
```

表示された内容（`ssh-ed25519 AAAA...`から始まる1行）をコピーします。

1. GitHubの右上アイコン→**Settings**→左メニューの**SSH and GPG keys**を開く
2. **New SSH key**をクリックし、Titleに分かりやすい名前（例：自分のパソコン名）、Keyの欄に先ほどコピーした内容を貼り付けて**Add SSH key**

設定できたか確認します。

```bash
ssh -T git@github.com
```

`Hi <ユーザー名>! You've successfully authenticated...`のようなメッセージが出れば成功です。最後に、リポジトリのリモートURLをHTTPSからSSH方式に変更します。

```bash
git remote set-url origin git@github.com:<ユーザー名>/<リポジトリ名>.git
git remote -v
```

| 項目 | 説明 |
|---|---|
| `ssh-keygen -t ed25519` | 鍵の種類として`ed25519`（近年推奨される方式）を指定して鍵ペアを生成する |
| 秘密鍵（`id_ed25519`） | **絶対に他人に渡さない**。このパソコンだけに置いておく |
| 公開鍵（`id_ed25519.pub`） | GitHubに登録する側の鍵。名前の通り公開しても問題ない |
| `git remote set-url` | 一度作ったリモートのURLを、HTTPS方式からSSH方式（`git@github.com:...`）に変更する |

### 動作確認

| 確認する操作 | 確認したいこと |
|---|---|
| `ssh -T git@github.com` | `successfully authenticated`のメッセージが表示される（`Permission denied`の場合は公開鍵の登録内容を確認する） |
| `git remote -v` | `origin`のURLが`git@github.com:...`（SSH形式）に変わっている |
| `git push` | パスワードやトークンの入力を求められずにpushできる |

## 13. ghコマンド（GitHub CLI）を使う

ここまでの「6. リポジトリ作成」「10. Pull Request」はブラウザ操作で行ってきましたが、GitHub公式のCLIツール**`gh`**を使うと、ターミナルを離れずに同じ操作ができます。慣れてくると、ブラウザとターミナルを行き来する手間が減って作業が速くなります。

```bash
# Mac（Homebrew）の場合
brew install gh
```

Windows/Linuxの場合は[公式のインストール手順](https://github.com/cli/cli#installation)を参照してください。

```bash
gh auth login
```

対話形式で「GitHub.com」「HTTPS or SSH」「ブラウザで認証 or トークンを貼り付け」を選んでいくと、ブラウザが自動で開いて認証コードの入力を求められます。これだけで、「6. GitHubでアカウントを作り〜」以降で必要だったPersonal Access TokenやSSH鍵の手動設定（[12. SSH鍵で認証する](#12-ssh鍵で認証する)）を`gh`に任せることもできます。

### リポジトリ作成からpushまでを1コマンドで

```bash
gh repo create my-flask-app --public --source=. --remote=origin --push
```

`git init`してコミット済みのフォルダの中でこれを実行すると、「6. GitHubでアカウントを作り、空のリポジトリを作成する」〜「7. ローカルのリポジトリとGitHubを繋いでpushする」で行った、GitHub上でのリポジトリ作成・`git remote add`・`git push`が一度に完了します。

### Pull Requestをターミナルから作る

```bash
gh pr create --fill
```

現在のブランチから、直前のコミットメッセージを使ってPRを作成します（`--fill`を付けない場合はタイトル・本文を対話形式で入力する）。「10. Pull Requestを出す」の手順1〜3をこのコマンド1つで済ませられます。

```bash
gh pr view --web    # 作成したPRをブラウザで開いて確認する
gh pr checkout 12   # 他の人が作ったPR番号12をローカルに取り込んで動作確認する
gh pr merge          # PRをマージする（対話形式でMerge/Squash/Rebaseを選べる）
```

### ポイント

| コマンド | 説明 |
|---|---|
| `gh auth login` | GitHubへの認証をまとめて行う。以降のコマンドはこの認証情報を使う |
| `gh repo create <名前> --source=. --push` | 今いるフォルダをそのままGitHub上の新規リポジトリにし、pushまで行う |
| `gh pr create` | 現在のブランチから、そのブランチとの差分でPRを作成する |
| `gh pr checkout <番号>` | 他の人（または自分の別のブランチ）が作ったPRを、ローカルのブランチとしてチェックアウトする。動作確認やレビューに便利 |
| `gh pr merge` | PRをマージする。ブラウザを開かずに完結できる |

### 動作確認

| 確認する操作 | 確認したいこと |
|---|---|
| `gh auth status` | ログイン済みのアカウント名が表示される |
| `gh repo create ... --push`を実行 | GitHub上に新しいリポジトリが作成され、`git remote -v`で`origin`が設定されていることも確認できる |
| `gh pr create --fill`のあと`gh pr view --web` | ブラウザで、先ほど作成したPRのページが開く |

`gh`はあくまでブラウザ操作の代わりとなる**便利ツール**です。まずは1〜12の手順でブラウザ操作の流れそのものを理解し、慣れてきたら`gh`で置き換えていくとよいでしょう。

---

## トラブルシューティング

| 症状 | 原因・対処 |
|---|---|
| `git: command not found` | Gitがインストールされていない。[公式サイト](https://git-scm.com/)からインストールする |
| `fatal: not a git repository` | `git init`していないフォルダでコマンドを実行している。プロジェクトのフォルダに移動してから`git init`する |
| `fatal: remote origin already exists` | すでに`origin`という名前でリモートが設定されている。`git remote -v`で確認し、URLを変更したい場合は`git remote set-url origin <新しいURL>`を使う |
| `Updates were rejected because the remote contains work that you do not have locally` | GitHub側にローカルに無いコミット（README生成など）がある。`git pull origin main --allow-unrelated-histories`で取り込んでからpushし直す |
| pushしたのに`instance/`や`*.sqlite`がGitHub上に見える | `.gitignore`を追加する前にコミットしてしまっている。「5. コミットしてはいけないファイルを除外する」の`git rm -r --cached`で追跡を外してから再度コミット・pushする |
| GitHubへのpushでユーザー名・パスワードを求められて失敗する | GitHubはパスワード認証を廃止済み。[Personal Access Token](https://docs.github.com/ja/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)を発行してパスワード欄に使うか、[SSH鍵での認証](#12-ssh鍵で認証する)に切り替える |
| PRの「Merge」ボタンが押せない（グレーアウトしている） | `main`側で先に加えられた変更とコンフリクト（衝突）している可能性がある。GitHub上の案内、または手元で`git switch main && git pull && git switch feature/xxx && git merge main`でコンフリクトを解消してからpushし直す |
| `git revert`したのにファイルの中身が変わらない | `git revert`は新しいコミットを作るだけなので、`git pull`していない・違うブランチで確認しているなど、実際に見ているファイルが最新の状態になっているか確認する |
| `gh: command not found` | GitHub CLIがインストールされていない。`brew install gh`（Mac）または[公式のインストール手順](https://github.com/cli/cli#installation)を参照する |
| `gh`のコマンドで`To get started with GitHub CLI, please run: gh auth login`と出る | 認証がまだ済んでいない。`gh auth login`を実行してから再度試す |
| `gh auth login`でブラウザが自動で開かない | 表示された認証コードとURLを手動でブラウザに入力すれば認証できる |
