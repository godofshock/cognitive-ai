def analyze(data):
    speeds = []

    for i in range(1, len(data)):
        diff = data[i][1] - data[i-1][1]
        speeds.append(diff)

    avg_speed = sum(speeds)/len(speeds) if speeds else 0

    return avg_speed
