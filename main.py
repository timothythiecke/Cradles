import math
import time

CradlesRaw = """Berc. 182;70;105;15;110;80;175;70
Berc. 264;50;55;40;50;50;;70
Berc. 286;80;190;20;190;100;;80
Berc. 234;70;80;35;95;70;;80
Berc. 178;75;90;35;90;75;;80
Berc. 107;50;60;40;60;45;120;80
Berc. 72;65;95;40;95;70;180;80
Berc. 1;45;60;50;60;45;133;80
Berc. 73;60;70;50;70;60;125;80
Berc. 235;85;110;50;110;85;;80
Berc. 3;55;75;65;75;66;175;80
Berc. 104;60;110;10;120;75;200;140
Berc. 156;80;120;10;120;70;210;140
Berc. 240;90;135;10;135;95;;140
Berc. 227;90;135;15;135;115;;140
Berc. 71;70;100;20;100;70;170;140
Berc. 2;80;135;20;140;110;230;140
Berc. 214;60;120;25;120;75;225;140
Berc. 172;75;115;25;115;80;205;140
Berc. 250;70;110;30;110;110;;140
Berc. 116;75;120;30;130;90;220;140
Berc. 247;90;100;30;105;100;;140
Berc. 219;95;100;30;100;80;;140
Berc. 39;100;130;30;135;90;220;140
Berc. 238;110;130;30;130;115;;140
Berc. 187;75;100;40;100;80;170;140
Berc. 176;80;105;40;105;95;175;140
Berc. 114;90;105;40;105;80;165;140
Berc. 175;95;135;40;130;70;250;140
Berc. 57;100;140;40;140;100;240;140
Berc. 177;110;150;40;145;100;255;140
Berc. 231;130;150;40;135;100;;140
Berc. 34;75;100;45;100;75;180;140
Berc. 157;70;90;50;90;70;170;140
Berc. 220;80;110;50;110;100;;140
Berc. 270;80;110;50;110;80;;140
Berc. 271;80;95;50;100;75;;140
Berc. 206;95;120;50;120;100;195;140
Berc. 19;115;140;50;140;115;220;140
Berc. 269;80;115;55;115;90;;140
Berc. 263;85;115;55;115;80;;140
Berc. 151;100;120;55;120;100;190;140
Berc. 22;103;106;55;100;80;143;140
Berc. 111;55;90;60;90;80;180;140
Berc. 4;80;115;60;120;80;263;140
Berc. 190;85;120;60;120;95;225;140
Berc. 5;80;125;65;125;80;237;140
Berc. 222;92;115;70;115;90;;140
Berc. 180;95;130;75;120;95;250;140
Berc. 37;;;;;;250;150
Berc. 16;45;130;5;130;45;250;200
Berc. 134;105;160;10;160;105;255;200
Berc. 202;110;130;10;140;100;180;200
Berc. 120;90;160;15;160;110;270;200
Berc. 262;105;165;20;170;140;;200
Berc. 195;110;140;20;140;115;185;200
Berc. 237;110;150;20;150;110;;200
Berc. 254;85;170;25;190;120;;200
Berc. 30;90;150;25;150;70;270;200
Berc. 233;90;140;25;150;100;;200
Berc. 112;95;150;25;155;95;270;200
Berc. 121;95;145;30;145;80;265;200
Berc. 217;105;150;30;150;100;250;200
Berc. 123;110;140;30;140;100;225;200
Berc. 249;110;160;30;170;155;;200
Berc. 272;110;170;30;170;90;;200
Berc. 255;115;180;30;180;165;;200
Berc. 191;120;165;30;160;100;275;200
Berc. 230;95;130;35;130;95;;200
Berc. 170;105;140;35;140;70;255;200
Berc. 38;80;170;40;170;120;315;200
Berc. 69;100;140;40;150;100;250;200
Berc. 223;100;140;40;150;100;250;200
Berc. 285;95;130;45;135;115;;200
Berc. 218;110;160;50;160;110;;200
Berc. 199;120;140;50;140;100;230;200
Berc. 86;110;150;55;150;110;270;200
Berc. 239;115;185;55;190;130;;200
Berc. 70;75;130;60;130;85;265;200
Berc. 24;95;165;65;165;95;335;200
Berc. 75;110;150;70;150;110;285;200
Berc. 167;110;150;75;160;85;320;200
Berc. 158;160;250;80;240;125;470;200
Berc. 18;90;150;85;160;95;340;200
Berc. 60;60;135;90;135;95;310;200
Berc. 13;100;180;90;180;100;395;200
Berc. 14;100;200;90;200;120;420;200
Berc. 10;;;;;;500;200
Berc. 45;;;;;;400;200
Berc. 25;;;;;;1235;205
Berc. 54;75;165;10;165;75;307;240
Berc. 23;60;220;15;220;180;435;240
Berc. 74;140;200;15;210;140;325;240
Berc. 143;110;185;20;190;115;320;240
Berc. 171;115;190;20;180;120;310;240
Berc. 197;130;180;20;180;115;285;240
Berc. 131;105;190;25;190;115;337;240
Berc. 162;110;190;25;195;105;354;240
Berc. 115;115;200;25;205;100;370;240
Berc. 41;120;205;25;210;120;370;240
Berc. 242;125;200;25;190;120;;240
Berc. 48;85;180;30;190;85;360;240
Berc. 58;105;185;30;185;125;320;240
Berc. 224;105;185;30;185;125;320;240
Berc. 161;125;200;30;205;115;360;240
Berc. 203;140;185;30;190;110;315;240
Berc. 106;60;170;35;170;100;335;240
Berc. 92;85;205;35;205;130;390;240
Berc. 193;85;190;35;190;120;355;240
Berc. 226;85;205;35;205;130;390;240
Berc. 127;95;200;35;200;125;370;240
Berc. 241;105;200;35;200;125;;240
Berc. 173;110;200;35;210;140;365;240
Berc. 205;125;210;35;210;135;370;240
Berc. 246;130;210;35;220;200;;240
Berc. 273;80;170;40;170;120;;240
Berc. 186;110;190;40;200;130;355;240
Berc. 194;120;170;40;165;120;;240
Berc. 154;130;210;40;210;150;355;240
Berc. 132;115;200;45;200;110;380;240
Berc. 279;115;210;45;210;140;;240
Berc. 67;95;170;50;170;95;330;240
Berc. 253;110;195;50;185;160;;240
Berc. 126;125;190;50;200;100;370;240
Berc. 243;145;190;50;190;135;;240
Berc. 87;80;160;55;160;100;325;240
Berc. 148;90;180;55;185;120;375;240
Berc. 43;100;190;55;200;100;395;240
Berc. 276;110;200;55;210;135;;240
Berc. 267;135;230;55;210;115;;240
Berc. 278;140;180;55;190;125;;240
Berc. 98;70;160;60;170;100;335;240
Berc. 110;85;150;60;170;110;318;240
Berc. 150;100;210;60;210;120;420;240
Berc. 283;110;195;60;200;135;;240
Berc. 125;115;165;60;170;90;330;240
Berc. 192;85;210;65;215;130;430;240
Berc. 85;100;180;65;180;90;375;240
Berc. 91;110;180;65;180;115;350;240
Berc. 275;145;240;65;220;150;;240
Berc. 109;100;180;70;210;135;385;240
Berc. 225;110;190;70;200;135;380;240
Berc. 96;80;175;75;175;110;370;240
Berc. 113;140;180;75;160;115;335;240
Berc. 56;85;190;80;190;100;415;240
Berc. 183;110;190;80;190;130;385;240
Berc. 232;120;185;80;190;160;;240
Berc. 256;85;190;85;290;250;;240
Berc. 208;135;200;85;200;150;370;240
Berc. 55;80;190;95;200;100;440;240
Berc. 119;140;210;100;200;130;410;240
Berc. 155;90;200;130;210;150;455;240
Berc. 196;130;210;180;210;145;500;240
Berc. 160;20;20;0;350;100;;300
Berc. 122;70;240;15;245;70;480;300
Berc. 61;80;210;30;210;120;395;300
Berc. 236;165;280;30;285;105;;300
Berc. 46;100;230;35;240;100;467;300
Berc. 137;110;210;35;210;135;;300
Berc. 216;120;260;40;240;120;480;300
Berc. 59;100;250;45;250;85;520;300
Berc. 20;105;220;45;210;120;415;300
Berc. 245;180;260;45;260;170;;300
Berc. 99;80;170;50;170;110;330;300
Berc. 6;110;215;50;215;110;425;300
Berc. 47;110;240;50;250;90;495;300
Berc. 101;110;230;50;230;100;460;300
Berc. 174;110;220;50;230;150;425;300
Berc. 248;120;250;50;250;190;;300
Berc. 215;130;240;50;240;120;460;300
Berc. 146;110;270;55;290;150;550;300
Berc. 210;110;260;55;270;180;500;300
Berc. 90;80;200;60;210;115;420;300
Berc. 83;100;180;60;185;110;360;300
Berc. 94;105;220;60;230;120;450;300
Berc. 261;105;235;60;250;165;;300
Berc. 181;130;240;60;240;150;460;300
Berc. 118;150;240;60;220;95;445;300
Berc. 66;70;220;65;220;120;455;300
Berc. 260;100;260;65;270;140;;300
Berc. 282;115;220;65;205;115;;300
Berc. 211;120;230;65;260;185;453;300
Berc. 95;125;200;65;190;115;375;300
Berc. 201;140;260;65;270;140;525;300
Berc. 88;90;260;70;250;125;530;300
Berc. 84;105;230;70;220;130;455;300
Berc. 144;110;250;70;260;160;505;300
Berc. 184;110;210;70;210;150;400;300
Berc. 204;130;240;70;240;150;460;300
Berc. 257;140;250;70;255;165;;300
Berc. 97;70;220;75;230;110;485;300
Berc. 147;110;230;75;230;150;455;300
Berc. 259;160;265;75;270;185;;300
Berc. 228;90;230;80;250;110;;300
Berc. 108;110;260;80;270;140;550;300
Berc. 185;110;240;80;240;125;500;300
Berc. 93;80;210;90;210;90;480;300
Berc. 124;100;240;90;260;130;535;300
Berc. 142;110;240;90;250;145;510;300
Berc. 280;120;260;90;255;155;;300
Berc. 152;135;270;90;270;180;525;300
Berc. 138;165;250;90;260;155;490;300
Berc. 258;110;230;95;230;150;;300
Berc. 89;65;210;100;210;85;495;300
Berc. 284;160;260;105;265;130;;300
Berc. 277;140;250;110;250;155;;300
Berc. 244;170;225;110;210;110;;300
Berc. 105;50;180;125;180;110;445;300
Berc. 287;160;280;160;280;180;;300
Berc. 163;250;100;160;;;;300
Berc. 164;250;100;160;;;;300
Berc. 77;100;270;25;270;115;525;380
Berc. 81;115;250;25;250;115;475;380
Berc. 44;120;290;30;280;100;565;380
Berc. 213;140;300;60;300;140;590;380
Berc. 141;135;280;65;280;160;545;380
Berc. 198;100;280;70;280;180;550;380
Berc. 15;110;270;70;270;140;550;380
Berc. 188;120;280;70;280;180;540;380
Berc. 136;160;280;70;295;220;580;380
Berc. 266;175;320;70;330;190;;380
Berc. 252;90;310;80;320;140;;380
Berc. 68;75;260;85;270;150;560;380
Berc. 129;130;250;85;260;135;525;380
Berc. 179;150;280;85;280;150;;380
Berc. 200;160;300;85;310;210;580;380
Berc. 145;105;270;95;280;170;570;380
Berc. 165;130;310;100;320;180;650;380
Berc. 209;160;290;100;290;160;590;380
Berc. 133;180;280;100;270;140;543;380
Berc. 265;210;305;105;300;195;;380
Berc. 207;60;270;110;270;85;590;380
Berc. 268;80;310;110;330;200;;380
Berc. 65;100;290;110;290;190;610;380
Berc. 159;110;300;110;290;180;;380
Berc. 117;140;290;110;270;130;600;380
Berc. 221;150;270;110;270;85;590;380
Berc. 212;150;280;120;280;170;580;380
Berc. 135;190;280;120;180;100;620;380
Berc. 140;130;290;125;280;145;625;380
Berc. 78;120;280;130;270;155;610;380
Berc. 130;130;280;130;280;170;600;380
Berc. 153;140;290;130;280;170;605;380
Berc. 80;130;270;140;270;175;580;380
Berc. 102;105;240;145;240;140;555;380
Berc. 103;70;250;170;250;190;575;380
Berc. 139;130;280;250;;;;380
Berc. 79;55;280;45/57;270;45;585;380
Berc. 82;95;290;100;290;150;625;400
Berc. 229;100;270;50;310;180;;450
Berc. 128;130;340;70;340;145;700;450
Berc. 76;90;285;90;285;120;620;450
Berc. 149;120;340;115;340;210;705;450
Berc. 100;80;270;120;270;170;605;450
Berc. 64;165;330;120;330;150;715;450
Berc. 40;100;320;130;320;240;650;450
Berc. 63;130;290;130;300;130;670;450
Berc. 62;180;400;45;400;170;770;500
Berc. A13;140;200;0;200;140;295;145
Berc. A9;45;120;0;120;45;220;150
Berc. A5;45;90;10;110;75;175;155
Berc. A6;85;100;20;120;90;200;160
Berc. A12;55;90;10;140;90;205;160
Berc. A3;90;125;65;120;90;250;175
Berc. A1;65;115;15;115;100;200;190
Berc. A7;65;125;20;125;80;250;190
Berc. A14;95;155;10;155;85;290;190
Berc. A2;75;120;10;150;90;220;195
Berc. A18;145;165;20;130;85;240;195
Berc. A10;80;135;15;140;80;255;200
Berc. A11;70;110;30;115;75;240;200
Berc. A15;110;160;10;135;85;265;200
Berc. A16;75;150;40;150;105;265;200
Berc. A19;120;155;30;155;125;250;205
Berc. A23;80;155;10+30;155;95;290;205
Berc. A8;65;140;10;140;80;260;210
Berc. A17;100;155;20;130;75;250;210
Berc. A20;80;13;10;140;80;250;210
Berc. A21;80;155;10+30;160;120;305;210
Berc. A24;105;170;0;180;85;300;210
Berc. A25;60;200;0;200;55;405;210
Berc. A30;125;205;5;190;100;335;210
Berc. A4;80;150;15;150;100;250;215
Berc. A22;65;135;15+15;135;80;280;215
Berc. A27;80;130;10;150;60;250;215
Berc. A28;100;145;10;155;100;275;215
Berc. A29;150;180;60;170;130;285;215
Berc. A32;80;135;10;135;80;275;220
Berc. A26;110;130;10+60;135;70;285;225
Berc. A31;60;140;10+25;140;105;275;225
Berc. A33;130;200;5;165;105;300;225
Berc. A35;95;150;30;150;95;270;225
Berc. A36;155;210;20;150;85;290;230
Berc. A37;155;195;5;150;80;270;230
Berc. A34;55;130;10+40;145;35;310;235
Berc. A38;95;175;10;170;95;315;260"""

Cradles = []

for RawCradle in CradlesRaw.split('\n'):
    (ID, E, D, C, B, A, Glob, H) = RawCradle.split(';')

    print (f"\nCreating {ID}...")

    try:
        pass
        #print(ID, int(E), int(D), int(C), int(B), int(A), int(Glob), int(H))
        # overkill
    except:
        pass
        #print("Problem with one of the elements")
    # E
    
    # This can be replaced with a map?
    Dimensions = [E, D, C, B, A, Glob, H]
    for Index, Dimension in enumerate(Dimensions):
        try:
            Dimension = int(Dimension)
        except:
            Dimension = 0
        Dimensions[Index] = Dimension
    print(Dimensions)

    # Calculate the angle of the left part of the cradle
    AngleGauche = 0.0
    AngleDroite = 0.0

    try:
        AngleGaucheRad = math.asin(Dimensions[4]/Dimensions[3]) # hauteur partie gauche / plat a gauche = O/S
        AngleGauche = math.degrees(AngleGaucheRad)
    except:
        print("Division by zero: plat gauche is zero")

    try:
        AngleDroiteRad = math.asin(Dimensions[0]/Dimensions[1]) # hauteur partie droite / plat a droite = O/S
        AngleDroite = math.degrees(AngleDroiteRad)
    except:
        print("Division by zero: plat droite is zero")

    Cradle = {
        "ID": ID,
        "A": Dimensions[4], # Hauteur (partie gauche)
        "B": Dimensions[3], # Plat (a gauche)
        "C": Dimensions[2], # Largeur dos
        "D": Dimensions[1], # Plat (a droit)
        "E": Dimensions[0], # Hauteur (partie droite)
        "H": Dimensions[6], # Profondeur
        "Z": None, # largeur globale du berceaux # not always present
        
        # additional dimensions calculated automatically but not measured
        "AngleLeft" : AngleGauche,
        "AngleRight": AngleDroite,
    }
    Cradles.append(Cradle)
    print(Cradle)

print(f"\n\nDone processing {len(Cradles)} cradles!")
time.sleep(1)
print(f"You will now be asked to enter the dimensions of the book...")
time.sleep(1)

Ms15137 = {
    "ID": "Ms. 15137",
    "E": 75, # Hauteur pardie droite    # == M
    "D": 144, # Plat (a droit)          # == L
    "C": 15, # Largeur dos              # == K
    "B": 148, # Plat (a gauche)         # == J
    "A": 120, # Hauteur partie gauche   # == I
    "H": 190, # Profondeur
}
Books = [Ms15137]

# Dimensions fetched from user input
#BookDimensionI = 0
BookDimensionJ = 0
BookDimensionK = 0
BookDimensionL = 0
#BookDimensionM = 0
BookDimensionH = 0

BookDimensionHauteurGauche = 0
BookDimensionHauteurDroite = 0

try:
    #BookDimensionI = int(input("Enter Hauteur (partie gauche) in mm: "))
    #BookDimensionJ = int(input("Enter Hauteur (partie droite) in mm: "))
    print("Please enter the dimensions of the book:", "\n")
    BookDimensionJ = int(input("Enter \'Plat a gauche\' (J) in mm: "))
    BookDimensionK = int(input("Enter \'Largeur dos\' (K) in mm: "))
    BookDimensionHauteurGauche = int(input("Enter \'Hauteur gauche\' in mm: "))
    
    BookDimensionL = int(input("Enter \'Plat a droite\' (L) in mm: "))
    BookDimensionH = int(input("Enter \'Profondeur\' (H) in mm: "))
    BookDimensionHauteurDroite = int(input("Enter \'Hauteur droite\' in mm: "))

except:
    print("Problem while entering dimensions of the book. Exiting...")
    exit() # maybe until dimensions non zero

print(f"\nThanks, book dimensions: {BookDimensionJ}x{BookDimensionK}x{BookDimensionL}x{BookDimensionH} (JxKxLxH) mm")

BookLeftAngleInRads = math.asin(BookDimensionHauteurGauche / BookDimensionJ)
BookLeftAngleInDegrees = math.degrees(BookLeftAngleInRads)

BookRightAngleInRads = math.asin(BookDimensionHauteurDroite / BookDimensionL)
BookRightAngleInDegrees = math.degrees(BookRightAngleInRads)
print(f"Calculated angle left: {BookLeftAngleInDegrees:.2f}°, angle right: {BookRightAngleInRads:.2f}°")

print("I will now begin matching the book to cradles.")

TimeOut = 6
while TimeOut > 0:
    time.sleep(1)
    print(". ")
    TimeOut = TimeOut - 1

Matches = []

print ("Cradles: ", Cradles)
print ("Matches: ", Matches)

for Cradle in Cradles:
    id = Cradle["ID"]
    print(f"\nBegin matching with cradle {id}")
    
    Match = True
    # Ignore the A/I, E/M dimensions for now
    #if Cradle["A"] >= (I - 10) and Cradle["A"] <= (I + 10):
    #Match = Match and ((I - 10) <= Cradle["A"] <= (I + 10))
    #CradleHauteurGauche = Cradle["A"]
    #Match = Match and CradleHauteurGauche - 10 <= I <= CradleHauteurGauche + 10
    #print("Hauteur (partie gauche): ", CradleHauteurGauche - 10, I, CradleHauteurGauche + 10, Match)
    
    #Match = Match and ((M - 10) <= Cradle["E"] <= (M + 10))
    #print("Hauteur (partie droite): ", M - 10, Cradle["E"], (M + 10))
    
    # 1: match on H
    # depth of the cradle <= height of the book (always)
    CradleDepth = Cradle["H"]
    #BookDepth = H
    BookDepth = BookDimensionH
    Match = Match and (CradleDepth <= BookDepth)
    print(f"Cradle depth: {CradleDepth} mm, book depth: {BookDepth} mm, CradleDepth <= BookDepth: {CradleDepth <= BookDepth}, match?: {Match}")

    # 2: match on C/K (dos)
    # opening of the cradle needs to always equal or exceed the back of the book
    CradleOpening = Cradle["C"]
    #BookBack = K
    BookBack = BookDimensionK
    Match = Match and (CradleOpening >= BookBack)
    print(f"Cradle opening: {CradleOpening} mm, book back: {BookBack} mm, CradleOpening >= BookBack: {CradleOpening >= BookBack}, match?: {Match}")
    
    # 3: match on the plats
    CradlePlatLeft = Cradle["B"]
    CradlePlatRight = Cradle["D"]
    BookPlatLeft = BookDimensionJ
    BookPlatRight = BookDimensionL

    # the book dimensions here should exceed the cradle dimensions
    # essentially, 
    # boek plat = 100 --> wieg plat 50 tot 90
    #Match = Match and #CradlePlatLeft - 50 <= BookPlatLeft <= CradlePlatLeft - 10

    # beokplat 100, wiegplat 
    Match = Match and CradlePlatLeft <= BookPlatLeft - 10
    print(f"Cradle plat left: {CradlePlatLeft} mm, book plat left: {BookPlatLeft} mm, CradlePlatLeft <= BookPlatLeft - 10: {CradlePlatLeft <= BookPlatLeft - 10}, match?: {Match}")

    Match = Match and CradlePlatRight <= BookPlatRight - 10
    print(f"Cradle plat right: {CradlePlatRight} mm, book plat right: {BookPlatRight} mm, CradlePlatRight <= BookPlatRight - 10: {CradlePlatRight <= BookPlatRight - 10}, match?: {Match}")

    #Match = Match and ((J - 10) <= Cradle["B"] <= (J + 50))
    #print("Plat (a gauche): ", J - 10, Cradle["B"], (J + 50))
    
    #Match = Match and ((L - 10) <= Cradle["D"] <= (L + 50))
    #print("Plat (a droit): ", L - 10, Cradle["D"], (L + 50))
    
    # match for the angle as well i.e. the cradle angle should be within 5 degrees of the book angle
    CradleLeftAngle = Cradle["AngleLeft"]
    CradleRightAngle = Cradle["AngleRight"]
    AngleTolerance = 5
    
    Match = Match and BookLeftAngleInDegrees - AngleTolerance <= CradleLeftAngle <= BookLeftAngleInDegrees + AngleTolerance
    print(f"Cradle left angle: {CradleLeftAngle:.2f} mm, book angle range: {BookLeftAngleInDegrees - AngleTolerance:.2f}-{BookLeftAngleInDegrees + AngleTolerance:.2f} mm, match?: {Match}")

    Match = Match and BookRightAngleInDegrees - AngleTolerance <= CradleRightAngle <= BookRightAngleInDegrees + AngleTolerance
    print(f"Cradle right angle: {CradleRightAngle:.2f} mm, book angle range: {BookRightAngleInDegrees - AngleTolerance:.2f}-{BookRightAngleInDegrees + AngleTolerance:.2f} mm, match?: {Match}")

    if Match:
        Matches.append(Cradle)

print(f"\n\nDone matching book to cradles! I found {len(Matches)}. Printing overview...\n\n")

for Match in Matches:        
    print("Match: ", Match)




