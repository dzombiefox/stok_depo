from lxml.html.diff import tag_token
from django.core.exceptions import ObjectDoesNotExist
from django import template
register = template.Library()
from stok .models import Stok,StokPabrik,Standard
from django.db.models import Sum
from datetime import datetime
import pyodbc
from django.http import HttpResponse


@register.filter(name="boxkita")
def boxkita(tanggal,size):
    data = Stok.objects.filter(tanggal=tanggal,size = size)
    totalbox = 0
    for data in data :
        totalbox += int(data.kita)
    return totalbox

@register.filter(name="boxatena")
def boxatena(tanggal,size):
    data = Stok.objects.filter(tanggal=tanggal,size = size)
    totalbox = 0
    for data in data :
        totalbox += int(data.atena)
    return totalbox

@register.filter(name="boxpicasso")
def boxpicasso(tanggal,size):
    data = Stok.objects.filter(tanggal=tanggal,size = size)
    totalbox = 0
    for data in data :
        totalbox += int(data.picasso)
    return totalbox

@register.filter(name="boxharmony")
def boxharmony(tanggal,size):
    data = Stok.objects.filter(tanggal=tanggal,size = size)
    totalbox = 0
    for data in data :
        totalbox += int(data.harmony)
    return totalbox



@register.filter(name="grandtotalkita")
def grandtotalkita(tanggal):
    cdata = Stok.objects.filter(tanggal=tanggal)
    totalkita = 0
    for data in cdata :
        totalkita += int(data.kita)
    return totalkita

@register.filter(name="grandtotalpicasso")
def grandtotalpicasso(tanggal):
    cdata = Stok.objects.filter(tanggal=tanggal)
    totalpicasso = 0
    for data in cdata :
        totalpicasso += int(data.picasso)
    return totalpicasso

@register.filter(name="grandtotalharmony")
def grandtotalharmony(tanggal):
    cdata = Stok.objects.filter(tanggal=tanggal)
    totalharmony = 0
    for data in cdata :
        totalharmony += int(data.harmony)
    return totalharmony

@register.filter(name="grandtotalatena")
def grandtotalatena(tanggal):
    cdata = Stok.objects.filter(tanggal=tanggal)
    totalatena = 0
    for data in cdata :
        totalatena += int(data.atena)
    return totalatena



@register.filter(name="persenkita")
def persenkita(tanggal,size) :
    totalkita = grandtotalkita(tanggal)
    data = Stok.objects.filter(tanggal = tanggal ,size = size)
    totalbox = 0
    for data in data :
        totalbox += int(data.kita)
    if totalkita == 0:
        total =0
    else :
        total = 100 *(float(totalbox)/float(totalkita))
    return "{:.2f}".format(total)


@register.filter(name="totalpersenkita")
def totalpersenkita(tanggal) :
    totalkita = grandtotalkita(tanggal)
    data = Stok.objects.filter(tanggal = tanggal)
    totalbox = 0
    for data in data :
        totalbox += int(data.kita)
    if totalkita ==0:
        total = 0
    else :
        total = 100 *(float(totalbox)/float(totalkita))
    return "{:.2f}".format(total)

@register.filter(name="persenpicasso")
def persenpicasso(tanggal,size) :
    totalpicasso = grandtotalpicasso(tanggal)
    # return totalpicasso
    data = Stok.objects.filter(tanggal = tanggal ,size = size)
    totalbox = 0
    for data in data :
        totalbox += int(data.picasso)
    if totalpicasso == 0 :
        totalbox = 0
    else :
        totalbox = 100 *(float(totalbox)/float(totalpicasso))
    return "{:.2f}".format(totalbox)


@register.filter(name="totalpersenpicasso")
def totalpersenpicasso(tanggal) :
    totalpicasso = grandtotalpicasso(tanggal)
    data = Stok.objects.filter(tanggal = tanggal)
    totalbox = 0
    for data in data :
        totalbox += int(data.picasso)
    if totalpicasso ==0:
        total = 0
    else :
        total = 100 *(float(totalbox)/float(totalpicasso))
    return "{:.2f}".format(total)

@register.filter(name="persenharmony")
def persenharmony(tanggal,size) :
    totalharmony = grandtotalharmony(tanggal)
    data = Stok.objects.filter(tanggal = tanggal ,size = size)
    totalbox = 0
    for data in data :
        totalbox += int(data.harmony)
    if totalharmony == 0 :
        total = 0
    else :
        total = 100 *(float(totalbox)/float(totalharmony))
    return "{:.2f}".format(total)


@register.filter(name="totalpersenharmony")
def totalpersenharmony(tanggal) :
    totalharmony = grandtotalharmony(tanggal)
    data = Stok.objects.filter(tanggal = tanggal)
    totalbox = 0
    for data in data :
        totalbox += int(data.harmony)
    if totalharmony == 0 :
        total =0
    else :
        total = 100 *(float(totalbox)/float(totalharmony))
    return "{:.2f}".format(total)

@register.filter(name="persenatena")
def persenatena(tanggal,size) :
    totalatena = grandtotalatena(tanggal)
    data = Stok.objects.filter(tanggal = tanggal ,size = size)
    totalbox = 0
    for data in data :
        totalbox += int(data.atena)
    if totalatena ==0:
        total = 0
    else :
        total = 100 *(float(totalbox)/float(totalatena))
    return "{:.2f}".format(total)


@register.filter(name="totalpersenatena")
def totalpersenatena(tanggal) :
    totalatena = grandtotalatena(tanggal)
    data = Stok.objects.filter(tanggal = tanggal)
    totalbox = 0
    for data in data :
        totalbox += int(data.atena)
    if totalatena ==0:
        total = 0
    else :
        total = 100 *(float(totalbox)/float(totalatena))
    return "{:.2f}".format(total)


@register.filter(name='boxpicharmony')
def boxpicharmony(tanggal , size) :
    # return 1
    data  = Stok.objects.filter(tanggal = tanggal , size = size)
    picasso = 0
    harmony = 0
    for data in data :
        picasso += int (data.picasso)
        harmony += int(data.harmony)
    return int(picasso)+int(harmony)

@register.filter(name='grandtotalboxpicharmony')
def grandtotalboxpicharmony(tanggal) :
    # return 1
    data  = Stok.objects.filter(tanggal = tanggal )
    picasso = 0
    harmony = 0
    for data in data :
        picasso += int (data.picasso)
        harmony += int(data.harmony)
    return int(picasso)+int(harmony)


@register.filter(name="totalpersenpicharmony")
def totalpersenpicharmony(tanggal,size) :
    box =boxpicharmony(tanggal,size)
    totalbox = grandtotalboxpicharmony(tanggal)
    if box == 0:
        total = 0
    else :
        total = 100*(float (box) / float(totalbox))
    return "{:.2f}".format(total)

@register.filter(name='grandtotalpersenpicharmony')
def grandtotalpersenpicharmony(tanggal) :
    # return 1
    totalpicasso = grandtotalpicasso(tanggal)
    totalharmony = grandtotalharmony(tanggal)
    totalbox = int(totalpicasso)+ int(totalharmony)
    data = Stok.objects.filter(tanggal = tanggal)
    totalboxpicasso = 0
    totalboxharmony = 0

    for data in data :
        totalboxpicasso += int(data.picasso)
        totalboxharmony += int(data.harmony)
    if totalpicasso == 0 | totalharmony == 0:
        total =0
    else :
        total = 100*((float(totalboxpicasso) + float (totalboxharmony)) / float(totalbox))
    return total

@register.filter(name="totalbox")
def totalbox(tanggal ,size):
    kita = boxkita(tanggal,size)
    picasso = boxpicasso(tanggal, size)
    harmony = boxharmony(tanggal, size)
    atena = boxatena(tanggal, size)
    total = int(kita) + int(picasso)+int(harmony)+int(atena)
    return total

@register.filter(name ="grandtotalbox")
def grandtotalbox(tanggal):
    atena = grandtotalatena(tanggal)
    picasso = grandtotalpicasso(tanggal)
    harmony = grandtotalharmony(tanggal)
    kita =grandtotalkita(tanggal)
    total =int(atena) +int(picasso) + int(harmony) +int(kita)
    return  total

@register.filter(name="totalpersen")
def totalpersen(tanggal,size):
    # return 1
    gbox =grandtotalbox(tanggal)
    tbox = totalbox(tanggal,size)
    if gbox == 0 | tbox == 0:
        total =0
    else :
        total = 100*(float (tbox) / float(gbox))

    return "{:.2f}".format(total)

@register.filter(name = "grandtotalpersen")
def grandtotalpersen(tanggal):
    # return 1
    grandtotal = grandtotalbox(tanggal)
    data = Stok.objects.filter(tanggal=tanggal)
    totalatena = 0
    totalpicasso = 0
    totalharmony = 0
    totalkita = 0
    for data in data:
        totalatena += int(data.atena)
        totalpicasso += int(data.picasso)
        totalharmony += int(data.harmony)
        totalkita += int(data.kita)
    totalbox = totalatena + totalpicasso + totalharmony +totalkita
    if totalbox == 0 :
        return 0
    else :
        total =100 * (float(totalbox) / float(grandtotal))
    return total


@register.filter(name = "kurang_k")
def kurang_k(tanggal):
    # return 1
    total = grandtotalkita(tanggal)
    std = Standard.objects.get(pk=1)
    totalkurang =int(total) -int(std.sk_box)
    return totalkurang


@register.filter(name="lkpersen_kita")
def lkpersen_kita(tanggal):
    # return 1
    kurang = kurang_k(tanggal)
    totalbox = grandtotalbox(tanggal)
    # return kurang
    if totalbox == 0  :
        total = 0
    else :
        total = 100*(float(kurang)/float(totalbox))
    return  "{:.2f}".format(total)

@register.filter(name="lkpicasso_box")
def lkpicasso_box(tanggal):
    std = Standard.objects.get(pk=1)
    total =int(grandtotalpicasso(tanggal)) - int (std.sp_box)
    return total

@register.filter(name = "lkpicasso_persen")
def lkpicasso_persen(tanggal):
    data =grandtotalbox(tanggal)
    kurang = lkpicasso_box(tanggal)
    if data == 0 :
        total = 0
    else :
        total = 100*(float(kurang)/float(data))
    return "{:.2f}".format(total)

@register.filter(name="lkharmony_box")
def lkharmony_box(tanggal):
    std = Standard.objects.get(pk=1)
    total =int(grandtotalharmony(tanggal)) - int (std.sh_box)
    return total

@register.filter(name = "lkharmony_persen")
def lkharmony_persen(tanggal):
    # return 1
    data =grandtotalbox(tanggal)
    kurang = lkharmony_box(tanggal)
    if data == 0:
        total = 0
    else :
        total = 100*(float(kurang)/float(grandtotalbox(tanggal)))
    return "{:.2f}".format(total)


@register.filter(name="lkatena_box")
def lkatena_box(tanggal):
    std = Standard.objects.get(pk=1)
    total =int(grandtotalatena(tanggal)) - int (std.sa_box)
    return total

@register.filter(name = "lkatena_persen")
def lkatena_persen(tanggal):
    # return 1
    data =grandtotalbox(tanggal)
    kurang = lkatena_box(tanggal)
    if data ==0:
        total = 0
    else :
        total = 100*(float(kurang)/float(data))
    return "{:.2f}".format(total)


@register.filter(name="lkpicharmony_box")
def lkpicharmony_box(tanggal):
    std = Standard.objects.get(pk=1)
    total =int(grandtotalboxpicharmony(tanggal)) - int (std.s_boxph)
    return total

@register.filter(name="lkpicharmony_persen")
def lkpicharmony_persen(tanggal):
    kurang = lkpicharmony_box(tanggal)
    data =grandtotalbox(tanggal)
    if data ==0:
        total =0
    else :
        total = 100*(float(kurang)/float(data))
    return "{:.2f}".format(total)

@register.filter(name="totalbox_lk")
def totalbox_lk(tanggal):
    picasso = lkpicasso_box(tanggal)
    harmony = lkharmony_box(tanggal)
    atena =lkatena_box(tanggal)
    kita =kurang_k(tanggal)
    total = int(picasso)+int(harmony)+int(atena)+int(kita)
    return total

@register.filter(name="totalpersen_lk")
def totalpersen_lk(tanggal):
    std = Standard.objects.get(pk=1)
    tbox = totalbox_lk(tanggal)
    total =float(tbox) / float(std.s_totalbox)
    return "{:.2f}".format(total)


@register.filter(name="tpersen_kita")
def tpersen_kita(tanggal):
    kita = grandtotalkita(tanggal)
    box= grandtotalbox(tanggal)
    if kita ==0 | box ==0 :
        total =0
    else :
        total = 100 *(float(kita) / float(box))
    return "{:.2f}".format(total)

@register.filter(name="tpersen_picasso")
def tpersen_picasso(tanggal):
    picasso = grandtotalpicasso(tanggal)
    box= grandtotalbox(tanggal)
    if picasso == 0 | box ==0 :
        total = 0
    else :
        total = 100 *(float(picasso) / float(box))
    return "{:.2f}".format(total)

@register.filter(name="tpersen_harmony")
def tpersen_harmony(tanggal):
    harmony = grandtotalharmony(tanggal)
    box= grandtotalbox(tanggal)
    if harmony ==0 | box ==0 :
        total = 0
    else :
        total = 100 *(float(harmony) / float(box))
    return "{:.2f}".format(total)

@register.filter(name="tpersen_atena")
def tpersen_atena(tanggal):
    atena = grandtotalatena(tanggal)
    box= grandtotalbox(tanggal)
    if atena == 0 | box ==0 :
        total = 0
    else :
        total = 100 *(float(atena) / float(box))
    return "{:.2f}".format(total)

@register.filter(name="tpersen_pichar")
def tpersen_pichar(tanggal):
    tile = grandtotalboxpicharmony(tanggal)
    box= grandtotalbox(tanggal)
    if tile == 0 | box ==0 :
        total = 0
    else :
        total = 100 *(float(tile) / float(box))
    return "{:.2f}".format(total)

@register.filter(name="selisih_kita")
def selisih_kita(tanggal):
    # return 1
    total = float(tpersen_kita(tanggal))-float(35.00)
    return "{:.2f}".format(total)

@register.filter(name="selisih_pichar")
def selisih_pichar(tanggal):
    # return 1
    total = float(tpersen_pichar(tanggal))-float(50.00)
    return "{:.2f}".format(total)

@register.filter(name="selisih_atena")
def selisih_atena(tanggal):
    # return 1
    total = float(tpersen_atena(tanggal))-float(15.00)
    return "{:.2f}".format(total)

@register.filter(name="pabrik_kita")
def pabrik_kita(tanggal):
    try :
        data = StokPabrik.objects.get(tanggal = tanggal,barang= 'KITA')
        return int(data.stok)
    except ObjectDoesNotExist:
        return 0

@register.filter(name="pabrik_picasso")
def pabrik_picasso(tanggal):
    try :
        data = StokPabrik.objects.get(tanggal=tanggal, barang='PICASSO')
        return int(data.stok)
    except ObjectDoesNotExist:
        return 0
@register.filter(name="pabrik_harmony")
def pabrik_harmony(tanggal):
    try :
        data = StokPabrik.objects.get(tanggal=tanggal, barang='HARMONY')
        return int(data.stok)
    except ObjectDoesNotExist:
        return 0

@register.filter(name="pabrik_atena")
def pabrik_atena(tanggal):
    try :
        data = StokPabrik.objects.get(tanggal=tanggal, barang='ATENA')
        return int(data.stok)
    except ObjectDoesNotExist:
        return 0

@register.filter(name="pabrik_masimo")
def pabrik_masimo(tanggal):
    try :
        data = StokPabrik.objects.get(tanggal=tanggal, barang='MASIMO')
        return int(data.stok)
    except ObjectDoesNotExist:
        return 0

@register.filter(name = "totalpabrik")
def totalpabrik(tanggal):
    kita = pabrik_kita(tanggal)
    picasso = pabrik_picasso(tanggal)
    harmony = pabrik_harmony(tanggal)
    atena = pabrik_atena(tanggal)
    masimo =pabrik_masimo(tanggal)
    total = kita + picasso + harmony + atena + masimo
    return total

@register.filter(name = "persenpabrik_kita")
def persenpabrik_kita(tanggal):
    # return 1
    try :
        totalstok = totalpabrik(tanggal)
        # return totalstok
        stok = pabrik_kita(tanggal)
        # return stok
        if totalstok == 0 | stok == 0 :
            total = 0
        else :
            total = 100*(float (stok) / float (totalstok))
        return  "{:.2f}".format(total)
    except ObjectDoesNotExist:
        return 0
@register.filter(name="persenpabrik_picasso")
def persenpabrik_picasso(tanggal):
    try :
        # return 1
        totalstok = totalpabrik(tanggal)
        stok = pabrik_picasso(tanggal)
        if totalstok == 0 | stok == 0 :
            total = 0
        else :
            total = 100*(float (stok) / float (totalstok))
        return  "{:.2f}".format(total)
    except ObjectDoesNotExist:
        return 0

@register.filter(name="persenpabrik_harmony")
def persenpabrik_harmony(tanggal):
    # return 1
    try :
        totalstok = totalpabrik(tanggal)
        stok = pabrik_harmony(tanggal)
        if totalstok == 0 | stok == 0:
           total = 0
        else :
           total = 100 * (float(stok) / float(totalstok))
        return "{:.2f}".format(total)
    except ObjectDoesNotExist:
        return 0

@register.filter(name="persenpabrik_atena")
def persenpabrik_atena(tanggal):
    try :
        totalstok = totalpabrik(tanggal)
        stok = pabrik_atena(tanggal)
        if totalstok ==0 | stok ==0 :
            total = 0
        else :
            total = 100 * (float(stok) / float(totalstok))
        return "{:.2f}".format(total)
    except ObjectDoesNotExist:
        return 0

@register.filter(name="persenpabrik_masimo")
def persenpabrik_masimo(tanggal):
    # return 1
    try :
        totalstok = totalpabrik(tanggal)
        stok = pabrik_masimo(tanggal)
        if totalstok == 0 | stok == 0:
            total = 0
        else :
            total = 100 * (float(stok) / float(totalstok))
        return "{:.2f}".format(total)
    except ObjectDoesNotExist:
        return 0

@register.filter(name = "persenpabrik_total")
def persenpabrik_total(tanggal):
    kita = persenpabrik_kita(tanggal)
    picasso = persenpabrik_picasso(tanggal)
    harmony = persenpabrik_harmony(tanggal)
    atena = persenpabrik_atena(tanggal)
    masimo = persenpabrik_masimo(tanggal)
    total = float (kita) + float (picasso) + float (harmony) + float (atena) + float (masimo)
    return "{:.2f}".format(total)

@register.filter(name="kita_depo")
def kita_depo(tanggal):
    data = Stok.objects.filter(tanggal = tanggal)
    stoknya = 0
    for data in data :
        stoknya += int(data.kita)
    return stoknya

@register.filter(name="picasso_depo")
def picasso_depo(tanggal):
        data = Stok.objects.filter(tanggal=tanggal)
        stoknya = 0
        for data in data:
            stoknya += int(data.picasso)
        return stoknya

@register.filter(name="harmony_depo")
def harmony_depo(tanggal):
    data = Stok.objects.filter(tanggal=tanggal)
    stoknya = 0
    for data in data:
        stoknya += int(data.harmony)
    return stoknya

@register.filter(name="atena_depo")
def atena_depo(tanggal):
    data = Stok.objects.filter(tanggal=tanggal)
    stoknya = 0
    for data in data:
        stoknya += int(data.atena)
    return stoknya

@register.filter(name="grandtotaldepo")
def grandtotaldepo(tanggal):
    kita = kita_depo(tanggal)
    picasso = picasso_depo(tanggal)
    harmony = harmony_depo(tanggal)
    atena = atena_depo(tanggal)
    total = kita + picasso + harmony +atena
    return total

@register.filter(name = "persen_kitadepo")
def persen_kitadepo(tanggal):
    tot = grandtotaldepo(tanggal)
    kita = kita_depo(tanggal)
    total = 0
    if kita == 0 :
        total = 0
    else :
        total = 100 * (float(kita)/float(tot))
    return "{:.2f}".format(total)

@register.filter(name="persen_picassodepo")
def persen_picassodepo(tanggal):
    tot = grandtotaldepo(tanggal)
    data = picasso_depo(tanggal)
    total = 0
    if data == 0:
       total = 0
    else:
       total = 100 * (float(data) / float(tot))
    return "{:.2f}".format(total)

@register.filter(name="persen_harmonydepo")
def persen_harmonydepo(tanggal):
    tot = grandtotaldepo(tanggal)
    data = harmony_depo(tanggal)
    total = 0
    if data == 0:
       total = 0
    else:
       total = 100 * (float(data) / float(tot))
    return "{:.2f}".format(total)

@register.filter(name="persen_atenadepo")
def persen_atenadepo(tanggal):
    tot = grandtotaldepo(tanggal)
    data = atena_depo(tanggal)
    total = 0
    if data == 0:
       total = 0
    else:
       total = 100 * (float(data) / float(tot))
    return "{:.2f}".format(total)

@register.filter(name="grandtotalpersen_depo")
def grandtotalpersen_depo(tanggal):
    # return 1
    kita = persen_kitadepo(tanggal)
    picasso = persen_picassodepo(tanggal)
    harmony = persen_harmonydepo(tanggal)
    atena = persen_atenadepo(tanggal)
    total = float(kita)+float(picasso)+float(harmony)+float(atena)
    return "{:.2f}".format(total)

@register.filter(name="totalkita_depo")
def totalkita_depo(tanggal):
    pkita = pabrik_kita(tanggal)
    dkita = kita_depo(tanggal)
    total =pkita + dkita
    return total

@register.filter(name="totalpicasso_depo")
def totalpicasso_depo(tanggal):
    pabrik = pabrik_picasso(tanggal)
    depo = picasso_depo(tanggal)
    total =pabrik + depo
    return total

@register.filter(name="totalharmony_depo")
def totalharmony_depo(tanggal):
    pabrik = pabrik_harmony(tanggal)
    depo = harmony_depo(tanggal)
    total =pabrik + depo
    return total

@register.filter(name="totalatena_depo")
def totalatena_depo(tanggal):
    pabrik = pabrik_atena(tanggal)
    depo = atena_depo(tanggal)
    total =pabrik + depo
    return total

@register.filter(name="grandtotal_depo")
def grandtotal_depo(tanggal):
    kita = totalkita_depo(tanggal)
    picasso = totalpicasso_depo(tanggal)
    harmony = totalharmony_depo(tanggal)
    atena = totalatena_depo(tanggal)
    masimo = pabrik_masimo(tanggal)
    total = kita + picasso + harmony + atena + masimo
    return total

@register.filter(name="totalpersen_kita")
def totalpersen_kita(tanggal):
    # return 1
    try :
        grandtotal = grandtotal_depo(tanggal)
        kita =totalkita_depo(tanggal)
        if grandtotal == 0 | kita == 0 :
            total = 0
        else :
             total = 100*(float(kita)/float(grandtotal))
        return "{:.2f}".format(total)
    except ObjectDoesNotExist:
        return 0

@register.filter(name="totalpersen_picasso")
def totalpersen_picasso(tanggal):
    try :
        # return 1
        grandtotal = grandtotal_depo(tanggal)
        data =totalpicasso_depo(tanggal)
        if grandtotal == 0 | data == 0 :
            total = 0
        else :
            total = 100*(float(data)/float(grandtotal))
        return "{:.2f}".format(total)
    except ObjectDoesNotExist:
        return 0

@register.filter(name="totalpersen_harmony")
def totalpersen_harmony(tanggal):
    # return 1
    try :
        grandtotal = grandtotal_depo(tanggal)
        data =totalharmony_depo(tanggal)
        if grandtotal == 0 | data ==0 :
            total = 0
        else :
            total = 100*(float(data)/float(grandtotal))
        return "{:.2f}".format(total)
    except ObjectDoesNotExist:
        return 0

@register.filter(name="totalpersen_atena")
def totalpersen_atena(tanggal):
    # return 1
    try :
        grandtotal = grandtotal_depo(tanggal)
        data =totalatena_depo(tanggal)
        if grandtotal ==0 | data ==0:
            total = 0
        else :
            total = 100*(float(data)/float(grandtotal))
        return "{:.2f}".format(total)
    except ObjectDoesNotExist:
        return 0

@register.filter(name="totalpersen_masimo")
def totalpersen_masimo(tanggal):
    try :
        grandtotal = grandtotal_depo(tanggal)
        data = pabrik_masimo(tanggal)
        if grandtotal == 0 | data == 0:
            total = 0
        else :
            total = 100*(float(data)/float(grandtotal))
        return "{:.2f}".format(total)
    except ObjectDoesNotExist:
        return 0

@register.filter(name="grandtotal_persen")
def grandtotal_persen(tanggal):
    kita = totalpersen_kita(tanggal)
    picasso = totalpersen_picasso(tanggal)
    harmony = totalpersen_harmony(tanggal)
    atena = totalpersen_atena(tanggal)
    masimo = totalpersen_masimo(tanggal)
    total = float (kita)+float(picasso)+float(harmony)+float(atena)+float(masimo)
    return  "{:.2f}".format(total)


@register.filter(name= "tanggal")
def tanggal(tanggal):
    datetime_object = datetime.strptime(tanggal,  '%Y-%d-%m')
    return datetime_object























#
#
# @register.filter(name="t_phbox")
# def s_kbox(p,h):
#     return  int(p) + int(h)
#
# @register.filter(name="t_phpersen")
# def s_kbox(p,h):
#     return  float(p) + float(h)
#
#
#
# @register.filter(name="s_kbox")
# def s_kbox(total,standard):
#     return  int(total) - int(standard)
#
# @register.filter(name="s_kpersen")
# def s_kpersen(total,standard):
#     return  float(total) - float(standard)
#
# @register.filter(name="varian_total")
# def varian_total(total,standard):
#     return  int(total) - int(standard)
#
# @register.filter(name="boxdepo_kita")
# def boxdepo_kita(tanggal,depo):
#     stok = Stok.objects.filter(tanggal = tanggal, depo = depo)
#     total = 0
#     for data in stok :
#        total += int(data.k_box)
#     return  total
#
# @register.filter(name="persendepo_kita")
# def persendepo_kita(tanggal,depo):
#     stok = Stok.objects.filter(tanggal = tanggal, depo = depo)
#     total = 0
#     for data in stok :
#        total += float(data.k_persen)
#     return  total
#
# @register.filter(name="boxdepo_atena")
# def boxdepo_atena(tanggal,depo):
#     stok = Stok.objects.filter(tanggal = tanggal, depo = depo)
#     total = 0
#     for data in stok :
#        total += int(data.a_box)
#     return  total
#
# @register.filter(name="persendepo_atena")
# def persendepo_atena(tanggal,depo):
#     stok = Stok.objects.filter(tanggal = tanggal, depo = depo)
#     total = 0
#     for data in stok :
#        total += float(data.a_persen)
#     return  total
#
# @register.filter(name="boxdepo_harmony")
# def boxdepo_harmony(tanggal,depo):
#     stok = Stok.objects.filter(tanggal = tanggal, depo = depo)
#     total = 0
#     for data in stok :
#        total += int(data.h_box)
#     return  total
#
# @register.filter(name="total_boxdepo") # fsdfds
# def total_boxdepo(tanggal,depo):
#     picasso = boxdepo_picasso(tanggal,depo)
#     atena = boxdepo_atena(tanggal,depo)
#     harmony = boxdepo_harmony(tanggal,depo)
#     kita = boxdepo_kita(tanggal,depo)
#
#     totals = float(picasso) + float(atena) + float(harmony) + float(kita)
#     return  totals
#
# @register.filter(name="total_persendepo") # fsdfds
# def total_persendepo(tanggal,depo):
#     picasso = persendepo_picasso(tanggal,depo)
#     atena = persendepo_atena(tanggal,depo)
#     harmony = persendepo_harmony(tanggal,depo)
#     kita = persendepo_kita(tanggal,depo)
#     totals = float(picasso) + float(atena) + float(harmony) + float(kita)
#     return  totals
#
# @register.filter(name="total_picasso")
# def total_picasso(tanggal,depo):
#     pabrik=stok_pabrik_picasso(tanggal)
#     depo = boxdepo_picasso(tanggal,depo)
#     total = float(pabrik) + float(depo)
#     return int(total)
#
# @register.filter(name="total_kita")
# def total_kita(tanggal,depo):
#     pabrik=stok_pabrik_kita(tanggal)
#     depo = boxdepo_kita(tanggal,depo)
#     total = float(pabrik) + float(depo)
#     return int(total)
#
# @register.filter(name="total_atena")
# def total_atena(tanggal,depo):
#     pabrik=stok_pabrik_atena(tanggal)
#     depo = boxdepo_atena(tanggal,depo)
#     total = float(pabrik) + float(depo)
#     return int(total)
#
# @register.filter(name="total_harmony")
# def total_harmony(tanggal,depo):
#     pabrik=stok_pabrik_harmoni(tanggal)
#     depo = boxdepo_harmony(tanggal,depo)
#     total = float(pabrik) + float(depo)
#     return int(total)
#
#
# @register.filter(name="total_all_depoparbrik")
# def total_all_depoparbrik(tanggal,depo):
#     picasso = total_picasso(tanggal,depo)
#     atena = total_atena(tanggal, depo)
#     kita = total_kita(tanggal, depo)
#     harmony = total_harmony(tanggal, depo)
#     masimo = stok_pabrik_masimo(tanggal)
#     total = float(picasso) + float(atena) + float(kita) + float(harmony) +float(masimo)
#     return int(total)
#
# @register.filter(name="total_persenkita")
# def total_persenkita(tanggal,depo):
#     all = total_all_depoparbrik(tanggal,depo)
#     kita =total_kita(tanggal,depo)
#     total = (float(kita) / float (all))*100
#     return "{:.2f}".format(total)
#
# @register.filter(name="total_persenharmony")
# def total_persenharmony(tanggal,depo):
#     all = total_all_depoparbrik(tanggal,depo)
#     kita =total_harmony(tanggal,depo)
#     total = 100*(float(kita) / float (all))
#     return "{:.2f}".format(total)
#
# @register.filter(name="total_persenatena")
# def total_persenatena(tanggal,depo):
#     all = total_all_depoparbrik(tanggal,depo)
#     kita =total_atena(tanggal,depo)
#     total = 100*(float(kita) / float (all))
#     return "{:.2f}".format(total)
#
# @register.filter(name="total_persenmasimo")
# def total_persenmasimo(tanggal,depo):
#     all = total_all_depoparbrik(tanggal,depo)
#     masimo =stok_pabrik_masimo(tanggal)
#     total = 100*(float(masimo) / float (all))
#     return "{:.2f}".format(total)
#
# @register.filter(name="total_persenall")
# def total_persenall(tanggal,depo):
#     kita = total_persenkita(tanggal, depo)
#     harmony = total_persenharmony(tanggal, depo)
#     picasso = total_persenpicasso(tanggal, depo)
#     atena = total_persenatena(tanggal,depo)
#     masimo = total_persenmasimo(tanggal,depo)
#     total = float(picasso) + float(atena) + float(kita) + float(harmony) + float(masimo)
#     return "{:.2f}".format(total)
#
# @register.filter(name="total_persenpicasso")
# def total_persenpicasso(tanggal,depo):
#     all = total_all_depoparbrik(tanggal,depo)
#     picasso =total_picasso(tanggal,depo)
#     total = 100*(float(picasso) / float (all))
#     return "{:.2f}".format(total)
#
#
#
# @register.filter(name="persendepo_harmony")
# def persendepo_harmony(tanggal,depo):
#     stok = Stok.objects.filter(tanggal = tanggal, depo = depo)
#     total = 0
#     for data in stok :
#        total += float(data.h_persen)
#     return  total
#
# @register.filter(name="boxdepo_picasso")
# def boxdepo_picasso(tanggal,depo):
#     stok = Stok.objects.filter(tanggal = tanggal, depo = depo)
#     total = 0
#     for data in stok :
#        total += int(data.p_box)
#     return  total
#
# @register.filter(name="persendepo_picasso")
# def persendepo_picasso(tanggal,depo):
#     stok = Stok.objects.filter(tanggal = tanggal, depo = depo)
#     total = 0
#     for data in stok :
#        total += float(data.p_persen)
#     return  total
#
# @register.filter(name="stok_pabrik_kita")
# def stok_pabrik_kita(tanggal):
#     data = StokPabrik.objects.get(tanggal='2017-12-31',barang = 'KITA')
#     return data.stok
#
# @register.filter(name="stok_pabrik_picasso")
# def stok_pabrik_picasso(tanggal):
#     data = StokPabrik.objects.get(tanggal='2017-12-31',barang = 'PICASSO')
#     return data.stok
#
# @register.filter(name="stok_pabrik_harmoni")
# def stok_pabrik_harmoni(tanggal):
#     data = StokPabrik.objects.get(tanggal='2017-12-31',barang = 'HARMONI')
#     return data.stok
#
# @register.filter(name="stok_pabrik_atena")
# def stok_pabrik_atena(tanggal):
#     data = StokPabrik.objects.get(tanggal='2017-12-31',barang = 'ATENA')
#     return data.stok
#
# @register.filter(name="stok_pabrik_masimo")
# def stok_pabrik_masimo(tanggal):
#     data = StokPabrik.objects.get(tanggal='2017-12-31',barang = 'MASIMO')
#     return data.stok
#
# @register.filter(name="sue")
# def getvalue(a,b,c):
#     return b
# @register.filter(name="tes")
# def tes(x):
#     return 0
#
#
# @register.filter(name="totalStok_depo")
# def getTotal_stokpabrik(tanggal):
#     data = StokPabrik.objects.all()
#     stok = 0
#     for item in data :
#         stok += item.stok
#     return stok
#
# @register.filter(name="persenStok_depokita")
# def getPersen_stokpabrikKita(tanggal):
#     stok = getTotal_stokpabrik(tanggal)
#     kita = stok_pabrik_kita(tanggal)
#     total = 100*(float(kita) / float(stok))
#     return "{:.2f}".format(total)
#
# @register.filter(name="persenStok_depoatena")
# def getPersen_stokpabrikAtena(tanggal):
#     stok = getTotal_stokpabrik(tanggal)
#     atena = stok_pabrik_atena(tanggal)
#     total = 100*(float(atena) / float(stok))
#     return "{:.2f}".format(total)
#
# @register.filter(name="persenStok_depoharmony")
# def getPersen_stokpabrikHarmony(tanggal):
#     stok = getTotal_stokpabrik(tanggal)
#     harmony = stok_pabrik_harmoni(tanggal)
#     total = 100*(float(harmony) / float(stok))
#     return "{:.2f}".format(total)
#
# @register.filter(name="persenStok_depopicasso")
# def getPersen_stokpabrikPicasso(tanggal):
#     stok = getTotal_stokpabrik(tanggal)
#     picasso = stok_pabrik_picasso(tanggal)
#     total = 100*(float(picasso) / float(stok))
#     return "{:.2f}".format(total)
#
# @register.filter(name="persenStok_depomasimo")
# def getPersen_stokpabrikMasimo(tanggal):
#     stok = getTotal_stokpabrik(tanggal)
#     masimo = stok_pabrik_masimo(tanggal)
#     total = 100*(float(masimo) / float(stok))
#     return "{:.2f}".format(total)
#
# @register.filter(name="total_persen")
# def gettotal_Persen(tanggal):
#     picasso = getPersen_stokpabrikPicasso(tanggal)
#     atena = getPersen_stokpabrikAtena(tanggal)
#     harmony = getPersen_stokpabrikHarmony(tanggal)
#     kita = getPersen_stokpabrikKita(tanggal)
#     masimo = getPersen_stokpabrikMasimo(tanggal)
#     total = float(picasso) + float(atena) + float(harmony) + float(kita) + float(masimo)
#
#     return "{:.2f}".format(total)


@register.filter(name='range')
def _range(_min, args=None):
    _max, _step = None, None
    if args:
        if not isinstance(args, int):
            _max, _step = map(int, args.split(','))
        else:
            _max = args
    args = filter(None, (_min, _max, _step))
    return range(*args)


@register.filter(name="encode_id")
def encoded_id(value):
        from Crypto.Cipher import AES
        import base64
        MASTER_KEY = "Some-long-base-key-to-use-as-encyrption-key"
        enc_secret = AES.new(MASTER_KEY[:32])
        tag_string = (str(value) +
                      (AES.block_size -
                       len(str(value)) % AES.block_size) * "\0")
        cipher_text = base64.b64encode(enc_secret.encrypt(tag_string))
        return cipher_text


