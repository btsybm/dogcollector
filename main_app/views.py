from django.shortcuts import render
from django.http import HttpResponse


class Dog:  
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

dogs = [
  Dog('Gus', 'goldendoodle', 'A giant baby', 1),
  Dog('Beeps', 'french bulldog', 'Very classy lady', 10),
]



# Define the home view
def home(request):
  return HttpResponse('<h1>cats over dogs</h1>')

def about(request):
  return render(request, 'about.html')

def dogs_index(request):
  return render(request, 'dogs/index.html', { 'dogs': dogs })