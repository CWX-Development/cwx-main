import sqlite3
import re
from datetime import datetime

# Datenbankverbindung herstellen
conn = sqlite3.connect('notes.db')
cursor = conn.cursor()

# Tabelle erstellen, falls sie nicht existiert
cursor.execute('''
CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')
conn.commit()

def validate_note_title(title):
    """
    Validiert den Titel einer Notiz mithilfe von Regex.
    """
    if not re.match(r'^[A-Za-z0-9\s]{1,50}$', title):
        raise ValueError("Titel darf nur aus alphanumerischen Zeichen bestehen und maximal 50 Zeichen lang sein.")
    return True

def validate_note_content(content):
    """
    Validiert den Inhalt einer Notiz mithilfe von Regex.
    """
    if not re.match(r'^[A-Za-z0-9\s\.,?!]{1,1000}$', content):
        raise ValueError("Inhalt darf nur aus alphanumerischen Zeichen und Satzzeichen bestehen und maximal 1000 Zeichen lang sein.")
    return True

def add_note():
    """
    Funktion zum Hinzufügen einer Notiz zur Datenbank.
    """
    title = input("Gib den Titel der Notiz ein: ")
    content = input("Gib den Inhalt der Notiz ein: ")

    try:
        validate_note_title(title)
        validate_note_content(content)
        cursor.execute('INSERT INTO notes (title, content) VALUES (?, ?)', (title, content))
        conn.commit()
        print("Notiz erfolgreich hinzugefügt!")
    except ValueError as e:
        print(f"Fehler: {e}")

def delete_note():
    """
    Funktion zum Löschen einer Notiz aus der Datenbank.
    """
    note_id = input("Gib die ID der zu löschenden Notiz ein: ")
    
    # ID Validierung
    if not re.match(r'^\d+$', note_id):
        print("Fehler: Die ID muss eine Zahl sein.")
        return

    cursor.execute('DELETE FROM notes WHERE id = ?', (note_id,))
    conn.commit()

    if cursor.rowcount > 0:
        print("Notiz erfolgreich gelöscht!")
    else:
        print("Fehler: Notiz mit dieser ID existiert nicht.")

def list_notes():
    """
    Funktion zum Auflisten aller Notizen aus der Datenbank.
    """
    cursor.execute('SELECT * FROM notes')
    notes = cursor.fetchall()

    if not notes:
        print("Keine Notizen gefunden.")
        return

    for note in notes:
        print(f"ID: {note[0]}, Titel: {note[1]}, Inhalt: {note[2]}, Erstellungsdatum: {note[3]}")

def count_notes():
    """
    Funktion zur Berechnung und Ausgabe der Anzahl der Notizen.
    """
    cursor.execute('SELECT COUNT(*) FROM notes')
    count = cursor.fetchone()[0]
    print(f"Gesamtanzahl der Notizen: {count}")

def main():
    while True:
        print("\nNotiz-Anwendung")
        print("1. Notiz hinzufügen")
        print("2. Notiz löschen")
        print("3. Notizen auflisten")
        print("4. Anzahl der Notizen anzeigen")
        print("5. Beenden")

        try:
            choice = int(input("Wähle eine Option: "))
        except ValueError:
            print("Ungültige Eingabe. Bitte gib eine Zahl zwischen 1 und 5 ein.")
            continue

        if choice == 1:
            add_note()
        elif choice == 2:
            delete_note()
        elif choice == 3:
            list_notes()
        elif choice == 4:
            count_notes()
        elif choice == 5:
            print("Programm beendet.")
            break
        else:
            print("Ungültige Option. Bitte wähle eine Zahl zwischen 1 und 5.")

if __name__ == "__main__":
    main()

# Verbindung schließen, wenn das Programm beendet wird
conn.close()
