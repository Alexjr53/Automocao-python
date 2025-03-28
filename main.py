import random
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

botoes_clicados = 0


def obter_dados_automacao():
    total_a_enviar = int(input("quantos convites deseja enviar?: "))
    cargo = input("qual o cargo quer pesquisar?: ")
    return total_a_enviar, cargo


def iniciar_navegador():
    try:
        servico = Service(ChromeDriverManager().install())  # instala a versão do chromedirver
        navegador = webdriver.Chrome(service=servico)  # faz o navegador iniciar com a versão atual do chromedriver

        navegador.maximize_window()
        sleep(1)
        navegador.get('https://www.linkedin.com/feed/')
        wait = WebDriverWait(navegador, 10)
    except Exception as error:
        print(f"Erro ao abrir o navegador ou carregar a página: {error}")
        exit(1)
    return navegador, wait


def intervalo_login():  # mover a função para outro arquivo
    print("voce tem 60 segundos para efetuar o login")
    for time in range(60, 0, -1):
        print(f"restam {time} segundos\n")
        sleep(1)


def pesquisar_cargo(navegador, wait, cargo):
    try:
        print(f"pesquisando o cargo: {cargo}")
        campo_pesquisa = navegador.find_element(By.XPATH, '//*[@id="global-nav-typeahead"]/input')
        sleep(2)
        campo_pesquisa.send_keys(f"{cargo}")
        sleep(2)
        campo_pesquisa.send_keys(Keys.ENTER)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="search-reusables__filters-bar"]/ul/li[1]/button'))).click()
        sleep(6)
    except Exception as error:
        print(f"Erro ao realizar a pesquisa: {error}")
        navegador.quit()


def rolar_pagina_para_cima(navegador):
    navegador.execute_script("window.scrollTo(0, 0);")
    sleep(1)


def rolar_pagina_para_baixo(navegador):
    navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(1)


def clicar_botoes_conectar(navegador, wait, total_a_enviar):
    global botoes_clicados
    try:
        print("buscando por botões de conectar na página atual\n")
        rolar_pagina_para_baixo(navegador)
        rolar_pagina_para_cima(navegador)
    except Exception as error:
        print(f"erro ao tentar rolar a pagina: {error}")

    sleep((random.randint(2, 5)))
    try:
        botoes_conectar = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button[contains(@aria-label, 'Convidar')]")))
        if botoes_conectar:
            for botao in botoes_conectar:
                if botoes_clicados < total_a_enviar:
                    try:
                        navegador.execute_script("arguments[0].scrollIntoView();", botao)
                        navegador.execute_script("window.scrollBy(0, -150);")
                        sleep(2)
                        botao.click()
                        print("botão clicado")
                        sleep((random.randint(2, 5)))
                        botao_sem_nota = navegador.find_element(By.XPATH, "//button[@aria-label='Enviar sem nota']")
                        sleep((random.randint(2, 5)))
                        botao_sem_nota.click()
                        print("convite enviado sem nota")
                        botoes_clicados += 1
                        sleep((random.randint(3, 7)))
                    except Exception as error:
                        print(f"Erro ao ao enviar o convite, talvez um modal inesperado tenha sido aberto: {error}")
                else:
                    print("limite de convites alcançado")
                    return True
        else:
            print("Os botões 'conectar' da pagina atual acabaram")
            return False
    except TimeoutException:
        print("Timeout: Não foi possível encontrar botões 'Convidar' na pagina atual. ")
        return False


def ir_proxima_pagina(navegador, wait):
    try:
        rolar_pagina_para_baixo(navegador)
        print("buscando botão para ir para proxima pagina")
        botao_proxima_pagina = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Avançar']")))
        sleep((random.randint(2, 5)))

        if botao_proxima_pagina.is_enabled() is True:
            botao_proxima_pagina.click()
            sleep((random.randint(3, 7)))
        else:
            print("programa chegou na ultima pagina, encerrando programa")
            navegador.quit()
    except Exception as error:
        print(f"erro ao ir para a proxima pagina: {error}")


def iniciar_automacao():
    total_a_enviar, cargo = obter_dados_automacao()
    navegador, wait = iniciar_navegador()
    intervalo_login()
    pesquisar_cargo(navegador, wait, cargo)

    while botoes_clicados <= total_a_enviar:
        encontrou_botoes = clicar_botoes_conectar(navegador, wait, total_a_enviar)
        if not encontrou_botoes:
            print("indo para a proxima pagina")
            ir_proxima_pagina(navegador, wait)
        else:
            print("botoes encontrados, porem a meta de convites a enviar já foi alcançada")
            break

    if botoes_clicados >= total_a_enviar:
        print(f"Programa encerrado. Total de convites enviados: {botoes_clicados}.")
    else:
        print(f"O programa foi encerrado por algum motivo não previsto. Total de convites enviados: {botoes_clicados}.")
    navegador.quit()


if __name__ == "__main__":
    iniciar_automacao()
