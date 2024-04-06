import re

def separador_arquivo_lrd(arquivoEntrada):
    # função para garantir o inicio e fechamento do arquivo. feito pelo o arquivo.read()
    with open(arquivoEntrada, 'r', encoding='utf-8') as arquivo:
        conteudoLdr = arquivo.read()
    
    resultado_do_arquivo_aberto = re.finditer(r'<nfeProc[^>]*>.*?</nfeProc>', conteudoLdr, re.DOTALL)

    # laço para enumerar a saida de cada arquivo emitido
    for i, match in enumerate(resultado_do_arquivo_aberto, 1):
        arquivo_xml_gerado = match.group()

        arquivo_xml_gerado = arquivo_xml_gerado.replace('{EOL}', '')

        # em caso de duplicação de aspas duplas
        arquivo_xml_gerado = re.sub(r'""', '"', arquivo_xml_gerado)

        # parte onde faz a criação do arquivos de saída
        arquivoSaida = f'nota_{i}.xml'
        
        # função para garantir o inicio e fechamento do arquivo. feito pelo o arquivo.read()
        with open(arquivoSaida, 'w', encoding='utf-8') as arquivo_saida:
            arquivo_saida.write(arquivo_xml_gerado)

if __name__ == "__main__":
    arquivoEntrada = 'notas.ldr'
    separador_arquivo_lrd(arquivoEntrada)

