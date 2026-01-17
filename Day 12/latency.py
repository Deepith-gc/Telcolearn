# latency_values = [20,30,35,67,89,34,67,88]

# def calc_avg(data):
#     return sum(data) / len(data)

# def get_summary(data):
#     minimum = min(data)
#     maximum = max(data)
#     average = calc_avg(data)
   
#     return minimum, maximum, average
# result = get_summary(latency_values)
# print("Latency summary", result)

def avg1(l):
    total =sum(l)
    avg = total/len(l)

def MinMaxAvg(l):
    minimum = min(l)
    maximum = max(l)
    average = avg1(l)
    dict = {'minimim':minimum,'maximum':maximum,'average':average}
    return dict

latency_values = [10,15,22,34,50]
print(MinMaxAvg(latency_values))