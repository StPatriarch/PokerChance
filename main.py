from time import sleep
import lang_arm as am
import lang_eng as en
import lang_rus as ru

print('Հայերենի համար մուտքագրեք։ H | For English input: E | Для Русского языка введите: R\n')
sleep(0.5)
print('')
sleep(0.5)
user_language = str.upper(input('Լեզու|Language|Язык\t'))

if user_language == 'H':
    am.position()
elif user_language == 'E':
    en.position()
elif user_language == 'R':
    ru.position()
else:
    print('Սխալ մուտքագրում։ Կրկին փորձեք:\tInvalid input: Try again.\tВведено неверно: Попробуйте еще раз.')
