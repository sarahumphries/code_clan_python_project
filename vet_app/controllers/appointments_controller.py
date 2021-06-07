
from db.run_sql import run_sql
from flask import Flask, render_template, redirect, Blueprint, request
from repositories import owner_repository, vet_repository, pet_respository, appointment_repository


appointments_blueprint = Blueprint("appointments", __name__)

@appointments_blueprint.route('/appointments')
def list_all_appointments():
    appointments = appointment_repository.select_all()

    return render_template('appointments/index.html', appointments = appointments)

@appointments_blueprint.route('/appointments/new')
def new_appointment_form():
    vets = vet_repository.select_all()
    pets = pet_respository.select_all()

    return render_template('appointments/new.html', vets = vets, pets = pets)

