from flask import Flask
import pandas as pd

app = Flask(__name__)

@app.route('/')
def show_excle():
    df = pd.read_excel("./监控标准v2-20220513.xlsx")
    table_html = df.to_html()
    return f"""
        <html>
            <body>
                <h1>监控标准v2-20220513</h1>
                <div>{table_html}</div>
            </body>
        </html>
    """

if __name__ == '__main__':
    app.run(host="0.0.0.0")