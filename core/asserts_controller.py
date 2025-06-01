class Asserts():
    
    def __init__(self):
        self.sucessos = 0
        self.falhas = 0
        self.asserts_total = 0
        return None


    def relatorio_asserts(self):
        func = open("relatorio.html", "w")

        html = """
        <h1>Relat&oacute;rio de execu&ccedil;&atilde;o de testes - beta</h1>
        <div>
            <table>
            <tbody>
            <tr>
            <th>Sucessos</th>
            <th>Erros</th>
            <th>Testes totais</th>
            </tr>
            <tr>
            <td>2</td>
            <td>2</td>
            <td>4</td>
            </tr>
            </tbody>
            </table>
            </div>
            """
        func.write(f"<html> <head> <title> teste </title> </head> <body> {html}  <html>")