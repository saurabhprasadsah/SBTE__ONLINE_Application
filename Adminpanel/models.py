# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Paymentordertbl(models.Model):
    studentid = models.BigIntegerField()
    order_number = models.CharField(db_column='Order_Number', max_length=50)  # Field name made lowercase.
    rollno = models.CharField(db_column='RollNo', max_length=50)  # Field name made lowercase.
    payamount = models.CharField(db_column='PayAmount', max_length=10)  # Field name made lowercase.
    ordercreationdate = models.CharField(db_column='OrderCreationDate', max_length=10)  # Field name made lowercase.
    paymentstatus = models.CharField(db_column='PaymentStatus', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tran_datetime = models.CharField(db_column='Tran_datetime', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PaymentOrderTbl'
        unique_together = (('id', 'studentid'),)


class PaymentReturnencdata(models.Model):
    encid = models.AutoField(db_column='encID', primary_key=True)  # Field name made lowercase.
    merchantordernumber = models.CharField(db_column='MerchantOrderNumber', unique=True, max_length=45)  # Field name made lowercase.
    sbiepayrefid = models.CharField(db_column='SBIePayRefID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    transactionstatus = models.CharField(db_column='TransactionStatus', max_length=45, blank=True, null=True)  # Field name made lowercase.
    paidamount = models.CharField(db_column='PaidAmount', max_length=45, blank=True, null=True)  # Field name made lowercase.
    merchantcurrency = models.CharField(db_column='MerchantCurrency', max_length=45, blank=True, null=True)  # Field name made lowercase.
    paymode = models.CharField(db_column='Paymode', max_length=45, blank=True, null=True)  # Field name made lowercase.
    otherdetails = models.CharField(db_column='OtherDetails', max_length=100, blank=True, null=True)  # Field name made lowercase.
    reason_message = models.CharField(db_column='Reason_Message', max_length=45, blank=True, null=True)  # Field name made lowercase.
    bank_code = models.CharField(db_column='Bank_Code', max_length=45, blank=True, null=True)  # Field name made lowercase.
    bank_reference_number = models.CharField(db_column='Bank_Reference_Number', max_length=45, blank=True, null=True)  # Field name made lowercase.
    transaction_date = models.CharField(db_column='Transaction_Date', max_length=45, blank=True, null=True)  # Field name made lowercase.
    transaction_country = models.CharField(db_column='Transaction_Country', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cin = models.CharField(db_column='CIN', max_length=45, blank=True, null=True)  # Field name made lowercase.
    merchantid = models.CharField(db_column='MerchantID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    total_fee_gst = models.CharField(db_column='Total_Fee_GST', max_length=45, blank=True, null=True)  # Field name made lowercase.
    operatingmode = models.CharField(db_column='OperatingMode', max_length=45, blank=True, null=True)  # Field name made lowercase.
    merchantcountry = models.CharField(db_column='MerchantCountry', max_length=45, blank=True, null=True)  # Field name made lowercase.
    aggregatorid = models.CharField(db_column='AggregatorID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    merchantcustomerid = models.CharField(db_column='MerchantCustomerID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    accessmedium = models.CharField(db_column='AccessMedium', max_length=45, blank=True, null=True)  # Field name made lowercase.
    transactionsource = models.CharField(db_column='TransactionSource', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ref1 = models.CharField(db_column='Ref1', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ref2 = models.CharField(db_column='Ref2', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ref3 = models.CharField(db_column='Ref3', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ref4 = models.CharField(db_column='Ref4', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ref5 = models.CharField(db_column='Ref5', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ref6 = models.CharField(db_column='Ref6', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ref7 = models.CharField(db_column='Ref7', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ref8 = models.CharField(db_column='Ref8', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ref9 = models.CharField(db_column='Ref9', max_length=45, blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Payment_ReturnEncData'


class AcademicSession(models.Model):
    id = models.BigAutoField(primary_key=True)
    for_le = models.TextField()  # This field type is a guess.
    is_current = models.TextField()  # This field type is a guess.
    is_deleted = models.TextField()  # This field type is a guess.
    name = models.CharField(unique=True, max_length=255)
    remarks = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'academic_session'


class CourseRegistrationOld(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    code = models.CharField(max_length=255)
    is_deleted = models.IntegerField()
    name = models.CharField(max_length=255)
    registration_old_id = models.BigIntegerField()
    type = models.CharField(max_length=255)
    is_scrutiny = models.IntegerField()
    is_verified = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'course_registration_old'


class Exams(models.Model):
    id = models.BigAutoField(primary_key=True)
    academic_term = models.CharField(max_length=255)
    exam_held = models.CharField(max_length=255, blank=True, null=True)
    is_current = models.TextField()  # This field type is a guess.
    term = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exams'


class FeeStructure(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_over = models.DateTimeField()
    due_date = models.DateTimeField()
    fee = models.DecimalField(max_digits=7, decimal_places=2)
    fee_type = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.TextField()  # This field type is a guess.
    late_fee = models.DecimalField(max_digits=7, decimal_places=2)
    max_fee = models.DecimalField(max_digits=7, decimal_places=2)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    term = models.IntegerField()
    academic_term = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fee_structure'


class FilePath(models.Model):
    id = models.BigAutoField(primary_key=True)
    path = models.CharField(max_length=255)
    row_page = models.IntegerField()
    type = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'file_path'


class Institute(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(unique=True, max_length=255)
    is_deleted = models.TextField()  # This field type is a guess.
    name = models.CharField(unique=True, max_length=255)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    short_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'institute'



class OldMarks(models.Model):
    id = models.BigIntegerField(primary_key=True) # here i have added primary_key = True
    version = models.BigIntegerField()
    is_absent = models.IntegerField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    marks1 = models.IntegerField(blank=True, null=True)
    marks2 = models.IntegerField(blank=True, null=True)
    marks_obtained = models.IntegerField(blank=True, null=True)
    old_task_id = models.BigIntegerField()
    remarks = models.CharField(max_length=255, blank=True, null=True)
    roll_number = models.CharField(max_length=20)
    student_id = models.BigIntegerField()
    updated_by = models.CharField(max_length=255, blank=True, null=True)
    is_absent1 = models.IntegerField()
    is_absent2 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'old_marks'


class OldTask(models.Model):
    id = models.BigIntegerField(primary_key=True) # here i have added primary_key = True
    version = models.BigIntegerField()
    academic_term = models.CharField(max_length=255)
    compiler_id = models.BigIntegerField(blank=True, null=True)
    course_title = models.CharField(max_length=255)
    institute_id = models.BigIntegerField()
    is_compiled = models.IntegerField()
    is_deleted = models.TextField()  # This field type is a guess.
    is_finalized = models.IntegerField()
    is_opr1finalized = models.IntegerField()
    is_opr2finalized = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    max_marks = models.IntegerField()
    operator1_id = models.BigIntegerField(blank=True, null=True)
    operator2_id = models.BigIntegerField(blank=True, null=True)
    program_id = models.BigIntegerField()
    student_count = models.IntegerField()
    term = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    updated_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'old_task'


class Program(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(unique=True, max_length=255)
    is_deleted = models.TextField()  # This field type is a guess.
    name = models.CharField(unique=True, max_length=255)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    short_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'program'


class RegistrationOld(models.Model):
    id = models.BigIntegerField(primary_key=True) # here i have added primary_key = True
    version = models.BigIntegerField()
    academic_term = models.CharField(max_length=255)
    form_amount = models.FloatField(blank=True, null=True)
    form_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    is_form_filled = models.IntegerField()
    is_form_verified = models.IntegerField()
    is_online_form_filled = models.IntegerField()
    is_repeat_registration = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    registration_code = models.CharField(max_length=255)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    roll_number = models.CharField(max_length=255)
    student_id = models.BigIntegerField()
    updated_by = models.CharField(max_length=255, blank=True, null=True)
    valid_till = models.DateTimeField(blank=True, null=True)
    scrutiny_amount = models.FloatField(blank=True, null=True)
    scrutiny_date = models.DateTimeField(blank=True, null=True)
    scrutiny_verified_date = models.DateTimeField(blank=True, null=True)
    is_scrutiny_verified = models.IntegerField()
    is_individual = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'registration_old'


class RoleView(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_by = models.CharField(max_length=255, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.TextField()  # This field type is a guess.
    modified_by = models.CharField(max_length=255, blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'role_view'


class Student(models.Model):
    id = models.BigIntegerField(primary_key=True) # here i have added primary_key = True
    created_by = models.CharField(max_length=255, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.TextField()  # This field type is a guess.
    modified_by = models.CharField(max_length=255, blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    aadhar_number = models.CharField(max_length=255, blank=True, null=True)
    admission_type = models.CharField(max_length=255, blank=True, null=True)
    bcece = models.BigIntegerField(blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    category_admission = models.CharField(max_length=255, blank=True, null=True)
    class_roll_no = models.BigIntegerField(blank=True, null=True)
    comm_city = models.CharField(max_length=255, blank=True, null=True)
    comm_country = models.CharField(max_length=255, blank=True, null=True)
    comm_line1 = models.CharField(max_length=255, blank=True, null=True)
    comm_line2 = models.CharField(max_length=255, blank=True, null=True)
    comm_pin = models.CharField(max_length=6, blank=True, null=True)
    comm_state = models.CharField(max_length=255, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    doj = models.DateField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    father_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    is_iti = models.TextField(blank=True, null=True)  # This field type is a guess.
    is_rec = models.TextField()  # This field type is a guess.
    last_name = models.CharField(max_length=255, blank=True, null=True)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    mobile_no = models.CharField(max_length=255, blank=True, null=True)
    mother_name = models.CharField(max_length=255, blank=True, null=True)
    perm_city = models.CharField(max_length=255, blank=True, null=True)
    perm_country = models.CharField(max_length=255, blank=True, null=True)
    perm_line1 = models.CharField(max_length=255, blank=True, null=True)
    perm_line2 = models.CharField(max_length=255, blank=True, null=True)
    perm_pin = models.CharField(max_length=6, blank=True, null=True)
    perm_state = models.CharField(max_length=255, blank=True, null=True)
    reg_amount = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    reg_no = models.BigIntegerField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    student_name = models.CharField(max_length=255, blank=False, null=False)
    academic_session = models.BigIntegerField(blank=True, null=True)
    institute = models.BigIntegerField()
    program = models.BigIntegerField()
    is_issued = models.TextField(blank=True, null=True)  # This field type is a guess.
    is_provisional = models.TextField(blank=True, null=True)  # This field type is a guess.
    is_registered = models.IntegerField(blank=True, null=True)
    is_provisnal = models.TextField()  # This field type is a guess.
    is_new = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'student'


class User(models.Model):
    id = models.BigIntegerField(primary_key=True) # here i have added primary_key = True
    created_by = models.CharField(max_length=255, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.TextField()  # This field type is a guess.
    modified_by = models.CharField(max_length=255, blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    bcece = models.BigIntegerField(blank=True, null=True)
    dob = models.DateField()
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    institute = models.BigIntegerField(blank=True, null=True)
    mobile = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    student = models.BigIntegerField(blank=True, null=True)
    username = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'user'
