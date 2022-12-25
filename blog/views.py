from django.shortcuts import render,redirect
from multiprocessing import context
from .models import Artikel,Kategori
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
import requests

def is_creator(user):
    if user.groups.filter(name='Creator').exists():
        return True
    else:
        return False

@login_required
def dashboard(request):
    if request.user.groups.filter(name='Creator').exists():
        request.session['is_creator'] = 'creator'
    
    template_name = "back/barang_list.html"
    context = {
        'title' : 'dashboard',
    } 
    return render(request, template_name, context)

@login_required
def artikel(request):
    template_name = "back/barang_list.html"
    artikel = Artikel.objects.all()
    print(artikel)
    context = {
        'title' : 'dashboard',
        'artikel': artikel,
    }
    return render(request, template_name, context)

def sinkron_artikel(request):
	url = "https://indonesia-public-static-api.vercel.app/api/heroes"
	data = requests.get(url).json()
	for d in data:
		cek_berita = Artikel.objects.filter(nama=d['name'])
		if cek_berita:
			print('data sudah ada')
			c = cek_berita.first()
			c.nama=d['nama']
			c.save()
		else: 
      		#jika belum ada maka tulis baru kedatabase
			d = Artikel.objects.create(
				nama = d['name'],
				deskripsi = d['description'],
				tahun_lahir = d['birth_year'],
				tahun_wafat = d['death_year'],
				tahun_kenaikan = d['ascension_year'],
				
			)
	return redirect(artikel)
@login_required
def users(request):
    template_name = "back/user_list.html"
    list_user = User.objects.all()
    context = {
        'title' : 'dashboard',
        'list_user' : list_user
    }
    return render(request, template_name, context)

@login_required
def tambah_artikel(request):
    template_name = "back/barang_add.html"
    if request.method == "POST":
        nama = request.POST.get('nama')
        tahun_lahir = request.POST.get('tahun_lahir')
        tahun_wafat = request.POST.get('tahun_wafat')
        tahun_kenaikan = request.POST.get('tahun_kenaikan')
        #simpan produk karena ada relasi ke tabel kategori 
        Artikel.objects.create(
            nama = nama,
            tahun_lahir = tahun_lahir,
            tahun_wafat = tahun_wafat,
            tahun_kenaikan = tahun_kenaikan,
        )
        return redirect (artikel)
    context = {
        'title':'Tambah Artikel',

    }
    return render(request, template_name, context)

@login_required
def lihat_artikel(request, id):
    template_name = "back/lihat_artikel.html"
    artikel = Artikel.objects.get(id=id)
    context = {
        'title' : 'View Artikel',
        'artikel' :artikel,
    }
    return render(request, template_name, context)

@login_required
def edit_artikel(request ,id ):
    template_name = 'back/edit_artikel.html'
    a = Artikel.objects.get(id=id)
    if request.method == "POST":
        
        nama = request.POST.get('nama')
        tahun_lahir = request.POST.get('tahun_lahir')
        tahun_wafat = request.POST.get('tahun_wafat')
        tahun_kenaikan = request.POST.get('tahun_kenaikan')


        #input Kategori Dulu
        

        #simpan produk karena ada relasi ke tabel kategori 
        a.nama = nama
        a.tahun_lahir = tahun_lahir
        a.tahun_wafat = tahun_wafat
        a.tahun_kenaikan = tahun_kenaikan
        a.save() 
        return redirect(artikel)
    context = {
        'title':'Edit Artikel',
        'artikel' : artikel,

    }
    return render(request, template_name, context)

@login_required
def delete_artikel(request,id):
    Artikel.objects.get(id=id).delete()
    return redirect(artikel)