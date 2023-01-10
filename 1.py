from collections import deque

daily_portions_steak = [int(x) for x in input().split(', ')]
daily_stamina = [int(x) for x in input().split(', ')]
daily_stamina_queue = deque(daily_stamina)
conquered_peaks = []

peaks_and_high = [
    ('Vihren', 80),
    ('Kutelo', 90),
    ('Banski Suhodol', 100),
    ('Polezhan', 60),
    ('Kamenitza', 70),

]
i=0
while i < len(peaks_and_high):
    peak, high = peaks_and_high[i]
    if daily_stamina and daily_stamina_queue:
        portion = daily_portions_steak.pop()
        stamina = daily_stamina_queue.popleft()
        daily_expense = portion + stamina
        if daily_expense >= high:
            conquered_peaks.append(peak)
            i+=1
    else:
        break

if len(conquered_peaks) == len(peaks_and_high):
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
    print("Conquered peaks:")
    for pea in conquered_peaks:
        print(pea)
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
