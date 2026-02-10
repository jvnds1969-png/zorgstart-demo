from typing import List, Optional
from pydantic import BaseModel


class MedicalDocument(BaseModel):
    id: str
    type: str
    title: str
    content: str
    created_at: str


class ProblemArea(BaseModel):
    id: str
    category: str
    label: str
    severity: str
    active: bool = False


class Context(BaseModel):
    living_situation: str
    age: int
    has_informal_caregiver: bool
    caregiver_burden: str
    discharge_type: str
    mobility: str


class BundleItem(BaseModel):
    type: str
    role: str
    description: str


class CareBundle(BaseModel):
    id: str
    theme: str
    title: str
    items: List[BundleItem]


class ProviderRole(BaseModel):
    role: str
    specialization: Optional[str] = None


class Provider(BaseModel):
    id: str
    name: str
    role: str
    specialization: Optional[str]
    location: str
    language: str
    culture: Optional[str]
    availability: str


class CarePlanProfessional(BaseModel):
    medical_summary: str
    context_summary: str
    bundles: List[CareBundle]
    medication_overview: str


class CarePlanPatient(BaseModel):
    plain_language_summary: str
    what_and_why: str
    choices_explained: str
    reassurance: str


class CarePlan(BaseModel):
    id: str
    patient_id: str
    professional_view: CarePlanProfessional
    patient_view: CarePlanPatient


class CommunicationAgreement(BaseModel):
    who: str
    topic: str
    channel: str
    when_escalate: str


class DashboardItem(BaseModel):
    patient_id: str
    patient_name: str
    discharge_status: str
    active_careplan_id: Optional[str]
    context_changes: List[str]
    medication_alerts: List[str]
    communication_signals: List[str]
