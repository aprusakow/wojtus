# ---------------------------- WPROWADZANIE WIELOKĄTA I GŁÓWNA PĘTLA PROGRAMU ----------------------------

def petla():
    draw_enabled = True  # czy możemy rysować, czy zmieniamy na False gdy zamknęliśmy wielokąt
    co_najmniej_trzy_punkty = False  # czy narysowaliśmy co najmniej 3 punkty
    czy_pierwszy_wierzcholek = True  # czy rysujemy aktualnie pierwszy wierzchołek, czy kolejne

    last_pos = None  # współrzędne ostatniego narysowanego punktu
    current_pos = None  # współrzędne aktualnego punktu
    first_pos = None  # współrzędne pierwszego wierzchołka

    punkty = []  # lista do przechowywania punktów

    wyswietl_tekst('Narysuj pierwszy punkt wielokąta, klikając myszą w dowolne miejsce w obszarze płótna.', screen)

    while True:
        for event in pygame.event.get():

            # zamknięcie programu
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # kliknięcie myszą
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos

                if draw_enabled:
                    if canvas_rect.collidepoint(mouse_x, mouse_y):  # gdy kliknięto obszar płótna

                        current_pos = (mouse_x, mouse_y)

                        # gdy zamykamy wielokąt, kończymy rysowanie i zapisujemy plik ze współrzędnymi
                        if circle_collidepoint(first_pos, point_radius, current_pos):
                            if co_najmniej_trzy_punkty:
                                draw_enabled = False
                                pygame.draw.line(screen, BLACK, last_pos, first_pos)
                                zapisz_wspolrzedne(punkty)
                                wyswietl_tekst(['Wielokąt zamknięty!','Aby wyjść z programu, zamknij okno.'], screen)
                            continue

                        pygame.draw.circle(screen, center=current_pos, radius=point_radius, color=BLACK)  # rysowanie punktu na płótnie
                        punkty.append(current_pos)  # dodajemy punkt do listy
                        if czy_pierwszy_wierzcholek:
                            first_pos = current_pos
                            czy_pierwszy_wierzcholek = False
                            wyswietl_tekst(['Zaznacz kolejne wierzchołki wielokąta.',
                                            'Następnie zamknij wielokąt, ponownie klikając pierwszy narysowany wierzchołek.'], screen)
                        else:
                            pygame.draw.line(screen, BLACK, last_pos, current_pos)
                        last_pos = current_pos

                        if not co_najmniej_trzy_punkty:
                            if len(punkty) == 3:
                                co_najmniej_trzy_punkty = True

            if event.type == pygame.MOUSEMOTION:   # pobranie współrzędnych kursora myszy 
                mouse_x, mouse_y = event.pos
                wyswietl_tekst(f'x:{mouse_x}, y:{mouse_y}', screen, wspolrzedne_rect, font_size=15, background_color=GREY)  # wyświetlenie współrzędnych kursora
                                                                                                                            # myszy na dole ekranu
 
        pygame.display.update()