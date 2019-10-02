from django.db import models

# Create your models here.

class AddProjects(models.Model):

    status_choices = (
        ('Started' , 'Started'),
        ('New' , 'New'),
        ('In Progress','In Progress'),
        ('Waiting for feedback','Waiting for feedback'),
        ('On hold','On hold'),
        ('Completed','Completed'),
        ('Delivered','Delivered'),
    )

    priority_choices = (
        ('High','High'),
        ('Medium','Medium'),
        ('Low','Low'),
    )
    progress_choices = (
        (20,20),
        (40,40),
        (50,50),
        (70,70),
        (90,90),
        (100,100),
    )

    pro_name= models.CharField(max_length=100)
    status =models.CharField(max_length=100 , choices= status_choices)
    realted_to = models.CharField(max_length=100)
    assigned_to = models.CharField(max_length=100)
    start_date = models.DateField()
    target_end_date = models.DateField()
    actual_end_date = models.DateField()
    opportunity_name = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100)
    budget = models.IntegerField()
    project_url = models.URLField()
    priority = models.CharField(max_length=100 , choices=priority_choices)
    progress = models.DecimalField(max_digits=100 ,decimal_places=2 ,choices=progress_choices)
    desc = models.TextField()


    def __str__(self):
        return self.pro_name

class AddTasks(models.Model):
    status_choices = (
        ('Started', 'Started'),
        ('New', 'New'),
        ('In Progress', 'In Progress'),
        ('Waiting for feedback', 'Waiting for feedback'),
        ('On hold', 'On hold'),
        ('Completed', 'Completed'),
        ('Delivered', 'Delivered'),
    )
    priority_choices = (
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    )
    progress_choices = (
        (20, 20),
        (40, 40),
        (50, 50),
        (70, 70),
        (90, 90),
        (100, 100),
    )
    task_name = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=status_choices)
    realted_to = models.CharField(max_length=100)
    assigned_to = models.CharField(max_length=100)
    milestone_name = models.CharField(max_length=100)
    priority = models.CharField(max_length=100, choices=priority_choices)
    workedHours = models.IntegerField()
    progress = models.DecimalField(max_digits=100, decimal_places=2, choices=progress_choices)
    start_date = models.DateField()
    end_date = models.DateField()
    desc = models.TextField()
    def str__(self):
        return self.task_name

class AddMilestone(models.Model):
    milestone_name = models.CharField(max_length=100)
    realted_to = models.CharField(max_length=100)
    assigned_to = models.CharField(max_length=100)
    milestone_date = models.DateField()
    desc = models.TextField()
    def str__(self):
        return self.milestone_name
class AddContact(models.Model):
    contact_type_choices = (
        ('Lead', 'Lead'),
        ('Customer', 'Customer'),
        ('Partner', 'Partner'),
        ('Analyst', 'Analyst'),
        ('Vendor', 'Vendor'),
    )
    portal_choices=(
        ('Yes' , 'Yes'),
    )
    country_choices=(
        ('INDIA','INDIA'),
        ('UNITED STATES','UNITED STATES'),
        ('CHINA','CHINA'),
        ('AUSTRALIA','AUSTRALIA'),
        ('FRANCE','FRANCE'),
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    primary_email = models.EmailField()
    office_phone = models.BigIntegerField()
    mobile_phone = models.BigIntegerField()
    home_phone = models.BigIntegerField()
    dob = models.DateField()
    organization = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    assigned_to = models.CharField(max_length=100)
    contact_type = models.CharField(max_length=100 , choices=contact_type_choices)
    language = models.CharField(max_length=100)
    reffered_by = models.CharField(max_length=100)
    SLA_name = models.CharField(max_length=100)
    portal_user = models.CharField(max_length=100, choices=portal_choices)
    support_start_date = models.DateField()
    support_end_date = models.DateField()
    country = models.CharField(max_length=100, choices=country_choices)
    street = models.TextField()
    postal_code=models.IntegerField()
    desc=models.TextField()
    imgg=models.FileField(upload_to='pictures/')

    linkedin_url=models.URLField()
    fb_url = models.URLField()
    def str__(self):
        return self.first_name

class AddOrganization(models.Model):
    country_choices1 = (
        ('INDIA', 'INDIA'),
        ('UNITED STATES', 'UNITED STATES'),
        ('RUSSIA','RUSSIA'),
        ('CHINA', 'CHINA'),
        ('AUSTRALIA', 'AUSTRALIA'),
        ('FRANCE', 'FRANCE'),
    )

    industry_choices=(
        ('Goverment','Goverment'),
        ('Transportation','Transportation'),
        ('Telecommunications','Telecommunications'),
        ('Utilities','Utilities'),
        ('Other','Other')
    )
    org_name = models.CharField(max_length=100)
    p_email = models.EmailField()
    website= models.URLField()
    p_phone = models.BigIntegerField()
    employees = models.IntegerField()
    industry = models.CharField(max_length=100,choices=industry_choices)
    revenue = models.IntegerField()
    ownership = models.CharField(max_length=100)
    SLA_name = models.CharField(max_length=100)
    assigned_to = models.CharField(max_length=100)
    sic_code = models.IntegerField()
    billing_country = models.CharField(max_length=100,choices=country_choices1)
    shipping_country = models.CharField(max_length=100, choices=country_choices1)
    billing_address = models.TextField()
    shipping_address = models.TextField()
    billing_postal_code = models.IntegerField()
    shipping_postal_code = models.IntegerField()
    desc = models.TextField()
    org_img = models.ImageField(upload_to='pictures')
    def str__(self):
        return self.org_name

class AddCompaign(models.Model):
    comp_type_choices = (
        ('Webinar','Webinar'),
        ('Trade Show','Trade Show'),
        ('Advertisement','Advertisement'),
        ('Public Relations','Public Relations'),
    )
    comp_status_choices = (
        ('Planning','Planning'),
        ('Queued','Queued'),
        ('In Progress','In Progress'),
        ('Completed','Completed'),
        ('Canceled','Canceled'),
    )
    response_choices = (
        ('Excellent','Excellent'),
        ('Good','Good'),
        ('Average','Average'),
        ('Poor','Poor'),
    )
    comp_name = models.CharField(max_length=100)
    close_date = models.DateField()
    product = models.CharField(max_length=100)
    assigned_to = models.CharField(max_length=100)
    comp_type = models.CharField(max_length=100,choices=comp_type_choices)
    comp_status = models.CharField(max_length=100,choices=comp_status_choices)
    audience = models.IntegerField()
    target_size = models.IntegerField()
    sponsor = models.CharField(max_length=100)
    numsent = models.IntegerField()
    budget = models.IntegerField()
    cost = models.IntegerField()
    revenue = models.IntegerField()
    response = models.CharField(max_length=100, choices=response_choices)
    sales_count = models.IntegerField()
    actual_sales_count = models.IntegerField()
    ROI = models.IntegerField()
    actual_ROI = models.IntegerField()
    desc = models.TextField()
    def str__(self):
        return self.comp_name

class AddOppurtunity(models.Model):
    pipeline_choices=(
        ('Standard','Standard'),
    )
    sales_stages_choices=(
        ('New','New'),
        ('Requirements Gathering','Requirements Gathering'),
        ('Value Proposition','Value Proposition'),
        ('Negotiation','Negotiation'),
        ('Ready to close','Ready to close'),
        ('Closed won','Closed won'),
    )
    lead_source_choices=(
        ('Cold Call','Cold Call'),
        ('Refferal','Refferal'),
        ('World of mouth','World of mouth'),
        ('Website','Website'),
        ('Existing customer','Existing customer'),
        ('Direct Mail','Direct Mail'),
        ('Facebook','Facebook')
    )
    type_b_choices=(
        ('Existing Business','Existing Business'),
        ('New Business','New Business'),
    )
    lost_reason_choices=(
        ('Price','Price'),
        ('Authority','Authority'),
        ('Timing','Timing'),
        ('Missing Feature','Missing Feature'),
        ('Usability','Usability'),
        ('No need','No need'),
    )

    oppo_name = models.CharField(max_length=100)
    amount = models.IntegerField()
    org_name = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100)
    close_date = models.DateField()
    pipeline = models.CharField(max_length=100 , choices=pipeline_choices)
    sales_stages = models.CharField(max_length=100,choices=sales_stages_choices)
    assigned_to = models.CharField(max_length=100)
    lead_source = models.CharField(max_length=100, choices=lead_source_choices)
    type_b = models.CharField(max_length=100 , choices=type_b_choices)
    probability = models.CharField(max_length=100)
    camp_source = models.CharField(max_length=100)
    revenue = models.IntegerField()
    p_mail= models.EmailField()
    lost_reason = models.CharField(max_length=100, choices=lost_reason_choices)
    desc = models.TextField()

class AddQuotes(models.Model):
    country_choices = (
        ('INDIA', 'INDIA'),
        ('UNITED STATES', 'UNITED STATES'),
        ('RUSSIA', 'RUSSIA'),
        ('CHINA', 'CHINA'),
        ('AUSTRALIA', 'AUSTRALIA'),
        ('FRANCE', 'FRANCE'),
    )
    csaf_choices = (
        ('Organization', 'Organization'),
        ('Related To', 'Related To'),
        ('Shipping Address', 'Shipping Address'),

    )
    carrier_choices = (
        ('FedEx', 'FedEx'),
        ('UPS', 'UPS'),
        ('USPS', 'USPS'),
        ('DHL', 'DHL'),
        ('BlueDart', 'BlueDart'),

    )
    quote_stage_choices = (
        ('New', 'New'),
        ('Reviewed', 'Reviewed'),
        ('Delivered', 'Delivered'),
        ('Accepted', 'Accepted'),
        ('Rejeted', 'Rejeted'),

    )

    subject = models.CharField(max_length=100)
    oppo_name = models.CharField(max_length=100)
    quote_stage = models.CharField(max_length=100 , choices=quote_stage_choices)
    valid_until= models.DateField()
    org_name = models.CharField(max_length=100)
    related_to =models.CharField(max_length=100)
    shipping = models.CharField(max_length=100)
    carrier =models.CharField(max_length=100,choices=carrier_choices)
    assigned_to = models.CharField(max_length=100)
    cbaf = models.CharField(max_length=100 , choices=csaf_choices)
    csaf = models.CharField(max_length=100 , choices=csaf_choices)
    billing_country = models.CharField(max_length=100 , choices=country_choices)
    shipping_country = models.CharField(max_length=100 , choices=country_choices)
    billing_address = models.CharField(max_length=100)
    shipping_address = models.CharField(max_length=100)
    billing_postal_code=models.IntegerField()
    shipping_postal_code=models.IntegerField()
    def str__(self):
        return self.subject
class AddProduct(models.Model):
    pro_active_choices = (
        ("Yes" , "Yes"),
        ("No" , "No"),
    )
    pro_cat_choices = (
        ("Hardware" , "Hardware"),
        ("Software" , "Software"),
        ("CRM Application" , "CRM Application"),
    )
    b_type_choices = (
        ('One Time',"One Time"),
        ("Subscription","Subscription"),
    )
    a = models.CharField(max_length=100)
    b = models.IntegerField()
    c = models.CharField(max_length=100 , choices=pro_active_choices)
    d = models.CharField(max_length=100 , choices=pro_cat_choices)
    e = models.CharField(max_length=100)
    f = models.CharField(max_length=100)
    g = models.DateField()
    h = models.DateField()
    i =models.DateField()
    j = models.DateField()
    k = models.IntegerField()
    l = models.IntegerField()
    m = models.IntegerField()
    n = models.URLField()
    o = models.IntegerField()
    p = models.IntegerField()
    q = models.IntegerField()
    r = models.IntegerField()
    s = models.IntegerField()
    t = models.IntegerField()
    u = models.CharField(max_length=100 , choices=b_type_choices)
    v= models.IntegerField()
    w = models.IntegerField()
    x = models.IntegerField()
    y = models.CharField(max_length=100)
    z = models.FileField(upload_to='media/', null=True,blank=True)
    A = models.TextField()
    def str__(self):
        return self.a
class AddService(models.Model):
    b_type_choices = (
        ('One Time', "One Time"),
        ("Subscription", "Subscription"),
    )
    pro_active_choices = (
        ("Yes", "Yes"),
        ("No", "No"),
    )
    cat_choices = (
        ("Installation","Installation"),
        ("Support","Support"),
        ("Customization","Customization"),
        ("Migration","Migration"),
        ("Training","Training"),
    )
    service_name = models.CharField(max_length=100)
    active = models.CharField(max_length=100, choices=pro_active_choices)
    cat = models.CharField(max_length=100, choices=cat_choices)
    owner = models.CharField(max_length=100)
    sale_date = models.DateField()
    sale_end_date = models.DateField()
    supp_date = models.DateField()
    supp_end_date = models.DateField()
    website = models.URLField()
    price = models.IntegerField()
    commission_rate = models.IntegerField()
    VAT = models.IntegerField()
    sale = models.IntegerField()
    service = models.IntegerField()
    p_cost = models.IntegerField()
    b_type = models.CharField(max_length=100, choices=b_type_choices)
    desc = models.TextField()
    def str__(self):
        return self.service_name

class AddInvoices(models.Model):
    status_choices=(
        ("Auto Created","Auto Created"),
        ("New","New"),
        ("Approved","Approved"),
        ("Partially Paid","Partially Paid"),
        ("Paid","Paid"),
    )
    country_choices = (
        ('INDIA', 'INDIA'),
        ('UNITED STATES', 'UNITED STATES'),
        ('RUSSIA', 'RUSSIA'),
        ('CHINA', 'CHINA'),
        ('AUSTRALIA', 'AUSTRALIA'),
        ('FRANCE', 'FRANCE'),
    )
    csaf_choices = (
        ('Organization', 'Organization'),
        ('Related To', 'Related To'),
        ('Shipping Address', 'Shipping Address'),

    )
    sub = models.CharField(max_length=100)
    org = models.CharField(max_length=100)
    in_date = models.DateField()
    due_date = models.DateField()
    contact = models.CharField(max_length=100)
    num = models.BigIntegerField()
    s_order = models.CharField(max_length=100)
    p_order = models.CharField(max_length=100)
    assigned_to = models.CharField(max_length=100)
    status = models.CharField(max_length=100 , choices=status_choices)
    s_duty = models.IntegerField()
    e_duty = models.IntegerField()
    oppo = models.CharField(max_length=100)
    pro = models.CharField(max_length=100)
    q_name = models.CharField(max_length=100)
    r_to = models.CharField(max_length=100)
    cbaf = models.CharField(max_length=100,choices=csaf_choices)
    csaf = models.CharField(max_length=100,choices=csaf_choices)
    bill_c = models.CharField(max_length=100,choices=country_choices)
    shipp_c = models.CharField(max_length=100,choices=country_choices)
    b_a = models.TextField()
    s_a = models.TextField()
    bpc = models.IntegerField()
    spc = models.IntegerField()
    desc = models.TextField()
    def str__(self):
        return self.sub
class AddSalesOrder(models.Model):
    carrier_choices = (
        ('FedEx', 'FedEx'),
        ('UPS', 'UPS'),
        ('USPS', 'USPS'),
        ('DHL', 'DHL'),
        ('BlueDart', 'BlueDart'),
    )
    csaf_choices = (
        ('Organization', 'Organization'),
        ('Related To', 'Related To'),
        ('Shipping Address', 'Shipping Address'),

    )
    country_choices1 = (
        ('INDIA', 'INDIA'),
        ('UNITED STATES', 'UNITED STATES'),
        ('RUSSIA', 'RUSSIA'),
        ('CHINA', 'CHINA'),
        ('AUSTRALIA', 'AUSTRALIA'),
        ('FRANCE', 'FRANCE'),
    )
    status_choices = (
        ('New', 'New'),
        ('Approved', 'Approved'),
        ('Fully Delivered', 'Fully Delivered'),
    )

    sub = models.CharField(max_length=100)
    oppo = models.CharField(max_length=100)
    q_name = models.CharField(max_length=100)
    p_order = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    org = models.CharField(max_length=100)
    assigned_to = models.CharField(max_length=100)
    status = models.CharField(max_length=100,choices=status_choices)
    s_duty = models.IntegerField()
    e_duty = models.IntegerField()
    cbaf = models.CharField(max_length=100,choices=csaf_choices)
    csaf = models.CharField(max_length=100,choices=csaf_choices)
    carrier = models.CharField(max_length=100,choices=carrier_choices)
    bill_c = models.CharField(max_length=100,choices=country_choices1)
    shipp_c = models.CharField(max_length=100,choices=country_choices1)
    bpc = models.IntegerField()
    spc = models.IntegerField()
    desc = models.TextField()
    def str__(self):
        return self.sub

class AddVendors(models.Model):
    country_choices1 = (
        ('INDIA', 'INDIA'),
        ('UNITED STATES', 'UNITED STATES'),
        ('RUSSIA', 'RUSSIA'),
        ('CHINA', 'CHINA'),
        ('AUSTRALIA', 'AUSTRALIA'),
        ('FRANCE', 'FRANCE'),
    )
    vendor = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    p_email = models.EmailField()
    website = models.URLField()
    ass_to = models.CharField(max_length=100)
    cat = models.CharField(max_length=100)
    country = models.CharField(max_length=100 , choices=country_choices1)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.IntegerField()
    desc = models.TextField()
    def str__(self):
        return self.vendor
class AddPurchaseOrder(models.Model):
    country_choices1 = (
        ('INDIA', 'INDIA'),
        ('UNITED STATES', 'UNITED STATES'),
        ('RUSSIA', 'RUSSIA'),
        ('CHINA', 'CHINA'),
        ('AUSTRALIA', 'AUSTRALIA'),
        ('FRANCE', 'FRANCE'),
    )
    carrier_choices = (
        ('FedEx', 'FedEx'),
        ('UPS', 'UPS'),
        ('USPS', 'USPS'),
        ('DHL', 'DHL'),
        ('BlueDart', 'BlueDart'),

    )
    status_choices = (
        ('New', 'New'),
        ('Approved', 'Approved'),
        ('Fully Received', 'Fully Received'),
        ('Canceled' ,'Canceled' ),
    )
    sub = models.CharField(max_length=100)
    vendor = models.CharField(max_length=100)
    status = models.CharField(max_length=100,choices=status_choices)
    req_num = models.IntegerField()
    contact = models.CharField(max_length=100)
    date=models.DateField()
    commission =models.IntegerField()
    e_duty = models.IntegerField()
    carrier = models.CharField(max_length=100,choices=carrier_choices)
    tracking_num= models.IntegerField()
    ass_to = models.CharField(max_length=100)
    org = models.CharField(max_length=100)
    bill_c = models.CharField(max_length=100,choices=country_choices1)
    shipp_c = models.CharField(max_length=100,choices=country_choices1)
    b_a = models.TextField()
    s_a = models.TextField()
    b_postal_code = models.IntegerField()
    s_postal_code = models.IntegerField()
    desc = models.TextField()
    def str__(self):
        return self.sub
class AddCase(models.Model):
    status_choices = (
        ('New', 'New'),
        ('Assigned', 'Assigned'),
        ('Resolved', 'Resolved'),
        ('Waiting', 'Waiting'),
    )
    priority_choices = (
        ('Urgent' , 'Urgent'),
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    )
    channel_choices=(
        ('Email','Email'),
        ('Phone' , 'Phone'),
        ('Webform' , 'Webform'),

    )
    summ = models.TextField()
    c_t = models.CharField(max_length=100)
    status = models.CharField(max_length=100,choices=status_choices)
    pri = models.CharField(max_length=100,choices=priority_choices)
    contact = models.CharField(max_length=100)
    ass_to = models.CharField(max_length=100)
    channel = models.CharField(max_length=100 , choices=channel_choices)
    p_name = models.CharField(max_length=100)
    group = models.CharField(max_length=100)
    res = models.TextField()
    cat = models.CharField(max_length=100)
    date1 = models.DateField()
    sla = models.CharField(max_length=100)
    def str__(self):
        return self.summ
class AddServiceContract(models.Model):
    priority_choices = (
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    )
    status_choices = (
        ('Started', 'Started'),
        ('New', 'New'),
        ('In Progress', 'In Progress'),
        ('Waiting for feedback', 'Waiting for feedback'),
        ('On hold', 'On hold'),
        ('Completed', 'Completed'),
    )
    type_choices = (
        ('Support','Support'),
        ('Services','Services'),
        ('Administrative','Administrative'),
    )
    tu_choices=(
        ('Hours','Hours'),
        ('Days','Days'),
        ('Incidents','Incidents'),
    )


    sub = models.CharField(max_length=100)
    type = models.CharField(max_length=100 , choices=type_choices)
    pri = models.CharField(max_length=100,choices=priority_choices)
    status = models.CharField(max_length=100,choices=status_choices)
    tu = models.CharField(max_length=100,choices=tu_choices)
    uu = models.IntegerField()
    total = models.IntegerField()
    s_d = models.DateField()
    e_d = models.DateField()
    contact = models.CharField(max_length=100)
    def str__(self):
        return self.sub
class AddInternalTicket(models.Model):
    status_choices = (
        ('New', 'New'),
        ('Assigned', 'Assigned'),
        ('Resolved', 'Resolved'),
        ('Waiting', 'Waiting'),
    )
    priority_choices = (
        ('Urgent', 'Urgent'),
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    )
    channel_choices = (
        ('Email', 'Email'),
        ('Phone', 'Phone'),
        ('Webform', 'Webform'),

    )
    summ = models.TextField()
    i_t = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=status_choices)
    pri = models.CharField(max_length=100, choices=priority_choices)
    p_name = models.CharField(max_length=100)
    ass_to = models.CharField(max_length=100)
    channel = models.CharField(max_length=100, choices=channel_choices)
    res = models.TextField()
    mail = models.EmailField()
    date1 = models.DateField()
    sla = models.CharField(max_length=100)

    def str__(self):
        return self.summ
class AddWorkOrder(models.Model):
    status_choices = (
        ('New', 'New'),
        ('Assigned', 'Assigned'),
        ('Resolved', 'Resolved'),
        ('Waiting', 'Waiting'),
    )
    priority_choices = (
        ('Urgent', 'Urgent'),
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    )
    loc_choices=(
        ('Onsite','Onsite'),
        ('Remote' , 'Remote'),
    )
    sub = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=status_choices)
    org = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    pri = models.CharField(max_length=100, choices=priority_choices)
    service = models.CharField(max_length=100)
    work_desc = models.TextField()
    type = models.CharField(max_length=100)
    loc = models.CharField(max_length=100,choices=loc_choices)
    loc1 = models.TextField()
    s_d = models.DateField()
    t_c = models.TextField()
    def str__(self):
        return self.sub
class AddOurSite(models.Model):
    b_n = models.CharField(max_length=100)
    b_u = models.URLField()
    def str__(self):
        return self.b_n
class AddEmployee(models.Model):
    country_choices1 = (
        ('INDIA', 'INDIA'),
        ('UNITED STATES', 'UNITED STATES'),
        ('RUSSIA', 'RUSSIA'),
        ('CHINA', 'CHINA'),
        ('AUSTRALIA', 'AUSTRALIA'),
        ('FRANCE', 'FRANCE'),
    )
    b_hours_choices = (
        ('Standard Business Hours - Asia/Kolkata','Standard Business Hours - Asia/Kolkata'),
    )
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    mail = models.EmailField()
    lang = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    dep = models.CharField(max_length=100)
    off_phone = models.BigIntegerField()
    mob = models.BigIntegerField()
    b_hours = models.CharField(max_length=100 ,choices=b_hours_choices)
    region = models.CharField(max_length=100)
    country = models.CharField(max_length=100, choices=country_choices1)
    address = models.TextField()
    pincode = models.IntegerField()
    pic = models.FileField(upload_to='media/' , null=True,blank=True)

    def str__(self):
        return self.f_name

class AddTemplate(models.Model):
    m_choices=(
        ('Compaign','Compaign'),
        ('Cases','Cases'),
        ('Employees','Employees'),
        ('Service Contacts','Service Contacts'),
        ('Sales Order','Sales Order'),
        ('Vendors','Vendors'),
        ('Services','Services'),
        ('Quotes','Quotes'),
        ('Work Orders','Work Orders'),
    )
    t = models.CharField(max_length=100)
    m = models.CharField(max_length=100,choices=m_choices)
    desc = models.TextField()
    d_t = models.CharField(max_length=100)
    a = models.CharField(max_length=100)
    def str__(self):
        return self.t
































