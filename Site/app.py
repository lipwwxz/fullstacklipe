from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sua_senha",
    database="estoque"
)

@app.route("/total")
def total():

    cursor = conexao.cursor()

    # total de itens
    cursor.execute("SELECT SUM(quantidade) FROM estoque")
    total = cursor.fetchone()[0]

    # ultimo mes
    cursor.execute("""
    SELECT SUM(quantidade)
    FROM estoque
    WHERE data_cadastro >= NOW() - INTERVAL 1 MONTH
    """)
    ultimo_mes = cursor.fetchone()[0]

    # ultimos 12 meses
    cursor.execute("""
    SELECT SUM(quantidade)
    FROM estoque
    WHERE data_cadastro >= NOW() - INTERVAL 12 MONTH
    """)
    ultimos_12 = cursor.fetchone()[0]

    # ultimos 24 meses
    cursor.execute("""
    SELECT SUM(quantidade)
    FROM estoque
    WHERE data_cadastro >= NOW() - INTERVAL 24 MONTH
    """)
    ultimos_24 = cursor.fetchone()[0]

    return render_template(
        "total_prod.html",
        total=total,
        ultimo_mes=ultimo_mes,
        ultimos_12=ultimos_12,
        ultimos_24=ultimos_24
    )

app.run(debug=True)