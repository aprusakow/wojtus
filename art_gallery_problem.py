import pygame
import sys
from rysowanie_okna import *
from user_input_polygon import *
from funkcje_pomocnicze import *

def main():
    # Inicjalizacja i rysowanie okna
    screen = init_window()
    draw_canvas_area(screen)
    draw_komunikat_area(screen)
    draw_grid(screen)
    draw_axes(screen)

    # Główna pętla programu
    running = True
    draw_enabled = True
    co_najmniej_trzy_punkty = False
    czy_pierwszy_wierzcholek = True
    last_pos = None
    current_pos = None
    first_pos = None
    punkty = []

    wyswietl_tekst('Narysuj pierwszy punkt wielokąta, klikając myszą w dowolne miejsce w obszarze płótna.', screen, komunikat_rect)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if draw_enabled and canvas_rect.collidepoint(mouse_x, mouse_y):
                    current_pos = (mouse_x, mouse_y)
                    point_radius=5
                    if circle_collidepoint(first_pos, point_radius, current_pos) and co_najmniej_trzy_punkty:
                        draw_enabled = False
                        pygame.draw.line(screen, BLACK, last_pos, first_pos)
                        zapisz_wspolrzedne(punkty)
                        wyswietl_tekst(['Wielokąt zamknięty!', 'Aby wyjść z programu, zamknij okno.'], screen, komunikat_rect)
                    else:
                        pygame.draw.circle(screen, BLACK, current_pos, point_radius)
                        punkty.append(current_pos)
                        if czy_pierwszy_wierzcholek:
                            first_pos = current_pos
                            czy_pierwszy_wierzcholek = False
                            wyswietl_tekst(['Zaznacz kolejne wierzchołki wielokąta.',
                                            'Następnie zamknij wielokąt, ponownie klikając pierwszy wierzchołek.'], screen, komunikat_rect)
                        else:
                            pygame.draw.line(screen, BLACK, last_pos, current_pos)
                        last_pos = current_pos
                        if len(punkty) >= 3:
                            co_najmniej_trzy_punkty = True
            elif event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = event.pos
                wyswietl_tekst(f'x:{mouse_x}, y:{mouse_y}', screen, wspolrzedne_rect, font_size=15, background_color=GREY)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
