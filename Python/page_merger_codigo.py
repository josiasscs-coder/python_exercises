
#Juntar várias páginas de varios PDFs em um só ficheiro utilizando a biblioteca PyPDF2
from PyPDF2 import PdfReader, PdfWriter

# Estrutura de dados: ficheiro e páginas a extrair
estrutura_dados = {
    "pdf_exemplo.pdf":[0],
    "pdf_exemplo2.pdf":[0,1,2],
    "pdf_exemplo3.pdf":[2,5]
    }


# Abrir e tentar precaver potenciais erros no nosso ficheiro
def ler_pdf (ficheiro_entrada):
    try:
        input_pdf = PdfReader(ficheiro_entrada)
        return input_pdf

# Mostra mensagem de erro se não conseguir abir o ficheiro   
    except ValueError as e:
        print(f"Erro: {e}")
        return None

# Função para criar um novo PDf e junta as páginas dos nossos ficheiros    
def criar_pdf(estrutura_dados):
    writer = PdfWriter()
    
    for ficheiro, paginas in estrutura_dados.items():
        reader = ler_pdf(ficheiro)
        if reader is None:
            continue

# Validação do indice        
        for pagina in paginas:
            if not isinstance(pagina,int):
                print(f"Erro: indice em página {pagina}, não é inteiro")
                continue

            if pagina < len(reader.pages):
                page = reader.pages[pagina]
                writer.add_page(page)
            else:
                print(f"Página {pagina} não existe em pdf {ficheiro}")

    with open ("pdf_final.pdf", "wb") as f:
        writer.write(f)

# Função para aplicar marca de água às páginas 1, 3 e 5
def aplicar_marca_agua():
    reader = PdfReader("pdf_final.pdf")
    writer = PdfWriter()

    marca_reader = PdfReader("pdf_watermark.pdf")
    marca = marca_reader.pages[0]
    
    paginas_marca = [0, 2, 4]

    for i, pagina in enumerate(reader.pages):
        if i in paginas_marca:
            pagina.merge_page(marca)
        writer.add_page(pagina)

# Guardar o pdf final com a marca de água
    with open("pdf_final_marca.pdf", "wb") as f:
        writer.write(f)
    

    print(f"Páginas e marca de água adicionadas com sucesso no ficheiro pdf_final_marca.pdf")

 # Executar programa
criar_pdf(estrutura_dados)
aplicar_marca_agua()       
