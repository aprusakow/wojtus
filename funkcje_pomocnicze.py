import pygame
import csv
from typing import List, Tuple, Union



def circle_collidepoint(center: Tuple[int, int], radius: float, point: Tuple[int, int]) -> bool:
    '''Sprawdza, czy punkt o współrzędnych point należy do koła o środku w punkcie center i promieniu radius'''
    if center is None:
        return False
    elif (center[0] - point[0]) ** 2 + (center[1] - point[1]) ** 2 <= radius ** 2:
        return True
    else:
        return False


def zapisz_wspolrzedne(punkty: List[Tuple[int, int]]) -> None:
    '''Zapisuje współrzędne punktów do pliku wspolrzedne_punktow.csv'''
    with open('wspolrzedne_punktow.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['X', 'Y'])  # Nagłówki kolumn
        for punkt in punkty:
            writer.writerow(punkt)  # Zapisuje każdy punkt


def wyswietl_tekst(teksty: Union[str, List[str]], screen, tekst_rect, font_size=20, color=pygame.Color('black'), background_color=pygame.Color('white')):
    '''
    Wyświetla komunikat na ekranie. Każdy element listy teksty będzie wyświetlany w nowej linijce.
    
    Parametry:
    - teksty: lista tekstów (każdy element to nowa linijka)
    - screen: obiekt ekranu Pygame
    - komunikat_rect: obiekt prostokąta w Pygame, na którym wyświetlamy komunikat
        (domyślnie na górze okna, w miejscu do wyświetlania komunikatów/instrukcji dla użytkownika)
    - komunikat_font_size: rozmiar czcionki (domyślnie 20)
    - color: kolor tekstu (domyślnie czarny)
    - background_color: kolor tła (domyślnie biały)
    '''

    if isinstance(teksty, str):
        teksty = [teksty]  # Konwersja na listę, jeśli podany jest pojedynczy string

    font = pygame.font.Font(None, font_size)
    pygame.draw.rect(screen, background_color, tekst_rect)  # Czyszczenie prostokąta (rysowanie tła)
    total_height = len(teksty) * font.get_height()  # Obliczenie całkowitej wysokości tekstu
    y_offset = tekst_rect.top + (tekst_rect.height - total_height) // 2  # Wyśrodkowanie tekstu pionowo w prostokącie
    
    # Renderowanie każdej linijki tekstu
    for tekst in teksty:
        text_surface = font.render(tekst, True, color)
        text_rect = text_surface.get_rect()
        text_rect.centerx = tekst_rect.centerx  # Wyśrodkowanie w poziomie
        text_rect.top = y_offset  # Ustawienie pionowo na odpowiedniej wysokości
        screen.blit(text_surface, text_rect)
        y_offset += font.get_height()  # Przesunięcie w dół o wysokość tekstu


def wspol_osiowe(x, y, canvas_rect:pygame.Rect):
    """Zamienia współrzędne pobrane z pygame na takie, by były zgodne z narysowanymi osiami
    (punkt (0.0) w lewym dolnym rogu płótna, wzrost wartości y w kierunku górnym)"""
    return x - canvas_rect.left, - y + canvas_rect.bottom




