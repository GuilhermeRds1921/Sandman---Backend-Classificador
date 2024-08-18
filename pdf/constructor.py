from weasyprint import HTML
import base64

def generate_pdf(job, notes, name, technician, CDEnf):
    BASE = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Laudo Médico</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 20px;
                color: #333;
            }}
            h1, h2 {{
                color: #444;
            }}
            p {{
                font-size: 14px;
                color: #555;
            }}
            .imagem {{
                max-width: 100%;
                height: auto;
                margin-bottom: 20px;
            }}
            .info {{
                margin-bottom: 20px;
            }}
            .info h2 {{
                margin-top: 0;
            }}
            .info h3 {{
                margin-bottom: 5px;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-bottom: 20px;
            }}
            table, th, td {{
                border: 1px solid #ddd;
                padding: 8px;
            }}
            th {{
                background-color: #f4f4f4;
                text-align: center;
            }}
            td {{
                text-align: center;
            }}
        </style>
    </head>
    <body>
        <h1>SANDMAN - Laudo do Eletroencefalograma</h1>
        <div class="info">
            <h2>Informações</h2>
            <p><strong>Nome:</strong> {name}</p>
            <p><strong>Técnico Responsável:</strong> {technician} <strong>CDEnf:</strong> {CDEnf}</p>
        </div>
        <div class="info">
            <h2>Eletroencefalografia</h2>
            <img class="imagem" src="data:image/png;base64,{eeg_reading_plot}" alt="Imagem do Eletroencefalograma">
        </div>
        <div class="info">
            <h2>Hipnograma</h2>
            <img class="imagem" src="data:image/png;base64,{classified_eeg_reading_plot}" alt="Leitura EEG Classificada">
        </div>
        <div class="info">
            <h2>Distribuição dos Estágios do Sono</h2>
            <img class="imagem" src="data:image/png;base64,{sleep_stages_distribution_plot}" alt="Distribuição dos Estágios do Sono">
        </div>
        <div class="info">
            <h2>Tabela dos Estágios do Sono</h2>
            <table>
                <tr>
                    <th></th>
                    <th>Acordado</th>
                    <th>N1</th>
                    <th>N2</th>
                    <th>N3</th>
                    <th>REM</th>
                </tr>
                {table_rows}
            </table>
        </div>
        <div class="info">
            <h2>Notas</h2>
            <p>{notes}</p>
        </div>
    </body>
    </html>
    """

    stage_table = job["stage_table"]
    plots = job["plots"]
    eeg_reading_plot = plots["eeg_reading_plot"]
    sleep_stages_distribution_plot = plots["sleep_stages_distribution_plot"]
    classified_eeg_reading_plot = plots["classified_eeg_reading_plot"]

    stages = {0: "Acordado", 1: "N1", 2: "N2", 3: "N3", 4: "REM"}

    table_rows = ""
    for i, row in enumerate(stage_table):
        table_rows += "<tr><th>{}</th>".format(stages[i])
        for cell in row:
            table_rows += "<td>{}</td>".format(cell)
        table_rows += "</tr>"

    html_content = BASE.format(
        name=name,
        technician=technician,
        CDEnf=CDEnf,
        notes=notes,
        eeg_reading_plot=eeg_reading_plot,
        sleep_stages_distribution_plot=sleep_stages_distribution_plot,
        classified_eeg_reading_plot=classified_eeg_reading_plot,
        table_rows=table_rows
    )

    pdf_bytes = HTML(string=html_content).write_pdf()
    pdf_base64 = base64.b64encode(pdf_bytes).decode("utf-8")
    return pdf_base64
