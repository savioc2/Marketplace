from typing import List, Dict
from time import sleep

from models.produto import Product
from utils.helper import formata_float_str_moeda

products: List[Product] = []
cart: List[Dict[Product, int]] = []


def main() -> None:
    menu()


def menu() -> None:
    print('===================================')
    print('=========== Welcome ==========')
    print('=========== Sávio shop ==========')
    print('===================================')

    print('Select an option below: ')
    print('1 - Register product')
    print('2 - List product')
    print('3 - Buy product')
    print('4 - View cart')
    print('5 - Close order')
    print('6 - exit system')

    option: int = int(input())

    if option == 1:
        register_product()
    elif option == 2:
        list_product()
    elif option == 3:
        buy_product()
    elif option == 4:
        view_cart()
    elif option == 5:
        close_order()
    elif option == 6:
        print('Check back often!')
        sleep(2)
        exit(0)
    else:
        print('Invalid option!')
        sleep(1)
        menu()


def register_product() -> None:
    print('register_product')
    print('===================')

    nome: str = input('Enter the product name: ')
    price: float = float(input('Inform the price of the product: '))

    product: Product = Product(nome, price)

    products.append(product)

    print(f'The product {product.nome} has been registered successfully!')
    sleep(2)
    menu()


def list_product() -> None:
    if len(products) > 0:
        print('Oroduct listing')
        print('--------------------')
        for produto in products:
            print(produto)
            print('----------------')
            sleep(1)
    else:
        print('There are no registered products yet.')
    sleep(2)
    menu()


def buy_product() -> None:
    if len(products) > 0:
        print('Enter the code of the product you want to add to the cart: ')
        print('--------------------------------------------------------------')
        print('==================  Products Available ======================')
        for produto in products:
            print(produto)
            print('---------------------------------------------------------')
            sleep(1)
        codigo: int = int(input())

        produto: Product = pega_produto_por_codigo(codigo)

        if produto:
            if len(cart) > 0:
                tem_no_carrinho: bool = False
                for item in cart:
                    quant: int = item.get(produto)
                    if quant:
                        item[produto] = quant + 1
                        print(f'The product {produto.nome} now owns {quant + 1} units in cart.')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    cart.append(prod)
                    print(f'The product {produto.nome} has been added to cart.')
                    sleep(2)
                    menu()
            else:
                item = {produto: 1}
                cart.append(item)
                print(f'The product {produto.nome} has been added to cart.')
                sleep(2)
                menu()
        else:
            print(f'The product with code {codigo} was not found..')
            sleep(2)
            menu()
    else:
        print('There are no products to sell yet.')
    sleep(2)
    menu()


def view_cart() -> None:
    if len(cart) > 0:
        print('Products in cart: ')

        for item in cart:
            for dados in item.items():
                print(dados[0])
                print(f'The amount: {dados[1]}')
                print('-----------------------')
                sleep(1)
    else:
        print('There are no products to sell yet.')
    sleep(2)
    menu()


def close_order() -> None:
    if len(cart) > 0:
        valor_total: float = 0

        print('Product in cart')
        for item in cart:
            for dados in item.items():
                print(dados[0])
                print(f'The amount: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print('------------------------')
                sleep(1)
        print(f'Your invoice is {formata_float_str_moeda(valor_total)}')
        print('Check back often!')
        cart.clear()
        sleep(5)
    else:
        print('There are no products in the cart yet.')
    sleep(2)
    menu()


def pega_produto_por_codigo(codigo: int) -> Product:
    p: Product = None

    for produto in products:
        if produto.codigo == codigo:
            p = produto
    return p


if __name__ == '__main__':
    main()
