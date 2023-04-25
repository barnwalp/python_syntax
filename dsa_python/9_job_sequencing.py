from operator import itemgetter


def job_sequencing(input_data):
    # finding the maximum deadline in the given job_details
    maximum = max(input_data, key=itemgetter(0))[0]

    # sort the job_details in descending order based on profit
    input_data = sorted(input_data, key=itemgetter(1), reverse=True)

    # create an array of size of max deadline
    sequenced_data = [0] * (maximum)

    count = 0
    profit = 0
    for index in reversed(range(0, maximum)):
        sequenced_data[index] = input_data[count][1]
        count += 1
        profit += sequenced_data[index]

    return profit


job_details = [
    (5, 200),
    (3, 180),
    (3, 190),
    (2, 300),
    (4, 120),
    (2, 100)
]

print("\nMaximum achievable profit for the job: " + str(job_details) + " is: " + str(job_sequencing(job_details)))