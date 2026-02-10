# Demo logic - simplified version
from typing import List
from .models import *

PATIENTS = [
    {"id": "p1", "name": "Jan Janssens"},
]

DOCUMENTS = {
    "p1": [
        MedicalDocument(
            id="d1", type="discharge", title="Ontslagbrief orthopedie",
            content="Val met heupfractuur, operatie, valrisico verhoogd.",
            created_at="2026-02-01"
        ),
    ]
}

CONTEXTS = {
    "p1": Context(
        living_situation="alone", age=82, has_informal_caregiver=True,
        caregiver_burden="medium", discharge_type="planned", mobility="needs_assistance"
    )
}

PROVIDERS = [
    Provider(id="prov1", name="Thuisverpleging De Zorgzame", role="nurse",
             specialization="wound_care", location="Herentals", language="NL",
             culture="BE", availability="soon"),
]

CAREPLANS = {}
COMMUNICATION = {}
DASHBOARD = {}

def scrape_documents(patient_id: str):
    return DOCUMENTS.get(patient_id, [])

def detect_problem_areas(docs):
    return [ProblemArea(id="pa_fall", category="fall", label="Valrisico", severity="high", active=False)]

def context_filter(patient_id: str, problems):
    for p in problems[:3]:
        p.active = True
    return problems

def build_bundles(patient_id: str, problems):
    bundles = []
    for p in problems:
        if p.active and p.category == "fall":
            bundles.append(CareBundle(
                id="b_fall", theme="fall", title="Valrisico & veiligheid",
                items=[
                    BundleItem(type="care", role="nurse", description="Valrisicoscreening"),
                    BundleItem(type="wellbeing", role="occupational_therapist", description="Woningaanpassingen"),
                    BundleItem(type="practical", role="practical_service", description="Alarmknop"),
                ]
            ))
    return bundles

def suggested_roles_for_bundles(bundles):
    return [ProviderRole(role="nurse"), ProviderRole(role="occupational_therapist")]

def match_providers(location: str, roles):
    return [p for p in PROVIDERS if p.location == location]

def build_careplan(patient_id: str, bundles):
    cp = CarePlan(
        id=f"cp_{patient_id}", patient_id=patient_id,
        professional_view=CarePlanProfessional(
            medical_summary="Heupfractuur na val, verhoogd valrisico.",
            context_summary="82-jarige alleenwonende met mantelzorg.",
            bundles=bundles,
            medication_overview="Polyfarmacie, bloeddrukmedicatie."
        ),
        patient_view=CarePlanPatient(
            plain_language_summary="U bent gevallen en geopereerd. We zorgen voor veilig herstel thuis.",
            what_and_why="Focus op valveiligheid en medicatie.",
            choices_explained="U kiest zelf welke zorgverleners u wilt.",
            reassurance="Uw traject wordt opgevolgd door de Nurseline."
        )
    )
    CAREPLANS[patient_id] = cp
    return cp

def build_communication(patient_id: str):
    return [
        CommunicationAgreement(
            who="huisarts ↔ verpleegkundige", topic="medicatie",
            channel="EPD / telefoon", when_escalate="bij acute wijziging"
        )
    ]

def ensure_dashboard_item(patient_id: str, patient_name: str):
    if patient_id in DASHBOARD:
        return DASHBOARD[patient_id]
    item = DashboardItem(
        patient_id=patient_id, patient_name=patient_name,
        discharge_status="recently_discharged",
        active_careplan_id=f"cp_{patient_id}",
        context_changes=[],
        medication_alerts=["Start anticoagulantia."],
        communication_signals=["Nieuw zorgplan aangemaakt."]
    )
    DASHBOARD[patient_id] = item
    return item
