# Carbon-Aware Route Optimizer (Hackathon Starter)

## Setup
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate   # (On Windows: venv\Scripts\activate)

# Install dependencies
pip install -r requirements.txt
```

## Train PPO Agent
```bash
cd train
python train_ppo.py
```

## Run Demo App
```bash
cd demo
streamlit run app.py
```

## Notes
- This is a toy synthetic environment for hackathon prototyping.
- Integrate with real AWS Location Service & emission data later.
# carbon_aware_route_optimizer
