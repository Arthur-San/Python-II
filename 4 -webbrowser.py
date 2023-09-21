import webbrowser

done = False

while not done:
    print('o que deseja fazer?')
    print('1- aprender python')
    print('2- aprender sobre módulos')
    print('3- aprender python, fullstack JS,ingles e no code')
    print('4- Sair')

    choice = input('>')

    if choice == '1':
        webbrowser.open("http:/www.python.org")
    elif choice == '2':
        webbrowser.open("https://docs.python.org/pt-br/3/py-modindex.html")
    elif choice == '3':
        webbrowser.open("https:/www.onebitcode.com/")
    elif choice == '4':
        done = True
    else:
        print('Opção inválida!')