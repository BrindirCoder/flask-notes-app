from flask import render_template, redirect, url_for, request, abort, flash
from models import NoteData
from app import db
from datetime import datetime


def register_routes(app):
    @app.route("/")
    def index():
        notes = NoteData.query.all()
        return render_template("index.html", notes=notes)

    @app.route("/add", methods=["GET", "POST"])
    def add_note():
        if request.method == "POST":
            title = request.form.get("title")
            content = request.form.get("content")
            if not title or not content:
                flash("Please provide title and content!", "error")
                return redirect(url_for("add_note"))
            new_note = NoteData(title=title, content=content)
            db.session.add(new_note)
            db.session.commit()
            return redirect(url_for("index"))

        return render_template("addnote.html")

    @app.route("/edit/<int:id>", methods=["GET", "POST"])
    def edit_note(id):
        item = NoteData.query.get(id)
        if item is None:
            # return 404 or show friendly message
            abort(404, description="Note not found")

        if request.method == "POST":
            item.title = request.form.get("title", item.title)
            item.content = request.form.get("content", item.content)
            db.session.commit()

            # redirect to avoid re-post on refresh
            return redirect(url_for("all_notes"))

        return render_template("edit_note.html", item=item)

    @app.route("/all")
    def all_notes():
        notes = NoteData.query.all()
        return render_template("allnotes.html", notes=notes)

    @app.route("/show_note_to_delete")
    def show_note_to_delete():
        notes = NoteData.query.all()
        return render_template("delete_note.html", notes=notes)

    @app.route("/delete/<int:id>", methods=["GET", "POST"])
    def delete_note(id):
        item = NoteData.query.get_or_404(id)
        db.session.delete(item)
        db.session.commit()
        return redirect(url_for("show_note_to_delete"))

    @app.route("/note_detail")
    def note_detail():
        notes = NoteData.query.all()
        return render_template("note_detail.html", notes=notes)

    @app.route("/sortenote")
    def sorte_note():
        sort_order = request.args.get("order", "new")  # default: newest first

        if sort_order == "old":
            sorted_notes = NoteData.query.order_by(NoteData.date.asc()).all()
        else:
            sorted_notes = NoteData.query.order_by(NoteData.date.desc()).all()

        return render_template(
            "sorte_note_by_date.html", sorte_note=sorted_notes, order=sort_order
        )
