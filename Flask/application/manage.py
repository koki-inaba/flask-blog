from flask_script import Manager

from flask_blog import app

from flask_blog.scripts.db import InitDB

if __name__ == "__main__":
    manager = Manager(app)
    manager.add_command("init_db",InitDB())
    manager.run()
    
    
#flask_scriptパッケージは、Flaskアプリケーションに対してコマンドラインから操作を行うことができるようにするための拡張機能です。例えば、flask_scriptを使うと、以下のような操作が可能になります。

#python app.py init_db: InitDBコマンドを実行して、データベースを初期化する
#python app.py runserver: アプリケーションを起動する

#manager = Manager(app)は、flask_scriptパッケージのManagerクラスを初期化し、appを引数に渡しています。これにより、ManagerオブジェクトがFlaskアプリケーションと紐付けられます。

#次に、manager.add_command("init_db",InitDB())によって、InitDBコマンドがinit_dbという名前で登録されます。

#最後に、manager.run()によって、コマンドラインから渡されたコマンド（例えば、init_dbなど）を実行するようにManagerオブジェクトが指示されます。

#manager = Manager(app)は、appとManagerクラスを連携させるためのコードですか？
#はい、その通りです。manager = Manager(app)は、flask_scriptパッケージのManagerクラスを初期化し、appを引数に渡して、両者を紐付けるためのコードです。これにより、FlaskアプリケーションをManagerオブジェクトに関連付けて、flask_scriptを使ったコマンドの実行が可能になります。

#なぜappとManagerクラスを連携させる必要があるのですか？
#FlaskアプリケーションとFlask-ScriptのManagerクラスを結びつけることで、アプリケーション内で定義されたカスタムコマンドをFlask-Scriptを使って実行できるようになります。具体的には、manager.add_command()メソッドを使って、Flaskアプリケーションで定義されたカスタムコマンドを追加することができます。例えば、上記のコードでは、"init_db"というカスタムコマンドを定義しています。このコマンドを実行すると、InitDBクラスのrun()メソッドが呼び出され、データベースを初期化する処理が実行されます。このように、Flask-Scriptを使うことで、アプリケーション内のカスタムコマンドを簡単に定義して、実行できるようになります。