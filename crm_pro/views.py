from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.models import User , auth


from .forms import *
from .models import *
# Create your views here.
def index(request):

   return render(request, "index.html")


def add_project(request):
   return render(request, 'add_project.html')

def add_project_task(request):
   return render(request, 'add_project_tasks.html')

def add_project_milestones(request):
   return render(request, 'add_project_milestones.html')

def view_project(request):
    dests = AddProjects.objects.all()
    return render(request, "view_projects.html", {'dests': dests})

def view_task(request):
    dests = AddTasks.objects.all()
    return render(request, 'view_tasks.html', {'dests': dests})

def view_milestone(request):
    dests = AddMilestone.objects.all()
    return render(request, 'view_milestones.html',{'dests': dests})
def add_oppurtunities(request):
   return render(request, 'add_oppurtunities.html')
def view_oppurtunity(request):
    dests = AddOppurtunity.objects.all()
    return render(request, 'view_opportunities.html',{'dests': dests})
def add_quote(request):
    return render(request, 'add_quotes.html')
def view_quote(request):
    dests = AddQuotes.objects.all()
    return render(request , 'view_quotes.html',{'dests': dests})
def add_product(request):
    if request.method == 'POST':
        form = add_product_form(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return render(request, 'index.html')
    else:
        form = add_product_form()
        return render(request, "add_products.html", {'form': form})
def view_product(request):
    #return Story.objects.filter(user=request.user.id).order_by('-create_date')
    dests = AddProduct.objects.all()
    return render(request , 'view_products.html',{'dests': dests})
def add_service(request):
    return render(request, 'add_services.html')
def view_service(request):
    dests = AddService.objects.all()
    return render(request , 'view_services.html' , {'dests':dests})

def add_invoice(request):
    dests, dest1 = AddProduct.objects.all(), AddService.objects.all()
    context = {'dests':dests , 'dest1':dest1}
    return render(request , 'add_invoices.html',context)
   
def view_invoice(request):
    dests = AddInvoices.objects.all()
    return render(request , 'view_invoices.html', {'dests':dests})
def add_salesorder(request):
    return render(request , 'add_saleorder.html')
def view_salesorder(request):
    dests = AddSalesOrder.objects.all()
    return render(request , 'view_salesorder.html', {'dests':dests})
def add_vendor(request):
    form = add_vendors(request.POST or None)
    if form.is_valid():
        form.save()
        return render(request,'index.html')
    return render(request, "add_vendors.html", {'form': form})


def view_vendor(request):
    dests = AddVendors.objects.all()
    return render(request ,'view_vendors.html', {'dests':dests})

def add_purOrder(request):
    form = add_purchaseorders(request.POST or None)
    if form.is_valid():
        form.save()
        return render(request,'index.html')
    return render(request,'add_purOrders.html' , {'form' : form})


def view_purOrder(request):
    dests = AddPurchaseOrder.objects.all()
    return render(request , 'view_purOrders.html',{'dests':dests})
def add_compaign(request):

    return render(request , 'add_compaigns.html')
def view_compaign(request):
    dests = AddCompaign.objects.all()
    return render(request , 'view_compaigns.html',{'dests':dests})
def add_serviceContract(request):
    form = add_serviceContracts(request.POST or None)
    if form.is_valid():
        form.save()
        return render(request, 'index.html')
    return render(request, "add_serviceContracts.html", {'form': form})
def view_serviceContract(request):
    dests = AddServiceContract.objects.all()
    return render(request , 'view_serviceContracts.html',{'dests':dests})
def add_internalTicket(request):
    form = add_internalTickets(request.POST or None)
    if form.is_valid():
        form.save()
        return render(request, 'index.html')
    return render(request, "add_internalTickets.html", {'form': form})
def view_internalTicket(request):
    dests = AddInternalTicket.objects.all()
    return render(request , 'view_internalTickets.html',{'dests':dests})
def add_workOrders(request):
    form = add_workOrder(request.POST or None )
    if form.is_valid():
        form.save()
        return render(request, 'index.html')
    return render(request, "add_workOrders.html", {'form': form})
def view_workOrder(request):
    dests = AddWorkOrder.objects.all()
    return render(request , 'view_workOrders.html',{'dests':dests})
def add_case(request):
    return render(request , 'add_cases.html')
def view_case(request):
    dests=AddCase.objects.all()
    return render(request , 'view_cases.html',{'dests':dests})
def add_FAQ(request):
    return render(request , 'add_FAQ.html')
def view_FAQ(request):
    return render(request , 'view_FAQ.html')
def add_bookmark(request):
    form = add_sites(request.POST or None)
    if form.is_valid():
        form.save()
        return render(request, 'index.html')
    return render(request, "add_bookmark.html", {'form': form})
def view_bookmark(request):
    dests = AddOurSite.objects.all()
    return render(request , 'view_bookmark.html',{'dests':dests})
def add_employee(request):
    if request.method=='POST':
        form = add_employees_form(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return render(request, 'index.html')
    else :
        form=add_employees_form()
        return render(request, "add_employees.html", {'form': form})
def view_employee(request):
    dests = AddEmployee.objects.all()
    return render(request, 'view_employees.html', {'dests':dests})
def add_printTemplate(request):
    form = add_templat(request.POST or None)
    if form.is_valid():
        form.save()
        return render(request, 'index.html')
    return render(request, "add_printTemp.html", {'form': form})


def view_printTemplate(request):
    dests = AddTemplate.objects.all()
    return render(request , 'view_printTemplate.html',{'dests': dests})
def add_contact(request):
    return render(request , 'add_contacts.html')
def view_contact(request):
    #return AddContact.objects.filter(user=request.user.id).group_by('image')
    dests = AddContact.objects.all()
    return render(request , 'view_contacts.html',{'dests': dests})
def add_organization(request):
    return render(request , 'add_organizations.html')
def view_organization(request):
    dests = AddOrganization.objects.all()
    return render(request , 'view_organizations.html' , {'dests' : dests})
def save_projects(request):
    a=request.POST.get('project_name')
    b=request.POST.get('status')
    c=request.POST.get('related_to')
    d=request.POST.get('assigned_to')
    e=request.POST.get('start_date')
    f=request.POST.get('target_end_date')
    g=request.POST.get('actual_end_date')
    h=request.POST.get('opportunity_name')
    i=request.POST.get('contact_name')
    j=request.POST.get('budget')
    k=request.POST.get('project_url')
    l=request.POST.get('priority')
    m=request.POST.get('progress')

    n=request.POST.get('description')

    o=AddProjects(pro_name =a,status=b,realted_to=c,assigned_to=d,start_date=e,target_end_date=f,actual_end_date=g,opportunity_name=h,contact_name=i,budget=j,project_url=k ,priority=l,progress=m,desc=n)
    o.save()

    return render(request , 'index.html')

def save_tasks(request):
    a = request.POST.get('task_name')
    b = request.POST.get('status')
    c = request.POST.get('related_to')
    d = request.POST.get('assigned_to')
    e = request.POST.get('milestone_name')
    f = request.POST.get('priority')
    g = request.POST.get('worked_hours')
    h = request.POST.get('progress')
    i = request.POST.get('start_date')
    j = request.POST.get('end_date')
    k = request.POST.get('description')

    l = AddTasks(task_name=a, status=b, realted_to=c, assigned_to=d, milestone_name=e, priority=f,
                    workedHours=g, progress=h, start_date=i, end_date=j, desc=k)
    l.save()

    return render(request, 'index.html')
def save_milestones(request):
    a=request.POST.get('milestone_name')
    b=request.POST.get('related_to')
    c=request.POST.get('assigned_to')
    d=request.POST.get('milestone_date')
    e=request.POST.get('description')
    f=AddMilestone(milestone_name=a,realted_to=b,assigned_to=c,milestone_date=d,desc=e)
    f.save()

    return render(request, 'index.html')
def save_contacts(request):
    a=request.POST.get('first_name')
    b=request.POST.get('last_name')
    c=request.POST.get('primary_email')
    d=request.POST.get('office_phone')
    e=request.POST.get('mobile_phone')
    f=request.POST.get('home_phone')
    g=request.POST.get('dob')
    h=request.POST.get('organization')
    i=request.POST.get('department')
    j=request.POST.get('assigned_to')
    k=request.POST.get('contact_type')
    l=request.POST.get('language')
    m=request.POST.get('reffered_by')
    n=request.POST.get('SLA_name')
    o= request.POST.get('portal_user')
    p = request.POST.get('support_start_date')
    q = request.POST.get('support_end_date')
    r = request.POST.get('country')
    s = request.POST.get('street')
    t = request.POST.get('postal_code')
    u = request.POST.get('description')
    v= request.POST.get('image')
    w = request.POST.get('linkedin')
    x= request.POST.get('fb_url')
    y=AddContact(first_name=a,last_name=b,primary_email=c,office_phone=d,mobile_phone=e,home_phone=f,dob=g,organization=h,department=i,assigned_to=j,contact_type=k,language=l,reffered_by=m,SLA_name=n,portal_user=o,support_start_date=p,support_end_date=q,country=r,street=s,postal_code=t,desc=u,imgg=v,linkedin_url=w,fb_url=x)
    y.save()
    return render(request,'index.html')
def save_organizations(request):
    a=request.POST.get('org_name')
    b=request.POST.get('p_email')
    c=request.POST.get('website')
    d=request.POST.get('p_phone')
    e=request.POST.get('employees')
    f=request.POST.get('industry')
    g=request.POST.get('revenue')
    h=request.POST.get('ownership')
    i=request.POST.get('SLA_name')
    j=request.POST.get('assigned_to')
    k=request.POST.get('sic_code')
    l=request.POST.get('billing_country')
    m=request.POST.get('shipping_country')
    n=request.POST.get('billing_address')
    o= request.POST.get('shipping_address')
    p = request.POST.get('billing_postal_code')
    q = request.POST.get('shipping_postal_code')
    r = request.POST.get('desc')
    s= request.Files['org_img']
    t=AddOrganization(org_name=a,p_email=b,website=c,p_phone=d,employees=e,industry=f,revenue=g,ownership=h,SLA_name=i,assigned_to=j,sic_code=k,billing_country=l,shipping_country=m,billing_address=n,shipping_address=o,billing_postal_code=p,shipping_postal_code=q,desc=r)
    t.save()
    fs=FileSystemStorage()
    fs.save(s.name,s)

    return render(request,'index.html')
def save_compaigns(request):
    a=request.POST.get('comp_name')
    b=request.POST.get('close_date')
    c=request.POST.get('product')
    d=request.POST.get('assigned_to')
    e=request.POST.get('comp_type')
    f=request.POST.get('comp_status')
    g=request.POST.get('audience')
    h=request.POST.get('target_size')
    i=request.POST.get('sponsor')
    j=request.POST.get('numsent')
    k=request.POST.get('budget')
    l=request.POST.get('cost')
    m=request.POST.get('revenue')
    n=request.POST.get('response')
    o= request.POST.get('sales_count')
    p = request.POST.get('actual_sales_count')
    q = request.POST.get('ROI')
    r = request.POST.get('actual_ROI')
    s= request.POST.get('desc')
    t=AddCompaign(comp_name=a,close_date=b,product=c,assigned_to=d,comp_type=e,comp_status=f,audience=g,target_size=h,sponsor=i,numsent=j,budget=k,cost=l,revenue=m,response=n,sales_count=o,actual_sales_count=p,ROI=q,actual_ROI=r,desc=s)
    t.save()
    return render(request,"index.html")
def save_opportunities(request):
    a=request.POST.get('oppo_name')
    b=request.POST.get('amount')
    c=request.POST.get('org_name')
    d=request.POST.get('contact_name')
    e=request.POST.get('close_date')
    f=request.POST.get('pipeline')
    g=request.POST.get('sales_stages')
    h=request.POST.get('assigned_to')
    i=request.POST.get('lead_source')
    j=request.POST.get('type_b')
    k=request.POST.get('probability')
    l=request.POST.get('camp_source')
    m=request.POST.get('revenue')
    n=request.POST.get('p_mail')
    o= request.POST.get('lost_reason')
    p = request.POST.get('desc')
    q = AddOppurtunity(oppo_name=a,amount=b,org_name=c,contact_name=d,close_date=e,pipeline=f,sales_stages=g,assigned_to=h,lead_source=i,type_b=j,probability=k,camp_source=l,revenue=m,p_mail=n,lost_reason=o,desc=p)
    q.save()
    return render(request , "index.html")
def save_quotes(request):
    a=request.POST.get('subject')
    b=request.POST.get('oppo_name')
    c=request.POST.get('quote_stage')
    d=request.POST.get('valid_until')
    e=request.POST.get('org_name')
    f=request.POST.get('related_to')
    g=request.POST.get('shipping')
    h=request.POST.get('carrier')
    i=request.POST.get('assigned_to')
    j=request.POST.get('cbaf')
    k=request.POST.get('csaf')
    m=request.POST.get('billing_country')
    n=request.POST.get('shipping_country')
    o= request.POST.get('billing_address')
    p = request.POST.get('shipping_address')
    q = request.POST.get('billing_postal_code')
    r = request.POST.get('shipping_postal_code')
    s= AddQuotes(subject=a,oppo_name=b,quote_stage=c,valid_until=d,org_name=e,related_to=f,shipping=g,carrier=h,assigned_to=i,cbaf=j,csaf=k,billing_country=m,shipping_country=n,billing_address=o,shipping_address=p,billing_postal_code=q,shipping_postal_code=r)
    s.save()
    return render(request,'index.html')
def save_products(request):
    a=request.POST.get('pro_name')
    b=request.POST.get('part_num')
    c=request.POST.get('pro_active')
    d=request.POST.get('pro_cat')
    e=request.POST.get('vendor')
    f=request.POST.get('builder')
    g=request.POST.get('start_date')
    h=request.POST.get('end_date')
    i=request.POST.get('support_date')
    j=request.POST.get('supp_end_date')
    k=request.POST.get('serialno')
    l=request.POST.get('mfr_part_no')
    m=request.POST.get('vendor_part_no')
    n=request.POST.get('website')
    o= request.POST.get('price')
    p = request.POST.get('commission_rate')
    q = request.POST.get('VAT')
    r = request.POST.get('sale')
    s= request.POST.get('service')
    t = request.POST.get('p_cost')
    u = request.POST.get('b_type')
    v = request.POST.get('unit')
    w = request.POST.get('stock')
    x = request.POST.get('demand')
    y = request.POST.get('handler')
    z = request.POST.get('p_image')
    A = request.POST.get('desc')
    B=AddProduct(pro_name=a,part_num=b,pro_active=c,pro_cat=d,vendor=e,builder=f,start_date=g,end_date=h,support_date=i,supp_end_date=j,serialno=k,mfr_part_no=l,vendor_part_no=m,website=n,price=o,commission_rate=p, VAT=q,sale=r,service =s,p_cost=t,b_type=u,unit=v,stock=w,demand=x,handler=y,p_image=z,desc=A)
    B.save()
    return render(request,'index.html')
def save_invoices(request):
    a=request.POST.get('sub')
    b=request.POST.get('org')
    c=request.POST.get('in_date')
    d=request.POST.get('due_date')
    e=request.POST.get('contact')
    f=request.POST.get('num')
    g=request.POST.get('s_order')
    h=request.POST.get('p_order')
    i=request.POST.get('assigned_to')
    j=request.POST.get('status')
    k=request.POST.get('s_duty')
    l=request.POST.get('e_duty')
    m=request.POST.get('oppo')
    n=request.POST.get('pro')
    o= request.POST.get('q_name')
    p = request.POST.get('r_to')
    q = request.POST.get('cbaf')
    r = request.POST.get('csaf')
    s=request.POST.get('bill_c')
    t = request.POST.get('shipp_c')
    u = request.POST.get('b_a')
    v = request.POST.get('s_a')
    w = request.POST.get('bpc')
    x = request.POST.get('spc')
    y = request.POST.get('desc')
    z= AddInvoices(sub=a,org=b,in_date=c,due_date=d,contact=e,num=f,s_order=g,p_order=h,assigned_to=i,status=j,s_duty=k,e_duty=l,oppo=m,pro=n,q_name=o,r_to=p,cbaf=q,csaf=r,bill_c=s,shipp_c=t,b_a=u,s_a=v,bpc=w,spc=x,desc=y)
    z.save()
    return render(request,'index.html')
def save_sale_orders(request):
    a = request.POST.get('sub')
    b = request.POST.get('oppo')
    c = request.POST.get('q_name')
    d = request.POST.get('p_order')
    e = request.POST.get('contact')
    f = request.POST.get('org')
    g = request.POST.get('assigned_to')
    h = request.POST.get('status')
    i = request.POST.get('s_duty')
    j = request.POST.get('e_duty')
    k = request.POST.get('cbaf')
    l = request.POST.get('csaf')
    m = request.POST.get('carrier')
    n = request.POST.get('bill_c')
    o = request.POST.get('shipp_c')
    p = request.POST.get('bpc')
    q = request.POST.get('spc')
    r = request.POST.get('desc')
    s = AddSalesOrder(sub=a,oppo=b,q_name=c,p_order=d,contact=e,org=f,assigned_to=g,status=h,s_duty=i,e_duty=j,cbaf=k,csaf=l,carrier=m,bill_c=n,shipp_c=o,bpc=p,spc=q,desc=r)
    s.save()
    return render(request,'index.html')


def save_cases(request):
    a = request.POST.get('summ')
    b = request.POST.get('c_t')
    c = request.POST.get('status')
    d = request.POST.get('pri')
    e = request.POST.get('contact')
    f = request.POST.get('ass_to')
    g = request.POST.get('channel')
    h = request.POST.get('p_name')
    i = request.POST.get('group')
    j = request.POST.get('res')
    k = request.POST.get('cat')
    l = request.POST.get('date1')
    m = request.POST.get('sla')
    n = AddCase(summ=a,c_t=b,status=c,pri=d,contact=e,ass_to=f,channel=g,p_name=h,group=i,res=j,cat=k,date1=l,sla=m)
    n.save()
    return render(request,'index.html')


def index_google(request):


    return render(request, 'index_google.html')
    auth.index_google(request)
    return redirect('/')



def login_fb(request):
    return render(request, 'login_fb.html')


def home_fb(request):
    return render(request, 'home_fb.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
    return render(request, 'login.html')



def register(request):
    return render(request,'register.html')

def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/index')
        else:
            messages.info(request, 'invalid usename or password')
            return redirect('login')

    else:
        return render(request, 'login.html')

def register1(request):
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        con_password = request.POST['con_password']
        email = request.POST['email']


        if password==con_password:
            if User.objects.filter(username=username).exists():

                messages.info(request,'username taken')
                return redirect('register1');

            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('register1');
            else:
                user = User.objects.create_user(username=username, password=password, email=email,
                                                first_name=first_name,
                                                last_name=last_name)
                user.save();
                return redirect('login')
        else:
            return render(request, 'register.html')
def save_services(request):
    a = request.POST.get('service_name')
    b = request.POST.get('active')
    c = request.POST.get('cat')
    d = request.POST.get('owner')
    e = request.POST.get('sale_date')
    f = request.POST.get('sale_end_date')
    g = request.POST.get('supp_date')
    h = request.POST.get('supp_end_date')
    i = request.POST.get('website')
    j = request.POST.get('price')
    k = request.POST.get('commission_rate')
    l = request.POST.get('VAT')
    m = request.POST.get('sale')
    n = request.POST.get('service')
    o = request.POST.get('p_cost')
    p = request.POST.get('b_type')
    q = request.POST.get('desc')
    r = AddService(service_name=a,active=b,cat=c,owner=d,sale_date=e,sale_end_date=f,supp_date=g,supp_end_date =h,website=i,price=j,commission_rate=k,VAT=l,sale=m,service=n,p_cost=o,b_type=p, desc=q)
    r.save()
    return render(request,'index.html')









