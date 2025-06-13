from core.logger import Logger
from core.html_controller import HTML
class Asserts():
    
    def __init__(self):
        self.sucessos = 0
        self.falhas = 0
        self.asserts_total = 0
        return None


    def relatorio_asserts(self, nome_relatorio="test_form"):
       self.html = HTML()
       self.html.gera_e_insere_relatorio(self, nome_relatorio)

       return None

    def checar (self, valor_enviado, valor_salvo):
        Logger.info_log(f"[ASSERT] Verificando sucesso, valor/string enviada: {valor_enviado} valor salvo: {valor_salvo}")
        self.asserts_total += 1 
        valor_salvo_formatado = str(valor_salvo).replace("\n", " ").strip()
        valor_enviado_formatado = str(valor_enviado).replace("\n", " ").strip()
        try:
            assert valor_enviado_formatado == valor_salvo_formatado, f"[ASSERT] Falha: valor_enviado -> {valor_enviado} != valor_salvo -> {valor_salvo}"
            Logger.info_log("[ASSERT] ✔️ Validação concluída.")
            self.sucessos += 1     
        except AssertionError as e:
            self.falhas += 1
            Logger.warning_log(e)
            return False