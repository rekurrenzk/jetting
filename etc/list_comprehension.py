"""
                distance<=10km          distance > 10km

regular              0.5                   0.3
student              0.3                   0.1
teacher              0.4                   0.2
senior citizens      0.3                   0.2


"""

distance = int(input("your distance: "))
cardInfo = input("your card: ")


passenger = {

        "regular": {
            "regular_under": int(distance) * 0.5,
            "regular_over": int(distance) * 0.3

        },

        "student": {
            "student_under": int(distance) * 0.3,
            "student_over": int(distance) * 0.1

        },

        "teacher": {
            "teacher_under": int(distance) * 0.4,
            "teacher_over": int(distance) * 0.2

        },

        "senior": {
            "senior_under": int(distance) * 0.3,
            "senior_over": int(distance) * 0.2

        }
    }
dataSv = []

def main():

    if passenger.keys():

        overPassenger = list(passenger.values())
        print(type(overPassenger))

        if passenger.keys() in overPassenger:

            dataSv.append(overPassenger)
            print(dataSv)





main()
"""
if "student" in cardInfo:
    
    if distance > 10:
        return overPassenger"""


"""
def money(): ### showing how much is the cost

    return print(distance * cardFare, "$")


def fare(passenger):

    for i in passengerDict.keys():

        if passenger in passengerDict.keys():

            if distance > 10:

                print(passengerDict.values()[1], money())

            if distance <= 10:
                print(passengerDict.values()[0], money())

            return passenger

    passenger = cardInfo


fare(cardInfo)"""