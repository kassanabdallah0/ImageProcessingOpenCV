import cv2
import matplotlib.pyplot as plt
import numpy as np
import pickle
import os


def rescale_frame(frame, scale=0.75):
    # works with photos, videos, live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

    # rescale_frame: pour faire l'image plus gros ou plus petit


def extrfct(image, i, contours, filename):
    blank = np.zeros(image.shape, dtype='uint8')
    cv2.drawContours(blank, contours, i, (255, 255, 255), 3)
    cv2.fillConvexPoly(blank, contours[i], (255, 255, 255))
    # crpim = cropobj(blank, contours)
    # if area < 400:
    # return None
    # else:
    return cv2.imwrite(filename + f'{i}.jpg', blank)
    # extrfct: pour sauvgarder chaque impact dans une image


def centrefct(cnt):
    M = cv2.moments(cnt)
    if M['m00'] == 0:
        cx = int(M['m10'] / (M['m00'] + 1))
        cy = int(M['m01'] / (M['m00'] + 1))
    else:
        cx = int(M['m10'] / (M['m00']))
        cy = int(M['m01'] / (M['m00']))
    center = (cx, cy)
    return center
    # centrefct: pour calculer le centre d'impact


def plot1(name, titre, im0):
    plt.figure(f'{name}')
    plt.imshow(im0)
    plt.title(f'{titre}')
    plt.show()
    # plot: pour faire le dessin d'image


def cropobj(image, contours):
    idnum = 0
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        if w > 50 and h > 50:
            idnum += 1
            new_img = image[y:y + h, x:x + w]
            return new_img
        else:
            return None
    # cropobj: pour extract un objet d'une image (à fixer)


def puText(im0, surface, perimetre, index, centre):

    bi = False
    ba = False
    bp = False

    try:
        with open('txt/boolindx.bin', 'rb') as file:
            bi = pickle.load(file)
    except (IOError, pickle.UnpicklingError):
        print('Erreur de lecture.')

    try:
        with open('txt/boolarea.bin', 'rb') as file:
            ba = pickle.load(file)
    except (IOError, pickle.UnpicklingError):
        print('Erreur de lecture.')

    try:
        with open('txt/boolperimètre.bin', 'rb') as file:
            bp = pickle.load(file)
    except (IOError, pickle.UnpicklingError):
        print('Erreur de lecture.')

    if ba == True:
        cv2.putText(im0, "A: {0:2.1f}".format(surface), centre,
                    cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 1)
    if bp == True:
        cv2.putText(im0, "P: {0:2.1f}".format(perimetre), (centre[0], centre[1] + 40),
                    cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 1)
    if bi == True:
        cv2.putText(im0, "IDX: {0:2.1f}".format(index), (centre[0], centre[1] + 70),
                    cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 1)
    return None
    # puText: pour mettre les informations des impact sur l'image initiale qui contient tous les impacts


def Debug(contours, filename):
    ii = 0
    list_1 = []
    list_2 = []
    lengthtotal = 0
    for iI in contours:
        im = cv2.imread(filename + f'{ii}.jpg', 0)
        ret0, thresh0 = cv2.threshold(im, 127, 255, cv2.THRESH_BINARY)
        contoursI, _ = cv2.findContours(thresh0, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        lengthcontours = len(contoursI)
        lengthtotal += lengthcontours
        for cntr in contoursI:
            image1 = aproximation(im)
            center1 = centrefct(cntr)
            center0 = (center1[0] / 5, center1[1] / 5)
            area1 = (cv2.contourArea(cntr)) / 25
            perimetre1 = (cv2.arcLength(cntr, True)) / 5
            puText(image1, area1, perimetre1, ii, center1)
            if lengthcontours > 1:
                list_1.append(ii)
                plot1('debug', 'erreur dans 'f'{ii}', image1)
            else:
                list_2.append(ii)
        ii += 1
        cv2.destroyAllWindows()

    return None
    # filtreimg: pour faire des filtre sur l'image pour adapter le plus grands nombres des impacts


def filtreimg(img, i, auto):
    blur = cv2.cv2.GaussianBlur(img, (3, 3), 0)
    if auto:
        n = np.array(blur)
        mean = np.mean(n)
        print(mean)
        if mean < 100:
            ret, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        else:
            print(999)
            ret, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
            print(999)
    else:
        n = np.array(blur)
        mean = np.mean(n)
        if mean < 100:
            ret, thresh = cv2.threshold(blur, i, 255, cv2.THRESH_BINARY)
        else:
            print(999)
            ret, thresh = cv2.threshold(blur, i, 255, cv2.THRESH_BINARY_INV)
            print(999)
    return thresh

def resolution(img):
    wid = img.shape[1]
    hgt = img.shape[0]
    return None
    # resolution: nous donne la resolution d'une image

def aproximation(cnt):
    epsilon = 0.01 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    return approx
    # pour entourer les impacts dans une image avec une approximation precis

def hierarchysplit(hierarchy, length):
    if length == 0:
      h = [[0,0], [0,0]]
    else:
        h = np.array_split(hierarchy[0], length)
        i = 0
        test_list = []

    while i < len(h):
        test_list.insert(i - 1, h[i])
        i += 1
    return test_list

def child(hierarchy, length):
    test_list = hierarchysplit(hierarchy, length)
    childlist = []
    j = 0
    i = 0
    while i < len(test_list):
        if test_list[i][0][2] != -1:
            childlist.insert(j, test_list[i][0][2])
            j += 1
        i += 1
    return childlist

def parents(hierarchy, length):
    test_list = hierarchysplit(hierarchy, length)
    parentslist = []
    j = 0
    i = 0
    while i < len(test_list):
        if test_list[i][0][3] != -1:
            parentslist.insert(j, test_list[i][0][3])
            j += 1
        i += 1
    return parentslist

def filtragedecontourschild(contours, hierarchy, length):
    childlist = child(hierarchy, length)
    contoursfiltrerlist = []
    i = 0
    m = 0
    while i < length:
        j = 0
        while j < len(childlist):
            if i == childlist[j]:
                i += 1
            j += 1
        contoursfiltrerlist.insert(m, contours[i])
        m += 1
        i += 1
    return contoursfiltrerlist

def filtragedecontoursparents(contours, hierarchy, length):
    parentslist = parents(hierarchy, length)
    contoursfiltrerlist = []
    i = 0
    m = 0
    while i < length:
        j = 0
        while j < len(parentslist):
            if i == parentslist[j]:
                i += 1
            j += 1
        contoursfiltrerlist.insert(m, contours[i])
        m += 1
        i += 1
    return contoursfiltrerlist

def filtreimgcanny(img):
    blur = cv2.cv2.GaussianBlur(img, (5, 5), 0)
    canny = cv2.Canny(blur, 125, 175)
    ret, thresh = cv2.threshold(canny, 127, 255, cv2.THRESH_BINARY)
    return thresh

def MaxArea(test_list1):
    """"
    i = 2
   x = (test_list1[2])

   while i < length:
       j = 2
       while j < length:
           if x >= test_list1[j]:
               j += 4
           else:
               break
       x = (test_list1[j])
       i += 4
   return x, j
   """
    i = 0
    j = 0
    listxl3 = test_list1[2::4]
    length = len(listxl3)
    x = listxl3[0]
    j = 0
    while j < length:
        if x >= listxl3[j]:
            j += 1
        else:
            x = listxl3[j]
            i = j
    return x, i

def MaxPerimetre(length, test_list1):
    global j
    i = 3
    x = (test_list1[3])
    while i < length:
        j = 2
        while j < length:
            if x >= test_list1[j]:
                j += 4
            else:
                break
        x = (test_list1[j])
        i += 4
    return x, j

def nbfiltre(img, i, tresh1, auto):
    if i > 0:
        ii = 0
        while ii < i:
            img = filtreimg(img, tresh1, auto)
            ii += 1
    return img

def ECHELLE():
    if os.path.exists('txt/echell.bin'):
        try:
            with open('txt/echell.bin', 'rb') as file:
                echelle = pickle.load(file)
                return echelle
        except (IOError, pickle.UnpicklingError):
            print('Erreur de lecture.')

def main(nbrefiltre=1, tresh1=127, thikn1=1,auto=True):
    img = cv2.imread(r'./img/img_cut_grav.jpg')
    img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img1 = nbfiltre(img1, nbrefiltre, tresh1, auto)
    default = cv2.countNonZero(img1)
    if default <= 10:
        img1 = cv2.imread(r'./Photos/Default.jpg', 0)

    thresh = img1
    contours1, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    i = 0
    area_List = []
    perimetre_list = []
    listx = []
    listy = []
    test_list = []
    test_list1 = []

    for cnt in contours1:
        area = cv2.contourArea(cnt)
        if not area == 0:
            '''
            epsilon = 0.000001 * cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, epsilon, True)
            '''
            cv2.drawContours(img, [cnt], 0, (0, 255, 0), thikn1)
            center = centrefct(cnt)
            center0 = (center[0], center[1])

            area_List.insert(i, area)

            i += 1
            perimetre = cv2.arcLength(cnt, True)  # divisé par scale pour calculer le vrai perimetre du contour
            perimetre_list += [perimetre]
            # pour calculer les vrais coordonnes des contours dans l'image et le metre dans une list
            puText(img, area, perimetre, i, center)
            listx += [center[0]]
            listy += [center[1]]
            test_list1 += [i, center0, area, perimetre]
            test_list += ["numero d'impact: " + str(i), " coordonnes d'impact= " + str(center0), "area= " + str(area),
                          "perimetre= " + str(perimetre)]

    return test_list1, listx, listy, img, len(area_List), area_List, perimetre_list

def plotimage(valuefiltre, valuetresh, valuecontour):
    _, _, _, img, _, _, _ = main(valuefiltre, valuetresh, valuecontour)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    plot1('Exemple', 'binary contour plot', img)


def img_binary(img_in, v_threshold, max_threshold, background):
    # background color  0: black; 255: white
    gray = cv2.cvtColor(img_in, cv2.COLOR_BGR2GRAY)
    if background == 0:  # Le fond de l'image est noir et les lignes sont blanches
        # Traitement du seuil Méthode binaire Paramètres : image d'entrée ; seuil réglable (les valeurs inférieures au seuil deviennent 0 et les valeurs supérieures au seuil deviennent la valeur maximale) ; la valeur maximale spécifiée ; le mode de sélection est binaire
        ret, img_out = cv2.threshold(gray, v_threshold, max_threshold, cv2.THRESH_BINARY)
    else:
        ret, img_out = cv2.threshold(gray, v_threshold, max_threshold, cv2.THRESH_BINARY_INV)
    return img_out


def delete_line(treated_img, h, v, times):
    # définir la forme du noyau comme rectangulaire
    h_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, h))
    v_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (v, 1))
    # Opération d'ouverture, paramètres : graphique d'entrée ; l'opération est une opération d'ouverture ; élément de structure (noyau) utilisé
    h_opening = cv2.morphologyEx(treated_img, cv2.MORPH_OPEN, h_kernel, times)  # obtenir des lignes verticales
    v_opening = cv2.morphologyEx(treated_img, cv2.MORPH_OPEN, v_kernel, times)  # obtenir des lignes horizontales
    # différence c = a - b, paramètres : a ; b
    h_delete = cv2.subtract(treated_img, h_opening)  # supprimer les lignes verticales
    hv_delete = cv2.subtract(h_delete, v_opening)  # puis supprimer les lignes horizontales
    return hv_delete


# obtenir le pourcentage de pixel blanc sur toute l'image
def get_surface(img_in):
    # renvoie le nombre d'éléments non nuls dans src ; 0 est noir et 255 est blanc
    default_s = cv2.countNonZero(img_in)
    # renvoie le nombre de pixels de l'image entière
    sur = img_in.size
    percent = default_s / sur
    return percent * 100


# supprimer les lignes noires inattendues
def morph_close_cross(treated_img, a):
    if a == 0:
        return treated_img
    # Définir les éléments structurels, les paramètres : la forme de la structure est une grille ; la longueur et la largeur de la structure ; le point d'ancrage
    c_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (a, a), (-1, -1))
    # Opération de fermeture : éliminer les lignes noires
    close_res = cv2.morphologyEx(treated_img, cv2.MORPH_CLOSE, c_kernel)
    return close_res


# dessiner les contours
def draw_contours(img_in, img_org):
    contours, hierarchy = cv2.findContours(img_in, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    img_org_1 = img_org.copy()
    draw = cv2.drawContours(img_org_1, contours, -1, (0, 255, 0), 1)
    return draw


# utilisez MORPH_CROSS pour supprimer la grille
def delete_line_cross(treated_img, cross_len, cross_wide):
    # Définir les éléments structurels, les paramètres : la forme de la structure est une grille ; la longueur et la largeur de la structure ; le point d'ancrage
    c_kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (int(cross_len), int(cross_wide)), (-1, -1))
    # Chapeau haut de forme : l'image d'origine moins le résultat de l'opération d'ouverture
    tophat_res = cv2.morphologyEx(treated_img, cv2.MORPH_TOPHAT, c_kernel)
    return tophat_res

def display_lines(img, lines):
  for line in lines:
    x1, y1, x2, y2 = line
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 0), 2)
    cv2.circle(img, (x1, y1), 1, (0, 0, 0), 2)
    cv2.circle(img, (x2, y2), 1, (0, 0, 0), 2)
  return img

def eliminate(img):
    thresh = np.zeros(img.shape, dtype='uint8')
    thr_org = np.zeros(img.shape, dtype='uint8')
    try:
        blur = cv2.bilateralFilter(img,9,75,75)
        ret, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        thr_org = thresh
        canny = cv2.Canny(thresh, 30, 300, apertureSize=3, L2gradient=True)
        lines = cv2.HoughLinesP(canny, 1, np.pi / 180, 50, minLineLength=100, maxLineGap=20)
        lines = np.squeeze(lines)
        thresh = display_lines(thresh, lines)
        thresh = cv2.rotate(thresh, cv2.ROTATE_90_CLOCKWISE)
        lines = cv2.HoughLinesP(thresh, 1, np.pi / 180, 50, minLineLength=100, maxLineGap=20)
        lines = np.squeeze(lines)
        thresh = display_lines(thresh, lines)
        thresh = cv2.rotate(thresh, cv2.ROTATE_90_COUNTERCLOCKWISE)
        ret, thresh = cv2.threshold(thresh, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        return thresh, thr_org
    except:
        return thresh, thr_org

