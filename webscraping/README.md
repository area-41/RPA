## Web Scraping com Beautiful Soup (bs4.py)

Este notebook explora o conceito de Web Scraping utilizando a biblioteca Beautiful Soup, que pode ser instalada com pip install beautifulsoup4. Ele é dividido em duas seções principais:

Operações Básicas de Web Scraping com Beautiful Soup: demonstra as funcionalidades básicas da biblioteca, como análise de HTML, formatação de saída, acesso a elementos e filtragem por atributos, utilizando como exemplo o site Quotes to Scrape para extrair citações, autores e tags.

Web Scraping de Livros do Books to Scrape: apresenta um exemplo mais complexo de web scraping, coletando informações detalhadas sobre livros (título, preço, disponibilidade e classificação) de um site fictício de livraria, o Books to Scrape. O processo envolve a navegação por múltiplas páginas, organização dos dados em um DataFrame do Pandas e a exportação para um arquivo Excel (.xlsx).

Operações Básicas de Web Scraping com Beautiful Soup
Primeiro, vamos explorar as funcionalidades básicas da biblioteca Beautiful Soup para extrair dados de páginas web. Vamos analisar o HTML, transformando o conteúdo em um objeto Python para fácil navegação e busca, formatar a saída para visualizar o código HTML de forma mais clara e organizada, acessar elementos específicos, seja o primeiro correspondente ou todos os que satisfaçam determinados critérios, e filtrar por atributos, realizando buscas utilizando tags HTML, classes CSS e conteúdos de atributos para identificar e extrair os dados.

Para isso, vamos utilizar o site Quotes to Scrape. A partir dele, vamos extrair as citações e os autores, além das tags sobre cada citação.

## Web Scraping de Livros do Books to Scrape (webscraping_books.py)

Nesse exemplo, vamos realizar o web scraping em um site fictício de livraria, o Books to Scrape, para coletar informações detalhadas sobre livros. O objetivo é extrair dados como título, preço, disponibilidade e classificação de estrelas de cada livro, navegando por múltiplas páginas do site.

Após a coleta, os dados serão organizados em um DataFrame do Pandas e, em seguida, salvos em uma planilha (.xlsx).