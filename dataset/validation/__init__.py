from IPython.display import display, Javascript
from utils.logger import danger, success

def stop_execution():
    display(Javascript('google.colab.kernel.interrupt();'))

# Definições de validação
def check_categories(training_products, categories):
    invalid_categories = set()
    for produto in training_products:
        if produto[1] not in categories:
            invalid_categories.add(produto[1])

    if invalid_categories:
        danger(f"categories inválidas encontradas: {invalid_categories}")
        return False;
    else:
        success("Todas as categories são válidas.")
        return True;

def check_duplicates(training_products):
    checked = set()
    duplicates = set()
    for produto in training_products:
        if produto[0] in checked:
            duplicates.add(produto[0])
        checked.add(produto[0])

    if duplicates:
        danger(f"Duplicatas encontradas: {duplicates}")
        return False;
    else:
        success("Nenhuma duplicata encontrada.")
        return True;

def check_non_categorized_items(training_products):
    itens_nao_categorizados = [produto for produto in training_products if produto[1] == ""]

    if itens_nao_categorizados:
        danger(f"Itens não categorizados encontrados: {itens_nao_categorizados}")
        return False;
    else:
        success("Todos os itens estão categorizados.")
        return True;

def check_class_labels(training_products, categories):
    categoria_para_inteiro = {categoria: i for i, categoria in enumerate(categories)}

    # Verifica se todos os produtos têm rótulos válidos
    rotulos_invalidos = []
    for produto in training_products:
        categoria = produto[1]
        if categoria not in categoria_para_inteiro:
            rotulos_invalidos.append((produto[0], categoria))

    if rotulos_invalidos:
        danger("Foram encontrados rótulos de classe inválidos:")
        for item in rotulos_invalidos:
            print(f"Produto: {item[0]}, Categoria: {item[1]}")
        return False;
    else:
        success("Todas as categorias são conhecidas.")
        return True;
