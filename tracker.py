import time

history = []

def record(action):
    history.append((action, time.time()))

def get_data():
    return history
