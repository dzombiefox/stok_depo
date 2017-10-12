# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.decorators import login_required,permission_required
from size .models import Size
from stok .forms import StokForm
from django.http import HttpResponse,HttpResponseRedirect
from depo .models import Depo
from django.db.models import Q
from stok .models import Stok,Standard
from django.db.models import Sum
import pyodbc
import datetime
from django.shortcuts import redirect
# Create your views here.
@login_required
def index(request):
    if request.user.is_superuser:
        return redirect('/admin/')
    else :
            user = request.user.useremployee.karyawan.depo.id
            if user == 3 :
                if request.POST:
                        # return HttpResponse("fsa")
                        bln = request.POST['month']
                        bul = int(bln)
                        bulkurang = bul - 1
                        bulan = 0
                        if (bul < 10):
                           bulan = "0" + bln
                        else:
                           bulan = bln
                        periode = request.POST['periode']
                        tgl = 0
                        if periode == "1":
                           tgl = "05"
                        else:
                           tgl = "19"
                        now = datetime.datetime.now()
                        year = str(now.year)
                        tanggal = year + "-" + bulan + "-" + tgl
                        tanggalopt = year+"-"+bulan+"-"+'01'

                        datas =Stok.objects.values('size__namaUkuran','size','tanggal').annotate(kita=Sum('kita'),picasso=Sum('picasso'),harmony=Sum('harmony'),atena=Sum('atena')).filter(tanggal=tanggal)
                        cdata = Stok.objects.filter(tanggal = tanggal )
                        std = Standard.objects.get(pk=1)
                        # return HttpResponse("dsd")
                        if tgl == '5' :
                            # return HttpResponse("yes")
                            disc =  Stok.objects.values('tanggal').distinct().filter(tanggal__lte=(tanggal)).order_by('-tanggal')[:2:1]
                        else :
                            # return HttpResponse(tgl)
                            disc = Stok.objects.values('tanggal').distinct().filter(tanggal__range=(tanggalopt,tanggal)).order_by('-tanggal')[:2:1]
                        return render(request,"stok/print.html",{"data":datas,"cdata":cdata,"tanggal":tanggal,"std":std,"disc":disc})

                else :

                    return render(request,"stok/print.html",{"tanggal":"2001-01-01"})
            else :
                frm = StokForm()
                # return HttpResponse
                size = Size.objects.all()
                # return  HttpResponse(size)
                return render(request, 'index.html',{"size":size})