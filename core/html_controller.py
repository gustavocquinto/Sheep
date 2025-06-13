
class HTML():

    def __init__(self):
        return None

    def html_header (self):
        func = open("relatorio.html", "w")

        
        func.write("""
                    <!DOCTYPE html>
                    <html lang="pt-BR">
                    <head>
                        <meta charset="UTF-8">
                        <title>Relatório de Testes</title>
                        <!-- Link para o Tailwind CSS via CDN -->
                        <script src="https://cdn.tailwindcss.com"></script>
                    </head>
                    <body>
                    <h1 class="text-3xl font-bold mb-4">Relatório de Testes</h1>
                    """)
        func.close()
        return None

    def gera_e_insere_relatorio(self, asserts, nome_do_test="_formTest"):
        from core.asserts_controller import Asserts
        func = open("relatorio.html", "a")
        html_base_relatorio = f"""
                                    <div class="mb-6">
                                    <h3> {nome_do_test}</h3>
                                    <table class="min-w-full border-collapse border border-gray-300">
                                        <thead>
                                            <tr>
                                                <th class="border border-gray-300 px-4 py-2 bg-gray-100">Sucessos</th>
                                                <th class="border border-gray-300 px-4 py-2 bg-gray-100">Erros</th>
                                                <th class="border border-gray-300 px-4 py-2 bg-gray-100">Testes totais</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr>
                                                <td class="border border-gray-300 px-4 py-2 text-green-600">{asserts.sucessos}</td>
                                                <td class="border border-gray-300 px-4 py-2 text-red-600">{asserts.falhas}</td>
                                                <td class="border border-gray-300 px-4 py-2">{asserts.asserts_total}</td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>
                                            """
        func.write(html_base_relatorio + "\n")
        func.close()
        return True
    
    def fecha_html(self):
        func = open("relatorio.html", "a")
        func.write("</body> \n </html> \n")
        func.close()

#1 - Chamada a função de abrir arquivo e configurar headers html no main.py (Instancia a controller uma vez)

#2 - Cada arquivo Validator deverá chamar um novo objeto de asserts para validar os dados. 
# Para cada validador será criado uma nova instância de asserts, com o intuito de segregar os resultados e possibilitando "acrescentar" no arquivo .html

#3 - Após executados todos os validadores, e inseridos os resultados no arquivo html. Insere o final do código html e fecha o objeto