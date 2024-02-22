# MS1チャレンジガイド

チャレンジはMS1の重要なコンポーネントであり、チャレンジに取り組むことで学んだことを実際に活用できるようになります。各ユニットの最後に1つまたは複数のチャレンジが用意されています。これまで学んだことにもとづいて取り組んでください。各チャレンジには一連の要件と手順があります。チャレンジの要件にはそのユニット以外で学んだスキルも含まれていることがあるため、カリキュラムに沿ってこれまで学んできたすべてのスキルを組み合わせて問題を解く必要があります。

## チャレンジにアクセスする
各ユニットの最後に、そのユニットの各チャレンジへのアクセス手順が書かれたページがあります。手順のページには、GitHub上のチャレンジリポジトリへのリンクと、リポジトリ内の特定のチャレンジへのパスが記載されています。

一般にリンクの構造は次のようになっています。

`https://github.com/ms1-learner/<学習パス>-<モジュール番号>-<言語>`

たとえば、日本語でC++学習パスを学んでいる場合、次のリンクでモジュール1のすべてのチャレンジにアクセスできます。

`https://github.com/ms1-learner/cpp-01-ja`

手順のページに記載されている次のようなリポジトリのパスをたどると、各チャレンジにアクセスできます。

`01_introduction_to_cpp/01_challenge`

## GitHubアカウントを作成する
> すでにGitHubのアカウントをお持ちの場合は、このセクションをスキップしてかまいません。

チャレンジの解答を提出するために、受講者は各自でGitHubにリモートリポジトリを作成する必要があります。チャレンジのすべての解答をこれらのリポジトリに保存してください。また、インストラクターが解答を確認して採点できるよう、リポジトリにインストラクターを追加してください。

GitHubのアカウント作成は簡単です。はじめに https://github.com/signup にアクセスします。

基本情報の入力を求めるプロンプトが表示されます。基本情報を記入してCAPTCHA (キャプチャ認証) の質問に答えると、次のような画面が表示されます。

![cv](https://github.com/ms1-learner/cpp-01-en/blob/main/assets/challenge-submission-9.png)

完了すると、追加の質問がいくつか表示されます。

![challenge-submission-10](https://github.com/ms1-learner/cpp-01-en/blob/main/assets/challenge-submission-10.png)
最後に、無料プランと有料プランのどちらを使用するかを尋ねられます。解答の提出には無料のアカウントで十分なので、無料プランを選択します。

![challenge-submission-11](https://github.com/ms1-learner/cpp-01-en/blob/main/assets/challenge-submission-11.png)

これでアカウントの作成は完了です。GitHubアカウントのダッシュボードが表示されるはずです。

## ローカルマシンにチャレンジをコピーする
チャレンジを提出するには、親リポジトリに移動してからリポジトリをフォークし、さらにそれをローカルマシンにクローンする必要があります。

例として、リポジトリ `https://github.com/ms1-learner/cpp-01-ja` をフォークしてクローンします。

> GitとGitHubに慣れていなくても心配はいりません。このガイドには必要な手順が詳細に記載されています。GitとGitHubの詳細については、この学習パスに含まれているアジャイル開発モジュールで学びます。

指定されたリンクからリポジトリに移動します。

<img width="1728" alt="Screenshot 2023-11-24 at 12 54 05" src="https://github.com/ms1-learner/cpp-01-ja/assets/5623716/bbc972f0-2905-499a-bdda-1a362073279e">

リポジトリをフォークすると、自分のアカウントのリポジトリにコピーが作成されます。

<img width="1728" alt="Screenshot 2023-11-24 at 13 00 21" src="https://github.com/ms1-learner/cpp-01-ja/assets/5623716/dc3dde94-f3ec-4104-bdbd-9254758c2075">

デフォルト設定のまま進み、[Create fork] をクリックしてフォークします。

<img width="1728" alt="Screenshot 2023-11-24 at 12 54 20" src="https://github.com/ms1-learner/cpp-01-ja/assets/5623716/b49fa800-0580-4b72-9441-4de364bff834">

フォークしたリポジトリのリンクをコピーします。

<img width="1728" alt="Screenshot 2023-11-24 at 13 01 27" src="https://github.com/ms1-learner/cpp-01-ja/assets/5623716/2f034874-5a32-4ff2-a409-ca9592cad344">

パソコンでターミナルを開き、リポジトリのクローン先となるフォルダーに移動します。たとえば、既存のDocumentsフォルダーに移動するには、`cd Documents` と入力してからEnterキーまたはReturnキーを押します。

<img width="990" alt="Screenshot 2023-11-24 at 13 07 44" src="https://github.com/ms1-learner/cpp-01-ja/assets/5623716/cb9da8e6-2ff5-46a0-80d3-383bec80d6f7">

Documentsフォルダーに移動した後、`git clone` に続けて先ほどコピーしたリポジトリのURLを入力し、EnterキーまたはReturnキーを押します。

<img width="990" alt="Screenshot 2023-11-24 at 13 06 35" src="https://github.com/ms1-learner/cpp-01-ja/assets/5623716/42d744a7-cc48-4dd5-8c5e-f568d323f064">

これでDocumentsフォルダーにリポジトリがクローンされるはずです。Visual Studio Codeでこのリポジトリを開きます。

<img width="1840" alt="Screenshot 2023-11-24 at 13 13 54" src="https://github.com/ms1-learner/cpp-01-ja/assets/5623716/331a66ec-963f-4f2f-b8d6-fc4e6e0022ab">

<img width="1840" alt="Screenshot 2023-11-24 at 13 12 07" src="https://github.com/ms1-learner/cpp-01-ja/assets/5623716/03f218d0-915b-4b1c-84a7-58665b63ac61">

このリポジトリ内のフォルダーにすべてのチャレンジが含まれています。これらの各フォルダー名には関連するユニットの名前と番号が付いています。

<img width="1840" alt="Screenshot 2023-11-24 at 13 12 36" src="https://github.com/ms1-learner/cpp-01-ja/assets/5623716/93561841-5464-4535-b1ac-413068d8e791">

これで、チャレンジに解答する準備が整いました。

## チャレンジに取り組んで提出する
チャレンジのREADMEファイルには、説明だけが記載されていることもあれば、一部が欠けている未完成のコードが記載されていることも、解答のベースとなるコードが記載されていることもあります (チャレンジでこれらのコードを完成させていくことになります)。

たとえば、チャレンジで2つの数値を加算するC++プログラムを作成する場合、解答は次のようになります。

> 注: 例として記載しているだけなので、このコードを理解する必要はありません。

```cpp
#include <iostream>
#include <string>

int add(int a,int b) {
   return a + b;
}
int main() {
    std::cout << "The result of adding 5 and 3 is " + std::to_string(add(5,3)) << std::endl;
    return 0;
}
```

このプログラムを `main.cpp` というファイルに保存したものとします。では、この解答をローカルリポジトリに保存してからGitHubにプッシュしましょう。

## 解答を準備して採点用にプッシュする

解答を準備してGitHubリポジトリにプッシュするには、まずこの解答をコミット (`commit`) する必要があります。コミットするには、ターミナルで次のコマンドを実行します。

`git add .`

`git commit -m "Submit challenge for grading"`

1つ目のコマンドでは、この新規ファイルを追跡するようGitに指示しています。2つ目のコマンドでは、“Submit challenge for grading” (採点用にチャレンジを提出) というメッセージを付けて保存しています。

<img width="1840" alt="Screenshot 2023-11-24 at 13 20 19" src="https://github.com/ms1-learner/cpp-01-ja/assets/5623716/365cb8f3-71da-4ec3-ba67-fb96be5aefe5">

解答をリモートリポジトリにプッシュする準備が整いました。

`git push`

<img width="1840" alt="Screenshot 2023-11-24 at 13 20 50" src="https://github.com/ms1-learner/cpp-01-ja/assets/5623716/93cab46a-deb5-410b-80cf-48877cc60935">

次に、GitHubリポジトリに移動します。変更が正常にプッシュされているはずです。

>    GitHubアカウントのユーザー名とパスワードを入力するよう求められ、次のようなエラーが発生することがあります。
>
>   **fatal: Authentication failed for 'https://github.com/ms1-learner/cpp-01-ja.git/'**
>
>   これを解決するには、認証に個人用アクセストークンを使用する必要があります。この手順の詳細は、[GitHubの公式ドキュメント](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic) (英語) に記載されています。

### MS1でリンクを送信する
自分のGitHubリポジトリに解答をプッシュしたら、MS1のチャレンジでそのGitHubへのリンクを送信する必要があります。リポジトリへのリンクではなく、該当するチャレンジへのリンクを送信してください。

例: `https://github.com/abolinsky/cpp-01-ja/tree/main/01_introduction_to_cpp/01_challenge`

MS1の該当するチャレンジページに移動します。

自分のGitHubリポジトリへのリンクをページの下部に追加して [提出] をクリックしてください。

<img width="1840" alt="Screenshot 2023-11-29 at 14 42 44" src="https://github.com/ms1-learner/cpp-01-ja/assets/5623716/9201986a-f035-4bb3-8919-942d91dfb308">

### 自分のリポジトリにインストラクターを追加する
インストラクターが解答を確認して採点できるよう、インストラクターをコラボレーターとしてGitHubリポジトリに追加する必要があります。

コラボレーターを追加するには、[Settings] ボタンをクリックします。

<img width="1840" alt="Screenshot 2023-11-29 at 14 45 52" src="https://github.com/ms1-learner/cpp-01-ja/assets/5623716/0eabba29-8340-4d71-8984-a8778e6325f1">

左側のパネルにある [Collaborators] をクリックします。 

[Manage access] にある [Add people] をクリックし、担当インストラクターのGitHubのユーザー名またはメールアドレスを追加します。

<img width="1840" alt="Screenshot 2023-11-29 at 14 46 00" src="https://github.com/ms1-learner/cpp-01-ja/assets/5623716/3d0871c9-2b66-4cfe-9627-270e304aeef5">

これで解答がアップロードされ、インストラクターが確認できるようになりました。

すばらしい解答を期待しています。
