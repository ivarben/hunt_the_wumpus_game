#klasser:
class Grafik:
    def __init__(self, root, karta, spelare, wumpus, svår):
        #duk (canvas)
        self.duk = Canvas(root, width = 800, height = 500, bg = '#004040')
        self.duk.place(x = 0, y = 0)

        #containers
        self.knappsats = Frame(self.duk, bg = '#004040')
        self.knappsats.place(x = 570, y = 250)

        self.spelplan = Frame(self.duk, width = 350, height = 350)
        self.spelplan.place(x = 100, y = 60)
        
        #knappar

        self.b1 = Button(self.knappsats, text = 'Höger', command = lambda: spelare.flytta_höger(karta, spelare, wumpus, svår, self), bg = '#0050A0', activebackground = '#0050A0')
        self.b1.pack(side = RIGHT)
        self.b2 = Button(self.knappsats, text = 'Vänster', command = lambda: spelare.flytta_vänster(karta, spelare, wumpus, svår, self), bg = '#0050A0', activebackground = '#0050A0')
        self.b2.pack(side = LEFT)
        self.b3 = Button(self.knappsats, text = 'Uppåt', command = lambda: spelare.flytta_uppåt(karta, spelare, wumpus, svår, self), bg = '#0050A0', activebackground = '#0050A0')
        self.b3.pack(side = TOP)
        self.b4 = Button(self.knappsats, text = 'Nedåt', command = lambda: spelare.flytta_nedåt(karta, spelare, wumpus, svår, self), bg = '#0050A0', activebackground = '#0050A0')
        self.b4.pack(side = BOTTOM)

        self.b5 = Button(self.duk, text = 'Skjut!', width = 10, height = 2, command = lambda: spelare.skjuta(karta, wumpus, self, svår), bg = '#0050A0', activebackground = '#0050A0')
        self.b5.place(x = 610, y = 180)
        
        #etiketter
        self.textbox = Label(self.duk, height = 5, width = 80, anchor = NW, justify = LEFT, bg = 'White')
        self.textbox.place(x = 100, y = 380)

        for i in range (1,6):
            karta.rummen[i-1].skapa_rumsgrafik(self.spelplan, 1, i)
        for i in range (6, 11):
            karta.rummen[i-1].skapa_rumsgrafik(self.spelplan, 2, i-5)
        for i in range (11, 16):
            karta.rummen[i-1].skapa_rumsgrafik(self.spelplan, 3, i-10)
        for i in range (16, 21):
            karta.rummen[i-1].skapa_rumsgrafik(self.spelplan, 4, i-15)

        for i in range(len(karta.rummen)):
            karta.rummen[i].uppdatera_rumsgrafik(spelare)

        self.ändra_instruktion(karta, spelare)
        #skapar fönster, spelplan, knappsats och 'textruta'
    def avsluta(self):
        self.knappsats.place_forget()
        self.b5.place_forget()
        self.knapp_avsluta = Button(self.duk, text = 'Tillbaka', height = 3, width = 15, command = self.duk.place_forget)
        self.knapp_avsluta.place(x = 600, y = 250)

    def uppdatera_grafik(self, karta, spelare):
        for i in range(len(karta.rummen)):
            karta.rummen[i].uppdatera_rumsgrafik(spelare)
        #sköter metoden för uppdatering av varje rums enskilda grafik

        self.ändra_instruktion(karta, spelare)

    def ändra_instruktion(self, karta, spelare):
        träff = False
        for i in range(len(karta.rummen)):
            if karta.rummen[i].position_x == spelare.pil.position_x and karta.rummen[i].position_y == spelare.pil.position_y and karta.rummen[i].wumpus == True:
                self.textbox.configure(text = 'Grattis! Du dödade den hemske Wumpus och räddade din by från en säker undergång.')
                träff = True
            elif karta.rummen[i].position_x == spelare.position_x and karta.rummen[i].position_y == spelare.position_y and träff == False:
                if karta.rummen[i].wumpus == True:
                    self.textbox.configure(text = 'Wumpus äter sakta upp dig med en träslev.')
                elif karta.rummen[i].avgrundshål == True:
                    self.textbox.configure(text = 'Du faller mot en säker död i ett avgrundshål.')
                elif karta.rummen[i].bredvid_fladdermöss == True or karta.rummen[i].bredvid_avgrundshål == True or karta.rummen[i].bredvid_wumpus == True:
                    if karta.rummen[i].bredvid_fladdermöss == True and karta.rummen[i].bredvid_avgrundshål == True and karta.rummen[i].bredvid_wumpus == True:
                        self.textbox.configure(text = 'Du känner den förfärliga stanken av Wumpus.\nDu känner draget från ett avgrundshål.\nDu hör ljudet av fladdermöss.\nRör dig åt något håll eller skjut en pil!')
                    elif karta.rummen[i].bredvid_fladdermöss == True and karta.rummen[i].bredvid_avgrundshål == True:
                        self.textbox.configure(text = 'Du känner draget från ett avgrundshål.\nDu hör ljudet av fladdermöss.\nRör dig åt något håll eller skjut en pil!')
                    elif karta.rummen[i].bredvid_fladdermöss == True and karta.rummen[i].bredvid_wumpus == True:
                        self.textbox.configure(text = 'Du känner den förfärliga stanken av Wumpus.\nDu hör ljudet av fladdermöss.\nRör dig åt något håll eller skjut en pil!')
                    elif karta.rummen[i].bredvid_avgrundshål == True and karta.rummen[i].bredvid_wumpus == True:
                        self.textbox.configure(text = 'Du känner den förfärliga stanken av Wumpus.\nDu känner draget från ett avgrundshål.\nRör dig åt något håll eller skjut en pil!')
                    elif karta.rummen[i].bredvid_fladdermöss == True:
                        self.textbox.configure(text = 'Du hör ljudet av fladdermöss.\nRör dig åt något håll eller skjut en pil!')
                    elif karta.rummen[i].bredvid_avgrundshål == True:
                        self.textbox.configure(text = 'Du känner draget från ett avgrundshål.\nRör dig åt något håll eller skjut en pil!')
                    elif karta.rummen[i].bredvid_wumpus == True:
                        self.textbox.configure(text = 'Du känner den förfärliga stanken av Wumpus.\nRör dig åt något håll eller skjut en pil!')
                else:
                    self.textbox.configure(text = 'Rör dig åt något håll eller skjut en pil!')
        #sköter textrutan med instruktioner nedanför spelplanen. Avgörs av vad som finns i rummet man står i

    def skapa_knappsats_pil(self, karta, spelare, wumpus, svår):
        self.b1.configure(command = lambda: spelare.pil.flytta_höger(karta, spelare, wumpus, self, svår))
        self.b2.configure(command = lambda: spelare.pil.flytta_vänster(karta, spelare, wumpus, self, svår))
        self.b3.configure(command = lambda: spelare.pil.flytta_uppåt(karta, spelare, wumpus, self, svår))
        self.b4.configure(command = lambda: spelare.pil.flytta_nedåt(karta, spelare, wumpus, self, svår))
        self.b5.place_forget()
        #ändrar om knappsatsen så att den styr pilen istället för spelaren

    def återskapa_knappsats(self, karta, spelare, wumpus, svår):
        self.b1.configure(command = lambda: spelare.flytta_höger(karta, spelare, wumpus, svår, self))
        self.b2.configure(command = lambda: spelare.flytta_vänster(karta, spelare, wumpus, svår, self))
        self.b3.configure(command = lambda: spelare.flytta_uppåt(karta, spelare, wumpus, svår, self))
        self.b4.configure(command = lambda: spelare.flytta_nedåt(karta, spelare, wumpus, svår, self))
        self.b5.place(x = 610, y = 180)
        #efter att pilen flyttats tre gånger blir knappsatsen vad den var från början
        
class Rum:
    def __init__ (self, nummer, position_x, position_y, gräns_fladdermöss, gräns_avgrundshål):

        self.nummer = nummer
        self.position_x = position_x #x-koordinat
        self.position_y = position_y #y-koordinat
        self.historik = False #om spelaren varit där nån gång eller inte
        self.wumpus = None #om wumpus är där
        self.bredvid_fladdermöss = None #om det finns fladdermöss
        self.bredvid_avgrundshål = None #om det finns ett avgrundshål
        self.bredvid_wumpus = None #om det är ett rum som har wumpus bredvid
        
        slump1 = random.randint(0,9)
        slump2 = random.randint(0,9)
        slump3 = random.randint(0,1)

        if slump1 < gräns_fladdermöss:
            self.fladdermöss = True
        else:
            self.fladdermöss = False
        if slump2 < gräns_avgrundshål:
            self.avgrundshål = True
        else:
            self.avgrundshål = False

        if self.fladdermöss == True and self.avgrundshål == True:
            if slump3 == 0:
                self.fladdermöss = False
            else:
                self.avgrundshål = False
        #skapar ett rum med "default" attribut
                        
    def uppdatera_historik(self, spelare):
        if self.position_x == spelare.position_x and self.position_y == spelare.position_y:
            self.historik = True
        #om spelarens och rummets positioner är samma ändras rummets historikattribut till True
            
    def flyga_fladdermus(self, karta, spelare, wumpus, grafik):
        if self.fladdermöss == True and self.position_x == spelare.position_x and self.position_y == spelare.position_y:
            slumpx = random.randint(1,5)
            slumpy = random.randint(1,4)
            spelare.position_x = slumpx
            spelare.position_y = slumpy
            kolla_historik(karta, spelare)
            spelare.kolla_fladdermus(karta, wumpus, grafik)
            #finns för att hindra att man "landar" och stannar på en ruta med fladdermöss == True
            spelare.kolla_förlust(karta, wumpus, grafik)
        #placerar iväg spelaren i ett slumpmässigt rum, hamnar man i ett rum med fladdermöss flyttas man igen

    def skapa_rumsgrafik(self, parent, rad, kolumn):
        self.ruta = Label(parent, width = 75, height = 75)
        self.ruta.grid(row = rad, column = kolumn)
        #grafiken som gäller i början av varje nytt spel, innan något egentligen har hänt
        
    def uppdatera_rumsgrafik(self, spelare):
        if self.historik == True:
            if self.position_x == spelare.position_x == spelare.pil.position_x and self.position_y == spelare.position_y == spelare.pil.position_y:
                if self.bredvid_fladdermöss == True or self.bredvid_avgrundshål == True or self.bredvid_wumpus == True:
                    if self.bredvid_fladdermöss == True and self.bredvid_avgrundshål == True and self.bredvid_wumpus == True:
                        bild = PhotoImage(file = 'Spelare_skjuter_rum_bredvid_alla_tre.png')
                    elif self.bredvid_fladdermöss == True and self.bredvid_avgrundshål == True:
                        bild = PhotoImage(file = 'Spelare_skjuter_rum_bredvid_avgrundshål_och_fladdermöss.png')
                    elif self.bredvid_fladdermöss == True and self.bredvid_wumpus == True:
                        bild = PhotoImage(file = 'Spelare_skjuter_rum_bredvid_fladdermöss_och_wumpus.png')
                    elif self.bredvid_avgrundshål == True and self.bredvid_wumpus == True:
                        bild = PhotoImage(file = 'Spelare_skjuter_rum_bredvid_avgrundshål_och_wumpus.png')
                    elif self.bredvid_fladdermöss == True:
                        bild = PhotoImage(file = 'Spelare_skjuter_rum_bredvid_fladdermöss.png')
                    elif self.bredvid_avgrundshål == True:
                        bild = PhotoImage(file = 'Spelare_skjuter_rum_bredvid_avgrundshål.png')
                    elif self.bredvid_wumpus == True:
                        bild = PhotoImage(file = 'Spelare_skjuter_rum_bredvid_wumpus.png')
                else:
                    bild = PhotoImage(file = 'Spelare_skjuter_utforskat_rum.png')
            elif self.position_x == spelare.position_x and self.position_y == spelare.position_y:
                if self.avgrundshål == True:
                    bild = PhotoImage(file = 'Spelare_ramlar.png')
                elif self.wumpus == True:
                    bild = PhotoImage(file = 'Wumpus_äter_spelare.png')
                elif self.bredvid_fladdermöss == True or self.bredvid_avgrundshål == True or self.bredvid_wumpus == True:
                    if self.bredvid_fladdermöss == True and self.bredvid_avgrundshål == True and self.bredvid_wumpus == True:
                        bild = PhotoImage(file = 'Rum_bredvid_alla_tre+spelare.png')
                    elif self.bredvid_fladdermöss == True and self.bredvid_avgrundshål == True:
                        bild = PhotoImage(file = 'Rum_bredvid_fladdermöss_och_avgrundshål+spelare.png')
                    elif self.bredvid_fladdermöss == True and self.bredvid_wumpus == True:
                        bild = PhotoImage(file = 'Rum_bredvid_fladdermöss_och_wumpus+spelare.png')
                    elif self.bredvid_avgrundshål == True and self.bredvid_wumpus == True:
                        bild = PhotoImage(file = 'Rum_bredvid_wumpus_och_avgrundshål+spelare.png')
                    elif self.bredvid_fladdermöss == True:
                        bild = PhotoImage(file = 'Rum_bredvid_fladdermöss+spelare.png')
                    elif self.bredvid_avgrundshål == True:
                        bild = PhotoImage(file = 'Rum_bredvid_avgrundshål+spelare.png')
                    elif self.bredvid_wumpus == True:
                        bild = PhotoImage(file = 'Rum_bredvid_wumpus+spelare.png')
                else:
                    bild = PhotoImage(file = 'Utforskat_rum+spelare.png')
            elif self.position_x == spelare.pil.position_x and self.position_y == spelare.pil.position_y:
                if self.wumpus == True:
                    bild = PhotoImage(file = 'Wumpus_träffad.png')
                elif self.fladdermöss == True:
                    bild = PhotoImage(file = 'Fladdermöss+pil.png')
                elif self.bredvid_fladdermöss == True or self.bredvid_avgrundshål == True or self.bredvid_wumpus == True:
                    if self.bredvid_fladdermöss == True and self.bredvid_avgrundshål == True and self.bredvid_wumpus == True:
                        bild = PhotoImage(file = 'Rum_bredvid_alla_tre+pil.png')
                    elif self.bredvid_fladdermöss == True and self.bredvid_avgrundshål == True:
                        bild = PhotoImage(file = 'Rum_bredvid_fladdermöss_och_avgrundshål+pil.png')
                    elif self.bredvid_fladdermöss == True and self.bredvid_wumpus == True:
                        bild = PhotoImage(file = 'Rum_bredvid_fladdermöss_och_wumpus+pil.png')
                    elif self.bredvid_avgrundshål == True and self.bredvid_wumpus == True:
                        bild = PhotoImage(file = 'Rum_bredvid_wumpus_och_avgrundshål+pil.png')
                    elif self.bredvid_fladdermöss == True:
                        bild = PhotoImage(file = 'Rum_bredvid_fladdermöss+pil.png')
                    elif self.bredvid_avgrundshål == True:
                        bild = PhotoImage(file = 'Rum_bredvid_avgrundshål+pil.png')
                    elif self.bredvid_wumpus == True:
                        bild = PhotoImage(file = 'Rum_bredvid_wumpus+pil.png')
                else:
                    bild = PhotoImage(file = 'Utforskat_rum+pil.png')
            else:
                if self.wumpus == True:
                    bild = PhotoImage(file = 'Wumpus.png')
                elif self.fladdermöss == True:
                    bild = PhotoImage(file = 'Fladdermöss.png')
                elif self.avgrundshål == True:
                    bild = PhotoImage(file = 'Avgrundshål.png')
                elif self.bredvid_fladdermöss == True or self.bredvid_avgrundshål == True or self.bredvid_wumpus == True:
                    if self.bredvid_fladdermöss == True and self.bredvid_avgrundshål == True and self.bredvid_wumpus == True:
                        bild = PhotoImage(file = 'Rum_bredvid_alla_tre.png')
                    elif self.bredvid_fladdermöss == True and self.bredvid_avgrundshål == True:
                        bild = PhotoImage(file = 'Rum_bredvid_fladdermöss_och_avgrundshål.png')
                    elif self.bredvid_fladdermöss == True and self.bredvid_wumpus == True:
                        bild = PhotoImage(file = 'Rum_bredvid_fladdermöss_och_wumpus.png')
                    elif self.bredvid_avgrundshål == True and self.bredvid_wumpus == True:
                        bild = PhotoImage(file = 'Rum_bredvid_wumpus_och_avgrundshål.png')
                    elif self.bredvid_fladdermöss == True:
                        bild = PhotoImage(file = 'Rum_bredvid_fladdermöss.png')
                    elif self.bredvid_avgrundshål == True:
                        bild = PhotoImage(file = 'Rum_bredvid_avgrundshål.png')
                    elif self.bredvid_wumpus == True:
                        bild = PhotoImage(file = 'Rum_bredvid_wumpus.png')
                else:
                    bild = PhotoImage(file = 'Utforskat_rum.png')
        else:
            if self.position_x == spelare.pil.position_x and self.position_y == spelare.pil.position_y and self.wumpus == True:
                bild = PhotoImage(file = 'Wumpus_träffad.png')
            elif self.position_x == spelare.pil.position_x and self.position_y == spelare.pil.position_y:
                bild = PhotoImage(file = 'Outforskat_rum+pil.png')
            else:
                bild = PhotoImage(file = 'Outforskat_rum.png')
        self.ruta.configure(image = bild)
        self.ruta.image = bild
    #uppdaterar det enskilda rummets grafik baserat på vad som "är" där (dvs vad som har samma position som rummet) och om splearen varit där eller inte

class Karta:
    def __init__(self, gräns_fladdermöss, gräns_avgrundshål):
        self.rummen = []
        for i in range (1,6):
            self.rummen.append(Rum(i, i, 1, gräns_fladdermöss, gräns_avgrundshål))
        for i in range (6,11):
            self.rummen.append(Rum(i, i-5, 2, gräns_fladdermöss, gräns_avgrundshål))
        for i in range (11,16):
            self.rummen.append(Rum(i, i-10, 3, gräns_fladdermöss, gräns_avgrundshål))
        for i in range (16,21):
            self.rummen.append(Rum(i, i-15, 4, gräns_fladdermöss, gräns_avgrundshål))
        #skapar upp alla rum och placerar dem i en lista
        j = 0
        for i in range(len(self.rummen)):
            if self.rummen[i].fladdermöss == True or self.rummen[i].avgrundshål == True:
                j += 1
                if j > 18:
                    self.rummen[i].fladdermöss = False
                    self.rummen[i].avgrundshål = False
                #eliminerar den minimala risk att det inte skulle finnas lediga rum för spelaren och wumpus

        rum_bredvid_fladdermöss = []
        rum_bredvid_avgrundshål = []
        for i in range(len(self.rummen)):
            if self.rummen[i].fladdermöss == True:
                xplus = self.rummen[i].position_x + 1
                if xplus == 6:
                    xplus = 1
                xminus = self.rummen[i].position_x - 1
                if xminus == 0:
                    xminus = 5
                yplus = self.rummen[i].position_y + 1
                if yplus == 5:
                    yplus = 1
                yminus = self.rummen[i].position_y - 1
                if yminus == 0:
                    yminus = 4
                for j in range(len(self.rummen)):
                    if self.rummen[j].position_x == xplus and self.rummen[j].position_y == self.rummen[i].position_y:
                        rum_bredvid_fladdermöss.append(self.rummen[j])
                    elif self.rummen[j].position_x == xminus and self.rummen[j].position_y == self.rummen[i].position_y:
                        rum_bredvid_fladdermöss.append(self.rummen[j])
                    elif self.rummen[j].position_y == yplus and self.rummen[j].position_x == self.rummen[i].position_x:
                        rum_bredvid_fladdermöss.append(self.rummen[j])
                    elif self.rummen[j].position_y == yminus and self.rummen[j].position_x == self.rummen[i].position_x:
                        rum_bredvid_fladdermöss.append(self.rummen[j])
            if self.rummen[i].avgrundshål == True:
                xplus = self.rummen[i].position_x + 1
                if xplus == 6:
                    xplus = 1
                xminus = self.rummen[i].position_x - 1
                if xminus == 0:
                    xminus = 5
                yplus = self.rummen[i].position_y + 1
                if yplus == 5:
                    yplus = 1
                yminus = self.rummen[i].position_y - 1
                if yminus == 0:
                    yminus = 4
                for j in range(len(self.rummen)):
                    if self.rummen[j].position_x == xplus and self.rummen[j].position_y == self.rummen[i].position_y:
                        rum_bredvid_avgrundshål.append(self.rummen[j])
                    elif self.rummen[j].position_x == xminus and self.rummen[j].position_y == self.rummen[i].position_y:
                        rum_bredvid_avgrundshål.append(self.rummen[j])
                    elif self.rummen[j].position_y == yplus and self.rummen[j].position_x == self.rummen[i].position_x:
                        rum_bredvid_avgrundshål.append(self.rummen[j])
                    elif self.rummen[j].position_y == yminus and self.rummen[j].position_x == self.rummen[i].position_x:
                        rum_bredvid_avgrundshål.append(self.rummen[j])
        for i in range(len(rum_bredvid_fladdermöss)):
            rum_bredvid_fladdermöss[i].bredvid_fladdermöss = True
        for i in range(len(rum_bredvid_avgrundshål)):
            rum_bredvid_avgrundshål[i].bredvid_avgrundshål = True
            #dubbla for-slingor för att lista ut "adjacency" till fladdermöss och avgrundshål

    def bredvid_wumpus(self):
        self.rum_bredvid_wumpus = []
        for i in range(len(self.rummen)):
            if self.rummen[i].wumpus == True:
                xplus = self.rummen[i].position_x + 1
                if xplus == 6:
                    xplus = 1
                xminus = self.rummen[i].position_x - 1
                if xminus == 0:
                    xminus = 5
                yplus = self.rummen[i].position_y + 1
                if yplus == 5:
                    yplus = 1
                yminus = self.rummen[i].position_y - 1
                if yminus == 0:
                    yminus = 4
                for j in range(len(self.rummen)):
                    if self.rummen[j].position_x == xplus and self.rummen[j].position_y == self.rummen[i].position_y:
                        self.rum_bredvid_wumpus.append(self.rummen[j])
                    elif self.rummen[j].position_x == xminus and self.rummen[j].position_y == self.rummen[i].position_y:
                        self.rum_bredvid_wumpus.append(self.rummen[j])
                    elif self.rummen[j].position_y == yplus and self.rummen[j].position_x == self.rummen[i].position_x:
                        self.rum_bredvid_wumpus.append(self.rummen[j])
                    elif self.rummen[j].position_y == yminus and self.rummen[j].position_x == self.rummen[i].position_x:
                        self.rum_bredvid_wumpus.append(self.rummen[j])
        for i in range(len(self.rum_bredvid_wumpus)):
            self.rum_bredvid_wumpus[i].bredvid_wumpus = True
        for i in range(len(self.rummen)):
            if self.rummen[i] not in self.rum_bredvid_wumpus:
                self.rummen[i].bredvid_wumpus = False
        #dubbla for-slingor för att lista ut "adjacency" till wumpus

class Spelare:
    def __init__(self, karta):
        slumpx = random.randint(1,5)
        slumpy = random.randint(1,4)
        lista = rumskontroll_för_spelare(karta, slumpx, slumpy)
        self.position_x = lista[0] #x-koordinat
        self.position_y = lista[1] #y- koordinat
        self.pil = Pil(0,0) #för att pil inte ska orsaka errors
        self.pilar = 5 #antal pilar

    def flytta_uppåt(self, karta, spelare, wumpus, svår, grafik):
        self.position_y -= 1
        if self.position_y == 0:
            self.position_y = 4
        kolla_historik(karta, spelare)
        self.kolla_fladdermus(karta, wumpus, grafik)
        wumpus.förflyttning(karta, spelare, svår)
        self.kolla_förlust(karta, wumpus, grafik)
        grafik.uppdatera_grafik(karta, spelare)

    def flytta_nedåt(self, karta, spelare, wumpus, svår, grafik):
        self.position_y += 1
        if self.position_y == 5:
            self.position_y = 1
        kolla_historik(karta, spelare)
        self.kolla_fladdermus(karta, wumpus, grafik)
        wumpus.förflyttning(karta, spelare, svår)
        self.kolla_förlust(karta, wumpus, grafik)
        grafik.uppdatera_grafik(karta, spelare)

    def flytta_höger(self, karta, spelare, wumpus, svår, grafik):
        self.position_x += 1
        if self.position_x == 6:
            self.position_x = 1
        kolla_historik(karta, spelare)
        self.kolla_fladdermus(karta, wumpus, grafik)
        wumpus.förflyttning(karta, spelare, svår)
        self.kolla_förlust(karta, wumpus, grafik)
        grafik.uppdatera_grafik(karta, spelare)

    def flytta_vänster(self, karta, spelare, wumpus, svår, grafik):
        self.position_x -= 1
        if self.position_x == 0:
            self.position_x = 5
        kolla_historik(karta, spelare)
        self.kolla_fladdermus(karta, wumpus, grafik)
        wumpus.förflyttning(karta, spelare, svår)
        self.kolla_förlust(karta, wumpus, grafik)
        grafik.uppdatera_grafik(karta, spelare)

    def kolla_fladdermus(self, karta, wumpus, grafik):
        for i in range(len(karta.rummen)):
            karta.rummen[i].flyga_fladdermus(karta, self, wumpus, grafik)

    def kolla_förlust(self, karta, wumpus, grafik):
        for i in range(len(karta.rummen)):
            if karta.rummen[i].avgrundshål == True and self.position_x == karta.rummen[i].position_x and self.position_y == karta.rummen[i].position_y:
                grafik.uppdatera_grafik(karta, self)
                game_over(karta, self, grafik)
                
        if self.position_x == wumpus.position_x and self.position_y == wumpus.position_y:
            grafik.uppdatera_grafik(karta, self)
            game_over(karta, self, grafik)

    def skjuta(self, karta, wumpus, grafik, svår):
        self.pil = Pil(self.position_x, self.position_y)
        grafik.skapa_knappsats_pil(karta, self, wumpus, svår)
        grafik.uppdatera_grafik(karta, self)
    #skapar upp en pil och en knappsats för att styra den

    def sluta_skjuta(self, karta, wumpus, grafik, svår):
        grafik.återskapa_knappsats(karta, self, wumpus, svår)
        grafik.uppdatera_grafik(karta, self)
        self.pilar -= 1
        self.pil = Pil(0,0)
        if self.pilar == 0:
            game_over(karta, self, grafik)
            grafik.textbox.configure(text = 'Tyvärr, pilarna är slut. Det är ute med dig och din by.')
    #fixar tillbaka gammal knappsats (avslutar om pilarna är slut)
class Wumpus:
    def __init__(self, karta, spelare):
        slumpx = random.randint(1,5)
        slumpy = random.randint(1,4)
        lista = rumskontroll_för_wumpus(karta, spelare, slumpx, slumpy)
        self.position_x = lista[0]
        self.position_y = lista[1]
        for i in range(len(karta.rummen)):
            if self.position_x == karta.rummen[i].position_x and self.position_y == karta.rummen[i].position_y:
                karta.rummen[i].wumpus = True
        karta.bredvid_wumpus()

    def förflyttning(self, karta, spelare, svår):
        if svår == True:
            tillgängliga_rum = []
            for i in range(len(karta.rummen)):
                if karta.rummen[i].fladdermöss == False and karta.rummen[i].avgrundshål == False and (karta.rummen[i] in karta.rum_bredvid_wumpus or karta.rummen[i].wumpus == True):
                    tillgängliga_rum.append(karta.rummen[i])
            if len(tillgängliga_rum) > 0:
                for i in range(len(tillgängliga_rum)):
                    ny_summa = abs(tillgängliga_rum[i].position_x - spelare.position_x) + abs(tillgängliga_rum[i].position_y - spelare.position_y)
                    if i == 0:
                        lägsta = ny_summa
                        nytt_rum = tillgängliga_rum[i]
                    else:
                        if ny_summa < lägsta:
                            lägsta = ny_summa
                            nytt_rum = tillgängliga_rum[i]
                self.position_x = nytt_rum.position_x
                self.position_y = nytt_rum.position_y
                for i in range(len(karta.rummen)):
                    if self.position_x == karta.rummen[i].position_x and self.position_y == karta.rummen[i].position_y:
                        karta.rummen[i].wumpus = True
                    else:
                        karta.rummen[i].wumpus = False
                karta.bredvid_wumpus()
        #wumpus rör sig till det närliggande rum som är närmast spelaren, förutsatt att det inte finns hål eller fladdermöss, och att spelaren inte varit där (då skulle man ju kunna se wumpus)

class Pil:
    def __init__(self, position_x, position_y):
        self.position_x = position_x #x-koordinat
        self.position_y = position_y #y-koordinat
        self.fart = 3 #förflyttningar kvar

    def flytta_uppåt(self, karta, spelare, wumpus, grafik, svår):
        self.position_y -= 1
        if self.position_y == 0:
            self.position_y = 4
        self.fart -= 1
        grafik.uppdatera_grafik(karta, spelare)
        self.kolla_fart_eller_träff(karta, spelare, wumpus, grafik, svår)

    def flytta_nedåt(self, karta, spelare, wumpus, grafik, svår):
        self.position_y += 1
        if self.position_y == 5:
            self.position_y = 1
        self.fart -= 1
        grafik.uppdatera_grafik(karta, spelare)
        self.kolla_fart_eller_träff(karta, spelare, wumpus, grafik, svår)

    def flytta_höger(self, karta, spelare, wumpus, grafik, svår):
        self.position_x += 1
        if self.position_x == 6:
            self.position_x = 1
        self.fart -= 1
        grafik.uppdatera_grafik(karta, spelare)
        self.kolla_fart_eller_träff(karta, spelare, wumpus, grafik, svår)

    def flytta_vänster(self, karta, spelare, wumpus, grafik, svår):
        self.position_x -= 1
        if self.position_x == 0:
            self.position_x = 5
        self.fart -= 1
        grafik.uppdatera_grafik(karta, spelare)
        self.kolla_fart_eller_träff(karta, spelare, wumpus, grafik, svår)

    def kolla_fart_eller_träff(self, karta, spelare, wumpus, grafik, svår):
        if self.position_x == wumpus.position_x and self.position_y == wumpus.position_y:
            vinst(karta, spelare, grafik)
        else:
            if self.fart == 0:
                spelare.sluta_skjuta(karta, wumpus, grafik, svår)
        #om pilens fart är slut (dvs pilen har gått genom tre rum) tas pilen bort

#funktioner:

def rumskontroll_för_spelare(karta, slumpx, slumpy):
    godkända_rum = []
    for i in range(len(karta.rummen)):
        if karta.rummen[i].fladdermöss == False and karta.rummen[i].avgrundshål == False:
            godkända_rum.append(karta.rummen[i])
    while True:
        for i in range(len(godkända_rum)):
            if godkända_rum[i].position_x == slumpx and godkända_rum[i].position_y == slumpy:
                return slumpx, slumpy
        slumpx = random.randint(1,5)
        slumpy = random.randint(1,4)
    #förhindrar att spelaren skapas upp "i" ett rum med fladdermöss eller hål, det skulle bara vara störande

def rumskontroll_för_wumpus(karta, spelare, slumpx, slumpy):
    godkända_rum = []
    for i in range(len(karta.rummen)):
        if (karta.rummen[i].fladdermöss == True or karta.rummen[i].avgrundshål == True) or (spelare.position_x == karta.rummen[i].position_x and spelare.position_y == karta.rummen[i].position_y):
            pass
        else:
            godkända_rum.append(karta.rummen[i])
    while True:
        for i in range(len(godkända_rum)):
            if godkända_rum[i].position_x == slumpx and godkända_rum[i].position_y == slumpy:
                return slumpx, slumpy
        slumpx = random.randint(1,5)
        slumpy = random.randint(1,4)
    #förhindrar att wumpus hamnar med hål eller fladdermöss, vilket är givet i lydelsen. Även att wumpus inte börjar med spelaren, vilket bara hade varit jobbigt

def kolla_historik(karta, spelare):
    for i in range(len(karta.rummen)):
            karta.rummen[i].uppdatera_historik(spelare)
    #sköter metoden som uppdaterar historikvariabeln för varje rum
            
def game_over(karta, spelare, grafik):
    for i in range(len(karta.rummen)):
        karta.rummen[i].historik = True
    grafik.uppdatera_grafik(karta, spelare)
    grafik.avsluta()
    #avslutar spelet
def vinst(karta, spelare, grafik):
    for i in range(len(karta.rummen)):
        karta.rummen[i].historik = True
    grafik.uppdatera_grafik(karta, spelare)
    grafik.avsluta()
    #avslutar spelet
            
#moduler:
from tkinter import *
import random

class Spel():
    def __init__(self):
        self.root = Tk()
        self.root.title('Wumpus')
        self.root.geometry('800x500+400+200')
        bild = PhotoImage(file = 'Startmeny.png')
        self.etikett = Label(self.root, image = bild)
        self.etikett.image = bild
        self.etikett.pack()

        self.menyknappar = Frame(self.root)
        self.menyknappar.place(x = 540, y = 300)
        
        knapp_spela = Button(self.menyknappar, text = 'Spela!', width = 27, height = 5, command = self.välja_svårighetsgrad).pack(side = TOP, fill = X)
        knapp_instruktion = Button(self.menyknappar, text = 'Hjälp', width = 13, height = 3, command = self.instruera).pack(side = LEFT)
        knapp_avsluta = Button(self.menyknappar, text = 'Avsluta', width = 13, height = 3, command = exit).pack(side = LEFT)
        #skapar huvudmenyn

    def instruera(self):
        self.menyknappar.place_forget()
        self.instruktion = Label(self.root, height = 15, width = 80, anchor = NW, justify = LEFT, bg = '#A0D0D0', text = 'Du befinner dig i kulvertarna under Nada, där den glupske Wumpus bor.\nFör att undvika att bli uppäten måste du skjuta Wumpus med din pil och båge.\nKulvertarna har 20 rum som är förenade med smala gångar.\nDu kan röra dig upp, ned, höger eller vänster från ett rum till ett annat.\nHär finns dock faror som lurar. I vissa rum finns bottenlösa hål. Kliver du ner i ett sådant\ndör du omedelbart. I andra rum finns fladdermöss som lyfter upp dig, flyger en bit\noch släpper dig i ett godtyckligt rum. I ett av rummen finns Wumpus, och om du vågar dig in\ni det rummet blir du genast uppäten. Som tur är kan du från rummen bredvid känna vinddraget\nfrån ett avgrundshål eller lukten av Wumpus. Du får också i varje rum reda på vilka rum som\nligger intill. För att vinna spelet måste du skjuta Wumpus. När du skjuter iväg en pil förflyttar den\nsig genom tre rum - du kan styra vilken riktning pilen ska välja i varje rum.\nDu har fem pilar. Lycka till!')
        self.instruktion.place(x = 10, y = 10)
        self.knapp_tillbaka = Button(self.root, text = 'Tillbaka', command = self.tillbaka, height = 3, width = 13)
        self.knapp_tillbaka.place(x = 540, y = 400)
        #instruktionssidan (när man trycker på hjälp)
        
    def tillbaka(self):
        self.instruktion.place_forget()
        self.knapp_tillbaka.place_forget()
        self.menyknappar.place(x = 540, y = 300)
        #skickar användaren tillbaka till huvudmenyn
    
    def välja_svårighetsgrad(self):
        self.menyknappar.place_forget()
        self.svårighetsknappar = Frame(self.root)
        self.svårighetsknappar.place(x = 540, y = 300)

        self.knapp_lätt = Button(self.svårighetsknappar, text = 'Lätt', width = 27, height = 2, command = lambda: self.spela(2, 1, False)).pack()
        self.knapp_medel = Button(self.svårighetsknappar, text = 'Medel', width = 27, height = 2, command = lambda: self.spela(3, 2, False)).pack()
        self.knapp_svår = Button(self.svårighetsknappar, text = 'Svår', width = 27, height = 2, command = lambda: self.spela(3, 2, True)).pack()
        #skickar användaren till en meny där man väljer svårighetsgrad

    def spela(self, gräns_fladdermöss, gräns_avgrundshål, svår):
        self.menyknappar.place(x = 540, y = 300)
        self.svårighetsknappar.place_forget()
        self.karta = Karta(gräns_fladdermöss, gräns_avgrundshål)
        self.spelare = Spelare(self.karta)
        self.wumpus = Wumpus(self.karta, self.spelare)
        kolla_historik(self.karta, self.spelare)
        self.grafik = Grafik(self.root, self.karta, self.spelare, self.wumpus, svår)
        #sätter igång spelet
spel = Spel()
