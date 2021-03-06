from bs4 import BeautifulSoup

html = """
<html>
 <body>
  <div>
   <ul>
    <li>A</li>
    <li>B</li>
    <li>C</li>
   </ul>
  </div>
 </body>
</html>
"""

# Removendo caracter '\n' para evitar problemas.
html = html.strip().split()
html = ''.join(html)

soup = BeautifulSoup(html, "lxml")

li_meio = soup.find_all("li")[1] # <li>B</li>

print(li_meio)                   # <li>B</li>
print(li_meio.next_sibling)      # <li>C</li>
print(li_meio.previous_sibling)  # <li>A</li>