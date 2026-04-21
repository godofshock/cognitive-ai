from tracker.tracker import record, get_data
from analysis.analyzer import analyze

# simulate user actions
record("click")
record("type")
record("submit")

data = get_data()

print("User behavior speed:", analyze(data))
