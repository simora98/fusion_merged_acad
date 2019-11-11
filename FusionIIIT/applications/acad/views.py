import json
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.views.generic import TemplateView
from .models import BatchSemester,Course,CurriculumCourse,CurriculumInstructor,BtechCurriculum,Constants,MtechCurriculum,MtechSemester
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.db import transaction

# Create your views here.

# class Homepage(TemplateView):
#     template_name = 'home.html'



def homepage(request):
    return render(request,'home.html')

def get_course_list(request):
    obj = Course.objects.all()
    print(obj)
    context ={'course_list':obj}
    return context

def add_course(request):
    course_name = request.POST.get('course_name')
    course_detail = request.POST.get('course_detail')
    # print(course_name,course_detail)
    courses = Course.objects.create(course_name=course_name,course_details=course_detail)
    obj = get_course_list(request)
    # print(obj)

    # if obj :
    #     data = render_to_string('acad/add_semester_response.html',
    #                             {'obj':obj,
    #                             'programme' : programme,
    #                             'batch' : batch,
    #                             'sem' :8
    #                             }, request)
    #     obj = json.dumps({'html' : data, 'msg' : 'obj found', 'done' : True})
    #     return HttpResponse(obj, content_type = 'application/json')
    # else :
    #     return JsonResponse({"success": True, "msg": "No Course available.",'done' : False })
    #


    try:
        print("one")
        data = render_to_string('acad/view_course.html',{'course_list':obj},
                                 request)
        print("abcd")
        obj = json.dumps({'d':data})
        print("gscdgascdbscabdfcasbfcdnabcfb")
        return HttpResponse(obj, content_type = 'application/json')
    except:
        return HttpResponse("fghjk")



def view_courses(request):
    obj = Course.objects.all()
    if obj :
        data = render_to_string('acad/view_course.html',
                                {'obj':obj
                                }, request)
        obj = json.dumps({'html' : data, 'msg' : 'obj found', 'done' : True})
        return HttpResponse(obj, content_type = 'application/json')
    else :
        return JsonResponse({"success": True, "msg": "No Course available.",'done' : False })



# def get_courses(request):
#     return render(request,'acad/view_course.html',get_course_list(request))
# Select Programme to add curriculum

def programme(request):
    return render(request,'completedmenutest.html')

def selectProgramme(request):
    programme = request.POST.get('programme')
    # print(programme)
    try:
        data = render_to_string('add_curriculum.html',{'programme':programme},
                                 request)
        # print("abcd")
        obj = json.dumps({'d' : data})
        # print("gscdgascdbscabdfcasbfcdnabcfb")
        return HttpResponse(obj, content_type = 'application/json')
    except:
        return HttpResponse("fghjk")


def add_btech_curriculum(request):
    print("dfsfds")
    programme_ = request.POST.get('programme')
    batch =request.POST.get('batch')
    professional_core_credit =request.POST.get('prof_core_credit')
    professional_elective_credit = request.POST.get('prof_elective_credit')
    professional_project_credit = request.POST.get('prof_project_credit')
    professional_lab_credit = request.POST.get('prof_lab_credit')
    Core_engineering_science_credit = request.POST.get('core_engineering_science_credit')
    Core_natural_science_credit = request.POST.get('core_natural_science_credit')
    Core_humanities_credit = request.POST.get('core_humanities_credit')
    Core_design_credit = request.POST.get('core_design_credit')
    Core_manufacturing_credit = request.POST.get('core_manufacturing_credit')
    Core_management_science_credit = request.POST.get('core_management_science_credit')
    pbi = request.POST.get('pbi')
    pr =request.POST.get('pr')

    print(programme_,batch,pbi,pr)
    btech_curr = BtechCurriculum.objects.create(
    programme=programme_,
    batch=batch,
    professional_core_credit=professional_core_credit,
    professional_elective_credit=professional_elective_credit,
    professional_project_credit=professional_project_credit,
    professional_lab_credit=professional_lab_credit,
    Core_engineering_science_credit=Core_engineering_science_credit,
    Core_natural_science_credit=Core_natural_science_credit,
    Core_humanities_credit=Core_humanities_credit,
    Core_design_credit=Core_design_credit,
    Core_manufacturing_credit=Core_manufacturing_credit,
    Core_management_science_credit=Core_management_science_credit,
    pbi=pbi,
    pr=pr)
    print(btech_curr)

    try:
        data = render_to_string('semester.html',{'btech':btech_curr},
                                 request)
        print("abcd")
        obj = json.dumps({'d' : data})
        print("gscdgascdbscabdfcasbfcdnabcfb")
        return HttpResponse(obj, content_type = 'application/json')
    except:
        return HttpResponse("fghjk")


def select_semester(request):
    semester = request.POST.get('sem')
    programme = request.POST.get('programme')
    batch = request.POST.get('batch')
    try:
        data = render_to_string('add_batch_semester.html',{'semester':semester,'batch':batch,'programme':programme},
                                 request)
        print("Sem Selected")
        obj = json.dumps({'d' : data})
        # print("gscdgascdbscabdfcasbfcdnabcfb")
        return HttpResponse(obj, content_type = 'application/json')
    except:
        return HttpResponse("fghjk")

# def add_btech_curriculum1(request):
#     if request.method =='POST':
#         programme_ = request.POST['programme']
#         batch =request.POST['batch']
#         professional_core_credit =request.POST['prof_core_credit']
#         professional_elective_credit = request.POST['prof_elective_credit']
#         professional_project_credit = request.POST['prof_project_credit']
#         professional_lab_credit = request.POST['prof_lab_credit']
#         Core_engineering_science_credit = request.POST['core_engineering_science_credit']
#         Core_natural_science_credit = request.POST['core_natural_science_credit']
#         Core_humanities_credit = request.POST['core_humanities_credit']
#         Core_design_credit = request.POST['core_design_credit']
#         Core_manufacturing_credit = request.POST['core_manufacturing_credit']
#         Core_management_science_credit = request.POST['core_management_science_credit']
#         pbi = request.POST['pbi']
#         pr =request.POST['pr']
#
#         print(programme,batch,pbi,pr)
#         btech_curr = BtechCurriculum.objects.create(
#         programme=programme_,
#         batch=batch,
#         professional_core_credit=professional_core_credit,
#         professional_elective_credit=professional_elective_credit,
#         professional_project_credit=professional_project_credit,
#         professional_lab_credit=professional_lab_credit,
#         Core_engineering_science_credit=Core_engineering_science_credit,
#         Core_natural_science_credit=Core_natural_science_credit,
#         Core_humanities_credit=Core_humanities_credit,
#         Core_design_credit=Core_design_credit,
#         Core_manufacturing_credit=Core_manufacturing_credit,
#         Core_management_science_credit=Core_management_science_credit,
#         pbi=pbi,
#         pr=pr)
#         print(btech_curr)
#     return render(request,'add_btech_curriculum.html')

def add_batch_semester(request):
    print("request granted")
    programme = request.POST.get('programme')
    batch = request.POST.get('batch')
    sem = request.POST.get('semester')
    total_courses = request.POST.get('total_number_of_courses')
    prof_core_courses = request.POST.get('professional_core_courses')
    prof_elective_courses = request.POST.get('professional_elective_courses')
    prof_project_courses = request.POST.get('professional_project_courses')
    prof_lab_courses = request.POST.get('professional_lab_courses')
    es_courses = request.POST.get('escourses')
    ns_courses = request.POST.get('nscourses')
    hs_courses = request.POST.get('hscourses')
    ds_courses = request.POST.get('dscourses')
    mn_courses = request.POST.get('mncourses')
    ms_courses = request.POST.get('mscourses')
    pbi = 'True'

    print(es_courses,mn_courses)
    batch_sem = BatchSemester.objects.create(
    programme=programme,
    batch=batch,
    semester=sem,
    total_number_of_courses=total_courses,
    professional_core_courses=prof_core_courses,
    professional_elective_courses=prof_elective_courses,
    professional_project_courses=prof_project_courses,
    professional_lab_courses=prof_lab_courses,
    Core_engineering_science_courses=es_courses,
    Core_natural_science_courses=ns_courses,
    Core_humanities_courses=hs_courses,
    Core_design_courses=ds_courses,
    Core_manufacturing_courses=mn_courses,
    Core_management_science_courses=ms_courses,
    pbi=pbi)
    print(batch_sem)
    find_sem = 'sem'+ str(sem)
    tcourses = total_courses
    print(find_sem,tcourses)
    if int(sem)==1 :
        obj = BtechCurriculum.objects.all().filter(batch=batch).update(sem1=batch_sem)
    elif int(sem)==2:
        obj = BtechCurriculum.objects.all().filter(batch=batch).update(sem2=batch_sem)
    elif int(sem)==3:
        obj = BtechCurriculum.objects.all().filter(batch=batch).update(sem3=batch_sem)
    elif int(sem)==4:
        obj = BtechCurriculum.objects.all().filter(batch=batch).update(sem4=batch_sem)
    elif int(sem)==5:
        obj = BtechCurriculum.objects.all().filter(batch=batch).update(sem5=batch_sem)
    elif int(sem)==6:
        obj = BtechCurriculum.objects.all().filter(batch=batch).update(sem6=batch_sem)
    elif int(sem)==7:
        obj = BtechCurriculum.objects.all().filter(batch=batch).update(sem7=batch_sem)
    elif int(sem)==8:
        obj = BtechCurriculum.objects.all().filter(batch=batch).update(sem8=batch_sem)

    context =  get_course_list(request)
    print(context)

    try:
        data = render_to_string('add_curriculum_course.html',{'batch':batch_sem,'course_list':context,'range':range(int(tcourses))},
                                 request)
        print("abcd")
        obj = json.dumps({'d' : data})
        print("gscdgascdbscabdfcasbfcdnabcfb")
        return HttpResponse(obj, content_type = 'application/json')
    except:
        return HttpResponse("fghjk")



# def add_batch_semester1(request):
#     if request.method=='POST':
#         programme = request.POST['programme']
#         batch = request.POST['batch']
#         sem = request.POST['semester']
#         total_courses = request.POST['total_number_of_courses']
#         prof_core_courses = request.POST['professional_core_courses']
#         prof_elective_courses = request.POST['professional_elective_courses']
#         prof_project_courses = request.POST['professional_project_courses']
#         prof_lab_courses = request.POST['professional_lab_courses']
#         es_courses = request.POST['escourses']
#         ns_courses = request.POST['nscourses']
#         hs_courses = request.POST['hscourses']
#         ds_courses = request.POST['dscourses']
#         mn_courses = request.POST['mncourses']
#         ms_courses = request.POST['mscourses']
#         pbi = request.POST['pbi']
#
#         print(es_courses,mn_courses)
#         batch_sem = BatchSemester.objects.create(
#         programme=programme,
#         batch=batch,
#         semester=sem,
#         total_number_of_courses=total_courses,
#         professional_core_courses=prof_core_courses,
#         professional_elective_courses=prof_elective_courses,
#         professional_project_courses=prof_project_courses,
#         professional_lab_courses=prof_lab_courses,
#         Core_engineering_science_courses=es_courses,
#         Core_natural_science_courses=ns_courses,
#         Core_humanities_courses=hs_courses,
#         Core_design_courses=ds_courses,
#         Core_manufacturing_courses=mn_courses,
#         Core_management_science_courses=ms_courses,
#         pbi=pbi)
#         print(batch_sem)
#         find_sem = 'sem'+ str(sem)
#         print(find_sem)
#         if int(sem)==1 :
#             obj = BtechCurriculum.objects.all().filter(batch=batch).update(sem1=batch_sem)
#         elif int(sem)==2:
#             obj = BtechCurriculum.objects.all().filter(batch=batch).update(sem2=batch_sem)
#         elif int(sem)==3:
#             obj = BtechCurriculum.objects.all().filter(batch=batch).update(sem3=batch_sem)
#         elif int(sem)==4:
#             obj = BtechCurriculum.objects.all().filter(batch=batch).update(sem4=batch_sem)
#         elif int(sem)==5:
#             obj = BtechCurriculum.objects.all().filter(batch=batch).update(sem5=batch_sem)
#         elif int(sem)==6:
#             obj = BtechCurriculum.objects.all().filter(batch=batch).update(sem6=batch_sem)
#         elif int(sem)==7:
#             obj = BtechCurriculum.objects.all().filter(batch=batch).update(sem7=batch_sem)
#         elif int(sem)==8:
#             obj = BtechCurriculum.objects.all().filter(batch=batch).update(sem8=batch_sem)
        # obj.save()

    # return render(request,"add_batch_semester.html")

# def get_course_list(request):
#
#     print(context)
#     return render(request,'add_curriculum_course.html',context)

def add_curriculum_course(request):
    print("dfdsf course")
    if request.method=='POST':
        sem = request.POST.get('semester')
        batch = request.POST.get('batch')
        tnc = request.POST.get('numberofcourses')
        # course = request.POST.getlist('course')
        # course_id = request.POST.getlist('course_id')
        # course_type = request.POST.getlist('course_type')
        # course_credits=request.POST.getlist('course_credits')
        # course_lecture = request.POST.getlist('course_lecture')
        # course_tutorials = request.POST.getlist('course_tutorials')
        # course_practical = request.POST.getlist('course_practical')
        # course_discussion= request.POST.getlist('course_discussion')
        #
        # print(course_lecture,course_credits)
        #
        # values_len = int(tnc)
        # print(values_len)
        # obj = BatchSemester.objects.all().filter(semester=sem).filter(batch=batch).first()
        # for i in range(values_len):
        #     for key,values in request.POST.lists():
        #         print(i)
        #         if(key == 'course'):
        #             obj2 = Course.objects.filter(course_name=values[i]).first()
        #             print(obj)
        #         if(key == 'course_id'):
        #             course_id=values[i]
        #             print(course_id)
        #         # CurriculumCourse.objects.create(
        #         # semester=obj,
        #         # curr_course=obj2,
        #         # course_id=course_id[i-1],
        #         # course_type=course_type[i-1],
        #         # course_credits=course_credits[i-1],
        #         # course_lecture=course_lecture[i-1],
        #         # course_tutorial=course_tutorials[i-1],
        #         # course_practical=course_practical[i-1],
        #         # course_discussion=course_discussion[i-1]
        #         # )


        try:
            data = render_to_string('semester.html',{'semester':sem},
                                     request)
            # print("abcd")
            obj = json.dumps({'d' : data})
            print("gscdgascdbscabdfcasbfcdnabcfb")
            return HttpResponse(obj, content_type = 'application/json')
        except:
            return HttpResponse("fghjk")



        # obj2 = Course.objects.filter(course_name = course)
        # CurriculumCourse.objects.all().filter(semester=sem).order_by('batch').update(curr_course=obj2)
        # obj = BatchSemester.objects.all().filter(semester=sem).order_by('batch')
        # obj1 = obj.first()
        # # print(obj)
        # CurriculumCourse.objects.all().filter(semester=sem).order_by('batch').update(semester=obj1)
        # # courses = Course.objects.all()
        # context = get_course_list(request)
    # return render(request,'add_curriculum_course.html',get_course_list(request))

def view_curriculum(request):
    if request.method == 'POST':
        batch = request.POST['batch']
        semester = request.POST['semester']
        programme = request.POST['programme']
        print(programme)
        # get_curriculum_list(request,batch,semester)
        # redirect_url = reverse_lazy('showCurriculum')

    return render(request,'get_curriculum.html',get_curriculum_list(request))



def get_curriculum_list(request):
    obj = BtechCurriculum.objects.filter(batch=2018).first()
    semester = 'all'
    if semester == "all":
        obj1 = obj.sem1
        obj2 = obj.sem2
        obj3 = obj.sem3
        obj4 = obj.sem4
        obj5 = obj.sem5
        obj6 = obj.sem6
        obj7 = obj.sem7
        obj8 = obj.sem8
        print(obj2,obj3,obj4)
        sem1 = CurriculumCourse.objects.all().filter(semester=obj1)
        sem2 = CurriculumCourse.objects.all().filter(semester=obj2)
        sem3 = CurriculumCourse.objects.all().filter(semester=obj3)
        sem4 = CurriculumCourse.objects.all().filter(semester=obj4)
        sem5 = CurriculumCourse.objects.all().filter(semester=obj5)
        sem6 = CurriculumCourse.objects.all().filter(semester=obj6)
        sem7 = CurriculumCourse.objects.all().filter(semester=obj7)
        sem8 = CurriculumCourse.objects.all().filter(semester=obj8)
        print(sem2,sem3,sem4,sem1)
        context = {'semester1':sem1,
        'semester2':sem2,
        'semester3':sem3,
        'semester4':sem4,
        'semester5':sem5,
        'semester6':sem6,
        'semester7':sem7,
        'semester8':sem8,
        'tab':'9'}
    elif semester == 1 :
        obj1 = obj.sem1
        sem1 = CurriculumCourse.objects.all().filter(semester=obj1)
        context = {'semester1':sem1,'tab':'1'}
    elif semester == 2 :
        obj2 = obj.sem2
        sem2 = CurriculumCourse.objects.all().filter(semester=obj2)
        context = {'semester2':sem2,'tab':'2'}
    elif semester == 3 :
        obj3 = obj.sem3
        sem3 = CurriculumCourse.objects.all().filter(semester=obj3)
        context = {'semester3':sem3,'tab':'3'}
    elif semester == 4 :
        obj4 = obj.sem4
        sem4 = CurriculumCourse.objects.all().filter(semester=obj4)
        context = {'semester4':sem4,'tab':'4'}
    elif semester == 5 :
        obj5 = obj.sem5
        sem5 = CurriculumCourse.objects.all().filter(semester=obj5)
        context = {'semester5':sem5,'tab':'5'}
    elif semester == 6 :
        obj6 = obj.sem6
        sem6 = CurriculumCourse.objects.all().filter(semester=obj6)
        context = {'semester6':sem6,'tab':'6'}
    elif semester == 7 :
        obj7 = obj.sem7
        sem7 = CurriculumCourse.objects.all().filter(semester=obj7)
        context = {'semester7':sem7,'tab':'7'}
    elif semester == 8 :
        obj8 = obj.sem8
        sem8 = CurriculumCourse.objects.all().filter(semester=obj8)
        context = {'semester8':sem8,'tab':'8'}

    return context

def testajax(request):
    batch = request.POST.get('batch')
    obj = BatchSemester.objects.filter(batch=int(batch)).first()
    print(obj)
    try:
        data = render_to_string('new.html',
                                {'object':obj}, request)
        print("abcd")
        obj = json.dumps({'d' : data})
        print("gscdgascdbscabdfcasbfcdnabcfb")
        return HttpResponse(obj, content_type = 'application/json')
    except:
        return HttpResponse("fghjk")








# sdgv
def main(request):
    return HttpResponseRedirect('admin/')

def acad_admin(request):

    pragramme_list = dict(Constants.PROGRAMME)
    branch_list = dict(Constants.BRANCH)
    specialization_list = dict(Constants.MTechSpecialization)

    return render(
                    request,
                     'acad/acad.html' ,
                     {
                        'pragramme_list' : pragramme_list,
                        'branch_list':branch_list,
                        'specialization_list':specialization_list,
                     })


def add_curriculum(request):
    programme  = request.POST.get('programme')
    batch = request.POST.get('batch')


    if programme == "BTECH":
        curr_obj = BtechCurriculum.objects.filter(batch = int(batch), programme = programme).first()
        if curr_obj :
            # return JsonResponse({"success": True, "msg": "This is an alternamtive message"})
            return JsonResponse({"success": True, "msg": "Curriculum has already been made."})
        else :
            professional_core_credit =request.POST.get('prof_core_credit')
            professional_elective_credit = request.POST.get('prof_elective_credit')
            professional_project_credit = request.POST.get('prof_project_credit')
            professional_lab_credit = request.POST.get('prof_lab_credit')
            Core_engineering_science_credit = request.POST.get('core_engineering_science_credit')
            Core_natural_science_credit = request.POST.get('core_natural_science_credit')
            Core_humanities_credit = request.POST.get('core_humanities_credit')
            Core_design_credit = request.POST.get('core_design_credit')
            Core_manufacturing_credit = request.POST.get('core_manufacturing_credit')
            Core_management_science_credit = request.POST.get('core_management_science_credit')
            pbi = request.POST.get('pbi')
            pr =request.POST.get('pr')

            print(programme,batch,pbi,pr)
            try:
                obj = BtechCurriculum.objects.create(
                    programme=programme,
                    batch=batch,
                    professional_core_credit=professional_core_credit,
                    professional_elective_credit=professional_elective_credit,
                    professional_project_credit=professional_project_credit,
                    professional_lab_credit=professional_lab_credit,
                    Core_engineering_science_credit=Core_engineering_science_credit,
                    Core_natural_science_credit=Core_natural_science_credit,
                    Core_humanities_credit=Core_humanities_credit,
                    Core_design_credit=Core_design_credit,
                    Core_manufacturing_credit=Core_manufacturing_credit,
                    Core_management_science_credit=Core_management_science_credit,
                    pbi=pbi,
                    pr=pr)
                obj.save()
                return JsonResponse({"success": True, "msg": "Curriculum  created."})
            except:
                return HttpResponseRedirect('/acad')

def add_mtech_curriculum(request):
    programme  = request.POST.get('programme')
    batch = request.POST.get('batch')

    if programme == "MTECH":
        # print("MT")
        curr_obj = MtechCurriculum.objects.filter(programme = programme,batch=int(batch)).first()

        if curr_obj:
            return JsonResponse({"success": True, "msg": "Curriculum has already been made."})
        else:
            total_number_of_courses =request.POST.get('total_number_of_courses')
            branch = request.POST.get('branch')
            specialization = request.POST.get('specialization')
            total_credits = request.POST.get('total_credits')
            elective_credits = request.POST.get('elective_credits')
            lab_credits = request.POST.get('lab_credits')
            thesis_credits = request.POST.get('thesis_credits')
            seminar_credits = request.POST.get('seminar_credits')
            core_credits = request.POST.get('core_credits')
            # print(programme,batch)
            try:
                obj1 = MtechCurriculum.objects.create(
                    programme= programme,
                    batch =batch,
                    total_number_of_courses =total_number_of_courses,
                    branch = branch,
                    specialization = specialization,
                    total_credits = total_credits,
                    elective_credits = elective_credits,
                    lab_credits = lab_credits,
                    thesis_credits = thesis_credits,
                    seminar_credits = seminar_credits,
                    core_credits = core_credits)
                obj1.save()
                # print("Succesfully Added")
                return JsonResponse({"success": True, "msg": "Curriculum  created."})
            except:
                return HttpResponseRedirect('/acad')


def get_batch_curriculum(request):
    programme = request.POST.get('programme')
    batch = int(request.POST.get('batch'))
    print(request.POST)
    if programme == "BTECH" :
        obj = BtechCurriculum.objects.filter(batch = int(request.POST.get('batch')), programme = programme).first()
    else:
        obj = None

    # Changes
    # sem_list = BtechCurriculum.objects.filter(batch = int(request.POST.get('batch')), programme = programme).first()
    # sem1 = sem_list.sem1



    if obj :
        data = render_to_string('acad/add_semester_response.html',
                                {'obj':obj,
                                'programme' : programme,
                                'batch' : batch,
                                'sem' :8
                                }, request)
        obj = json.dumps({'html' : data, 'msg' : 'obj found', 'done' : True})
        return HttpResponse(obj, content_type = 'application/json')
    else :
        return JsonResponse({"success": True, "msg": "There is no curriculum for given batch and programme.",'done' : False })

def get_mtech_curriculum(request):
    programme = request.POST.get('programme')
    batch = int(request.POST.get('batch'))
    if programme == "MTECH" :
        obj = MtechCurriculum.objects.filter(batch = int(request.POST.get('batch')), programme = programme).first()
    else:
        obj = None


    if obj :
        data = render_to_string('acad/add_semester_response.html',
                                {'obj':obj,
                                'programme' : programme,
                                'batch' : batch,
                                'sem' :4
                                }, request)
        obj = json.dumps({'html' : data, 'msg' : 'obj found', 'done' : True})
        return HttpResponse(obj, content_type = 'application/json')
    else :
        return JsonResponse({"success": True, "msg": "There is no curriculum for given batch and programme.",'done' : False })



def set_batch_semester(request):
    programme = request.POST.get('programme')
    batch = int(request.POST.get('batch'))
    sem = int(request.POST.get('semester'))

    obj = BatchSemester.objects.filter(programme = programme, batch = batch, semester = sem).first()

    # total_courses = request.POST.get('total_number_of_courses')
    prof_core_courses = request.POST.get('professional_core_courses')
    prof_elective_courses = request.POST.get('professional_elective_courses')
    prof_project_courses = request.POST.get('professional_project_courses')
    prof_lab_courses = request.POST.get('professional_lab_courses')
    es_courses = request.POST.get('escourses')
    ns_courses = request.POST.get('nscourses')
    hs_courses = request.POST.get('hscourses')
    ds_courses = request.POST.get('dscourses')
    mn_courses = request.POST.get('mncourses')
    ms_courses = request.POST.get('mscourses')
    pbi = request.POST.get('pbi')
    print(request.POST)
    try:
        print("SAved")
        batch_sem = BatchSemester.objects.create(
            programme=programme,
            batch=batch,
            semester=sem,
            professional_core_courses=prof_core_courses,
            professional_elective_courses=prof_elective_courses,
            professional_project_courses=prof_project_courses,
            professional_lab_courses=prof_lab_courses,
            Core_engineering_science_courses=es_courses,
            Core_natural_science_courses=ns_courses,
            Core_humanities_courses=hs_courses,
            Core_design_courses=ds_courses,
            Core_manufacturing_courses=mn_courses,
            Core_management_science_courses=ms_courses,
            pbi=pbi)
        batch_sem.save()
        print("SAved")
        obj_curr = BtechCurriculum.objects.filter(batch=batch, programme = programme).first()
        if sem == 1 :
            obj_curr.sem1=batch_sem
        elif sem == 2:
            obj_curr.sem2=batch_sem
        elif sem == 3:
            obj_curr.sem3=batch_sem
        elif sem == 4:
            obj_curr.sem4=batch_sem
        elif sem == 5:
            obj_curr.sem5=batch_sem
        elif sem == 6:
            obj_curr.sem6=batch_sem
        elif sem == 7:
            obj_curr.sem7=batch_sem
        elif sem == 8:
            obj_curr.sem8=batch_sem
        else:
            return JsonResponse({"success": True, "msg": "Related Curriculum does not exist.",'done' : False })
        obj_curr.save()
        return JsonResponse({"success": True, "msg": "Semester Updated.",'done' : True })

    except:
        return JsonResponse({"success": True, "msg": "Could not be created.",'done' : False })


def set_mtech_semester(request):
    programme = request.POST.get('programme')
    batch = int(request.POST.get('batch'))
    sem = int(request.POST.get('semester'))
    total_courses = request.POST.get('total_courses')
    core_courses = request.POST.get('core_courses')
    elective_courses = request.POST.get('elective_courses')
    seminar = request.POST.get('seminar')
    lab_courses = request.POST.get('lab_courses')
    thesis = request.POST.get('thesis')

    print(batch,sem,total_courses,core_courses,seminar,lab_courses,thesis,elective_courses)
    try:
        batch_sem = MtechSemester.objects.create(
            programme=programme,
            batch=batch,
            semester=sem,
            total_courses=total_courses,
            core_courses=core_courses,
            elective_courses=elective_courses,
            seminar=seminar,
            lab_courses=lab_courses,
            thesis=thesis)
        batch_sem.save()
        print("Semester Created")
        obj_curr = MtechCurriculum.objects.filter(batch=batch, programme = programme).first()
        if sem == 1 :
            obj_curr.sem1=batch_sem
        elif sem == 2:
            obj_curr.sem2=batch_sem
        elif sem == 3:
            obj_curr.sem3=batch_sem
        elif sem == 4:
            obj_curr.sem4=batch_sem
        else:
            return JsonResponse({"success": True, "msg": "Related Curriculum does not exist.",'done' : False })
        obj_curr.save()
        return JsonResponse({"success": True, "msg": "Semester Updated.",'done' : True })

    except:
        return JsonResponse({"success": True, "msg": "Could not be created.",'done' : False })



def get_batch_semesters(request):
    programme = request.POST.get('programme')
    batch = int(request.POST.get('batch'))
    if programme == "BTECH" :
        obj = BtechCurriculum.objects.filter(batch = int(request.POST.get('batch')), programme = programme).first()
    else:
        obj = None

    if obj :
        #

        total_credits = obj.total_credits
        pcc=obj.professional_core_credit
        pec=obj.professional_elective_credit
        ppc = obj.professional_project_credit
        plc = obj.professional_lab_credit
        cesc = obj.Core_engineering_science_credit
        cnsc = obj.Core_natural_science_credit
        chc = obj.Core_humanities_credit
        cdc = obj.Core_design_credit
        cmc = obj.Core_manufacturing_credit
        cmsc= obj.Core_management_science_credit
        pbi = obj.pbi
        pr = obj.pr

        sem_batch = BatchSemester.objects.all().filter(batch=batch).filter(programme=programme)

        trc=0
        tre=0
        trl=0
        trp=0
        tres=0
        trns=0
        trhs=0
        trds=0
        trmn=0
        trms=0

        for sem in sem_batch:
            rc = CurriculumCourse.objects.filter(course_type='Core').filter(semester=sem)
            for i in rc:
                trc = trc + int(i.course_credits)
            re = CurriculumCourse.objects.filter(course_type='Elective').filter(semester=sem)
            for i in re:
                tre = tre + int(i.course_credits)
            rl = CurriculumCourse.objects.filter(course_type='Lab').filter(semester=sem)
            for i in rl:
                trl = trl + int(i.course_credits)
            rp = CurriculumCourse.objects.filter(course_type='Project').filter(semester=sem)
            for i in rp:
                trp = trp + int(i.course_credits)
            res = CurriculumCourse.objects.filter(course_type='ES').filter(semester=sem)
            for i in res:
                tres = tres + int(i.course_credits)
            rns = CurriculumCourse.objects.filter(course_type='NS').filter(semester=sem)
            for i in rns:
                trns = trns + int(i.course_credits)
            rhs = CurriculumCourse.objects.filter(course_type='HS').filter(semester=sem)
            for i in rhs:
                trhs = trhs + int(i.course_credits)
            rds = CurriculumCourse.objects.filter(course_type='DS').filter(semester=sem)
            for i in rds:
                trds = trds + int(i.course_credits)
            rmn = CurriculumCourse.objects.filter(course_type='MN').filter(semester=sem)
            for i in rmn:
                trmn = trmn + int(i.course_credits)
            rms = CurriculumCourse.objects.filter(course_type='MS').filter(semester=sem)
            for i in rms:
                trms = trms + int(i.course_credits)


        trc = pcc-trc
        tre = pec-tre
        trl = plc-trl
        trp = ppc-trp
        tres = cesc-tres
        trns = cnsc-trns
        trhs = chc-trhs
        trds = cdc-trds
        trmn = cmc-trmn
        trms = cmsc-trms
        tt = trc+tre+trl+tres+trns+trhs+trds+trmn+trms


        #
        sem_list = [obj.sem1,obj.sem2,obj.sem3,obj.sem4,obj.sem5,obj.sem6,obj.sem7,obj.sem8]
        course_list = Course.objects.all();
        branch_list = ['CSE',"ME","ECE"]
        # print(course_list)
        data = render_to_string('acad/add_curr_course_response.html',
                                {'total_rem':tt,
                                'trc':trc,
                                'tre':tre,
                                'trl':trl,
                                'tres':tres,
                                'trns':trns,
                                'trhs':trhs,
                                'trds':trds,
                                'trmn':trmn,
                                'trms':trms,
                                'sem1' : obj.sem1,
                                'sem2' : obj.sem2,
                                'sem3' : obj.sem3,
                                'sem4' : obj.sem4,
                                'sem5' : obj.sem5,
                                'sem6' : obj.sem6,
                                'sem7' : obj.sem7,
                                'sem8' : obj.sem8,
                                'obj' : obj,
                                'sem_list' : sem_list,
                                'course_list' : course_list,
                                'programme' : programme,
                                'batch' : batch,
                                'sem' :8,
                                'branch_list' : branch_list
                                }, request)
        obj = json.dumps({'html' : data, 'msg' : 'obj found', 'done' : True})
        return HttpResponse(obj, content_type = 'application/json')
    else :
        return JsonResponse({"success": True, "msg": "There is no curriculum for given batch and programme.",'done' : False })



def get_mtech_semesters(request):
    print("Entered")
    programme = request.POST.get('programme')
    batch = int(request.POST.get('batch'))
    if programme == "MTECH" :
        obj = MtechCurriculum.objects.filter(batch = int(request.POST.get('batch')), programme = programme).first()
    else:
        obj = None

    if obj :
        total_credits = obj.total_credits
        elective_credits=obj.elective_credits
        lab_credits=obj.lab_credits
        thesis_credits = obj.thesis_credits
        seminar_credits = obj.seminar_credits
        core_credits = obj.core_credits
        branch = obj.branch
        specialization = obj.specialization

        #
        sem_list = [obj.sem1,obj.sem2,obj.sem3,obj.sem4]
        course_list = Course.objects.all();
        print(course_list)
        data = render_to_string('acad/add_mtech_course_response.html',
                                {
                                'sem1' : obj.sem1,
                                'sem2' : obj.sem2,
                                'sem3' : obj.sem3,
                                'sem4' : obj.sem4,
                                'obj' : obj,
                                'sem_list' : sem_list,
                                'course_list' : course_list,
                                'programme' : programme,
                                'batch' : batch,
                                'sem' :4
                                }, request)
        obj = json.dumps({'html' : data, 'msg' : 'obj found', 'done' : True})
        return HttpResponse(obj, content_type = 'application/json')
    else :
        return JsonResponse({"success": True, "msg": "There is no curriculum for given batch and programme.",'done' : False })


@transaction.atomic
def add_curr_course(request):
    seme =1
    batch =2018

    val_list = list()
    val_list.append(len(request.POST.getlist('pccbranch')))
    val_list.append(len(request.POST.getlist('pecbranch')))
    val_list.append(len(request.POST.getlist('ppcbranch')))
    val_list.append(len(request.POST.getlist('plcbranch')))
    val_list.append(len(request.POST.getlist('cescbranch')))
    val_list.append(len(request.POST.getlist('cnscbranch')))
    val_list.append(len(request.POST.getlist('chcbranch')))
    val_list.append(len(request.POST.getlist('cdcbranch')))
    val_list.append(len(request.POST.getlist('cmcbranch')))
    val_list.append(len(request.POST.getlist('cmscbranch')))

    print(val_list)

    prefix_list = ['pcc','pec','ppc','plc','cesc','cnsc','chc','cdc','cmc','cmsc']
    c_type = ['Core','Elective','Project','Lab','ES','NS','HS','DS','MN','MS']

    for x in range(1):
                for key, values in request.POST.lists():
                    if(key == 'semester'):
                        seme = values[x]
                    elif(key == 'batch'):
                        batch = values[x]

    a= list()
    b= list()
    c= list()
    d= list()
    e= list()
    f= list()
    g= list()
    h= list()

    sem = BatchSemester.objects.all().filter(batch=batch,programme="BTECH",semester=seme).first()

    ind =0

    with transaction.atomic():
        try:
            for val in val_list:
                for x in range(val):
                            for key, values in request.POST.lists():
                                if (key == prefix_list[ind] + 'branch'):
                                    a.append(values[x])
                                elif (key == prefix_list[ind] + 'course_id'):
                                    b.append(values[x])
                                elif (key == prefix_list[ind] + 'course'):
                                    c.append(Course.objects.all().filter(course_name=values[x]).first())
                                elif (key == prefix_list[ind] + 'course_credits'):
                                    d.append(values[x])
                                elif (key == prefix_list[ind] + 'course_lecture'):
                                    e.append(values[x])
                                elif (key == prefix_list[ind] + 'course_tutorial'):
                                    f.append(values[x])
                                elif (key == prefix_list[ind] + 'course_practical'):
                                    g.append(values[x])
                                elif (key == prefix_list[ind] + 'course_discussion'):
                                    h.append(values[x])

                for x in range(a.__len__()):
                    s_obj = None
                    s_obj = CurriculumCourse.objects.all().filter(course_id=b[x], semester=sem).first()
                    if s_obj:
                        s_obj.branch=a[x]
                        s_obj.course_type=c_type[ind]
                        s_obj.semester=sem
                        s_obj.curr_course=c[x]
                        s_obj.course_id=b[x]
                        s_obj.course_credits=d[x]
                        s_obj.course_lecture=e[x]
                        s_obj.course_tutorial=f[x]
                        s_obj.course_practical=g[x]
                        s_obj.course_discussion=h[x]
                        s_obj.save()

                    else :
                        s_obj = CurriculumCourse(branch=a[x],course_type=c_type[ind],semester=sem,curr_course=c[x],course_id=b[x],course_credits=d[x],course_lecture=e[x],course_tutorial=f[x],course_practical=g[x],course_discussion=h[x])
                        s_obj.save()
                a.clear()
                b.clear()
                c.clear()
                d.clear()
                e.clear()
                f.clear()
                g.clear()
                h.clear()

                ind+=1
        except :
            return JsonResponse({ "msg": "Courses Successfully not added.",'done' : False })

    obj = json.dumps({ 'msg' : 'Courses Successfully added.', 'done' : True})
    return HttpResponse(obj, content_type = 'application/json')



def add_mtech_curr_course(request):
    seme =1
    batch =2018

    val_list = list()
    val_list.append(len(request.POST.getlist('mpccbranch')))
    val_list.append(len(request.POST.getlist('mpecbranch')))
    val_list.append(len(request.POST.getlist('mppcbranch')))
    val_list.append(len(request.POST.getlist('mplcbranch')))
    val_list.append(len(request.POST.getlist('mcescbranch')))

    prefix_list = ['mpcc','mpec','mppc','mplc','mcesc']
    c_type = ['Core','Elective','Thesis','Seminar','Lab']

    for x in range(1):
                for key, values in request.POST.lists():
                    if(key == 'msemester'):
                        seme = values[x]
                    elif(key == 'mbatch'):
                        batch = values[x]

    a= list()
    b= list()
    c= list()
    d= list()
    e= list()
    f= list()
    g= list()
    h= list()

    sem = MtechSemester.objects.all().filter(batch=batch,programme="MTECH",semester=seme).first()

    ind =0

    for val in val_list:
        for x in range(val):
                    for key, values in request.POST.lists():
                        if (key == prefix_list[ind] + 'branch'):
                            a.append(values[x])
                        elif (key == prefix_list[ind] + 'course_id'):
                            b.append(values[x])
                        elif (key == prefix_list[ind] + 'course'):
                            c.append(Course.objects.all().filter(course_name=values[x]).first())
                        elif (key == prefix_list[ind] + 'course_credits'):
                            d.append(values[x])
                        elif (key == prefix_list[ind] + 'course_lecture'):
                            e.append(values[x])
                        elif (key == prefix_list[ind] + 'course_tutorial'):
                            f.append(values[x])
                        elif (key == prefix_list[ind] + 'course_practical'):
                            g.append(values[x])
                        elif (key == prefix_list[ind] + 'course_discussion'):
                            h.append(values[x])

        for x in range(a.__len__()):
            CurriculumCourse.objects.create(branch=a[x],course_type=c_type[ind],mtech_semester=sem,curr_course=c[x],course_id=b[x],course_credits=d[x],course_lecture=e[x],course_tutorial=f[x],course_practical=g[x],course_discussion=h[x])

        a.clear()
        b.clear()
        c.clear()
        d.clear()
        e.clear()
        f.clear()
        g.clear()
        h.clear()

        ind+=1

    data = render_to_string('acad/add_mtech_course_response.html',
                                {'sem' :8
                                }, request)
    obj = json.dumps({'html' : data, 'msg' : 'Courses Added', 'done' : True})
    return HttpResponse(obj, content_type = 'application/json')


def send_list(request):
    programme = "BTECH"
    batch = 2016
    if programme == "BTECH" :
        obj = BtechCurriculum.objects.filter(batch = batch, programme = programme).first()
    else:
        obj = None

    if obj :
        #

        total_credits = obj.total_credits
        pcc=obj.professional_core_credit
        pec=obj.professional_elective_credit
        ppc = obj.professional_project_credit
        plc = obj.professional_lab_credit
        cesc = obj.Core_engineering_science_credit
        cnsc = obj.Core_natural_science_credit
        chc = obj.Core_humanities_credit
        cdc = obj.Core_design_credit
        cmc = obj.Core_manufacturing_credit
        cmsc= obj.Core_management_science_credit
        pbi = obj.pbi
        pr = obj.pr

        sem_batch = BatchSemester.objects.all().filter(batch=batch).filter(programme=programme)

        trc=0
        tre=0
        trl=0
        trp=0
        tres=0
        trns=0
        trhs=0
        trds=0
        trmn=0
        trms=0

        for sem in sem_batch:
            rc = CurriculumCourse.objects.filter(course_type='Core').filter(semester=sem)
            for i in rc:
                trc = trc + int(i.course_credits)
            re = CurriculumCourse.objects.filter(course_type='Elective').filter(semester=sem)
            for i in re:
                tre = tre + int(i.course_credits)
            rl = CurriculumCourse.objects.filter(course_type='Lab').filter(semester=sem)
            for i in rl:
                trl = trl + int(i.course_credits)
            rp = CurriculumCourse.objects.filter(course_type='Project').filter(semester=sem)
            for i in rp:
                trp = trp + int(i.course_credits)
            res = CurriculumCourse.objects.filter(course_type='ES').filter(semester=sem)
            for i in res:
                tres = tres + int(i.course_credits)
            rns = CurriculumCourse.objects.filter(course_type='NS').filter(semester=sem)
            for i in rns:
                trns = trns + int(i.course_credits)
            rhs = CurriculumCourse.objects.filter(course_type='HS').filter(semester=sem)
            for i in rhs:
                trhs = trhs + int(i.course_credits)
            rds = CurriculumCourse.objects.filter(course_type='DS').filter(semester=sem)
            for i in rds:
                trds = trds + int(i.course_credits)
            rmn = CurriculumCourse.objects.filter(course_type='MN').filter(semester=sem)
            for i in rmn:
                trmn = trmn + int(i.course_credits)
            rms = CurriculumCourse.objects.filter(course_type='MS').filter(semester=sem)
            for i in rms:
                trms = trms + int(i.course_credits)


        trc = pcc-trc
        tre = pec-tre
        trl = plc-trl
        trp = ppc-trp
        tres = cesc-tres
        trns = cnsc-trns
        trhs = chc-trhs
        trds = cdc-trds
        trmn = cmc-trmn
        trms = cmsc-trms
        tt = trc+tre+trl+tres+trns+trhs+trds+trmn+trms


        #
        sem_list = [obj.sem1,obj.sem2,obj.sem3,obj.sem4,obj.sem5,obj.sem6,obj.sem7,obj.sem8]
        course_list = Course.objects.all();
        print(course_list)
        data =             {'total_rem':tt,
                                'trc':trc,
                                'tre':tre,
                                'trl':trl,
                                'tres':tres,
                                'trns':trns,
                                'trhs':trhs,
                                'trds':trds,
                                'trmn':trmn,
                                'trms':trms,
                                'sem1' : obj.sem1,
                                'sem2' : obj.sem2,
                                'sem3' : obj.sem3,
                                'sem4' : obj.sem4,
                                'sem5' : obj.sem5,
                                'sem6' : obj.sem6,
                                'sem7' : obj.sem7,
                                'sem8' : obj.sem8,
                                'obj' : obj,
                                'sem_list' : sem_list,
                                'course_list' : course_list,
                                'programme' : programme,
                                'batch' : batch,
                                'sem' :8
                                }
        return render(request,'acad/abc.html',data)
#
#
def add_curr_course_test(request):
    print("One")
    values_length1 = len(request.POST.getlist('cname'))
    values_length2 = len(request.POST.getlist('ctype'))

    for x in range(values_length1):
                for key, values in request.POST.lists():
                    if (key == 'cname'):
                        print("branch")
                        print(values[x])
                    elif (key == 'batch'):
                        print(values[x])

    for x in range(values_length2):
                for key, values in request.POST.lists():
                    if (key == 'ctype'):
                        print("type")
                        print(values[x])
                    elif (key == 'sem'):
                        print(values[x])

    #here i have demonstrated getting the list.
    return HttpResponse("ksjhvuw9r")
    # print(course[0])


def view_btech_curriculum(request):
    programme = request.POST.get('programme')
    batch = int(request.POST.get('batch'))
    sem1=None
    sem2=None
    sem3=None
    sem4=None
    sem5=None
    sem6=None
    sem7=None
    sem8=None
    if programme == "BTECH" :
        obj = BtechCurriculum.objects.filter(batch = int(request.POST.get('batch')), programme = programme).first()
    else:
        obj = None

    if obj :
        #

        total_credits = obj.total_credits
        if obj.sem1:
            sem1=CurriculumCourse.objects.filter(semester=obj.sem1)
        if obj.sem2:
            sem2=CurriculumCourse.objects.filter(semester=obj.sem2)
        if obj.sem3:
            sem3=CurriculumCourse.objects.filter(semester=obj.sem3)
        if obj.sem4:
            sem4=CurriculumCourse.objects.filter(semester=obj.sem4)
        if obj.sem5:
            sem5=CurriculumCourse.objects.filter(semester=obj.sem5)
        if obj.sem6:
            sem6=CurriculumCourse.objects.filter(semester=obj.sem6)
        if obj.sem7:
            sem7=CurriculumCourse.objects.filter(semester=obj.sem7)
        if obj.sem8:
            sem8=CurriculumCourse.objects.filter(semester=obj.sem8)


        print(sem1,sem2,sem3,sem4,sem5,sem6,sem7,sem8)
        sem_list = [obj.sem1,obj.sem2,obj.sem3,obj.sem4,obj.sem5,obj.sem6,obj.sem7,obj.sem8]
        print(sem_list)
        course_list = Course.objects.all();
        print(course_list)
        data = render_to_string('acad/view_btech_curr_response.html',
                                {'total':total_credits,
                                'sem1' :sem1,
                                'sem2' :sem2,
                                'sem3' :sem3,
                                'sem4' :sem4,
                                'sem5' :sem5,
                                'sem6' :sem6,
                                'sem7' :sem7,
                                'sem8' :sem8,
                                'obj' : obj,
                                'sem_list' : sem_list,
                                'course_list' : course_list,
                                'programme' : programme,
                                'batch' : batch,
                                'sem' :8
                                }, request)
        obj = json.dumps({'html' : data, 'msg' : 'obj found', 'done' : True})
        return HttpResponse(obj, content_type = 'application/json')
    else :
        return JsonResponse({"success": True, "msg": "There is no curriculum for given batch and programme.",'done' : False })



def view_mtech(request):
    programme = request.POST.get('programme')
    batch = int(request.POST.get('batch'))
    sem1=None
    sem2=None
    sem3=None
    sem4=None

    if programme == "MTECH" :
        obj = MtechCurriculum.objects.filter(batch = int(request.POST.get('batch')), programme = "MTECH").first()
    else:
        obj = None

    if obj :
        #
        print(obj)
        total_credits = obj.total_credits
        if obj.sem1:
            sem1=CurriculumCourse.objects.all().filter(mtech_semester=obj.sem1)
        if obj.sem2:
            sem2=CurriculumCourse.objects.all().filter(mtech_semester=obj.sem2)
        if obj.sem3:
            sem3=CurriculumCourse.objects.all().filter(mtech_semester=obj.sem3)
        if obj.sem4:
            sem4=CurriculumCourse.objects.all().filter(mtech_semester=obj.sem4)



        print(sem1,sem2)
        sem_list = [obj.sem1,obj.sem2,obj.sem3,obj.sem4]
        print(sem_list)
        course_list = Course.objects.all();
        print(course_list)
        data = render_to_string('acad/view_mtech_curr_response.html',
                                {'total':total_credits,
                                'sem1' :sem1,
                                'sem2' :sem2,
                                'sem3' :sem3,
                                'sem4' :sem4,
                                'obj' : obj,
                                'sem_list' : sem_list,
                                'course_list' : course_list,
                                'programme' : programme,
                                'batch' : batch,
                                'sem' :8
                                }, request)
        obj = json.dumps({'html' : data, 'msg' : 'obj found', 'done' : True})
        return HttpResponse(obj, content_type = 'application/json')
    else :
        return JsonResponse({"success": True, "msg": "There is no curriculum for given batch and programme.",'done' : False })



    #
