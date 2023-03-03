from flask_blog import db
from datetime import datetime

class Entry(db.Model): #db.Modelを継承したクラスは、SQLAlchemy ORMによって自動的にテーブルとして作成されます。
    __tablename__ = 'entries' #テーブルネームとして"entries"と名付けている
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True)
    text = db.Column(db.Text)
    created_at = db.Column(db.DateTime)

    def __init__(self, title=None, text=None):
        self.title = title
        self.text = text
        self.created_at = datetime.utcnow()

    def __repr__(self):
        return '<Entry id:{} title:{} text:{}>'.format(self.id, self.title, self.text)
    
    
#テーブルとは？
#リレーショナルデータベースにおいて、テーブルとはデータを格納するための構造で、行と列から構成されます。行は、テーブルに格納される実際のデータの値を表します。列は、各行に含まれるデータの型や属性を表します。テーブルは、関連するデータを格納するために使用され、一般的には1つのテーブルには同じ種類のデータが含まれます。例えば、ユーザー情報を格納するためのusersテーブル、製品情報を格納するためのproductsテーブルなどがあります。リレーショナルデータベースでは、テーブルを作成するときに、テーブルに含まれる各列の名前とデータ型、およびテーブルに関する制約を指定する必要があります。テーブルに関する制約としては、主キー、外部キー、一意制約、チェック制約などがあります。テーブルは、SQL（Structured Query Language）を使用して操作されます。SQLを使用して、データの挿入、更新、削除、検索などを行うことができます。リレーショナルデータベースは、多くのアプリケーションで使用されており、テーブルを使ったデータの格納と管理が中心的な役割を果たしています。

#このクラスは、テーブルのカラムを表すクラス属性を持ちます。id属性は、テーブルの主キーであり、自動的に生成されます。title属性は、文字列型で、50文字以内のタイトルを表します。text属性は、テキスト型で、記事の本文を表します。created_at属性は、DateTime型で、記事の作成日時を表します。このクラスには、__init__メソッドがあります。これは、エントリーのインスタンスを作成するときに呼び出されます。titleとtextの2つの引数を受け取ります。self.titleとself.textにそれぞれの値が設定されます。self.created_atには、現在の日時が設定されます。


#def __init__(self, title=None, text=None):の説明
#title=Noneとtext=Noneは、Entryクラスのコンストラクタの引数のデフォルト値を指定しています。引数が渡されなかった場合、titleとtextはそれぞれNoneという値が割り当てられます。
#title=Noneとtext=Noneを指定することで、Entryクラスのオブジェクトを作成するときにtitleとtextが必須であるという制約を緩和することができます。

#疑問　 def __repr__(self):return '<Entry id:{} title:{} text:{}>'.format(self.id, self.title, self.text)の結果はどこに表示されるの？


#return '<Entry id:{} title:{} text:{}>'.format(self.id, self.title, self.text)は、Entryクラスのインスタンスを文字列に変換する際に、<Entry id:id title:title text:text>というフォーマットの文字列を返します。ここで、id、title、textはそれぞれEntryクラスのインスタンス変数id、title、textの値に置き換えられます。

#例えば、以下のようにEntryクラスのオブジェクトを作成し、print関数で出力すると、__repr__メソッドで定義された文字列が表示されます。
#entry = Entry(title='Hello', text='World')
#print(entry)
#__repr__メソッドで定義された文字列は、オブジェクトをデバッグするために使われることが多いです。


#db.Integerは、SQLAlchemy ORMが提供する整数型のデータ型です。これは、データベーステーブルの列のデータ型を定義するために使用されます。db.Integerは、整数値を格納するために使用されます。例えば、このコードではid列のデータ型としてdb.Integerを使用しています。また、SQLAlchemy ORMは、Pythonの整数型とデータベースの整数型の間で自動的に変換を行います。

#ブログの記事をデータベースにまとめる場合、プライマリーキーは個々のブログを識別するための番号に当たりますか？

#はい、一般的にブログの記事をデータベースに格納する場合、プライマリーキーは個々のブログ記事を識別するための一意な番号になります。この番号は、通常、データベースが自動的に生成するシーケンシャルなIDまたはGUID（グローバルユニークID）など、一意な値を持つデータ型を使用して実現されます。この番号をプライマリーキーとして使用することで、特定のブログ記事を簡単に識別でき、データベース上での検索や更新、削除などの操作が迅速かつ正確に行えます。また、複数のテーブル間でデータを参照するために、外部キーとしてこの番号を使用することもできます。