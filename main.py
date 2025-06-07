from core.autoload import AutomationController
from tests.formTest import FormTest

def main():
    formTest = FormTest()
    formTest.preencher_formulario_corretamente()
    #formTest.campos_obrigatorios()

if __name__ == "__main__":
    main()