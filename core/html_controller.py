from datetime import datetime
class HTML():

    def __init__(self):
        return None

    def html_header (self):
        func = open("relatorio.html", "w")
    
        data_geracao = datetime.now()
        
        func.write(f"""
                    <!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Sheep - Relatório de Testes</title>
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-50 text-gray-900">
  <header class="bg-gradient-to-r from-indigo-600 to-purple-600 text-white shadow-md">
    <div class="max-w-7xl mx-auto px-6 py-6 flex items-center justify-between">
      <div class="flex items-center space-x-4">
        <img src="assets/pngwing.com.png" 
             alt="Ícone de Carneiro" 
             class="w-10 h-10 rounded-full bg-white p-1 shadow-md" />

        <h1 class="text-3xl font-bold tracking-tight">Relatório de Testes</h1>
      </div>
      <span class="text-sm text-white/80">Atualizado em: {data_geracao}</span>
    </div>
  </header>



                    """)
        func.close()
        return None

    def gera_e_insere_relatorio(self, asserts, nome_do_test="_formTest"):
        func = open("relatorio.html", "a")
        html_base_relatorio = f"""
                                    <div class="mb-4 p-4 border rounded-lg shadow-md bg-white">
  <h3 class="text-xl font-semibold mb-4">{nome_do_test}</h3>
  <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
    <div class="p-4 border rounded-lg bg-green-50 text-green-700">
      <h4 class="text-md font-medium mb-2">Sucessos</h4>
      <p class="text-2xl font-bold">{asserts.sucessos}</p>
    </div>
    <div class="p-4 border rounded-lg bg-red-50 text-red-700">
      <h4 class="text-md font-medium mb-2">Erros</h4>
      <p class="text-2xl font-bold">{asserts.falhas}</p>
    </div>
    <div class="p-4 border rounded-lg bg-gray-50 text-gray-800">
      <h4 class="text-md font-medium mb-2">Testes totais</h4>
      <p class="text-2xl font-bold">{asserts.asserts_total}</p>
    </div>
  </div>
</div>


                                            """
        func.write(html_base_relatorio + "\n")
        func.close()
        return True
    
    def fecha_html(self):
        func = open("relatorio.html", "a")
        func.write("</body> \n </html> \n")
        func.close()