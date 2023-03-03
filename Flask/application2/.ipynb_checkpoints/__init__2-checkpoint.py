from flask import Flask #Flaskのインポート

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) 

db = SQLAlchemy(app)

#app変数は、Flaskアプリケーションのインスタンスを表しています。このインスタンスを生成することで、Flaskアプリケーションを構築し、ルートURLやエンドポイントを定義し、HTTPリクエストに対するレスポンスを返すことができます。Flaskクラスのコンストラクタには、アプリケーション名や設定を渡すことができますが、通常は__name__を渡します。これにより、Flaskがアプリケーションのルートディレクトリを決定するために必要な情報を提供することができます。app変数には、Flaskアプリケーションのインスタンスが格納されます。このインスタンスは、Flaskアプリケーションを実行するために使用されます。app.run()メソッドを呼び出すことで、Flaskが内蔵するWebサーバーが起動し、アプリケーションがリクエストを受け取り、レスポンスを返すことができます。

#つまり、app = Flask(__name__) を書くことで、これからFlaskアプリを実行するということを宣言している

import flask_blog.views

#flask_blogディレクトリの中のviewsモジュールをインポートする

app.config.from_object("flask_blog.config")

#app.config.from_objectは、Flaskアプリケーションの設定をオブジェクトから読み込むためのメソッドです。このメソッドは、引数に渡されたオブジェクトから設定を読み込み、アプリケーションの構成を変更します。

#app.configは、Flaskアプリケーションの設定を格納するための辞書のようなオブジェクトです。このオブジェクトには、Flaskアプリケーションの動作を制御するための様々な設定が含まれています。例えば、app.config['DEBUG'] = Trueのようにして、アプリケーションのデバッグモードを有効にすることができます。また、app.config['SECRET_KEY']には、アプリケーションで使用される秘密鍵を設定することができます。他にも、データベースの接続情報やテンプレートの配置など、アプリケーションの動作に関する多くの設定があります。Flaskでは、app.configに直接設定を格納することができますが、一般的には、外部のファイルや環境変数などから設定を読み込むことが推奨されています。app.config.from_object()、app.config.from_pyfile()、app.config.from_envvar()などのメソッドを使用して、外部の設定をアプリケーションに読み込むことができます。