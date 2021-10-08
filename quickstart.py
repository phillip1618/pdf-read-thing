import tabula

url = 'cp44007.pdf'
table = tabula.read_pdf(url, pages='all', multiple_tables=True)

print(table)