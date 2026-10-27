# NG League

Página de la liga de PES NG League: base de jugadores, plantillas con presupuesto, plantillas de todos, liga (calendario, tabla, goleadores), draft e historia de los clubes.

- `index.html`: la página completa, lista para abrir (incluye datos de jugadores, escudos, logo y foto de portada).
- `src/template.html`: código fuente de la página (con marcadores `__DATA__`, `__COUNTRIES__`, `__CRESTS__`).
- `src/build.py`: arma `index.html` a partir de la plantilla y de los datos.
- `src/crests.json`, `src/hero.b64`, `src/logo.b64`: escudos, foto de portada y logo codificados.
