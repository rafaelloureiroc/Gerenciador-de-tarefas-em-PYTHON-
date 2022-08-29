import pygame
import psutil
import platform
import cpuinfo
import os
import time
from datetime import datetime, date
import subprocess
from pygame.locals import *
import matplotlib
matplotlib.use('Agg')
import matplotlib.backends.backend_agg as agg
import pylab
from time import sleep
from numpy import polyfit
import matplotlib.pyplot as plt
import numpy as np
import netifaces
import socket
from socket import AF_INET, SOCK_STREAM, SOCK_DGRAM



BRANCO = (255,255,255)
PRETO = (0,0,0)
LARANJA = (246,130,0)
VERMELHO = (230,0,0)
AZUL =  (0, 0, 255)
CINZA = (128,128,128)

pygame.init()
largura_tela, altura_tela = 1920, 1024
tela = pygame.display.set_mode((largura_tela, altura_tela))
tela.fill(BRANCO)
font = pygame.font.Font(None, 32)
info = cpuinfo.get_cpu_info()
pygame.display.init()
pygame.font.init()
l_cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
lista = os.listdir()






def mostra_texto(texto, pos, cor):
    font = pygame.font.Font(None, 24)
    text = font.render(f"{texto}",1, cor)
    textpos = text.get_rect(center=pos,)
    tela.blit(text, textpos)

def mostra_texto_grande(texto, pos, cor):
    font = pygame.font.Font(None, 36)
    text = font.render(f"{texto}", 1, cor)
    textpos = text.get_rect(center=pos,)
    tela.blit(text, textpos)
    
    
def mostra_uso_memoria():
    mem = psutil.virtual_memory()
    larg = largura_tela - 2*20
    pygame.draw.rect(tela, AZUL, (10, 160, larg, 35))
    larg = larg*mem.percent/100
    pygame.draw.rect(tela, VERMELHO, (10, 160, larg, 35))
    total = round(mem.total/(1024*1024*1024),2)
    texto_barra = "Uso de Memória (Total: " + str(total) + "GB):"
    text = font.render(texto_barra, 1, PRETO)
    tela.blit(text, (10, 125))
    
    
def mostra_uso_cpu():
    capacidade = psutil.cpu_percent()
    larg = largura_tela - 2*20
    pygame.draw.rect(tela, AZUL, (10, 265, larg, 35))
    larg = larg*capacidade/100
    pygame.draw.rect(tela, VERMELHO, (10, 265, larg, 35))
    text = font.render("Uso de CPU:", 1, PRETO)
    tela.blit(text, (10, 230))
    
    
def mostra_uso_disco():
    disco = psutil.disk_usage('.')
    larg = largura_tela - 2*20
    pygame.draw.rect(tela, AZUL, (10, 375, larg, 35))
    larg = larg*disco.percent/100
    pygame.draw.rect(tela, VERMELHO, (10, 375, larg, 35))
    total = round(disco.total/(1024*1024*1024), 2)
    texto_barra = "Uso de Disco: (Total: " + str(total) + "GB):"
    text = font.render(texto_barra, 1, PRETO)
    tela.blit(text, (10, 330))
    
    
    
    
def mostra_texto_cpu(tela, nome, chave, pos_y):
    info_cpu = cpuinfo.get_cpu_info()
    text = font.render(nome, True, PRETO)
    tela.blit(text, (10, pos_y))
    if chave == "freq":
        s = str(round(psutil.cpu_freq().current, 2))
    elif chave == "nucleos":
        s = str(psutil.cpu_count())
        s = s + " (" + str(psutil.cpu_count(logical=False)) + ")"
    else:
        s = str(info_cpu[chave])
    text = font.render(s, True, CINZA)
    tela.blit(text, (300, pos_y))
  
  
def mostra_info_cpu():
    mostra_texto_cpu(tela, "Nome:", "brand", 145)
    mostra_texto_cpu(tela, "Arquitetura:", "arch", 200)
    mostra_texto_cpu(tela, "Palavra (bits):", "bits", 255)
    mostra_texto_cpu(tela, "Frequência (MHz):", "freq", 310)
    mostra_texto_cpu(tela, "Núcleos (físicos):", "nucleos", 355)
    tela.blit(tela, (0, 0))
    
    
def mostra_uso_nucleo (tela, l_cpu_percent):
    num_cpu = len(l_cpu_percent)
    x, y = 360, 420
    desl = 10
    alt = 250
    larg = 62
    d = x + desl
    for i in l_cpu_percent:
        pygame.draw.rect(tela, VERMELHO, (d, y, larg, alt))
        pygame.draw.rect(tela, AZUL, (d, y, larg, (1-i/100)*alt))
        d = d + larg + desl
    
    
def desenha_abas():
    aba0 = pygame.Rect(0, 0, 384, 50)
    pygame.draw.rect(tela, PRETO, aba0)
    mostra_texto("DESEMPENHO",(192,25), BRANCO)

    aba1 = pygame.Rect(385, 0, 384, 50)
    pygame.draw.rect(tela, PRETO, aba1)
    mostra_texto("PROCESSADOR",(577,25), BRANCO)

    aba2 = pygame.Rect(770, 0, 384, 50)
    pygame.draw.rect(tela, PRETO, aba2)
    mostra_texto("ARQs E DIR",(962,25), BRANCO)

    aba3 = pygame.Rect(1155, 0, 384, 50)
    pygame.draw.rect(tela, PRETO, aba3)
    mostra_texto("PROCESSOS",(1347,25), BRANCO)
    
    aba4 = pygame.Rect(1540, 0, 384, 50)
    pygame.draw.rect(tela, PRETO, aba4)
    mostra_texto("REDE",(1732,25), BRANCO)
    
    
    
    aba5 = pygame.Rect(1155, 51, 75.8, 50)
    pygame.draw.rect(tela, PRETO, aba5)
    mostra_texto("P1",(1193.4,75.8), BRANCO)
    
    aba6 = pygame.Rect(1231.8, 51, 75.8, 50)
    pygame.draw.rect(tela, PRETO, aba6)
    mostra_texto("P2",(1268.2,75.8), BRANCO)
    
    aba7 = pygame.Rect(1308.6, 51, 75.8, 50)
    pygame.draw.rect(tela, PRETO, aba7)
    mostra_texto("P3",(1347,75.8), BRANCO)
    
    aba8 = pygame.Rect(1385.4, 51, 75.8, 50)
    pygame.draw.rect(tela, PRETO, aba8)
    mostra_texto("P4",(1423.8,75.8), BRANCO)
    
    aba9 = pygame.Rect(1462.2, 51, 77.8, 50)
    pygame.draw.rect(tela, PRETO, aba9)
    mostra_texto("P5",(1500.6,75.8), BRANCO)
    
    
    
    aba10 = pygame.Rect(1540.2, 51, 75.8, 50)
    pygame.draw.rect(tela, PRETO, aba10)
    mostra_texto("P1",(1578.6,75.8), BRANCO)
    
    aba11 = pygame.Rect(1616.8, 51, 76.8, 50)
    pygame.draw.rect(tela, PRETO, aba11)
    mostra_texto("P2",(1655.2,75.8), BRANCO)
    
    aba12 = pygame.Rect(1693.6, 51, 75.8, 50)
    pygame.draw.rect(tela, PRETO, aba12)
    mostra_texto("P3",(1732,75.8), BRANCO)
    
    
    
    
    return [aba0, aba1, aba2, aba3, aba4, aba5, aba6, aba7,aba8, aba9, aba10, aba11, aba12]


def mostrar_arquivos():
    tela.fill(BRANCO)
    lista = os.listdir()
    dic = {}
    altura_texto = 160
    altura_texto2 = 760
    lista_arq = []
    lista_dir = []
    
    for i in lista:
        if os.path.isfile(i):
            dic[i] = []
            dic[i].append(os.stat(i).st_size)
            dic[i].append(os.stat(i).st_atime)
            dic[i].append(os.stat(i).st_mtime)
    
    for i in dic:
        kb = dic[i][0] / 1024  
        tamanho = '{:10}'.format(str('{:.2f}'.format(kb)+' KB'))
        arquivos =  tamanho, time.ctime(dic[i][2]), time.ctime(dic[i][1]), i
        mostra_texto('Arquivos:', (530 ,100), PRETO)
        mostra_texto('Nome', (600 ,130), PRETO)
        mostra_texto('Tamanho', (895 ,130), PRETO)
        mostra_texto('Data de criação', (1150 ,130), PRETO)
        mostra_texto('Data de modificação', (1400 ,130), PRETO)
         
        mostra_texto(arquivos[0], (900 ,altura_texto), PRETO)
        mostra_texto(arquivos[1], (1150 ,altura_texto), PRETO)
        mostra_texto(arquivos[2], (1400 ,altura_texto), PRETO)
        mostra_texto(arquivos[3], (600 ,altura_texto), PRETO)
        altura_texto += 20
        
        
    for i in lista:
        if os.path.isfile(i):
            lista_arq.append(i)
        else:
            lista_dir.append(i)
    for i in lista_dir:
        mostra_texto('Diretórios:', (530 ,700), PRETO)
        mostra_texto(i, (880, altura_texto2), PRETO)
        altura_texto2 += 20
        
    
        
        
             
def mostra_info():
    lista_pids = psutil.pids()
    altura_texto = 160
    for i in lista_pids[:40]:
        try:
            
            processo = psutil.Process(i)
            nome = processo.name()
            usuario = processo.username()
            tempo_de_exec = processo.create_time()
            tempo_nostamp = time.localtime(tempo_de_exec)
            Tempo_PTBR = time.strftime("%d-%m-%Y, as %H:%M:%S", tempo_nostamp)
            uso_memoria = round(processo.memory_info().rss / (1024*1024),2)
            uso_memoria_gb = str(uso_memoria) + ' MB'
            
            
        except: pass
        mostra_texto(i,(450,altura_texto), PRETO)
        mostra_texto(nome,(600,altura_texto), PRETO)
        mostra_texto(Tempo_PTBR,(895,altura_texto), PRETO)
        mostra_texto(uso_memoria_gb,(1150,altura_texto), PRETO)
        altura_texto += 20
        
    mostra_texto("PID:  ",(450,130), PRETO)
    mostra_texto("Nome: ",(600,130), PRETO)
    mostra_texto("Iniciado em: ",(895,130), PRETO)
    mostra_texto("Uso de memória: ",(1150,130), PRETO)
    
def mostra_info2():
    lista_pids = psutil.pids()
    altura_texto = 160
    tempo_PTBR = ''
    nome = ''
    uso_memoria_gb = ''
    
    for i in lista_pids[40:80]:
        try:
            processo = psutil.Process(i)
            nome = processo.name()
            usuario = processo.username()
            tempo_de_exec = processo.create_time()
            tempo_nostamp = time.localtime(tempo_de_exec)
            tempo_PTBR = time.strftime("%d-%m-%Y, as %H:%M:%S", tempo_nostamp)
            uso_memoria = round(processo.memory_info().rss / (1024*1024), 2)
            uso_memoria_gb = str(uso_memoria) + ' MB'
            
            
        except: pass
        mostra_texto(i,(450,altura_texto), PRETO)
        mostra_texto(nome,(600,altura_texto), PRETO)
        mostra_texto(tempo_PTBR,(895,altura_texto), PRETO)
        mostra_texto(uso_memoria_gb,(1150,altura_texto), PRETO)
        altura_texto += 20
        
    mostra_texto("PID:  ",(450,130), PRETO)
    mostra_texto("Nome: ",(600,130), PRETO)
    mostra_texto("Iniciado em: ",(895,130), PRETO)
    mostra_texto("Uso de memória ",(1150,130), PRETO)
    
def mostra_info3():
    lista_pids = psutil.pids()
    altura_texto = 160
    tempo_PTBR = ''
    nome = ''
    uso_memoria_gb = ''
    
    for i in lista_pids[80:120]:
        try:
            processo = psutil.Process(i)
            nome = processo.name()
            usuario = processo.username()
            tempo_de_exec = processo.create_time()
            tempo_nostamp = time.localtime(tempo_de_exec)
            tempo_PTBR = time.strftime("%d-%m-%Y, as %H:%M:%S", tempo_nostamp)
            uso_memoria = round(processo.memory_info().rss / (1024*1024), 2)
            uso_memoria_gb = str(uso_memoria) + ' MB'
            
            
        except: pass
        mostra_texto(i,(450,altura_texto), PRETO)
        mostra_texto(nome,(600,altura_texto), PRETO)
        mostra_texto(tempo_PTBR,(895,altura_texto), PRETO)
        mostra_texto(uso_memoria_gb,(1150,altura_texto), PRETO)
        altura_texto += 20
        
    mostra_texto("PID:  ",(450,130), PRETO)
    mostra_texto("Nome: ",(600,130), PRETO)
    mostra_texto("Iniciado em : ",(895,130), PRETO)
    mostra_texto("Uso de memória: ",(1150,130), PRETO)
    
def mostra_info4():
    lista_pids = psutil.pids()
    altura_texto = 160
    tempo_PTBR = ''
    nome = ''
    uso_memoria_gb = ''
    
    for i in lista_pids[120:160]:
        try:
            processo = psutil.Process(i)
            nome = processo.name()
            usuario = processo.username()
            tempo_de_exec = processo.create_time()
            tempo_nostamp = time.localtime(tempo_de_exec)
            tempo_PTBR = time.strftime("%d-%m-%Y, as %H:%M:%S", tempo_nostamp)
            uso_memoria = round(processo.memory_info().rss / (1024*1024), 2)
            uso_memoria_gb = str(uso_memoria) + ' MB'
            
            
        except: pass
        mostra_texto(i,(450,altura_texto), PRETO)
        mostra_texto(nome,(600,altura_texto), PRETO)
        mostra_texto(tempo_PTBR,(895,altura_texto), PRETO)
        mostra_texto(uso_memoria_gb,(1150,altura_texto), PRETO)
        altura_texto += 20
        
    mostra_texto("PID:  ",(450,130), PRETO)
    mostra_texto("Nome: ",(600,130), PRETO)
    mostra_texto("Iniciado em : ",(895,130), PRETO)
    mostra_texto("Uso de memória: ",(1150,130), PRETO)

def mostra_info5():
    lista_pids = psutil.pids()
    altura_texto = 160
    tempo_PTBR = ''
    nome = ''
    uso_memoria_gb = ''
    
    for i in lista_pids[160:200]:
        try:
            processo = psutil.Process(i)
            nome = processo.name()
            usuario = processo.username()
            tempo_de_exec = processo.create_time()
            tempo_nostamp = time.localtime(tempo_de_exec)
            tempo_PTBR = time.strftime("%d-%m-%Y, as %H:%M:%S", tempo_nostamp)
            uso_memoria = round(processo.memory_info().rss / (1024*1024), 2)
            uso_memoria_gb = str(uso_memoria) + ' MB'
            
            
        except: pass
        mostra_texto(i,(450,altura_texto), PRETO)
        mostra_texto(nome,(600,altura_texto), PRETO)
        mostra_texto(tempo_PTBR,(895,altura_texto), PRETO)
        mostra_texto(uso_memoria_gb,(1150,altura_texto), PRETO)
        altura_texto += 20
        
    mostra_texto("PID:  ",(450,130), PRETO)
    mostra_texto("Nome: ",(600,130), PRETO)
    mostra_texto("Iniciado em : ",(895,130), PRETO)
    mostra_texto("Uso de memória: ",(1150,130), PRETO)       






def mostra_rede():               
    network = psutil.net_if_addrs()
    firstKey = list(network.keys())[0]
    ip = network[firstKey][1].address
    texto_barra = f"O IP da máquina é: {ip}"
    text = font.render(texto_barra, 1, PRETO)
    tela.blit(text, (15, 775))
    altura_texto = 850
            
    dados_rede = psutil.net_io_counters()
    bytes_enviados = dados_rede[0]
    bytes_recebidos = dados_rede[1]
    pacotes_enviados = psutil.net_io_counters()[2]
    pacotes_recebidos = psutil.net_io_counters()[3]
            
            
    mostra_texto(f' Nesta sessão, o tráfego de total de saída foi de : {bytes_enviados} Bytes', (1100, 800), PRETO) 
    mostra_texto(f' Nesta sessão, o tráfego de total de entrada foi de: {bytes_recebidos} Bytes', (1100, 850), PRETO)
    mostra_texto(f'Nesta sessão, o tráfego de total de saída foi de: {pacotes_enviados} Pacotes', (1100, 900), PRETO)
    mostra_texto(f' Nesta sessão, o tráfego de total de entrada foi de: {pacotes_recebidos} Pacotes', (1100, 950), PRETO)
    mostra_texto('Hosts disponíveis:', (85,950), PRETO)
            
    for i in netifaces.interfaces():
            endereço = netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr']
            máscara = netifaces.ifaddresses(i)[netifaces.AF_INET][0]['netmask']
            gateway = netifaces.gateways()['default'][netifaces.AF_INET][0]
            mostra_texto_grande('Características gerais de rede: ',(190,700),PRETO)
            mostra_texto('Endereço IP: ', (65, 850), PRETO)
            mostra_texto('Máscara: ', (260, 850), PRETO)
            mostra_texto('Gateway: ', (465, 850), PRETO)
            mostra_texto(endereço, (160, altura_texto), PRETO)
            mostra_texto(máscara, (350, altura_texto), PRETO)
            mostra_texto(gateway, (545, altura_texto), PRETO)
            altura_texto += 15
            
            

def uso_rede_processo():
    altura_texto = 250
    altura_texto2 = 200
    AD = "-"
    AF_INET6 = getattr(socket, 'AF_INET6', object())
    proto_map = {
    (AF_INET, SOCK_STREAM): 'tcp',
    (AF_INET6, SOCK_STREAM): 'tcp6',
    (AF_INET, SOCK_DGRAM): 'udp',
    (AF_INET6, SOCK_DGRAM): 'udp6',
}
    lista = []
    proc_names = {}
    for p in psutil.process_iter(['pid', 'name']):
        proc_names[p.info['pid']] = p.info['name']
    for c in psutil.net_connections(kind='inet')[:45]:
        laddr = "%s:%s" % (c.laddr)
        raddr = ""
        if c.raddr:
            raddr = "%s:%s" % (c.raddr)
        name = proc_names.get(c.pid, '?') or ''

        proto = proto_map[(c.family, c.type)]
        mostra_texto(name, (150, altura_texto), PRETO)
        mostra_texto(laddr, (550, altura_texto), PRETO)
        mostra_texto(raddr, (1000, altura_texto), PRETO)
        mostra_texto(c.status, (1350, altura_texto), PRETO)
        mostra_texto(c.pid, (1600, altura_texto), PRETO) 
        mostra_texto(proto, (1750, altura_texto), PRETO)
        altura_texto += 15
        
        mostra_texto_grande('Monitoramento do tráfego por processos',(250,100),PRETO)
        mostra_texto('NOME', (150, altura_texto2), PRETO)
        mostra_texto('ENDEREÇO LOCAL', (550, altura_texto2), PRETO)
        mostra_texto('ENDEREÇO REMOTO', (1000, altura_texto2), PRETO)
        mostra_texto('STATUS', (1350, altura_texto2), PRETO)
        mostra_texto('PID', (1600, altura_texto2), PRETO)
        mostra_texto('PROTOCOLO', (1750, altura_texto2), PRETO)
        
def uso_rede_processo2():
    altura_texto = 250
    altura_texto2 = 200
    AD = "-"
    AF_INET6 = getattr(socket, 'AF_INET6', object())
    proto_map = {
    (AF_INET, SOCK_STREAM): 'tcp',
    (AF_INET6, SOCK_STREAM): 'tcp6',
    (AF_INET, SOCK_DGRAM): 'udp',
    (AF_INET6, SOCK_DGRAM): 'udp6',
}
    lista = []
    proc_names = {}
    for p in psutil.process_iter(['pid', 'name']):
        proc_names[p.info['pid']] = p.info['name']
    for c in psutil.net_connections(kind='inet')[45:90]:
        laddr = "%s:%s" % (c.laddr)
        raddr = ""
        if c.raddr:
            raddr = "%s:%s" % (c.raddr)
        name = proc_names.get(c.pid, '?') or ''

        proto = proto_map[(c.family, c.type)]
        mostra_texto(name, (150, altura_texto), PRETO)
        mostra_texto(laddr, (550, altura_texto), PRETO)
        mostra_texto(raddr, (1000, altura_texto), PRETO)
        mostra_texto(c.status, (1350, altura_texto), PRETO)
        mostra_texto(c.pid, (1600, altura_texto), PRETO) 
        mostra_texto(proto, (1750, altura_texto), PRETO)
        altura_texto += 15
        
        mostra_texto_grande('Monitoramento do tráfego por processos',(250,100),PRETO)
        mostra_texto('NOME', (150, altura_texto2), PRETO)
        mostra_texto('ENDEREÇO LOCAL', (550, altura_texto2), PRETO)
        mostra_texto('ENDEREÇO REMOTO', (1000, altura_texto2), PRETO)
        mostra_texto('STATUS', (1350, altura_texto2), PRETO)
        mostra_texto('PID', (1600, altura_texto2), PRETO)
        mostra_texto('PROTOCOLO', (1750, altura_texto2), PRETO)
        
def uso_rede_processo3():
    altura_texto = 250
    altura_texto2 = 200
    AD = "-"
    AF_INET6 = getattr(socket, 'AF_INET6', object())
    proto_map = {
    (AF_INET, SOCK_STREAM): 'tcp',
    (AF_INET6, SOCK_STREAM): 'tcp6',
    (AF_INET, SOCK_DGRAM): 'udp',
    (AF_INET6, SOCK_DGRAM): 'udp6',
}
    lista = []
    proc_names = {}
    for p in psutil.process_iter(['pid', 'name']):
        proc_names[p.info['pid']] = p.info['name']
    for c in psutil.net_connections(kind='inet')[90:135]:
        laddr = "%s:%s" % (c.laddr)
        raddr = ""
        if c.raddr:
            raddr = "%s:%s" % (c.raddr)
        name = proc_names.get(c.pid, '?') or ''

        proto = proto_map[(c.family, c.type)]
        mostra_texto(name, (150, altura_texto), PRETO)
        mostra_texto(laddr, (550, altura_texto), PRETO)
        mostra_texto(raddr, (1000, altura_texto), PRETO)
        mostra_texto(c.status, (1350, altura_texto), PRETO)
        mostra_texto(c.pid, (1600, altura_texto), PRETO) 
        mostra_texto(proto, (1750, altura_texto), PRETO)
        altura_texto += 15
        
        mostra_texto_grande('Monitoramento do tráfego por processos',(250,100),PRETO)
        mostra_texto('NOME', (150, altura_texto2), PRETO)
        mostra_texto('ENDEREÇO LOCAL', (550, altura_texto2), PRETO)
        mostra_texto('ENDEREÇO REMOTO', (1000, altura_texto2), PRETO)
        mostra_texto('STATUS', (1350, altura_texto2), PRETO)
        mostra_texto('PID', (1600, altura_texto2), PRETO)
        mostra_texto('PROTOCOLO', (1750, altura_texto2), PRETO)

def retorna_codigo_ping(hostname):
    plataforma = platform.system()
    args = []
    if plataforma == "Windows":
        args = ["ping", "-n", "1", "-l", "1", "-w", "100", hostname]
  
    else:
        args = ['ping', '-c', '1', '-W', '1', hostname]
        
    ret_cod = subprocess.call(args,
                                stdout=open(os.devnull, 'w'),
                                stderr=open(os.devnull, 'w'))
    return ret_cod


def verifica_hosts(base_ip):
    host_validos = []
    return_codes = dict()
    
    for i in range(1, 255):
        return_codes[base_ip + '{0}'.format(i)] =   retorna_codigo_ping(base_ip + '{0}'.format(i))
        if i %20 ==0:
            print(".", end = "")
        if return_codes[base_ip + '{0}'.format(i)] == 0:
            host_validos.append(base_ip + '{0}'.format(i))
    
    return host_validos

def desenha_grafico(tempos, valores, titulo):
    fig, ax = plt.subplots()
    fig.set_size_inches(5, 5)  
    ax = fig.gca()
    y_pos = np.arange(len(tempos))
    ax.plot(tempos, valores)
    ax.set_xlabel('Medições')
    ax.set_title(titulo)


    canvas = agg.FigureCanvasAgg(fig)
    canvas.draw()
    renderer = canvas.get_renderer()
    raw_data = renderer.tostring_rgb()
    return canvas, raw_data

def mostra_matplot():
    tempos = []
    valores = []
    valores_mem = []

    for i in range(0,100):
        tempos.append(i)
        valores.append(psutil.cpu_percent())
        mem = psutil.virtual_memory()
        valores_mem.append(round((mem.used/mem.total),3) * 100)
        sleep(0.01)

    canvas, raw_data = desenha_grafico(tempos,valores, "CPU %")
    size = canvas.get_width_height()
    surf = pygame.image.fromstring(raw_data, size, "RGB")
    tela.blit(surf, (275,440))
    
    canvas, raw_data2 = desenha_grafico(tempos, valores_mem, "MEMÓRIA %")

    surf = pygame.image.fromstring(raw_data2, size, "RGB")
    tela.blit(surf, (1100,440))

    pygame.display.flip()
    
    
    
terminou = False
while not terminou:
    
    abas = desenha_abas()
    
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminou = True
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                for index, aba in enumerate(abas):
                    if aba.collidepoint(pos):
                        texto = f'clicou na aba {index}'
                        if index == 0:
                            tela.fill(BRANCO)
                            mostra_uso_memoria()
                            mostra_uso_cpu()
                            mostra_uso_disco()
                            mostra_matplot()
                        elif index == 1:
                            tela.fill(BRANCO)
                            mostra_info_cpu()
                            mostra_uso_nucleo(tela, l_cpu_percent)
                        elif index == 2:
                            mostrar_arquivos()
                        elif index == 3:
                            tela.fill(BRANCO)
                            mostra_info()
                        elif index == 4:
                            tela.fill(BRANCO)
                            uso_rede_processo()
                        elif index == 5:
                            tela.fill(BRANCO)
                            mostra_info()
                        elif index ==6:
                            tela.fill(BRANCO)
                            mostra_info2()
                        elif index == 7:
                            tela.fill(BRANCO)
                            mostra_info3()
                        elif index == 8:
                            tela.fill(BRANCO)
                            mostra_info4()
                        elif index == 9:
                            tela.fill(BRANCO)
                            mostra_info5()
                        elif index == 10:
                            tela.fill(BRANCO)
                            uso_rede_processo()
                        elif index == 11:
                            tela.fill(BRANCO)
                            uso_rede_processo2()
                        elif index == 12:
                            tela.fill(BRANCO)
                            uso_rede_processo3()
                            mostra_rede()
                            ip_string = '192.168.0.1'
                            ip_lista = ip_string.split('.')
                            base_ip = ".".join(ip_lista[0:3]) + '.'
                            mostra_texto(verifica_hosts(base_ip), (325,975), PRETO)
                            
                            
                           
                        else:
                            tela.fill(BRANCO)
                    
                         
    pygame.display.update()
pygame.display.quit()
pygame.quit()