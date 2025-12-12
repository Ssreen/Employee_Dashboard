from django.shortcuts import get_object_or_404, render


from employee.models import employee
from django.http import Http404, HttpResponse

# Create your views here.
def Employee_detail(request,pk):
    Employee= get_object_or_404(employee, pk=pk)
    context={
        'Employee':Employee,
    }
    return render(request,'Employee_detail.html',context)


