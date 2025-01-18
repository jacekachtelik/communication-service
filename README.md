# Communication Service

Mechanizm komunikujący się z różnymi usługami.

Zawiera dwie usługi:
- eksport wiadomości na kolejkę
- import wiadomości wrzuconej na kolejkę

Mechanizm ma wykorzystywać następujące elementy:

- **Redis** - przechowywanie stanu
- **AWS DynamoDB** / **MongoDB** - przechowywanie wiadomości (trwałe) - nierelacyjna baza danych
- **Rabbit** - Kolejka, która będzie punktem wyjscia / wejścia wiadomości. Symuluje np. Azure Service Bus
- **Python** - Język, w którym będzie to wszystko implementowane.


