Create a new project with a single app --done

/ - redirects to the "/blogs" route with a method called "root" --done

/blogs - display the string "placeholder to later display a list of all blogs" with a method named "index" --done

/blogs/new - display the string "placeholder to display a new form to create a new blog" with a method named "new" --done

/blogs/create - redirect to the "/" route with a method called "create" --done

/blogs/< number > - display the string "placeholder to display blog number: {number}" with a method named "show" (eg. localhost:8000/blogs/15 should display the message: 'placeholder to display blog number 15') --done

/blogs/< number >/edit - display the string "placeholder to edit blog {number}" with a method named "edit" --done

/blogs/< number >/delete - redirect to the "/blogs" route with a method called "destroy"

(**Bonus**) /blogs/json - return a JsonResponse with title and content keys. 