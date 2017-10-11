from __future__ import unicode_literals
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Stok,Standard,StokPabrik
from stok .forms import StokForm
from django.db.models import Sum
from useremployee .models import UserEmployee
import datetime
import pyodbc
from functions .functions import decript
from django.shortcuts import render_to_response
from django.template import RequestContext


def handler404(request):
    response = render_to_response('404.html', {},
                              context_instance=RequestContext(request))
    response.status_code = 404
    return response
# def index(request):
#     data = Stok.objects.values('size__namaUkuran').annotate(k_box=Sum('k_box'),k_persen=Sum('k_persen'),p_box=Sum('p_box'),p_persen=Sum('p_persen'),h_box=Sum('h_box'),h_persen=Sum('h_persen'),a_box=Sum('a_box'),a_persen=Sum('a_persen'))
    # return render(request,"stok/index.html",{"data":data})
@login_required
def index(request):
     if request.POST:
         depo = request.POST['depo']
         # return HttpResponse(depo)
         bulan = request.POST['bulan']
         tahun = request.POST['tahun']
         frm = StokForm()
         data = Stok.objects.values('size__namaUkuran').annotate(k_box=Sum('k_box'), k_persen=Sum('k_persen'),
                                                                 p_box=Sum('p_box'), p_persen=Sum('p_persen'),
                                                                 h_box=Sum('h_box'), h_persen=Sum('h_persen'),
                                                                 a_box=Sum('a_box'), a_persen=Sum('a_persen'),
                                                                 sudm_bosx=Sum('k_box') + Sum('p_box') + Sum(
                                                                     'a_box') + Sum('h_box'),
                                                                 sudm_peewrcn=Sum('a_persen') + Sum(
                                                                     'h_persen') + Sum('k_persen') + Sum(
                                                                     'p_persen')).filter(tanggal__month=bulan,
                                                                                         depo_id=depo)
         std = Standard.objects.get(pk=1)
         cdata = Stok.objects.filter(tanggal__month=bulan, tanggal__year=tahun, depo_id=depo)
         disc = Stok.objects.values('tanggal', 'depo_id').distinct().filter(tanggal__month=bulan, tanggal__year=tahun,
                                                                            depo_id=depo)

         totalbox_k = 0
         totalbox_p = 0
         totalbox_h = 0
         totalbox_a = 0
         totalpersen_k = 0
         totalpersen_p = 0
         totalpersen_h = 0
         totalpersen_a = 0
         ph_box = 0
         ph_persen = 0
         totalbox = 0
         totalpersen = 0
         for item in cdata:
             totalbox_k += int(item.k_box)
             totalbox_p += int(item.p_box)
             totalbox_h += int(item.h_box)
             totalbox_a += int(item.a_box)
             totalpersen_k += float(item.k_persen)
             totalpersen_p += float(item.p_persen)
             totalpersen_h += float(item.h_persen)
             totalpersen_a += float(item.a_persen)
             ph_box += int(item.p_box) + int(item.h_box)
             ph_persen += float(item.p_persen) + float(item.h_persen)
             totalbox += int(item.k_box) + int(item.p_box) + int(item.h_box) + int(item.a_box)
             totalpersen += float(item.k_persen) + float(item.p_persen) + float(item.h_persen) + float(item.a_persen)

         komposisi_k = float(totalpersen_k - 35)
         komposisi_pht = float(ph_persen - 50)
         komposisi_a = float(totalpersen_a - 15)
         # return HttpResponse("o")

         lkbox_total = int(totalbox) - int(std.s_totalbox)
         lkpersen_total2 = float(lkbox_total) / float(std.s_totalbox)
         lkpersen_total = "{:.2f}".format(lkpersen_total2)

         # return HttpResponse(std.s_totalbox)
         lkbox_kita = int(totalbox_k) - int(std.sk_box)
         lkpersen_kita2 = float(lkbox_kita) / float(lkbox_total) * 100
         lkpersen_kita = "{:.2f}".format(lkpersen_kita2)

         lkbox_atena = int(totalbox_a) - int(std.sa_box)
         lkpersen_atena2 = float(lkbox_atena) / float(std.s_totalbox)
         lkpersen_atena = "{:.2f}".format(lkpersen_atena2)

         lkbox_picasso = int(totalbox_p) - int(std.sp_box)
         lkpersen_picasso2 = float(lkbox_picasso) / float(lkbox_total) * 100
         lkpersen_picasso = "{:.2f}".format(lkpersen_picasso2)

         lkbox_harmony = int(totalbox_h) - int(std.sh_box)
         lkpersen_harmony2 = float(lkbox_harmony) / lkbox_total * 100
         lkpersen_harmony = "{:.2f}".format(lkpersen_harmony2)

         lkph_box = lkbox_picasso + lkbox_harmony
         lkph_persen2 = float(lkpersen_picasso2) + float(lkpersen_harmony2)
         lkph_persen = "{:.2f}".format(lkph_persen2)

         return render(request, "stok/index.html",
                       {"data": data, "std": std, "totalbox_k": totalbox_k, "totalbox_p": totalbox_p,
                        "totalbox_h": totalbox_h, "totalbox_a": totalbox_a, "totalpersen_a": totalpersen_a,
                        "totalpersen_p": totalpersen_p, "totalpersen_h": totalpersen_h,
                        "totalpersen_k": totalpersen_k, "ph_box": ph_box, "ph_persen": ph_persen,
                        "totalbox": totalbox, "totalpersen": totalpersen, "disc": disc, "lkbox_total": lkbox_total,
                        "lkbox_kita": lkbox_kita, "lkpersen_total": lkpersen_total, "lkbox_atena": lkbox_atena,
                        "lkpersen_atena": lkpersen_atena, "lkbox_picasso": lkbox_picasso,
                        "lkpersen_picasso": lkpersen_picasso, "lkpersen_kita": lkpersen_kita,
                        "lkbox_harmony": lkbox_harmony, "lkpersen_harmony": lkpersen_harmony, "lkph_box": lkph_box,
                        "lkph_persen": lkph_persen, "komposisi_k": komposisi_k, "komposisi_pht": komposisi_pht,
                        "komposisi_a": komposisi_a, "loop_year": range(1, 8),
                        # "tpicasso":tpicasso,"tkita":tkita,"tatena":tatena,"tharmoni":tharmoni
                        })

     #return render(request,"stok/index.html",{"data":data,"std":std,"totalbox_k":totalbox_k,"totalbox_p":totalbox_p,"totalbox_h":totalbox_h,"totalbox_a":totalbox_a,"totalpersen_a":totalpersen_a,"totalpersen_p":totalpersen_p,"totalpersen_h":totalpersen_h,"totalpersen_k":totalpersen_k,"ph_box":ph_box,"ph_persen":ph_persen,"totalbox":totalbox,"totalpersen":totalpersen,"disc":disc,"lkbox_total":lkbox_total,"lkbox_kita":lkbox_kita,"lkpersen_total":lkpersen_total,"lkbox_atena":lkbox_atena,"lkpersen_atena":lkpersen_atena,"lkbox_picasso":lkbox_picasso,"lkpersen_picasso":lkpersen_picasso,"lkpersen_kita":lkpersen_kita,"lkbox_harmony":lkbox_harmony,"lkpersen_harmony":lkpersen_harmony,"lkph_box":lkph_box,"lkph_persen":lkph_persen,"komposisi_k":komposisi_k,"komposisi_pht":komposisi_pht,"komposisi_a":komposisi_a,"loop_year":range(1,8)})
     else :
        return render(request, "stok/index.html")
@login_required
def save(request):
   try:
       # return HttpResponse("dda")
       # con = pyodbc.connect("DRIVER={FreeTds};server=192.168.10.2;database=Stok-Depo;uid=sa;pwd=5u1k0d3n2")
       # picasso = con.cursor()
       # picasso.execute("select sum(stok) as total from stok where left(kode_barang,4)= 'FG.P' ")
       # picasso_row = str(picasso.fetchone()).strip()
       # picasso_row1 = picasso_row.replace("(", " ")
       # picasso_row2 = picasso_row1.replace(",", " ")
       # tpicasso = picasso_row2.replace(")", " ")
       #
       # atena = con.cursor()
       # atena.execute("select sum(stok) as total from stok where LEFT(kode_barang,4) ='FG.G' ")
       # atena_row = str(atena.fetchone()).strip()
       # atena_row1 = atena_row.replace("(", " ")
       # atena_row2 = atena_row1.replace(",", " ")
       # tatena = atena_row2.replace(")", " ")
       #
       # harmoni = con.cursor()
       # harmoni.execute("select sum(stok) as total from stok where LEFT(kode_barang,4) ='FG.H' ")
       # harmoni_row = str(harmoni.fetchone()).strip()
       # harmoni_row1 = harmoni_row.replace("(", " ")
       # harmoni_row2 = harmoni_row1.replace(",", " ")
       # tharmoni = harmoni_row2.replace(")", " ")
       #
       # kita = con.cursor()
       # kita.execute("select sum(stok) as total from stok where LEFT(kode_barang,4) ='FG.K' ")
       # kita_row = str(kita.fetchone()).strip()
       # kita_row1 = kita_row.replace("(", " ")
       # kita_row2 = kita_row1.replace(",", " ")
       # tkita = kita_row2.replace(")", " ")
       #
       # masimo = con.cursor()
       # masimo.execute("select sum(stok) as total from stok where LEFT(kode_barang,4) ='FG.O' ")
       # masimo_row = str(masimo.fetchone()).strip()
       # masimo_row1 = masimo_row.replace("(", " ")
       # masimo_row2 = masimo_row1.replace(",", " ")
       # tmasimo =masimo_row2.replace(")", " ")
       jumlah = int(request.POST['jumlah']) + 1

       bln = request.POST['month']
       bul = int(bln)
       bulan = 0
       if (bul < 10):
           bulan = "0"+bln
       else :
           bulan = bln
       periode = request.POST['periode']
       tgl = 0
       if periode == "1" :
           tgl = "5"
       else :
           tgl = "19"
       now = datetime.datetime.now()
       year =str(now.year)
       # return HttpResponse(year+"-"+bulan+"-"+tgl)
       tanggal = year+"-"+bulan+"-"+tgl
       user = request.POST['user']
       quedepo = UserEmployee.objects.get(karyawan=user)
       depo = quedepo.karyawan.depo_id
       disc = Stok.objects.values('tanggal').distinct().filter(tanggal__month=bulan, tanggal__year=year, depo_id=depo).count()
       cekdata = Stok.objects.filter(tanggal = tanggal,depo_id=depo)
       if cekdata.exists():
           return HttpResponse('Maaf Data sudah ada !!')
       else :
               if disc >1 :
                  return HttpResponse("Maaf satu bulan maskimal 2 kali penginputan")
               else :
                   # stokpabrik = StokPabrik(tanggal=tanggal, barang='KITA', stok=tkita)
                   # stokpabrik.save()
                   # stokpabrik = StokPabrik(tanggal=tanggal, barang='PICASSO', stok=tpicasso)
                   # stokpabrik.save()
                   # stokpabrik = StokPabrik(tanggal=tanggal, barang='ATENA', stok=tatena)
                   # stokpabrik.save()
                   # stokpabrik = StokPabrik(tanggal=tanggal, barang='HARMONI', stok=tharmoni)
                   # stokpabrik.save()
                   # stokpabrik = StokPabrik(tanggal=tanggal, barang='MASIMO', stok=tmasimo)
                   # stokpabrik.save()
                   for i in range(1,jumlah):
                     size = request.POST["size"+str(i)]
                     spicasso = request.POST["picasso" + str(i)]
                     skita=request.POST['kita'+str(i)]
                     satena = request.POST["atena" + str(i)]
                     sharmony=request.POST['harmony'+str(i)]
                     stok = Stok(tanggal=tanggal,size_id=size,user_id=user,kita=skita,picasso=spicasso,atena=satena,harmony=sharmony,depo_id = depo)
                     stok.save()
                   return HttpResponse("ok")

   except pyodbc.Error as ex:
      return HttpResponse("cant connect database <a href '{% url 'stok'%}'>Back<a> ")


def tes(request):
    # City.objects.values('country__name') \
    #     .annotate(country_population=Sum('population')) \
    #     .order_by('-country_population')
    stok = Stok.objects.values('size__namaUkuran').annotate(k_box = Sum('k_box'))
    return render(request,"tes.html",{"data":stok})

@login_required
def printstok(request):
    data = Stok.objects.values('size__namaUkuran','size__stok__user').distinct()
    return render(request,"stok/print.html",{"data":data})

@login_required
def data(request):
   depo = request.user.useremployee.karyawan.depo.id
   data = Stok.objects.filter(depo_id=depo)
   return render(request,"stok/data.html",{"data":data})

@login_required
def edit(request , id):
    data = decript(id)
    stok = Stok.objects.get(pk=data)
    depo = request.user.useremployee.karyawan.depo.id
    data = Stok.objects.filter(depo_id=depo)
    # return HttpResponse(stok)
    if request.POST:
        form = StokForm(request.POST, instance=stok)
        # return HttpResponse(form)
        if form.is_valid():
            if form.save():
                return render(request, "stok/data.html", {"data": data})
            else :
                return HttpResponse("fail")
        else :
            return HttpResponse("form invalid")
    else :
          form = StokForm(instance=stok)
          return render(request,"stok/edit.html",{"form":form})