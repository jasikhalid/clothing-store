from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    if 'id' in request.session:
        name=register.objects.get(username=request.session['id'])
        data=products.objects.all()[:8]
        return render(request,'index.html',{'data':data,'name':name})
    else:
        data=products.objects.all()[:8]
        return render(request,'index.html',{'data':data})

def regis(request):
    if request.method == "POST":
        a = request.POST['full_name']
        b = request.POST['email']
        d = request.POST['phone']
        c = request.POST['pass']
        e = request.POST['user']
        h = request.POST['state']
        i = request.POST['city']
        j = request.POST['postc']
        k= request.POST['street']
        f1 = register.objects.filter(username=e)
        g1 = register.objects.filter(email=b)
        if list(f1) == []:
            if list(g1) == []:
                data1=register.objects.create(full_name=a,email=b,password=c,phone_number=d,username=e,country=h,city=i,postc=j,street=k)
                data1.save()
                data2=login.objects.create(password=c,username=e)
                data2.save()
                return render(request,'index.html')
            else:
                url = 'reg'
                msg = '''<script>alert('email already exist')
                                    window.location='%s'</script>''' % (url)
                return HttpResponse(msg)
        else:
            url = 'reg'
            msg = '''<script>alert('username already exist')
                        window.location='%s'</script>''' % (url)
            return HttpResponse(msg)
    else:
        return render(request,'register.html')
def logi(request):
    if request.method == "POST":
        a = request.POST['user']
        b=request.POST['password']
        if a=="admin" and b=="admin":
            return redirect(dashboard)
        else:
            try:
                d=login.objects.get(username=a)
                if(d.password==b):
                    request.session['id']=a
                    return redirect(index)
                else:
                    return HttpResponse('password error')
            except Exception as k:
                return HttpResponse(k)
    else:
        return render(request,'log.html')
def landing(request):
    return render(request,'landing.html')
def logout(request):
    if 'id' in request.session:
        request.session.flush()
        return redirect(landing)
def shop(request):
    data = products.objects.all()[:9]
    return render(request,'shop.html',{'data':data})
def shop_cart(request):
    data1=orders.objects.all()
    data = products.objects.all()
    return render(request,'shop-cart.html' ,{'data':data,'data1':data1})
def product_details(request):
    return render(request,'product-details.html')
def contact(request):
    if request.method == "POST":
        a = request.POST['name']
        b = request.POST['email']
        c = request.POST['phone']
        d = request.POST['message']
        data=ContactMessage.objects.create(name=a,email=b,phone_number=c,message=d)
        data.save()
        return render(request,'contact.html')
    else:
        return render(request,'contact.html')
def checkout(request):
    return render(request,'checkout.html')
#def adminpanel(request):
# return render(request,'adminpanel.html')
def admin_pro(request):
    if request.method == "POST":
        a = request.POST.get('name')
        b = request.POST.get('price')
        d = request.POST.get('description')
        e = request.POST.get('ids')
        h = request.FILES.get('img')
        i = request.POST.get('gender')
        j = request.POST.get('category')

        # Get size checkboxes safely
        k1 = request.POST.get('size1')
        k2 = request.POST.get('size2')
        k3 = request.POST.get('size3')

        # Get quantity only if size is selected, else default to 0
        c1 = request.POST.get('quantity1') if k1 else 0
        c2 = request.POST.get('quantity2') if k2 else 0
        c3 = request.POST.get('quantity3') if k3 else 0

        # Combine selected sizes into a single string (optional)
        size_list = []
        if k1: size_list.append(k1)
        if k2: size_list.append(k2)
        if k3: size_list.append(k3)
        sizes = ','.join(size_list)

        # Create one product entry only
        product = products.objects.create(
            name=a,
            price=b,
            quantity1=c1,
            quantity2=c2,
            quantity3=c3,
            description=d,
            gender=i,
            category=j,
            size=sizes,
            img=h,
            ids=e
        )
        product.save()

        return render(request, 'admin-pro.html', {'msg': 'Product added successfully!'})
    else:
        return render(request, 'admin-pro.html')
def product(request):
    return render(request, 'products.html')
def update(request):
    if request.method == "POST":
        product_id = request.POST.get('ids')

        # Try to find the existing product
        try:
            product = products.objects.get(ids=product_id)
        except products.DoesNotExist:
            return render(request, 'change-product.html', {'error': 'Product ID not found!'})

        # Update only fields that are filled in
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        gender = request.POST.get('gender')
        category = request.POST.get('category')
        image = request.FILES.get('img')

        # Sizes
        size1 = request.POST.get('size1')
        size2 = request.POST.get('size2')
        size3 = request.POST.get('size3')

        qty1 = request.POST.get('quantity1') if size1 else 0
        qty2 = request.POST.get('quantity2') if size2 else 0
        qty3 = request.POST.get('quantity3') if size3 else 0

        # Build size string
        size_list = []
        if size1: size_list.append(size1)
        if size2: size_list.append(size2)
        if size3: size_list.append(size3)
        sizes = ','.join(size_list)

        # Update only non-empty fields
        if name: product.name = name
        if price: product.price = price
        if description: product.description = description
        if gender: product.gender = gender
        if category: product.category = category
        if image: product.img = image
        if sizes: product.size = sizes
        if size1 or size2 or size3:
            product.quantity1 = qty1
            product.quantity2 = qty2
            product.quantity3 = qty3

        product.save()

        return render(request, 'update-pro.html', {'msg': 'Product updated successfully!'})

    else:
        return render(request, 'update-pro.html')

def delete(request):
    if request.method == "POST":
        a = request.POST.get('ids')
        data = products.objects.get(ids=a)
        data.delete()
        return render(request, 'delete-pro.html')
    else:
        return render(request, 'delete-pro.html')
def dashboard(request):
    return render(request, 'dashboard.html')
def admin_orders(request):
    orders = orders.objects.all()
    return render(request, 'admin-order.html',{'orders':orders})
def message(request):
    msgs = ContactMessage.objects.all().order_by('-date')
    return render(request, 'adminmessage.html', {'message': msgs})
def blog(request):
    return render(request, 'blog.html')
def blog_details(request):
    return render(request, 'blog-details.html')

def favorite(request):
    if 'id' in request.session:
        u = request.session['id']
        fav=favorites.objects.filter(username=u)
        return render(request, 'favorate.html', {'fav': fav})

def add_to_wishlist(request, ids):
    if 'id' in request.session:
        u = request.session['id']
        product = products.objects.get(ids=ids)
        created = favorites.objects.create(username=u, product_name=product.name,product_image=product.img,price=product.price)
        created.save()
        return redirect(favorite)
    else:
        return redirect(logi)


def remove_from_wishlist(request, ids):
    favorite = favorites.objects.filter(user=request.user, ids=ids)
    favorite.delete()
    return redirect('favorite')


def add_to_order(request, ids):
    if 'id' in request.session:
        u=request.session['id']
        product = products.objects.get(ids=ids)
        orderr=orders.objects.create(username=u, name=product.name,product_image=product.img,price=product.price,ids=products.ids)
        orderr.save()
        return redirect('index')
    else:
        return redirect('log')
def qty_inc(request, ids):
    try:
        order = orders.objects.get(ids=ids)
        orders.quantity += 1
        order.save()
        return redirect("shop_cart")
    except orders.DoesNotExist:
        return HttpResponse("Order not found")

def qty_dec(request,ids):
    try:
        order = orders.objects.get(ids=ids)
        if orders.quantity > 1:
            orders.quantity -= 1
        order.save()
        return redirect("shop_cart")
    except orders.DoesNotExist:
        return HttpResponse("Order not found")



