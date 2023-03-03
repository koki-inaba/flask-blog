from flask import Flask
app = Flask(__name__)

@app.route('/')

def hello_world():
    return "Hello World"

if __name__ == '__main__':
    app.run()
    

#Flask（name)がわかりません。なぜ__name__を入れるのですか？
#__name__はモジュール名を持つ特殊変数です。flask()コマンドの第一引数は、そのアプリケーションの名前となる文字列で、動作中に使われる各種リソースの名前やログなどのいろいろ情報に識別子として使われます。ようするに、どんな文字列を設定しても問題まないですが、__name__を入れておくといいことが多いということです。
