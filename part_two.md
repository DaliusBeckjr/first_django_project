
### blogs - update the routes as follows (content is the same):
        /blogs - display the string "placeholder to later display a list of all blogs" with a method named "index"
        /blogs/new - display the string "placeholder to display a new form to create a new blog" with a method named "new"
        /blogs/create - redirect to the "/blogs" route with a method called "create"
        /blogs/<number> - display the string "placeholder to display blog number: {{number}}" with a method named "show"
        /blogs/<number>/edit - display the string "placeholder to edit blog {{number}}" with a method named "edit"
        /blogs/<number>/delete - redirect to the "/blogs" route with a method called "destroy"
### surveys
        /surveys - display the string "placeholder to display all the surveys created"
        /surveys/new - display "placeholder for users to add a new survey"
### users
        /register - display the string "placeholder for users to create a new user record"
        /login - display the string "placeholder for users to log in"
        /users/new - have the same method that handles /register also handle the url request of /users/new
        /users - display the string "placeholder to later display all the list of users"
