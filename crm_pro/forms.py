from django import forms
from . models import *
class add_vendors(forms.ModelForm):
    class Meta():
        model=AddVendors
        fields = ['vendor','phone','p_email','website','ass_to','cat','country','state','city','postal_code','desc']

class add_purchaseorders(forms.ModelForm):
    class Meta():
        model = AddPurchaseOrder
        fields = ['sub','vendor','status','req_num','contact','date','commission','e_duty','carrier','tracking_num','ass_to','org','bill_c','shipp_c','b_a','s_a','b_postal_code','s_postal_code','desc']
class add_serviceContracts(forms.ModelForm):
    class Meta():
        model = AddServiceContract
        fields = ['sub','type','pri','status','tu','uu','total','s_d','e_d','contact']
class add_internalTickets(forms.ModelForm):
    class Meta():
        model = AddInternalTicket
        fields = ['summ', 'i_t', 'status', 'pri', 'p_name', 'ass_to', 'channel', 'res', 'mail', 'date1','sla']
class add_workOrder(forms.ModelForm):
    class Meta():
        model = AddWorkOrder
        fields = ['sub', 'status', 'org', 'contact', 'pri', 'service', 'work_desc', 'type', 'loc', 'loc1', 's_d', 't_c']
class add_sites(forms.ModelForm):
    class Meta():
        model = AddOurSite
        fields =['b_n' , 'b_u']
class add_employees_form(forms.ModelForm):
    class Meta():
        model = AddEmployee
        fields =['f_name','l_name','mail','lang','title','dep','off_phone','mob','b_hours','region','country','address','pincode','pic']
class add_templat(forms.ModelForm):
    class Meta():
        model = AddTemplate
        fields = ['t','m','desc','d_t','a']
class add_product_form(forms.ModelForm):
    class Meta():
        model = AddProduct
        fields = '__all__'