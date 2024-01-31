# Cuerpo del código HTML con el bucle para generar imágenes
html_cuerpo = ''
for i in range(1, 61):
    numero_formateado = f"{i:02d}"  # Formatea el número para que tenga dos dígitos (por ejemplo, 01 en lugar de 1)
    imagen_url = f'assets/prototype/1_page-00{numero_formateado}.jpg'
    html_cuerpo += f'<section class="prototype" data-auto-animate data-transition="slide-in fade-out" data-background-color="#dedfcf">\n'
    html_cuerpo += f'    <img src="{imagen_url}" alt="" style="width: 100%;">\n'
    html_cuerpo += f'</section>\n'

# Muestra el fragmento sin el inicio del código HTML
print(html_cuerpo)