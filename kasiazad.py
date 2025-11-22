def utworz_nowe_id(zadania:str):                  #Tworzy nową funkcje o nazwie utworz_nowe_id.
    if not zadania:                               #Sprawdza, czy lista zadań (zadania) jest pusta.
                                                  #Jeśli nie ma żadnych zadań na liście (wartość zadania jest "fałszywa", czyli pusta), to warunek jest spełniony.
        ID = 1                                    #Ustawia zmienną ID na wartość 1.
                                                  #Ponieważ lista była pusta, nowe zadanie będzie pierwszym, więc dostaje ID równe 1.
    else: ID = len(zadania)+1                     #Ta linijka wykonuje się tylko wtedy, gdy lista NIE była pusta.Funkcja wykonuje to w kilku krokach:
                                                  #len(zadania): Liczy, ile zadań jest aktualnie na liście,
                                                  #... + 1: Dodaje 1 do tej liczby,
                                                  #ID = ...: Przypisuje ten wynik do zmiennej ID.
                                                  #Nowe ID będzie równe liczbie elementów na liście plus jeden. Na przykład, jeśli na liście są 3 zadania, nowe ID będzie wynosić 3 + 1 = 4.

def dodaj_zadanie(zadania:str, nazwa:str, osoba:str):         #Tworzy nową funkcje o nazwie dodaj_zadanie
    zad_id = utworz_nowe_id(zadania)                          #Funkcja ta dostaje listę zadania, żeby sprawdzić, jakie numery są już zajęte.

    zadania.append({                                          #Rozpoczyna dodawanie nowego elementu na koniec listy o nazwie lista. Nowym elementem będzie słownik.
        "ID": zad_id,                                         #Dodaje do słownika parę: Klucz to "ID", a Wartość to tekst (ciąg znaków) "zad_id".
        "nazwa" : nazwa,                                      #Dodaje do słownika parę: Klucz to "nazwa", a Wartość to to, co jest przechowywane w zmiennej o nazwie nazwa.
        "osoba": osoba,                                       #Dodaje do słownika parę: Klucz to "osoba", a Wartość to to, co jest przechowywane w zmiennej o nazwie osoba.
        "status": 0                                           #Dodaje do słownika parę: Klucz to "status", a Wartość to liczba 0.
})
def usun_zadanie(zadania, zad_id):              #Tworzy funkcję do usuwania. Potrzebuje listy zadań i numeru ID do usunięcia.

     for i, zad in enumerate(zadania):          #Przegląda listę zadań, biorąc po kolei każde zadanie (zad) wraz z jego numerem pozycji (i).
        if zad["zadID"] == zad_id:              #Sprawdza: Czy numer ID aktualnego zadania jest taki sam jak numer ID, który chcemy usunąć.
            del zadania[i]                      #Usuwa słownik z listy

def zmien_status_zadania(zadania, zad_id, nowy_status):     #Tworzy funkcję do zmiany statusu. Potrzebuje: listy zadań, numeru ID zadania do znalezienia i nowego statusu (0 lub 1).                                                   #Rozpoczyna ostrożne działanie. Mówi: "Spróbuj to wykonać i bądź gotowy na ewentualne błędy."

        if not 0 <= nowy_status <= 1:                       #Sprawdza warunek: Jeśli nowy status nie jest ani 0, ani 1...
            return                                          #To przerywa działanie funkcji i nic nie robi (bo podano nieprawidłowy status).

        for zadanie in zadania:                             #Przegląda listę zadań po kolei. W każdej rundzie pętli zadanie to jedno zadanie z listy.
            if zadanie['ID'] == zad_id:                     #Sprawdza warunek: Jeśli numer ID tego zadania jest taki sam, jak numer, którego szukamy...
                zadanie['status'] = nowy_status             #To zmienia wartość pod kluczem 'status' w tym zadaniu na nowy_status.



