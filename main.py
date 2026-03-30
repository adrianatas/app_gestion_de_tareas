from flask import Flask, render_template, request, url_for, redirect
import db
from models import Tarea

app = Flask(__name__)

@app.route('/')
def home():
    todas_las_tareas = db.session.query(Tarea).all()
    print(todas_las_tareas)
    return render_template("index.html", lista_de_tareas=todas_las_tareas)

@app.route("/crear-tarea", methods=["GET", "POST"])
def crear():
    contenido = request.form.get("contenido-tarea")
    categoria = request.form.get("categoria-tarea")
    fecha_limite = request.form.get("fecha_limite_tarea") # viene en formato str YYYY-MM-DD

    #Convertir a objeto date si no esta vacio
    from datetime import datetime
    fecha_obj = datetime(fecha_limite, "%Y-%m-%d").date() if fecha_limite else None
    print(contenido)
    tarea = Tarea(contenido=contenido, categoria=categoria, hecha=False, fecha_limite=fecha_obj)
    db.session.add(tarea)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/editar-tarea/<int:id>", methods=["GET"])
def editar(id):
    tarea = db.session.query(Tarea).filter_by(id=id).first()
    return render_template("editar_tarea.html", tarea=tarea)

@app.route("/actualizar-tarea/<int:id>", methods=["POST"])
def actualizar(id):
    tarea = db.session.query(Tarea).filter_by(id=id).first()
    tarea.contenido = request.form.get("contenido-tarea")
    tarea.categoria = request.form.get("categoria-tarea","")
    fecha_limite = request.form.get("fecha_limite-tarea")
    from datetime import datetime
    tarea.fecha_limite = datetime.strptime(fecha_limite, "%Y-%m-%d").date() if fecha_limite else None

    db.session.commit()
    return redirect(url_for("home"))


@app.route("/eliminar-tarea/<id>")
def eliminar(id):
    db.session.query(Tarea).filter_by(id=int(id)).delete()
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/tarea-hecha/<id>")
def hecha(id):
    tarea = db.session.query(Tarea).filter_by(id=int(id)).first()
    tarea.hecha = not(tarea.hecha)
    db.session.commit()
    return redirect(url_for("home"))

if __name__ == '__main__':
    db.Base.metadata.create_all(bind=db.engine) # Creamos el modelo de datos
    app.run(debug=True)