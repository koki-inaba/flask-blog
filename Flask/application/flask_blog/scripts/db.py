from flask_script import Command
from flask_blog import db

class InitDB(Command):
    "create database"
    
    def run(self):
        db.create_all()
        
        
#db.create_all()は、SQLAlchemyを使用してFlaskアプリケーションのデータベースにテーブルを作成するメソッドです。このメソッドを呼び出すと、Flaskアプリケーションに登録されている全てのモデルに基づいて、データベース内にテーブルが作成されます。

#具体的には、Flask SQLAlchemyでは、モデルクラスがテーブルを定義するために、db.Modelを継承する必要があります。db.create_all()を呼び出すことによって、すべての継承されたdb.Modelのサブクラスが検出され、それぞれのテーブルがデータベースに作成されます。

#テーブルを作成するために一回だけ実行すればおけ