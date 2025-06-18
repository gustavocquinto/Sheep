from core.autoload import AutomationController
from tests.formTest import FormTest
from core.html_controller import HTML

def main():
    HTML().html_header()

    formTest = FormTest()


    HTML().fecha_html()

if __name__ == "__main__":
    main()