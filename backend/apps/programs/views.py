from django.shortcuts import render, get_object_or_404
from .models import Program, Term, Lesson

def program_list(request):
    programs = Program.objects.filter(is_active=True).order_by('-created_at')
    return render(request, 'programs/program_list.html', {'programs': programs})

def term_list(request, program_slug):
    program = get_object_or_404(Program, slug=program_slug)
    terms = program.terms.all().order_by('order')
    return render(request, 'programs/term_list.html', {'program': program, 'terms': terms})

def lesson_list(request, program_slug, term_slug):
    term = get_object_or_404(Term, slug=term_slug)
    lessons = term.lessons.all().order_by('order')
    return render(request, 'programs/lesson_list.html', {'term': term, 'lessons': lessons})
