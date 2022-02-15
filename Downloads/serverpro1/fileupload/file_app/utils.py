from django.db import transaction

@transaction.atomic
def bulk_emp_creation(emp_list):
    # Loop over each store and invoke save() on each entry
    for emp in emp_list:
        # save() method called on each member to create record
        emp.save()