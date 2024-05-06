import os, json, sys
try:
  import g4f
except:
  os.system('pip install g4f')
import g4f


def zapisz_pytanie(pytanie):
  with open('pytania.txt', 'a') as f:
    f.write(pytanie + '\n')


def odczytaj_pytania():
  with open('pytania.txt', 'r') as f:
    zawartosc = f.readlines()
  return zawartosc


def generuj_pytanie(stawka):
  try:
    response = g4f.ChatCompletion.create(
        model='gpt-4',
        messages=[{
            "role":
            "user",
            "content":
            '''Generuj pytanie do gry "Milionerzy" z podanymi odpowiedziami A, B, C, D oraz poprawną odpowiedzią z zachowaniem formatu: ```
    {"question": "{pytanie}", "a": "{odpowiedź A bez literki}", "b": "{odpowiedź B bez literki}", "c": "{odpowiedź C bez literki}", "d": "{odpowiedź D bez literki}", "correct": "{poprawna odpowiedź jako duża litera}"}```. Jedna ważna informacja: odpowiadaj dokładnie w tym formacie, bez **żadnych dodatkowych znaków** (w tym bez znaku ` ). '''
        }],
    )
    response_dict = json.loads(response)
    return response_dict
  except:
    return None


def main():
  os.system('cls')
  os.system('clear')
  stawka = 100
  pytanie = ' '
  while True:
    old_pytanie = pytanie
    pytanie = generuj_pytanie(stawka)
    if isinstance(pytanie, dict) and isinstance(
        old_pytanie,
        dict) and 'question' in pytanie and 'question' in old_pytanie:
      if pytanie['question'] == old_pytanie['question']:
        pytanie = generuj_pytanie(stawka)
    if pytanie:
      os.system('cls')
      os.system('clear')
      print(f"Odpowiedz na pytanie, aby wygrać {stawka}zł!")
      print("Oto pytanie:", pytanie['question'])
      print("A:", pytanie['a'])
      print("B:", pytanie['b'])
      print("C:", pytanie['c'])
      print("D:", pytanie['d'])
      odpowiedz = input("Podaj poprawną odpowiedź (A, B, C lub D): ").upper()
      if isinstance(pytanie, dict) and 'correct' in pytanie:
        poprawna_odpowiedz = pytanie['correct']
        if odpowiedz == poprawna_odpowiedz:
          print("Gratulacje, prawidłowa odpowiedź!")
          if stawka == 100:
            stawka = 200
          elif stawka == 200:
            stawka = 300
          elif stawka == 300:
            stawka = 500
          elif stawka == 500:
            stawka = 1000
          elif stawka == 1000:
            stawka = 2000
          elif stawka == 2000:
            stawka = 4000
          elif stawka == 4000:
            stawka = 8000
          elif stawka == 8000:
            stawka = 16000
          elif stawka == 16000:
            stawka = 32000
          elif stawka == 32000:
            stawka = 64000
          elif stawka == 64000:
            stawka = 125000
          elif stawka == 125000:
            stawka = 250000
          elif stawka == 250000:
            stawka = 500000
          elif stawka == 500000:
            stawka = 1000000
          elif stawka == 1000000:
            print('Gratulacje, wygrałeś grę!')
            break

        else:
          print(
              f"Niestety, zła odpowiedź, prawidłowa odpowiedź to odpowiedź {pytanie['correct']}. Koniec gry."
          )
          break
      else:
        pass
    else:
      pass


if __name__ == '__main__':
  main()
