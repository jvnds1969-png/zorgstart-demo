from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from .models import *
from . import logic

app = FastAPI(title="Zorgstart Demo API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/patients")
def list_patients():
    return logic.PATIENTS

@app.get("/patients/{patient_id}/documents", response_model=List[MedicalDocument])
def get_documents(patient_id: str):
    return logic.scrape_documents(patient_id)

@app.get("/patients/{patient_id}/problem-areas", response_model=List[ProblemArea])
def get_problem_areas(patient_id: str):
    docs = logic.scrape_documents(patient_id)
    return logic.detect_problem_areas(docs)

@app.get("/patients/{patient_id}/active-problems", response_model=List[ProblemArea])
def get_active_problems(patient_id: str):
    docs = logic.scrape_documents(patient_id)
    problems = logic.detect_problem_areas(docs)
    return logic.context_filter(patient_id, problems)

@app.get("/patients/{patient_id}/bundles", response_model=List[CareBundle])
def get_bundles(patient_id: str):
    docs = logic.scrape_documents(patient_id)
    problems = logic.detect_problem_areas(docs)
    active = logic.context_filter(patient_id, problems)
    return logic.build_bundles(patient_id, active)

@app.get("/patients/{patient_id}/suggested-providers", response_model=List[Provider])
def get_suggested_providers(patient_id: str, location: str = "Herentals"):
    docs = logic.scrape_documents(patient_id)
    problems = logic.detect_problem_areas(docs)
    active = logic.context_filter(patient_id, problems)
    bundles = logic.build_bundles(patient_id, active)
    roles = logic.suggested_roles_for_bundles(bundles)
    return logic.match_providers(location, roles)

@app.get("/patients/{patient_id}/careplan", response_model=CarePlan)
def get_careplan(patient_id: str):
    docs = logic.scrape_documents(patient_id)
    problems = logic.detect_problem_areas(docs)
    active = logic.context_filter(patient_id, problems)
    bundles = logic.build_bundles(patient_id, active)
    return logic.build_careplan(patient_id, bundles)

@app.get("/patients/{patient_id}/communication", response_model=List[CommunicationAgreement])
def get_communication(patient_id: str):
    return logic.build_communication(patient_id)

@app.get("/dashboard", response_model=List[DashboardItem])
def get_dashboard():
    items = []
    for p in logic.PATIENTS:
        item = logic.ensure_dashboard_item(p["id"], p["name"])
        items.append(item)
    return items
