# Communication Service

Mechanizm komunikujący się z różnymi usługami.

Zawiera dwie usługi:
- eksport wiadomości na kolejkę
- import wiadomości wrzuconej na kolejkę

Mechanizm ma wykorzystywać następujące elementy:

- **Redis** - przechowywanie stanu
- **AWS DynamoDB** / **MongoDB** - przechowywanie wiadomości (trwałe) oraz konfiguracji - nierelacyjna baza danych
- **RabbitMQ** - Kolejka, która będzie punktem wyjscia / wejścia wiadomości. Symuluje np. Azure Service Bus
- **Python** - Język, w którym będzie to wszystko implementowane.
- **Grafana / Zipkin** - obserwowanie tego, co się dzieje
- **Secret Manager** - przechowuje dane połączeń z elementami (opcjonalnie)

## Eksport wiadomości

Eksport wiadomości ma odbywać sie w sposób następujący:

1. Użytkownik w systemie opartym o PHP-a wykonuje operacje:
   1. zapisuje wiadomość na Redisie pod odpowiednim kluczem
   2. wysyła żądanie REST do API Communication Service (napisanego w Pythonie), z danymi klucza wiadomości do przetworzenia
2. Communication Service realizuje następujące kroki:
   1. Pobiera wiadomość z Redisa,
   2. Wysyła informacje na kolejkę RabbitMQ
3. W czasie komunikacji, każda operacja jest zapisywana w Grafanie.


Na poziomie kontekstowych projekt przedstawia si ę 
!['Eksport - diagram kontekstowy'](_media/cs-export-context.svg)

