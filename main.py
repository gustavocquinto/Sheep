from core.autoload import AutomationController
from tests.formTest import FormTest
from core.html_controller import HTML

def main():
    HTML().html_header()

    formTest = FormTest()
    formTest.preencher_formulario_corretamente()
    #formTest.campos_obrigatorios()

    HTML().fecha_html()

if __name__ == "__main__":
    main()