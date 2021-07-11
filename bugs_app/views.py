from django.shortcuts import render, redirect, reverse
from .models import Bug
from projects_app.models import Project
from .forms import AddBugForm
from .mail import send_email

def list_bugs(request,id):
    query_bugs = Bug.objects.filter(project_id=id)
    project = Project.objects.filter(id = id)[0]

    context = {
        'bugs_list': query_bugs,
        'project': project
    }
    return render(request, 'bugs_app/bugs.html', context)

def bug_add(request,project_id):
    form = AddBugForm()
    if request.method == "POST":
        form = AddBugForm(request.POST)
        if form.is_valid():
            project = Project.objects.filter(id=project_id)[0]
            bug = form.save(commit = False)
            bug.project_id = project
            bug.save()
            send_email("raziyazohra@gmail.com","Aditya123@",bug.developer_email,f"New bug assigned to you developer!!",f"Hey {bug.developer},\nThe bug \"{bug.name}\" of project \"{bug.project_id}\" was created on {bug.created_date} and is assigned to you.More specifically the bug is: \n \" {bug.desc} \"  ")
            a = reverse('bug_list', args=[project_id])
            
            return redirect(a)
            
    context = {
        'form': form
    }

    return render(request,'bugs_app/addbugs.html', context)

def bug_delete(request,project_id,bug_id):
    project = Project.objects.filter(id = project_id)[0]
    bug = Bug.objects.filter(project_id = project,id = bug_id)[0]
    bug.delete()
    return redirect(reverse('bug_list', args=[project_id]))

def bug_resolve(request,project_id,bug_id):
    project = Project.objects.filter(id = project_id)[0]
    bug = Bug.objects.filter(project_id = project,id = bug_id)[0]
    bug.state="Resolved"
    bug.save()
    return redirect(reverse('bug_list', args=[project_id]))