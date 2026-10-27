# NG League

Página de la liga de PES NG League: base de jugadores, plantillas con presupuesto, plantillas de todos, liga (calendario, tabla, goleadores), draft e historia de los clubes.

- `index.html`: la página completa, lista para publicar (GitHub Pages).
- `src/template.html`: código fuente de la página. `src/build.py` la arma con los datos de jugadores.
- `firestore.rules`: reglas de seguridad para pegar en Firebase > Firestore > Reglas.
- Inicio de sesión con Google y datos en Firebase (proyecto `ng-league`). El organizador se define por correo en `ADMINS` (en la plantilla) y en `firestore.rules`.
