# Making-Queries
Django-ORM Some Helpful Queries   

Use simple structure of qury languages:
  - a = (name="examle", attibute="is taken")                  # use to add new attribute in table in database 
  - a.save()                                                  # use to save attribute
  
Use "example.objects.filter()" query and their attributes: 
  - example.objects.all()                                     # use to show all attributes from database
  - example.objects.filter("tagline__endswith="example")      # search from database
  - example.objects.filter("tagline__iexact"="example")
  - example.objects.filter("tagline__contains="example")      # search value contain database 
  
