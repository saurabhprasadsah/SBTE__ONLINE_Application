# Generated by Django 4.1.2 on 2022-11-10 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminpanel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseRegistrationOld',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('version', models.BigIntegerField()),
                ('code', models.CharField(max_length=255)),
                ('is_deleted', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('registration_old_id', models.BigIntegerField()),
                ('type', models.CharField(max_length=255)),
                ('is_scrutiny', models.IntegerField()),
                ('is_verified', models.IntegerField()),
            ],
            options={
                'db_table': 'course_registration_old',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Exams',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('academic_term', models.CharField(max_length=255)),
                ('exam_held', models.CharField(blank=True, max_length=255, null=True)),
                ('is_current', models.TextField()),
                ('term', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'exams',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FeeStructure',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('date_over', models.DateTimeField()),
                ('due_date', models.DateTimeField()),
                ('fee', models.DecimalField(decimal_places=2, max_digits=7)),
                ('fee_type', models.CharField(blank=True, max_length=255, null=True)),
                ('is_deleted', models.TextField()),
                ('late_fee', models.DecimalField(decimal_places=2, max_digits=7)),
                ('max_fee', models.DecimalField(decimal_places=2, max_digits=7)),
                ('remarks', models.CharField(blank=True, max_length=255, null=True)),
                ('term', models.IntegerField()),
                ('academic_term', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'fee_structure',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FilePath',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('path', models.CharField(max_length=255)),
                ('row_page', models.IntegerField()),
                ('type', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'db_table': 'file_path',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OldMarks',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('version', models.BigIntegerField()),
                ('is_absent', models.IntegerField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
                ('marks1', models.IntegerField(blank=True, null=True)),
                ('marks2', models.IntegerField(blank=True, null=True)),
                ('marks_obtained', models.IntegerField(blank=True, null=True)),
                ('old_task_id', models.BigIntegerField()),
                ('remarks', models.CharField(blank=True, max_length=255, null=True)),
                ('roll_number', models.CharField(max_length=20)),
                ('student_id', models.BigIntegerField()),
                ('updated_by', models.CharField(blank=True, max_length=255, null=True)),
                ('is_absent1', models.IntegerField()),
                ('is_absent2', models.IntegerField()),
            ],
            options={
                'db_table': 'old_marks',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OldTask',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('version', models.BigIntegerField()),
                ('academic_term', models.CharField(max_length=255)),
                ('compiler_id', models.BigIntegerField(blank=True, null=True)),
                ('course_title', models.CharField(max_length=255)),
                ('institute_id', models.BigIntegerField()),
                ('is_compiled', models.IntegerField()),
                ('is_deleted', models.TextField()),
                ('is_finalized', models.IntegerField()),
                ('is_opr1finalized', models.IntegerField()),
                ('is_opr2finalized', models.IntegerField()),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
                ('max_marks', models.IntegerField()),
                ('operator1_id', models.BigIntegerField(blank=True, null=True)),
                ('operator2_id', models.BigIntegerField(blank=True, null=True)),
                ('program_id', models.BigIntegerField()),
                ('student_count', models.IntegerField()),
                ('term', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('updated_by', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'old_task',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Paymentordertbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentid', models.BigIntegerField()),
                ('order_number', models.CharField(db_column='Order_Number', max_length=50)),
                ('rollno', models.CharField(db_column='RollNo', max_length=50)),
                ('payamount', models.CharField(db_column='PayAmount', max_length=10)),
                ('ordercreationdate', models.CharField(db_column='OrderCreationDate', max_length=10)),
                ('paymentstatus', models.CharField(blank=True, db_column='PaymentStatus', max_length=255, null=True)),
                ('tran_datetime', models.CharField(blank=True, db_column='Tran_datetime', max_length=100, null=True)),
            ],
            options={
                'db_table': 'PaymentOrderTbl',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PaymentReturnencdata',
            fields=[
                ('encid', models.AutoField(db_column='encID', primary_key=True, serialize=False)),
                ('merchantordernumber', models.CharField(db_column='MerchantOrderNumber', max_length=45, unique=True)),
                ('sbiepayrefid', models.CharField(blank=True, db_column='SBIePayRefID', max_length=45, null=True)),
                ('transactionstatus', models.CharField(blank=True, db_column='TransactionStatus', max_length=45, null=True)),
                ('paidamount', models.CharField(blank=True, db_column='PaidAmount', max_length=45, null=True)),
                ('merchantcurrency', models.CharField(blank=True, db_column='MerchantCurrency', max_length=45, null=True)),
                ('paymode', models.CharField(blank=True, db_column='Paymode', max_length=45, null=True)),
                ('otherdetails', models.CharField(blank=True, db_column='OtherDetails', max_length=100, null=True)),
                ('reason_message', models.CharField(blank=True, db_column='Reason_Message', max_length=45, null=True)),
                ('bank_code', models.CharField(blank=True, db_column='Bank_Code', max_length=45, null=True)),
                ('bank_reference_number', models.CharField(blank=True, db_column='Bank_Reference_Number', max_length=45, null=True)),
                ('transaction_date', models.CharField(blank=True, db_column='Transaction_Date', max_length=45, null=True)),
                ('transaction_country', models.CharField(blank=True, db_column='Transaction_Country', max_length=45, null=True)),
                ('cin', models.CharField(blank=True, db_column='CIN', max_length=45, null=True)),
                ('merchantid', models.CharField(blank=True, db_column='MerchantID', max_length=45, null=True)),
                ('total_fee_gst', models.CharField(blank=True, db_column='Total_Fee_GST', max_length=45, null=True)),
                ('operatingmode', models.CharField(blank=True, db_column='OperatingMode', max_length=45, null=True)),
                ('merchantcountry', models.CharField(blank=True, db_column='MerchantCountry', max_length=45, null=True)),
                ('aggregatorid', models.CharField(blank=True, db_column='AggregatorID', max_length=45, null=True)),
                ('merchantcustomerid', models.CharField(blank=True, db_column='MerchantCustomerID', max_length=45, null=True)),
                ('accessmedium', models.CharField(blank=True, db_column='AccessMedium', max_length=45, null=True)),
                ('transactionsource', models.CharField(blank=True, db_column='TransactionSource', max_length=45, null=True)),
                ('ref1', models.CharField(blank=True, db_column='Ref1', max_length=45, null=True)),
                ('ref2', models.CharField(blank=True, db_column='Ref2', max_length=45, null=True)),
                ('ref3', models.CharField(blank=True, db_column='Ref3', max_length=45, null=True)),
                ('ref4', models.CharField(blank=True, db_column='Ref4', max_length=45, null=True)),
                ('ref5', models.CharField(blank=True, db_column='Ref5', max_length=45, null=True)),
                ('ref6', models.CharField(blank=True, db_column='Ref6', max_length=45, null=True)),
                ('ref7', models.CharField(blank=True, db_column='Ref7', max_length=45, null=True)),
                ('ref8', models.CharField(blank=True, db_column='Ref8', max_length=45, null=True)),
                ('ref9', models.CharField(blank=True, db_column='Ref9', max_length=45, null=True)),
                ('updatedby', models.CharField(blank=True, db_column='UpdatedBy', max_length=45, null=True)),
            ],
            options={
                'db_table': 'Payment_ReturnEncData',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RegistrationOld',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('version', models.BigIntegerField()),
                ('academic_term', models.CharField(max_length=255)),
                ('form_amount', models.FloatField(blank=True, null=True)),
                ('form_date', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.IntegerField()),
                ('is_form_filled', models.IntegerField()),
                ('is_form_verified', models.IntegerField()),
                ('is_online_form_filled', models.IntegerField()),
                ('is_repeat_registration', models.IntegerField()),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
                ('registration_code', models.CharField(max_length=255)),
                ('remarks', models.CharField(blank=True, max_length=255, null=True)),
                ('roll_number', models.CharField(max_length=255)),
                ('student_id', models.BigIntegerField()),
                ('updated_by', models.CharField(blank=True, max_length=255, null=True)),
                ('valid_till', models.DateTimeField(blank=True, null=True)),
                ('scrutiny_amount', models.FloatField(blank=True, null=True)),
                ('scrutiny_date', models.DateTimeField(blank=True, null=True)),
                ('scrutiny_verified_date', models.DateTimeField(blank=True, null=True)),
                ('is_scrutiny_verified', models.IntegerField()),
                ('is_individual', models.IntegerField()),
            ],
            options={
                'db_table': 'registration_old',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RoleView',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created_by', models.CharField(blank=True, max_length=255, null=True)),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.TextField()),
                ('modified_by', models.CharField(blank=True, max_length=255, null=True)),
                ('modified_date', models.DateTimeField(blank=True, null=True)),
                ('remarks', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'role_view',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('created_by', models.CharField(blank=True, max_length=255, null=True)),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.TextField()),
                ('modified_by', models.CharField(blank=True, max_length=255, null=True)),
                ('modified_date', models.DateTimeField(blank=True, null=True)),
                ('remarks', models.CharField(blank=True, max_length=255, null=True)),
                ('bcece', models.BigIntegerField(blank=True, null=True)),
                ('dob', models.DateField()),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('institute', models.BigIntegerField(blank=True, null=True)),
                ('mobile', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=255)),
                ('student', models.BigIntegerField(blank=True, null=True)),
                ('username', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Admin',
        ),
        migrations.DeleteModel(
            name='AuthGroup',
        ),
        migrations.DeleteModel(
            name='AuthGroupPermissions',
        ),
        migrations.DeleteModel(
            name='AuthPermission',
        ),
        migrations.DeleteModel(
            name='AuthUser',
        ),
        migrations.DeleteModel(
            name='AuthUserGroups',
        ),
        migrations.DeleteModel(
            name='AuthUserUserPermissions',
        ),
        migrations.DeleteModel(
            name='Bcece',
        ),
        migrations.DeleteModel(
            name='DjangoAdminLog',
        ),
        migrations.DeleteModel(
            name='DjangoContentType',
        ),
        migrations.DeleteModel(
            name='DjangoMigrations',
        ),
        migrations.DeleteModel(
            name='DjangoSession',
        ),
        migrations.DeleteModel(
            name='SeatApproval',
        ),
    ]
