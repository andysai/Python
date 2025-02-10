from flask import Flask
import pandas as pd

app = Flask(__name__)

@app.route('/')
def show_excle():
    df = pd.read_excel("./hips_report.xlsx")
    table_html = df.to_html()
    return f"""
        <html>
            <body>
                <h1>Rsync 漏洞修复</h1>
                <div>{table_html}</div>
            </body>
        </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
