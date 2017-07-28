Chris = ['Evans', 'Hemsworth', 'Paul', 'Pine', 'Pratt', 'Rock']
first = 0
last = len(Chris) - 1
notfound = True

term = input("Which Chris are you looking for?")

#index = (int(first + last)/2) here?

while first<= last and notfound:
    index = int((first + last)/2)
    if Chris[index] == term:
        notfound = False
        print("congratulations, you found him")
    else:
        if term < Chris[index]:
            last = index - 1
        else:
            first = index + 1
