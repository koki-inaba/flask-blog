from flask import request,redirect,url_for,render_template,flash,session

from flask_blog import app #__init__.pyで作成したappという変数をインポートしている

#このコードは、PythonのFlaskフレームワークを使用したWebアプリケーションの開発において、flask_blogという名前のパッケージまたはモジュールからappという名前の変数をインポートしています。具体的には、from flask_blogは、Pythonのモジュール検索パスの中でflask_blogという名前のパッケージまたはモジュールを探し、見つかった場合にはその中にあるコードを実行します。次に、import appは、flask_blogパッケージまたはモジュールの中にあるappという名前のオブジェクトをインポートします。この場合、appはFlaskのインスタンスを表していることが多いです。

#flask_blogはディレクトリ名ですか？はい、flask_blogはディレクトリ名として使用されることがあります。Pythonでは、ディレクトリはパッケージとして扱われ、その中にあるモジュールをインポートすることができます

@app.route('/')
def show_entries():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("entries/index.html")

#@app.routeはFlaskで使用されるデコレータの1つで、URLを関数にマッピングするために使用されます。つまり、特定のURLにアクセスした場合に実行される関数を指定するために使用されます。@app.routeデコレータを使用することで、Flaskアプリケーション内の関数を特定のURLにマッピングできます。

#render_template() 関数は、Flask web フレームワークで使用される、テンプレートをレンダリングするための関数です。この関数を使用することで、テンプレート内に動的なデータを挿入して、動的なWebページを生成することができます。render_template() 関数は、2つの引数を受け取ります。最初の引数は、レンダリングするテンプレートのファイル名で、通常は文字列として指定します。2番目の引数は、テンプレート内で使用するために渡すPythonオブジェクトです

#「レンダリング」とは、コンピューターグラフィックスやWebページなどを生成するためのプロセスのことを指します。一般的に、レンダリングは、コンピューターが入力データ（画像、テキスト、音声、ビデオなど）を取り込み、それを加工して出力データ（表示される画像やWebページ）を生成することを意味します。Flaskの render_template() 関数において、レンダリングとは、テンプレートエンジンがHTMLやCSS、JavaScriptなどのテンプレートファイルを取り込んで、Pythonコードに埋め込まれた動的なデータを組み込んでHTMLを生成することを指します。つまり、render_template() 関数は、Pythonオブジェクトに基づいて、動的なWebページを生成するために、テンプレートファイルとデータを組み合わせるプロセスを行っています。このようなレンダリングのプロセスにより、Web開発者は、Pythonでデータを処理して、それをHTMLとして表示することができるようになります。また、テンプレートエンジンを使用することで、HTMLの作成や修正をより簡単に行うことができます。

@app.route("/login",methods = ["GET","POST"]) #p82参照　「ゼロからFLASKがよくわかる本」

def login():
    if request.method == "POST":
        if request.form["username"] != app.config["USERNAME"]:
            flash("ユーザー名が異なります")
        elif request.form["password"] != app.config["PASSWORD"]:
            flash("パスワードが異なります")
        else:
            session["logged_in"] = True
            flash("ログインしました")
            return redirect(url_for("show_entries"))
    return render_template("login.html")

@app.route("/logout")

def logout():
    session.pop("logged_in",None)
    flash("ログアウトしました")
    return redirect(url_for("show_entries"))


#リダイレクト（Redirect）は、Webページの移動方法の1つで、ユーザーを自動的に別のWebページに転送する方法です。リダイレクトは、HTTPヘッダーを使用してブラウザに転送先のURLを伝えることで実現されます。Webアプリケーションでは、リダイレクトはよく使用されます。例えば、ログイン後にユーザーをダッシュボードページにリダイレクトするなどです。リダイレクトを使用することで、ユーザーの操作をスムーズに行うことができます。Flaskにおいて、リダイレクトはredirect()関数を使用することで実現できます。redirect()関数には、リダイレクト先のURLを引数として渡します。

#redirect('/')は、Flaskで提供されるredirect()関数を使用して、ルートURLにリダイレクトすることを示しています。'/'は、ルートURLを示しています。つまり、アプリケーションのホームページを指します。例えば、http://example.com/やhttp://localhost:5000/などのようになります。したがって、redirect('/')は、アプリケーションのホームページにユーザーをリダイレクトすることを意味します。このコードは、ログアウト機能が実行された場合に、ユーザーをアプリケーションのホームページにリダイレクトすることを示しています。

#@app.route('/')で指定されたURLパスは、ルートURL(/)を指します。つまり、WebアプリケーションのホームページのURLパスを指します。このURLパスは、WebブラウザでWebアプリケーションのURLを入力する際に、最初に表示されるページを指します。例えば、http://example.com/やhttp://localhost:5000/などのURLがある場合、/はWebアプリケーションのホームページを表し、@app.route('/')で指定されたURLパスとして扱われます。

#以下はif not session.get("logged_in"):return redirect("/login")の解説
#このコードはPythonのWebフレームワークであるFlaskを使用している場合に、ユーザーがログインしていない場合に/loginページにリダイレクトする機能を実装しています。以下はこのコードの詳細な解説です。session.get("logged_in"): Flaskアプリケーションには、HTTPセッションと呼ばれる機能があり、ユーザーの状態を保存することができます。session.get(key)は、keyに対応する値をセッションから取得します。この場合、logged_inというキーに対応する値があるかどうかを確認しています。if not session.get("logged_in"):: もしlogged_inの値がFalseやNoneなどのfalsyな値であれば、つまりユーザーがログインしていない状態であれば、以下の処理が実行されます。return redirect("/login"): Flaskのredirect()関数は、指定したURLにリダイレクトします。この場合、/loginページにリダイレクトするように指定されています。つまり、このコードはユーザーがログインしていない場合に、/loginページにリダイレクトするようになっています。このような機能は、Webアプリケーションにおいてセキュリティ上非常に重要な機能の一つです。

# 以下はsession["loogged_in"] = Trueの解説
#このコードは、sessionという変数にlogged_inというキーを持つブール値(True or False)を設定しています。このセッションは、Flaskアプリケーションが特定のユーザーに関する情報を保存するために使用される、Webアプリケーションのセッション機能を利用したものです。このようにセッションを使用することで、ユーザーがWebアプリケーションを使用している間に、アプリケーションに関する情報を保持することができます。セッションは、ユーザーの情報を保持するだけでなく、アプリケーションにとって重要な情報を格納することもできます。例えば、ユーザーがログインしているかどうかを示す情報をセッションに保存することができます。

#つまり、session["loogged_in"] = Trueで設定した、logged_inというキーを持つブール値(今回はTrue)がログインできていた場合は生成されるので、その値がない、つまりログインできていない状態の時にログイン画面に遷移させるのがif not session.get("logged_in"):return redirect("/login")のコードということ。

#この場合、sessionは辞書になりますか？ はい、多くのWebフレームワークでは、セッション情報を扱うために辞書を用いています。Pythonにおいても、セッション情報を辞書として表現することが一般的です。例えば、Flaskでは、セッション情報を保存するために、sessionという名前の辞書を使用します。この辞書には、各ユーザーごとに個別のセッション情報が保存されます。セッション情報を辞書として扱うことで、セッションに関連する情報を簡単に取得したり、セッションの有効期限を管理したりすることができます。

#session.pop("logged_in", None) は、セッション辞書から "logged_in" キーを削除します。もしセッション辞書に "logged_in" キーが存在しない場合は何も起こりません。つまり、ログアウトした時にセッション辞書の中身を削除するということ。もう一度ログインした時にsession["loogged_in"] = Trueでまた生成される。

#このコードにおけるflash()は、Flaskアプリケーションのフラッシュメッセージシステムを使用するための関数です。フラッシュメッセージは、Webページの操作結果や情報をユーザーに伝えるために使用されます。flash()関数は、引数で渡されたメッセージをフラッシュメッセージとして保存し、フラッシュメッセージを表示するためのテンプレート側の処理に使われます。

#flash()関数に入れたメッセージは、htmlのget_flashed_messages()関数に入れられ、ユーザーに表示される。

#url_for関数は、引数として指定された関数の名前を使用して、その関数に対応するURLを生成します。return redirect(url_for("login"))の場合は、login関数に対応するurlを生成している。