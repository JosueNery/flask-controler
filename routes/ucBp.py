from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from ..extensions import db
from ..models.uc import Uc
from datetime import date, datetime

ucBp = Blueprint('ucBp', __name__)


@ucBp.route('/uc')
def uc_list():
    db.create_all()
    ucs_query = Uc.query.all()
    return render_template('uc_list.html', ucs=ucs_query)


@ucBp.route('/uc/create')
@login_required
def create_uc():
    return render_template('uc_create.html')


@ucBp.route('/uc/add', methods=['POST'])
@login_required
def add_uc():

    sNome = request.form["nome"]
    sTipo = request.form["tipo"]
    dInicio = datetime.strptime(request.form["inicio"], '%Y-%m-%d')
    dFim = datetime.strptime(request.form["fim"], '%Y-%m-%d')

    uc = Uc(nome=sNome, tipo=sTipo, inicio=dInicio, fim=dFim)
    db.session.add(uc)
    db.session.commit()

    return redirect(url_for('ucBp.uc_list'))


@ucBp.route('/uc/update/<uc_id>')
@login_required
def update_uc(uc_id=0):
    uc_query = Uc.query.filter_by(id=uc_id).first()
    return render_template('uc_update.html', uc=uc_query)


@ucBp.route('/uc/upd', methods=['POST'])
@login_required
def upd_uc():

    iUc = request.form["id"]
    sNome = request.form["nome"]
    sTipo = request.form["tipo"]
    dInicio = datetime.strptime(request.form["inicio"], '%Y-%m-%d')
    dFim = datetime.strptime(request.form["fim"], '%Y-%m-%d')

    uc = Uc.query.filter_by(id=iUc).first()
    uc.nome = sNome
    uc.tipo = sTipo
    uc.inicio = dInicio
    uc.fim = dFim
    db.session.add(uc)
    db.session.commit()

    return redirect(url_for('ucBp.uc_list'))


@ucBp.route('/uc/delete/<uc_id>')
@login_required
def delete_uc(uc_id=0):
    uc_query = Uc.query.filter_by(id=uc_id).first()
    return render_template('uc_delete.html', uc=uc_query)


@ucBp.route('/uc/dlt', methods=['POST'])
@login_required
def dtl_uc():

    iUc = request.form["id"]
    uc = Uc.query.filter_by(id=iUc).first()
    db.session.delete(uc)
    db.session.commit()

    return redirect(url_for('ucBp.uc_list'))
