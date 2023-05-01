from django.shortcuts import render
from .models import Curso, Profesor, Estudiante
from .forms import ProfesorForm, EstudianteForm, CursoForm
from django.http import HttpResponse






# ----------------------------------------------------- CURSOS -----------------------------------------------------


def crear_curso(request):
    nombre_curso="python"
    comision_curso="51325"
    
    curso=Curso(nombre=nombre_curso, comision=comision_curso)
    curso.save()
    respuesta=f"curso creado ---- {nombre_curso} - {comision_curso}"
    return HttpResponse(respuesta)


def cursos(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            comision = form.cleaned_data["comision"]
            curso = Curso()
            curso.nombre = nombre
            curso.comision = comision
            curso.save()
            form = CursoForm()
        
    else:
        form = CursoForm()
    cursos = Curso.objects.all()
    context = {"cursos": cursos, "form": form }
    return render(request, "AppCoder/cursos.html", context)

# ----------------------------------------------------- ESTUDIANTES -----------------------------------------------------

def estudiantes(request):
    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            apellido = form.cleaned_data["apellido"]
            email = form.cleaned_data["email"]
            estudiante = Estudiante()
            estudiante.nombre = nombre
            estudiante.apellido = apellido
            estudiante.email = email
            
            estudiante.save()
            form = EstudianteForm()
        
    else:
        form = EstudianteForm()
    estudiantes = Estudiante.objects.all()
    context = {"estudiantes": estudiantes, "form": form }
    return render(request, "AppCoder/estudiantes.html", context)


def entregables(request):
    return render(request,"AppCoder/entregables.html")

def inicio(request):
    return render(request, "AppCoder/inicio.html")


def busquedaComision(request):
    return render (request, "AppCoder/busquedaComision.html")


def buscar(request):
        comision = request.GET["comision"]
        if comision!="":
            cursos= Curso.objects.filter(comision__icontains=comision)
            return render(request, "AppCoder/resultadosBusqueda.html", {"cursos":cursos})
        else:
            return render(request, "AppCoder/busquedaComision.html", {"mensaje": "Ingrese una comision para buscar"})
  
# ----------------------------------------------------- PROFESORES -----------------------------------------------------  

def profesores(request):

    if request.method == "POST":
        form = ProfesorForm(request.POST)
        if form.is_valid():
            profesor = Profesor()
            profesor.nombre = form.cleaned_data['nombre']
            profesor.apellido = form.cleaned_data['apellido']
            profesor.email = form.cleaned_data['email']
            profesor.profesion = form.cleaned_data['profesion']
            profesor.save()
            form = ProfesorForm()
    else:
        form = ProfesorForm()

    profesores = Profesor.objects.all() 

    
    
    return render(request, "AppCoder/profesores.html", {"profesores": profesores, "form" : form})

  
def eliminarProfesor (request, id):
    profesor=Profesor.objects.get(id=id)
    print(profesor)
    profesor.delete()
    profesores=Profesor.objects.all()
    form= ProfesorForm()
    return render(request, "AppCoder/Profesores.html", {"profesores": profesores, "mensaje": "Profesor eliminado correctamente"})


def editarProfesor(request, id):
    profesor=Profesor.objects.get(id=id)
    if request.method == "POST":
        form = ProfesorForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            profesor.nombre = info["nombre"]
            profesor.apellido =info["apellido"] 
            profesor.email = info["email"]
            profesor.profesion = info["profesion"]
            profesor.save()
            profesores=Profesor.objects.all()
            form= ProfesorForm()
            return render(request, "AppCoder/Profesores.html" , {"profesores":profesores, "mensaje": "Profesor editado correctamente", "form": form})
        pass
    else:
        formulario=ProfesorForm(initial={"nombre":profesor.nombre, "apellido":profesor.apellido, "email":profesor.email,"profesion":profesor.profesion})
        return render(request, "AppCoder/editarProfesor.html", {"form": formulario, "profesor":profesor})
    
