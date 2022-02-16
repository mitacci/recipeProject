from django.shortcuts import render, redirect

from coreProject.core.forms import RecipeForm, EditRecipeForm, DeleteRecipeForm
from coreProject.core.models import Recipe


def home(request):
    recipes = Recipe.objects.all()
    context = {
        'recipe': recipes,
    }
    return render(request, 'index.html', context)


def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RecipeForm()

    context = {
        'form': form,
    }
    return render(request, 'create.html', context)


def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditRecipeForm(instance=recipe)

    context = {
        'recipe': recipe,
        'form': form,
    }

    return render(request, 'edit.html', context)


def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    if request.method == 'POST':
        form = DeleteRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DeleteRecipeForm(instance=recipe)

    context = {
        'recipe': recipe,
        'form': form,
    }

    return render(request, 'delete.html', context)


def recipe_details(request, pk):
    recipes = Recipe.objects.get(pk=pk)
    ingredients = recipes.ingredients.split(',')
    context = {
        'recipes': recipes,
        'ingredients': ingredients,
    }
    return render(request, 'details.html', context)
