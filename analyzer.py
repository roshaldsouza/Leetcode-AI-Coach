def analyze(stats):
    
    result = {}

    for item in stats:
        result[item["difficulty"]] = item["count"]

    return result