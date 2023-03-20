if cpassowrd == password:
    if User.objects.filter(username=username).exist():
        messages.info(request, "already taken")
        return redirect('register')
    elif User.objects.filter(email=email).exist():
        messages.info(request, " email already taken")
        return redirect('register')
else:
    user = User.objects.create_user(username=username, first_name=first_name, last_name=secondname, email=email,
                                    password=password)

    user.save();
    print("user created")
else:
messages.info("password adik")
return redirect('register')
return redirect('/')