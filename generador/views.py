from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def nombre(request):
    #Listas de nombres con una y dos palabras (agregar muchas de cada una):
    moda1 = ['SPANKY', 'LENCESHOP', 'LOLARDA', 'STUDIOCHIC', 'URBAN', 'GUAPAS', 'SWEETLENCE', 'ROMMA']
    moda2 = ['BEAUTY MODE','MODERNIZE CLOTHES','TRENDY GIRLS','FASHION & PRETY','FASHION SHOP','FREE STYLE','VIP GIRLS','VIP ROOM','URBAN COLLECTION']
    tech1 = ['NAMTECH','PROTECH','NANOTECH','TECDROID','FALOTECH','ROBOTECH']
    tech2 = ['NAM TECHNOLOGIES','ASTRO TECHNOLOGIES']
    ecom1 = ['TODOCOMPRAS','CHANGOLLENO']
    ecom2 = ['PARAVOS SHOP','NOSE SHOP']
    rich1 = ['MENTESANA','RIQUE$AS','OPORTUNITY']
    rich2 = ['MENTE ABUNDANTE','JOVENES MILLONARIOS','HIGHRICH GROUP']
    educ1 = ['TECHDEMIA','TRODEMY']
    educ2 = ['TRON ACADEMY','ALPHABET ACADEMY','NEW TRADERS','ARLISTAN FOUNDATION']
    kiosko1 = ['LODECARLO','KIOSKERA','DIOSQUIERA','PAYAYA']
    kiosko2 = ['KIOSKO PUERCOESPIN','KIOSKO MILEI','KIOSKO ABUNDANTE']

    #Tenemos que saber que categoria fue seleccionada -> El valor de la categoria.
    categoria = request.GET.get('categorias')

    #Categoria moda:
    if(categoria=='moda'):
        #Modifico el valor de categoria para mostrarla despues.
        categoria = 'ropa/moda'
        if(request.GET.get('unapalabra')):
            nombregen = random.choice(moda1)
        elif(request.GET.get('dospalabras')):
            nombregen = random.choice(moda2)
        elif(request.GET.get('azar')):
            lista3 = moda1 + moda2
            nombregen = random.choice(lista3)

    #Categoria tech:
    if(categoria=='tech'):
        categoria = 'tecnología'
        if(request.GET.get('unapalabra')):
            nombregen = random.choice(tech1)
        elif (request.GET.get('dospalabras')):
            nombregen = random.choice(tech2)
        elif (request.GET.get('azar')):
            lista3 = tech1 + tech2
            nombregen = random.choice(lista3)

    #Categoria ecommerce:
    if(categoria=='ecommerce'):
        categoria = 'ecommerce'
        if (request.GET.get('unapalabra')):
            nombregen = random.choice(ecomm1)
        elif (request.GET.get('dospalabras')):
            nombregen = random.choice(ecomm2)
        elif (request.GET.get('azar')):
            lista3 = ecomm1 + ecomm2
            nombregen = random.choice(lista3)

    #Categoria riqueza
    if(categoria=='riqueza'):
        if (request.GET.get('unapalabra')):
            nombregen = random.choice(rich1)
        elif (request.GET.get('dospalabras')):
            nombregen = random.choice(rich2)
        elif (request.GET.get('azar')):
            lista3 = rich1 + rich2
            nombregen = random.choice(lista3)

    #Categoria educacion
    if (categoria == 'educacion'):
        if (request.GET.get('unapalabra')):
            nombregen = random.choice(educ1)
        elif (request.GET.get('dospalabras')):
            nombregen = random.choice(educ2)
        elif (request.GET.get('azar')):
            lista3 = educ1 + educ2
            nombregen = random.choice(lista3)

    #Categoria kioskos
    if (categoria == 'kiosko'):
        if (request.GET.get('unapalabra')):
            nombregen = random.choice(kiosko1)
        elif (request.GET.get('dospalabras')):
            nombregen = random.choice(kiosko2)
        elif (request.GET.get('azar')):
            lista3 = kiosko1 + kiosko2
            nombregen = random.choice(lista3)


    return render(request,'nombre.html',{'nombre':nombregen,'categoria':categoria})

