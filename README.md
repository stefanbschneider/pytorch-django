# Django + PyTorch Image Classification App

A simple Django web app classifying uploaded images using a pretrained PyTorch DenseNet.

As an example of how to integrate PyTorch with Django and deploy it on Heroku.

* Live demo: [Heroku](https://pytorch-django.herokuapp.com/)
* Corresponding blog post: [Using PyTorch Inside a Django App](https://stefanbschneider.github.io/blog/pytorch-django)

<img src="docs/demo.gif" alt="image classification demo" width="30%" />

## Setup

```
pip install -r requirements
```

## Usage

Live demo: [Heroku](https://pytorch-django.herokuapp.com/)

### Development

```
python manage.py runserver
```
The app is running on http://localhost:8000/

### Production Deployment on Heroku

See description in [blog post](https://stefanbschneider.github.io/blog/pytorch-django).
