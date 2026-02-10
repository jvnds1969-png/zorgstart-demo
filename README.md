# Zorgstart Demo

**Van ontslag naar levenslang thuis blijven**

Zorgstart is een zorgcoordinatie- en matchmakingsplatform dat mensen helpt om langer gezond, zelfstandig en veilig thuis te blijven - vanaf ontslag en ver daarna.

## Architectuur

- **Backend:** FastAPI (Python) met in-memory demodata
- **Frontend:** React + TypeScript + Vite

## Snel starten

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

De API draait op http://localhost:8000

### Frontend

```bash
cd frontend
npm install
npm run dev
```

De frontend draait op http://localhost:5173

## Visie

Zorgstart verbindt medische realiteit, levenscontext en keuzevrijheid tot een dynamisch traject dat ontslag mogelijk maakt en zelfstandig thuis leven duurzaam ondersteunt.
