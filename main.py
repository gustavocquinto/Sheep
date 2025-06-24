from core.autoload import AutomationController
from tests.formTest import FormTest
from tests.textBoxTest import TextBox
from core.html_controller import HTML

def main():
    HTML().html_header()

    formTest = FormTest().runner()
    textBox = TextBox().runner()

    HTML().fecha_html()

if __name__ == "__main__":
    main()