score = 100
attempt = 0
print("""Перед вами мишень и у Вас четыре попытки.
Вы можете попасть(hit) или промахнуться(miss).
Изначально ваш счет равен 100.
Попали +10 очков. Промазали -20 очков.
Итак, дерзайте!""")
while attempt <= 3:
  gunshot = input()
  if gunshot == "hit":
    score += 10
  elif gunshot == "miss":
    score -= 20
  attempt += 1
print(str(score))