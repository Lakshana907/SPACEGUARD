SPACEGUARD
AI-Powered Space-Debris Collision Early-Warning System
IBM Datathon 2026 --- Project Prototype
SPACEGUARD is a full-stack prototype designed to demonstrate how orbital
data can be transformed into understandable collision-risk intelligence.
Instead of only showing where satellites and debris are located, the
concept prioritizes potentially dangerous encounters, explains risk
factors, and raises alerts when a configurable risk threshold is
exceeded.
Prototype limitation: The bundled orbital objects and encounter
records are synthetic demonstration data. Risk values are produced by
a transparent heuristic scoring function, not a trained or validated
AI model. This project is not an operational collision-prediction
service and must not be used for real spacecraft manoeuvres or
collision-avoidance decisions.
Problem statement
The growing number of satellites and debris objects is making Earth's
orbital environment increasingly congested. A collision at orbital
velocity can damage spacecraft and create more fragments, potentially
contributing to the cascading-debris problem commonly called Kessler
Syndrome. Tracking positions alone is not enough for a user who needs
to know which encounters deserve attention first.
Proposed solution
SPACEGUARD demonstrates an early-warning workflow that: 1. Presents
satellite and debris encounters in an interactive 3D orbital scene. 2.
evaluates sample encounter attributes and calculates a collision-risk
score. 3. categorizes encounters into understandable risk levels. 4.
prioritizes high-risk encounters and explains contributing factors. 5.
displays alerts based on a user-adjustable threshold. 6. allows demo
scenarios to be changed to explore how the dashboard responds.
The current prototype uses synthetic data so the workflow can be
demonstrated without depending on a live orbital-data provider.
Key features
- Interactive 3D view: animated Earth, orbital paths, and
  debris/object markers.
- Risk overview: summary indicators and a prioritized encounter
  list.
- Risk explanations: heuristic factors are presented to help users
  understand why an encounter is flagged.
- Alert center: shows encounters that cross the configured
  threshold.
- Adjustable threshold: change the alert sensitivity for the demo.
- Scenario controls: switch between low, elevated, and critical
  sample conditions.
- Beginner-friendly interface: a welcome/login-style screen and a
  "How it works" explanation.
- REST API: FastAPI endpoints supply summary data, encounters,
  alerts, and scenario updates.
- IBM LinuxONE planning notes: deployment considerations are
  documented separately.
Demo sign-in note
The sign-in screen is a local prototype gate only. It does not
authenticate users securely, verify identities, or protect backend
endpoints. Do not enter a real password. Before public deployment,
replace it with a proper identity provider and backend session/token
validation.
Technology stack
  Layer                      Technology              Purpose
  Frontend                   React                   Component-based user
                                                     interface
  Language                   TypeScript              Typed frontend code
  Build and development      Vite                    Local development and
  server                                             production build
  3D visualization           Three.js, React Three   Render the Earth, orbit
                             Fiber, Drei             paths, and object
                                                     markers
  Styling                    CSS                     Responsive dashboard
                                                     and space-themed
                                                     interface
  Backend                    Python, FastAPI         REST API and
                                                     application logic
  API                        FastAPI / OpenAPI       Interactive API
  validation/documentation                           documentation
  Test framework             pytest                  Basic backend
                                                     risk-engine tests
  Demo data and scoring      Python modules          Synthetic encounters
                                                     and heuristic risk
                                                     indices
  Planned deployment target  IBM LinuxONE            Potential future
                                                     hosting environment;
                                                     not automatically
                                                     connected in this
                                                 prototype
System architecture
User
 |
 v
React + TypeScript + Vite frontend
 |  - Login-style demo screen
 |  - 3D orbital visualization
 |  - Encounter table and risk explanations
 |  - Alert threshold and scenario controls
 |
 | HTTP requests
 v
FastAPI backend
 |  - Summary endpoint
 |  - Encounter endpoint
 |  - Alert filtering
 |  - Scenario switching
 |  - Heuristic risk scoring
 |
 v
Synthetic demo orbital data
Current status: the frontend and backend can run locally. The
project does not currently ingest live satellite catalogues, run a
trained machine-learning model, calculate validated orbital
trajectories, or provide real collision probabilities.
Project structure
SPACEGUARD/
├── frontend/
│   ├── src/
│   │   ├── App.tsx
│   │   ├── main.tsx
│   │   └── styles.css
│   ├── index.html
│   ├── package.json
│   ├── tsconfig.json
│   ├── vite.config.ts
│   └── .gitignore
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── data.py
│   │   └── risk_engine.py
│   ├── tests/
│   │   └── test_risk_engine.py
│   ├── requirements.txt
│   └── .gitignore
├── linuxone/
│   └── DEPLOYMENT.md
├── .gitignore
└── README.md
Getting started
Prerequisites
Install: - Git - Node.js 20 or later (npm is included with
Node.js) - Python 3.10 or later - Visual Studio Code (or a
compatible editor such as Antigravity)
1. Open the project
Extract the ZIP. In VS Code, select File → Open Folder and open the
outer SPACEGUARD project folder---the folder that contains frontend,
backend, and README.md.
Open a terminal using Terminal → New Terminal.
2. Start the backend (Terminal 1)
From the project root:
Windows PowerShell
cd backend
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
If PowerShell blocks virtual-environment activation, run this in the
same terminal and retry activation:
Set-ExecutionPolicy -Scope Process Bypass
.\.venv\Scripts\Activate.ps1
Keep this terminal open. Backend URLs: - API root:
http://127.0.0.1:8000/ - Health check:
http://127.0.0.1:8000/health - Interactive API docs:
http://127.0.0.1:8000/docs
3. Start the frontend (Terminal 2)
Open a second terminal. Make sure it starts at the project root, then
run:
cd frontend
npm install
npm run dev
Open the local URL printed by Vite, usually http://localhost:5173/.
If your terminal is already inside frontend, do not run
cd frontend a second time.

4. Build the frontend
From the project root:
cd frontend
npm run build
5. Run backend tests
From the project root, activate the backend virtual environment and run:
cd backend
py -m pip install -r requirements.txt
py -m pytest
If pytest is not installed by the requirements file, install it with
py -m pip install pytest before running the tests.
API endpoints
The backend exposes these demo endpoints:
  Method                  Endpoint                     Purpose
  GET                   /                          API welcome/status
                                                       response
  GET                   /health                    Health check
  GET                   /api/summary               Dashboard summary
                                                       metrics
  GET                   /api/encounters            Sample encounter
                                                       records and risk
                                                       information
  GET                   /api/alerts?threshold=65   Alerts above the
                                                       selected threshold
  POST                  /api/scenarios/low         Load the low-risk demo
                                                       scenario
  POST                  /api/scenarios/elevated    Load the elevated-risk
                                                       demo scenario
  POST                  /api/scenarios/critical    Load the critical-risk
                                                   demo scenario
Open http://127.0.0.1:8000/docs while the backend is running to
inspect the actual request and response schemas.
Risk scoring and alerts
The backend uses a transparent heuristic scoring function to create
a demonstration risk index from the sample encounter attributes. The
dashboard uses that index to prioritize encounters and compare them with
the alert threshold.
- The score is a demo index, not a probability of collision.
- Risk levels are prototype categories, not official
  space-traffic-management classifications.
- Results depend on the synthetic data and current heuristic
  implementation.
- Any real-world system would require validated orbital data,
  uncertainty modelling, calibrated probability estimates, rigorous
  testing, and expert review.
IBM Datathon and IBM LinuxONE direction
The project is prepared as a prototype suitable for demonstrating a
possible space-safety workflow in a datathon setting. Its current
implementation is a local React/FastAPI application. The included
linuxone/DEPLOYMENT.md documents considerations for a potential IBM
LinuxONE deployment.
A future deployment could evaluate IBM LinuxONE as a resilient hosting
platform for API services and data processing, subject to environment
access, architecture review, dependency compatibility, and deployment
testing. This repository does not imply that IBM services or LinuxONE
are already connected or that the application has been deployed to IBM
infrastructure.
Current limitations
- Uses synthetic demonstration data only.
- Uses heuristic scoring rather than a trained AI/ML model.
- Does not calculate precise orbital trajectories or conjunction
  probabilities.
- Does not connect to a live satellite catalogue or space-agency API.
- Demo login is not secure authentication.
- IBM LinuxONE deployment is documented as a future step, not an
  active integration.
Future enhancements
1. Connect to a trusted orbital data source, with data provenance and
   refresh timestamps.
2. Implement validated orbital propagation and closest-approach
   calculations using appropriate domain libraries.
3. Train and evaluate an ML model only after collecting suitable
   labelled data; compare it against transparent baselines.
4. Display uncertainty, confidence, data freshness, and explanations
   alongside risk scores.
5. Add secure authentication, role-based access, audit logs, and
   server-side authorization.
6. Add automated tests, CI checks, containerization, monitoring, and
   deployment automation.
7. Validate performance and dependencies for IBM LinuxONE before
   deployment.
Contributing
1. Create a feature branch.
2. Make a focused change.
3. Run the frontend build and backend tests.
4. Open a pull request with a summary, screenshots where useful, and
   testing notes.
Please do not commit passwords, API tokens, SSH private keys, .env
files, virtual environments, node_modules, or other secrets.
License
No license has been specified yet. Unless a license is added to this
repository, all rights remain with the project author and reuse
permissions are not explicitly granted. Add a suitable LICENSE file
before inviting public reuse.#   S P A C E G U A R D 
 
 